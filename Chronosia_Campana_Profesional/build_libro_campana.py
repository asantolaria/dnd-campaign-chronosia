#!/usr/bin/env python3
"""
Genera un único archivo tipo 'libro de campaña' a partir de todos los .md de Chronosia.

Formatos de salida (útiles para el DM):
- Markdown (.md): un solo archivo para buscar con Ctrl+F, abrir en editor o exportar a PDF (pandoc).
- HTML (opcional): un solo archivo con índice clicable, ideal para leer en navegador o tablet.

Uso (requiere Python 3.9+):
  python build_libro_campana.py                    # Genera Libro_Campana_Chronosia.md
  python build_libro_campana.py --html             # Genera también .html con índice clicable
  python build_libro_campana.py -o ruta/custom.md  # Salida en ruta personalizada

En Windows, si 'python' no está en PATH:  py -3 build_libro_campana.py
Exportar a PDF desde el .md:  pandoc Libro_Campana_Chronosia.md -o libro.pdf --toc
"""

import re
import argparse
from pathlib import Path


# Carpetas raíz en el orden deseado para el libro (prefijo -> orden).
SECTION_ORDER = {
    "00_Indice_Campana": 0,
    "00_Esquemas": 1,
    "00_Esquema": 1,
    "01_Introduccion": 2,
    "02_Guia_DM": 3,
    "03_Regiones": 4,
    "04_Aventuras": 5,
    "05_Apendices": 6,
    "06_Recursos": 7,
    "README": 8,
    "00_Estudio": 9,
    "00_Plan_Desarrollo": 10,
}

# Fases dentro de 04_Aventuras (para ordenar Fase_0, Fase_1, ...).
PHASE_ORDER = {
    "00_Estructura": 0,
    "Fase_0": 1,
    "Fase_1": 2,
    "Fase_2": 3,
    "Fase_3": 4,
    "Fase_4_Ritual": 5,
    "Fase_4_Climax": 6,
    "Fase_5": 7,
    "Fase_6": 8,
}

# Archivos o patrones a excluir (por nombre o por segmento de ruta).
EXCLUDE = {
    "agents.md",
    "AGENTS.md",
    "70_Ideas_Creativas_DM.md",
    "00_Documento_Trabajo_Restructuracion.md",
}
EXCLUDE_PATH_PARTS = ("assets", ".git", "Prompt_Mapa", "Decisiones_Criticas")


def section_sort_key(rel_path: str, root_name: str) -> tuple:
    """Orden: sección principal, luego fase (si aplica), luego path como cadena."""
    parts = Path(rel_path).parts
    section = parts[0] if parts else ""
    order = 99
    for prefix, idx in SECTION_ORDER.items():
        if section.startswith(prefix) or root_name.startswith(prefix):
            order = idx
            break
    phase_order = 99
    if len(parts) >= 2 and "Aventuras" in section:
        phase = parts[1]
        for prefix, idx in PHASE_ORDER.items():
            if phase.startswith(prefix):
                phase_order = idx
                break
    return (order, phase_order, rel_path.replace("\\", "/"))


def should_exclude(rel_path: str) -> bool:
    path_lower = rel_path.lower().replace("\\", "/")
    name = Path(rel_path).name
    if name in EXCLUDE:
        return True
    for part in EXCLUDE_PATH_PARTS:
        if part in path_lower:
            return True
    return False


def slugify(text: str) -> str:
    """Ancla tipo GitHub: minúsculas, espacios a -, solo alfanum y -."""
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    text = text.strip().lower()
    return re.sub(r"[-\s]+", "-", text).strip("-") or "doc"


def first_h1(content: str, fallback_name: str = "Documento") -> str:
    m = re.match(r"^#\s+(.+?)(?:\n|$)", content, re.MULTILINE)
    return m.group(1).strip() if m else fallback_name


def bump_headers(content: str, levels: int = 1) -> str:
    """Aumenta el nivel de todos los encabezados (# -> ##, etc.)."""
    def replace(m):
        hashes, rest = m.group(1), m.group(2)
        return "#" * (len(hashes) + levels) + " " + rest
    return re.sub(r"^(#{1,6})\s+(.+)$", replace, content, flags=re.MULTILINE)


