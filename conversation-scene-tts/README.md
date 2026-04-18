# Conversation Scene TTS

Herramienta para **generar un único MP3** a partir de un guion con **varios personajes**, cada uno con su voz (text-to-speech). Pensada para escenas de discusión, debates, tensión verbal, etc.

## Requisitos

1. **Python 3.10+**
2. **FFmpeg** (necesario para que `pydub` lea/exporte MP3). El script lo busca en el `PATH`, en instalaciones típicas de **WinGet** (`Gyan.FFmpeg`), **Scoop** y **Chocolatey**, o puedes indicarlo con `--ffmpeg` o la variable de entorno `FFMPEG_PATH` (ruta al `ffmpeg.exe` o a la carpeta `bin`).
3. Dependencias:

```bash
cd conversation-scene-tts
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Formato de la escena

Archivo **YAML** o **JSON** con:

- `title` (opcional): título del audio.
- `characters`: objeto; cada clave es el id del personaje usado en `speaker`.
  - `voice`: id de voz de **edge-tts** (ver listado abajo).
  - `rate`, `volume`, `pitch` (opcionales): prosodia SSML de Edge, p. ej. `"+10%"`, `"-5%"`, `"+8Hz"` (pitch en hercios, rango habitual aprox. `-50Hz`…`+50Hz`).
- `lines`: lista de réplicas.
  - `speaker`: id del personaje.
  - `text`: texto a sintetizar.
  - `rate` / `volume` / `pitch` (opcionales): sobrescriben los del personaje en esa línea (útil para acento emocional: más rápido + más agudo en un reproche, más pausado en un remate irónico).

Ejemplo: `examples/disputa_consejo.yaml`.

## Uso

Listar voces (filtrar por idioma/región):

```bash
python render_conversation.py --list-voices --voice-filter es-
```

Generar el MP3:

```bash
python render_conversation.py examples/disputa_consejo.yaml -o output/mi_escena.mp3
```

Opciones útiles:

- `--pause-ms 400`: silencio entre réplicas (por defecto 350 ms).
- `--keep-parts`: guarda cada línea como MP3 en una carpeta junto al archivo final.
- `--ffmpeg "C:\ruta\bin\ffmpeg.exe"`: si acabas de instalar FFmpeg y la terminal aún no ve el `PATH`, o no quieres reiniciar el IDE.

## Notas

- Las voces y la calidad dependen del servicio **Edge TTS** usado por `edge-tts`; hace falta conexión a Internet.
- Tras `winget install Gyan.FFmpeg`, a veces hace falta **cerrar y abrir la terminal** (o Cursor) para que el `PATH` se actualice; mientras tanto usa `--ffmpeg` o `FFMPEG_PATH`.
