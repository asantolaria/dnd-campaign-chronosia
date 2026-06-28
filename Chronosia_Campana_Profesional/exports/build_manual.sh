#!/usr/bin/env bash
# Construye EL MANUAL de Chronosia como un único libro con estética de D&D
# (sin emojis): Historia → Capítulos 1-15 → Apéndices. Salidas: Markdown
# unificado, HTML estilizado (a 2 columnas; imprime a PDF para el mejor
# acabado) y PDF (xelatex).
#
# Uso:  cd exports && ./build_manual.sh
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
VERSION="v3.0 (libro por capítulos)"
TITLE="Chronosia — El Reino del Tiempo Fracturado"
SUBTITLE="Campaña de D&D 5e · Manual completo · ${VERSION}"
OUT_MD="$HERE/Chronosia_Manual.md"
OUT_HTML="$HERE/Chronosia_Manual.html"
OUT_PDF="$HERE/Chronosia_Manual.pdf"
cd "$ROOT"

# --- Orden del libro ---
FILES=()
add(){ local g; for g in $1; do [ -f "$g" ] && FILES+=("$g"); done; }
add "00_La_Historia_de_Chronosia.md"
add "01_Como_Dirigir.md"
add "02_El_Semiplano.md"
add "03_Cronopolis.md"
add "Capitulos_Regiones/*.md"
add "14_Arco_de_Barbanegra.md"
add "15_Climax_La_Torre.md"
# --- Apéndices ---
add "01_Introduccion/03_Creacion_Personajes.md"
add "02_Guia_DM/07_Cronologia_Maestra_Campana.md"
add "02_Guia_DM/03_NPCs_Importantes.md"
add "02_Guia_DM/02_Facciones/*.md"
add "02_Guia_DM/04_Cronofagos_Detallado/*.md"
add "02_Guia_DM/06_Nexo_Planar_y_Continuaciones.md"
add "05_Apendices/17_Monstruos_Enemigos.md"
add "06_Recursos/Tablas/21_Objetos_Magicos_Reliquias.md"
add "06_Recursos/Tablas/19_Tablas_Eventos.md"
add "06_Recursos/Tablas/20_Tablas_Tracking_Campana.md"
add "06_Recursos/Tablas/22_Encuentros_Aleatorios_por_Region.md"
add "06_Recursos/Handouts/README.md"

# --- Concatenar: rutas de imagen absolutas + sin emojis ---
: > "$OUT_MD"
for f in "${FILES[@]}"; do
  sed -E "s#\]\((\.\./)*assets/#](${ROOT}/assets/#g" "$f" \
  | perl -CSD -pe '
      s/[\x{1F000}-\x{1FFFF}\x{2300}-\x{23FF}\x{2600}-\x{27BF}\x{2B00}-\x{2BFF}\x{FE00}-\x{FE0F}\x{2049}\x{203C}]//g;
      s/^(\#{1,6})\s+/$1 /;
      s/\*\*\s+/**/g;
      s/[ \t]+$//;
    ' >> "$OUT_MD"
  printf '\n\n---\n\n' >> "$OUT_MD"
done
echo "Markdown del libro: $OUT_MD ($(wc -w < "$OUT_MD") palabras)"

# --- HTML estilizado (a 2 columnas; imprime a PDF para el mejor acabado) ---
pandoc "$OUT_MD" -f markdown -t html5 -s --toc --toc-depth=2 \
  -H "$HERE/dnd-style.html" \
  --metadata title="$TITLE" --metadata subtitle="$SUBTITLE" \
  -o "$OUT_HTML"
echo "HTML: $OUT_HTML  (ábrelo e 'Imprimir → Guardar como PDF' para 2 columnas)"

# --- PDF (xelatex, 1 columna) ---
if command -v xelatex >/dev/null; then
  pandoc "$OUT_MD" -f markdown --pdf-engine=xelatex \
    -H "$HERE/dnd-latex-header.tex" \
    -V geometry:margin=1.6cm -V fontsize=10pt \
    --toc --toc-depth=2 --metadata title="$TITLE" --metadata subtitle="$SUBTITLE" \
    -o "$OUT_PDF" && echo "PDF: $OUT_PDF"
else
  echo "Sin xelatex: usa el HTML e 'Imprimir → Guardar como PDF'."
fi