def collect_md_files(root: Path) -> list[tuple[str, Path]]:
    """Recorre root y devuelve lista de (rel_path, path_abs) ordenada para el libro."""
    root = root.resolve()
    collected = []
    for path in root.rglob("*.md"):
        try:
            rel = path.relative_to(root)
        except ValueError:
            continue
        rel_str = str(rel).replace("\\", "/")
        if should_exclude(rel_str):
            continue
        collected.append((rel_str, path))
    # Orden: por sección y fase, luego por path.
    collected.sort(key=lambda x: section_sort_key(x[0], Path(x[0]).parts[0] if Path(x[0]).parts else ""))
    return collected


def build_toc_and_anchors(files_with_content: list[tuple[str, str, str]]) -> str:
    """Genera líneas del índice (TOC) en Markdown. Cada título usa el anchor slugificado."""
    lines = ["## Índice del libro\n"]
    for rel_path, title, anchor in files_with_content:
        lines.append(f"- [{title}](#{anchor})  \n  `{rel_path}`")
    return "\n".join(lines) + "\n\n---\n\n"


def build_markdown(root: Path, files: list[tuple[str, Path]]) -> str:
    out = []
    out.append("# Chronosia — Libro de campaña\n")
    out.append("*Un único archivo generado para el DM. Búsqueda global con Ctrl+F.*\n\n")
    out.append("---\n\n")

    files_with_content = []
    for rel_path, path in files:
        try:
            raw = path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            raw = f"*Error leyendo archivo: {e}*"
        fallback = Path(rel_path).stem.replace("_", " ")
        first_title = first_h1(raw, fallback)
        anchor = slugify(first_title)
        # Evitar anclas duplicadas (añadir sufijo con parte del path).
        if any(a == anchor for _, _, a in files_with_content):
            anchor = slugify(Path(rel_path).stem) + "-" + anchor[:20]
        files_with_content.append((rel_path, first_title, anchor))

        content = bump_headers(raw)
        out.append(f"## <span id=\"{anchor}\"></span>{first_title}\n\n")
        out.append(f"*Origen: `{rel_path}`*\n\n")
        out.append(content.strip())
        out.append("\n\n---\n\n")

    toc = build_toc_and_anchors(files_with_content)
    # Insertar TOC después del título.
    body = "".join(out)
    first_sep = body.find("---\n\n", 0)
    if first_sep != -1:
        body = body[: first_sep + 4] + "\n\n" + toc + body[first_sep + 4:]
    else:
        body = body + "\n\n" + toc
    return body


