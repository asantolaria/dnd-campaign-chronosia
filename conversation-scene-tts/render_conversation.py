#!/usr/bin/env python3
"""
Genera un MP3 con una escena de diálogo entre varios personajes (TTS multivoz).

Requisitos:
  - Python 3.10+
  - FFmpeg instalado y en PATH (pydub lo usa para leer/exportar MP3)
  - pip install -r requirements.txt
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

import edge_tts
import yaml


def _load_scene(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        data = yaml.safe_load(text)
    elif path.suffix.lower() == ".json":
        data = json.loads(text)
    else:
        raise SystemExit("Formato no soportado. Usa .yaml, .yml o .json")
    if not isinstance(data, dict):
        raise SystemExit("La escena debe ser un objeto en la raíz del archivo.")
    return data


def _prepend_path_dir(bin_dir: Path) -> None:
    """Antepone un directorio al PATH (p. ej. carpeta bin de FFmpeg en Windows)."""
    d = str(bin_dir.resolve())
    path = os.environ.get("PATH", "")
    if d not in path.split(os.pathsep):
        os.environ["PATH"] = d + os.pathsep + path


def _find_ffmpeg_common_locations() -> Path | None:
    """Ubicaciones habituales si el usuario instaló FFmpeg pero no reinició la terminal."""
    local = os.environ.get("LOCALAPPDATA", "")
    if local:
        winget = Path(local) / "Microsoft" / "WinGet" / "Packages"
        if winget.is_dir():
            for pkg in sorted(winget.glob("Gyan.FFmpeg*"), reverse=True):
                for exe in pkg.rglob("ffmpeg.exe"):
                    if "bin" in exe.parts:
                        return exe
    scoop = Path.home() / "scoop" / "apps" / "ffmpeg" / "current" / "bin" / "ffmpeg.exe"
    if scoop.is_file():
        return scoop
    choco = Path(
        os.environ.get("ProgramData", r"C:\ProgramData")
    ) / "chocolatey" / "lib" / "ffmpeg" / "tools" / "ffmpeg" / "bin" / "ffmpeg.exe"
    if choco.is_file():
        return choco
    return None


def resolve_ffmpeg(explicit: Path | None) -> Path | None:
    """
    Devuelve la ruta a ffmpeg.exe si existe.
    Orden: --ffmpeg, FFMPEG_PATH, PATH, carpetas típicas (WinGet, Scoop, Chocolatey).
    FFMPEG_PATH puede ser el .exe o la carpeta bin.
    """
    candidates: list[Path] = []

    if explicit is not None:
        candidates.append(explicit)

    env = os.environ.get("FFMPEG_PATH", "").strip()
    if env:
        p = Path(env)
        if p.is_file() and p.name.lower().startswith("ffmpeg"):
            candidates.append(p)
        elif p.is_dir():
            for name in ("ffmpeg.exe", "ffmpeg"):
                q = p / name
                if q.is_file():
                    candidates.append(q)
                    break

    w = shutil.which("ffmpeg")
    if w:
        candidates.append(Path(w))

    found = _find_ffmpeg_common_locations()
    if found:
        candidates.append(found)

    for c in candidates:
        try:
            if c.is_file():
                return c
        except OSError:
            continue
    return None


def _get_str(d: dict[str, Any], key: str, default: str | None = None) -> str | None:
    v = d.get(key)
    if v is None:
        return default
    if not isinstance(v, str):
        raise SystemExit(f'"{key}" debe ser texto.')
    return v


async def _synthesize_line(
    text: str,
    voice: str,
    rate: str,
    volume: str,
    pitch: str,
    out_path: Path,
) -> None:
    communicate = edge_tts.Communicate(
        text, voice, rate=rate, volume=volume, pitch=pitch
    )
    await communicate.save(str(out_path))


async def _render_scene_async(
    scene: dict[str, Any],
    out_mp3: Path,
    pause_ms: int,
    keep_parts: bool,
) -> None:
    title = _get_str(scene, "title") or "Escena"
    characters = scene.get("characters")
    if not isinstance(characters, dict) or not characters:
        raise SystemExit('Define "characters" como objeto con al menos un personaje.')

    char_cfg: dict[str, dict[str, str]] = {}
    for cid, c in characters.items():
        if not isinstance(c, dict):
            raise SystemExit(f'Personaje "{cid}": debe ser un objeto.')
        voice = _get_str(c, "voice")
        if not voice:
            raise SystemExit(f'Personaje "{cid}": falta "voice" (id de voz edge-tts).')
        char_cfg[cid] = {
            "voice": voice,
            "rate": _get_str(c, "rate", "+0%") or "+0%",
            "volume": _get_str(c, "volume", "+0%") or "+0%",
            "pitch": _get_str(c, "pitch", "+0Hz") or "+0Hz",
        }

    lines = scene.get("lines")
    if not isinstance(lines, list) or not lines:
        raise SystemExit('Define "lines" como lista de réplicas.')

    out_mp3.parent.mkdir(parents=True, exist_ok=True)

    from pydub import AudioSegment

    with tempfile.TemporaryDirectory(prefix="scene_tts_") as tmp:
        tmp_path = Path(tmp)
        part_paths: list[Path] = []
        silence = AudioSegment.silent(duration=max(0, pause_ms))

        for i, line in enumerate(lines):
            if not isinstance(line, dict):
                raise SystemExit(f"Línea {i + 1}: debe ser un objeto.")
            speaker = line.get("speaker")
            if not isinstance(speaker, str) or not speaker:
                raise SystemExit(f"Línea {i + 1}: falta \"speaker\".")
            text = line.get("text")
            if not isinstance(text, str) or not text.strip():
                raise SystemExit(f"Línea {i + 1}: falta \"text\".")
            if speaker not in char_cfg:
                raise SystemExit(f"Línea {i + 1}: speaker desconocido \"{speaker}\".")

            ovoice = char_cfg[speaker]["voice"]
            orate = char_cfg[speaker]["rate"]
            ovolume = char_cfg[speaker]["volume"]
            opitch = char_cfg[speaker]["pitch"]
            line_rate = _get_str(line, "rate") or orate
            line_volume = _get_str(line, "volume") or ovolume
            line_pitch = _get_str(line, "pitch") or opitch

            part = tmp_path / f"line_{i:04d}.mp3"
            await _synthesize_line(
                text.strip(), ovoice, line_rate, line_volume, line_pitch, part
            )
            part_paths.append(part)

        merged = AudioSegment.empty()
        for j, p in enumerate(part_paths):
            merged += AudioSegment.from_mp3(p)
            if j < len(part_paths) - 1:
                merged += silence

        merged.export(str(out_mp3), format="mp3", tags={"title": title})

        if keep_parts:
            parts_dir = out_mp3.with_suffix("").parent / f"{out_mp3.stem}_partes"
            parts_dir.mkdir(parents=True, exist_ok=True)
            for j, p in enumerate(part_paths):
                shutil.copy2(p, parts_dir / f"line_{j:04d}.mp3")


async def list_voices_async(filter_substr: str | None) -> None:
    voices = await edge_tts.list_voices()
    rows: list[tuple[str, str]] = []
    for v in voices:
        short = v.get("ShortName", "")
        locale = v.get("Locale", "")
        if filter_substr and filter_substr.lower() not in (short + locale).lower():
            continue
        rows.append((locale, short))
    rows.sort(key=lambda x: (x[0], x[1]))
    for locale, short in rows:
        print(f"{locale}\t{short}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TTS multivoz: escena a un solo MP3 (edge-tts + pydub)."
    )
    parser.add_argument(
        "scene",
        nargs="?",
        type=Path,
        help="Archivo de escena (.yaml / .yml / .json)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("output") / "escena.mp3",
        help="Ruta del MP3 de salida (default: output/escena.mp3)",
    )
    parser.add_argument(
        "--pause-ms",
        type=int,
        default=350,
        help="Silencio entre réplicas en milisegundos (default: 350)",
    )
    parser.add_argument(
        "--keep-parts",
        action="store_true",
        help="Copia cada línea como MP3 suelta en una carpeta *_partes",
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help="Lista voces disponibles (edge-tts) y sale",
    )
    parser.add_argument(
        "--voice-filter",
        type=str,
        default=None,
        help="Con --list-voices, filtra por subcadena (ej: es-ES, es-MX)",
    )
    parser.add_argument(
        "--ffmpeg",
        type=Path,
        default=None,
        help="Ruta a ffmpeg.exe si no está en PATH (también variable FFMPEG_PATH)",
    )
    args = parser.parse_args()

    if args.list_voices:
        asyncio.run(list_voices_async(args.voice_filter))
        return

    if not args.scene:
        parser.error("Indica el archivo de escena o usa --list-voices.")

    ffmpeg_exe = resolve_ffmpeg(args.ffmpeg)
    if ffmpeg_exe is None:
        raise SystemExit(
            "No se encontró FFmpeg.\n"
            "  - Instálalo (Windows: winget install Gyan.FFmpeg) y abre una terminal nueva, o\n"
            "  - exporta FFMPEG_PATH a la carpeta bin o al ffmpeg.exe, o\n"
            "  - usa: python render_conversation.py --ffmpeg \"C:\\ruta\\a\\ffmpeg.exe\" ..."
        )

    _prepend_path_dir(ffmpeg_exe.parent)

    scene = _load_scene(args.scene)
    asyncio.run(
        _render_scene_async(
            scene,
            args.output,
            pause_ms=args.pause_ms,
            keep_parts=args.keep_parts,
        )
    )
    print(f"Listo: {args.output.resolve()}")


if __name__ == "__main__":
    main()
