#!/usr/bin/env bash
# Construye el manual de Chronosia con estética de libro D&D (sin iconos/emojis).
# Produce DOS documentos para mantener cada uno en un tamaño manejable:
#   1) Chronosia_Manual_Nucleo     — el "libro base": lore, guías DM, regiones,
#      facciones, lugartenientes, bestiario, objetos, tablas, handouts.
#   2) Chronosia_Apendice_Sesiones — el "módulo de aventura": la prep sesión a
#      sesión (Fases 0-4).
# Cada uno sale en HTML estilizado (imprime a PDF desde el navegador para el mejor
# acabado) y en PDF (xelatex si está; si no, LibreOffice de respaldo).
#
# Uso:  cd exports && ./build_manual.sh
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
VERSION="v2.0 (reloj + Torre)"
cd "$ROOT"

# --- NÚCLEO: el libro base (sin la prep de sesiones) ---
NUCLEO=()
addn(){ local g; for g in $1; do [ -f "$g" ] && NUCLEO+=("$g"); done; }
addn "00_Indice_Campana.md"
addn "01_Introduccion/*.md"
addn "02_Guia_DM/01_Dirigir_Campana.md"
addn "02_Guia_DM/10_Motor_de_Campana_Reloj_y_Puertas.md"
addn "02_Guia_DM/06_Nexo_Planar_y_Continuaciones.md"
addn "02_Guia_DM/07_Cronologia_Maestra_Campana.md"
addn "02_Guia_DM/08_Por_Que_Derrotar_Lugartenientes.md"
addn "02_Guia_DM/Eventos_Que_Siempre_Ocurren.md"
addn "02_Guia_DM/DM_Screen_Una_Pagina.md"
addn "02_Guia_DM/03_NPCs_Importantes.md"
addn "02_Guia_DM/09_Cronopolis_Capa_Civil.md"
addn "02_Guia_DM/02_Facciones/*.md"
addn "02_Guia_DM/04_Cronofagos_Detallado/*.md"
addn "03_Regiones/*.md"
addn "04_Aventuras/00_Estructura_Campana.md"
addn "05_Apendices/17_Monstruos_Enemigos.md"
addn "05_Apendices/Bestiario_Regional/*.md"
addn "06_Recursos/Tablas/*.md"
addn "06_Recursos/Handouts/*.md"

# --- APÉNDICE: la prep de sesiones (Fases 0-4) ---
SESIONES=()
adds(){ local g; for g in $1; do [ -f "$g" ] && SESIONES+=("$g"); done; }
adds "04_Aventuras/Fase_0_Railroad_Inicial/*.md"
adds "04_Aventuras/Fase_1_Robos_Traicion/*.md"
adds "04_Aventuras/Fase_2_Sandbox_Inicial/*.md"
adds "04_Aventuras/Fase_3_Sandbox_Avanzado/*.md"
adds "04_Aventuras/Fase_4_Climax_Torre/*.md"

# --- build_doc <basename> <title> <subtitle> <archivo...> ---
build_doc(){
  local base="$1"; shift
  local title="$1"; shift
  local subtitle="$1"; shift
  local out_md="$HERE/${base}.md" out_html="$HERE/${base}.html" out_pdf="$HERE/${base}.pdf"

  : > "$out_md"
  local f
  for f in "$@"; do
    sed -E "s#\]\((\.\./)*assets/#](${ROOT}/assets/#g" "$f" \
    | perl -CSD -pe '
        s/[\x{1F000}-\x{1FFFF}\x{2300}-\x{27BF}\x{2B00}-\x{2BFF}\x{FE00}-\x{FE0F}\x{2049}\x{203C}]//g;
        s/^(\#{1,6})\s+/$1 /;
        s/\*\*\s+/**/g;
        s/[ \t]+$//;
      ' >> "$out_md"
    printf '\n\n---\n\n' >> "$out_md"
  done
  echo "[$base] Markdown: $out_md ($(wc -w < "$out_md") palabras)"

  pandoc "$out_md" -f markdown -t html5 -s --toc --toc-depth=2 \
    -H "$HERE/dnd-style.html" \
    --metadata title="$title" --metadata subtitle="$subtitle" \
    -o "$out_html"
  echo "[$base] HTML: $out_html"

  if command -v xelatex >/dev/null; then
    pandoc "$out_md" -f markdown --pdf-engine=xelatex \
      -H "$HERE/dnd-latex-header.tex" \
      -V geometry:margin=1.6cm -V fontsize=10pt \
      --toc --toc-depth=2 --metadata title="$title" --metadata subtitle="$subtitle" \
      -o "$out_pdf" && echo "[$base] PDF (xelatex): $out_pdf"
  elif command -v soffice >/dev/null || command -v libreoffice >/dev/null; then
    SOFFICE="$(command -v soffice || command -v libreoffice)"
    "$SOFFICE" --headless --convert-to pdf --outdir "$HERE" "$out_html" >/dev/null 2>&1 \
      && echo "[$base] PDF (LibreOffice): $out_pdf" \
      || echo "[$base] AVISO: usa el HTML e 'Imprimir -> Guardar como PDF'."
  else
    echo "[$base] Sin motor PDF: usa el HTML e 'Imprimir -> Guardar como PDF'."
  fi
}

build_doc "Chronosia_Manual_Nucleo" \
  "Chronosia — El Reino del Tiempo Fracturado" \
  "Campaña de D&D 5e · Manual Núcleo · ${VERSION}" \
  "${NUCLEO[@]}"

build_doc "Chronosia_Apendice_Sesiones" \
  "Chronosia — Apéndice de Sesiones" \
  "Campaña de D&D 5e · Prep sesión a sesión (Fases 0-4) · ${VERSION}" \
  "${SESIONES[@]}"

echo "Listo. Dos documentos en $HERE/ (núcleo + apéndice de sesiones)."