def _table_rows_to_html(rows: list[str], html_module) -> str:
    """Convierte filas de tabla Markdown a <table>."""
    out = ["<table>"]
    for i, row in enumerate(rows):
        if re.match(r"^\|?[\s\-:]+\|", row.strip()):
            continue
        cells = [c.strip() for c in re.split(r"\|", row.strip()) if c.strip()]
        tag = "th" if i == 0 else "td"
        out.append("<tr>" + "".join(f"<{tag}>{html_module.escape(c)}</{tag}>" for c in cells) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def md_chunk_to_html(chunk: str) -> str:
    """Convierte un bloque de markdown a HTML (headers, párrafos, listas, tablas básicas)."""
    import html as html_module
    out = []
    in_list = False
    table_rows = []
    for line in chunk.split("\n"):
        stripped = line.strip()
        if "|" in line and re.match(r"^\|?.+\|", stripped) and not re.match(r"^\|?[\s\-:]+\|", stripped):
            table_rows.append(line)
            continue
        if table_rows:
            out.append(_table_rows_to_html(table_rows, html_module))
            table_rows = []
        if re.match(r"^\|?[\s\-:]+\|", stripped):
            continue
        # Encabezado con ancla opcional: ## <span id="x"></span>Título
        span_match = re.match(r"^#+\s*<span[^>]*></span>(.+)$", line)
        if span_match:
            level = len(re.match(r"^#+", line).group())
            text = span_match.group(1).strip()
            id_match = re.search(r'id="([^"]+)"', line)
            aid = id_match.group(1) if id_match else slugify(text)
            out.append(f"<h{level} id=\"{aid}\">{html_module.escape(text)}</h{level}>")
            continue
        if line.startswith("# "):
            out.append(f"<h1>{html_module.escape(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            text = line[2:].strip()
            out.append(f"<h2>{html_module.escape(text)}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{html_module.escape(line[3:].strip())}</h3>")
        elif line.startswith("#### "):
            out.append(f"<h4>{html_module.escape(line[4:].strip())}</h4>")
        elif line.startswith("- ") or (re.match(r"^\d+\.\s", line) and stripped):
            if not in_list:
                out.append("<ul>")
                in_list = True
            item_text = re.sub(r"^[-]\s+|\d+\.\s+", "", stripped, count=1).strip()
            out.append(f"<li>{html_module.escape(item_text)}</li>")
        elif stripped == "---":
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("<hr/>")
        elif stripped:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<p>{html_module.escape(stripped)}</p>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("<br/>")
    if table_rows:
        out.append(_table_rows_to_html(table_rows, html_module))
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def build_html(root: Path, md_content: str, output_path: Path) -> None:
    """Genera un HTML de una sola página con TOC lateral y estilos mínimos para el DM."""
    import html as html_mod
    toc_items = re.findall(r"-\s*\[([^\]]+)\]\((#[^)]+)\)", md_content)
    toc_html = "\n".join(
        f'<li><a href="{anchor}">{html_mod.escape(title[:70])}{"…" if len(title) > 70 else ""}</a></li>'
        for title, anchor in toc_items
    )
    # Dividir por secciones (---) y convertir cada una a HTML.
    chunks = re.split(r"\n---\n", md_content)
    body_parts = []
    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            continue
        body_parts.append(md_chunk_to_html(chunk))
    main_content = "\n<hr/>\n".join(body_parts)

    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Chronosia — Libro de campaña</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: system-ui, sans-serif; margin: 0; padding: 0; background: #1a1a2e; color: #eaeaea; line-height: 1.5; }}
  .layout {{ display: flex; min-height: 100vh; }}
  nav {{ width: 280px; padding: 1rem; background: #16213e; border-right: 1px solid #0f3460; overflow-y: auto; flex-shrink: 0; position: sticky; top: 0; max-height: 100vh; }}
  nav ul {{ list-style: none; padding: 0; }}
  nav a {{ color: #7eb; display: block; padding: 0.35rem 0; text-decoration: none; font-size: 0.9rem; }}
  nav a:hover {{ color: #9fd; }}
  main {{ flex: 1; padding: 2rem; overflow-y: auto; max-width: 900px; }}
  h1 {{ color: #7eb; border-bottom: 2px solid #0f3460; }}
  h2 {{ color: #9fd; margin-top: 2rem; scroll-margin-top: 1rem; }}
  h3, h4 {{ color: #bcf; margin-top: 1.5rem; }}
  .meta {{ font-size: 0.85rem; color: #888; margin-bottom: 1rem; }}
  hr {{ border: none; border-top: 1px solid #0f3460; margin: 2rem 0; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; }}
  th, td {{ border: 1px solid #0f3460; padding: 0.5rem; text-align: left; }}
  th {{ background: #16213e; color: #7eb; }}
  @media (max-width: 768px) {{ .layout {{ flex-direction: column; }} nav {{ width: 100%; position: relative; }} }}
</style>
</head>
<body>
<div class="layout">
<nav>
  <h3>Índice</h3>
  <ul>
{toc_html}
  </ul>
</nav>
<main>
{main_content}
</main>
</div>
</body>
</html>
"""
    output_path.write_text(html_doc, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Genera el libro de campaña en un solo archivo.")
    parser.add_argument(
        "-o", "--output",
        default="Libro_Campana_Chronosia.md",
        help="Ruta de salida del archivo Markdown.",
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Genera además un archivo HTML con índice clicable.",
    )
    parser.add_argument(
        "--root",
        default=None,
        help="Carpeta raíz de la campaña (por defecto: carpeta del script).",
    )
    args = parser.parse_args()

    root = Path(args.root) if args.root else Path(__file__).resolve().parent
    output_path = root / args.output if not Path(args.output).is_absolute() else Path(args.output)

    files = collect_md_files(root)
    if not files:
        print("No se encontraron archivos .md o todos están excluidos.")
        return

    print(f"Incluidos {len(files)} archivos.")
    md_content = build_markdown(root, files)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md_content, encoding="utf-8")
    print(f"Escrito: {output_path}")

    if args.html:
        html_path = output_path.with_suffix(".html")
        build_html(root, md_content, html_path)
        print(f"Escrito: {html_path}")


if __name__ == "__main__":
    main()
