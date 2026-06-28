#!/usr/bin/env bash
# Construye el manual de Chronosia como UN único documento con estética de libro D&D
# (sin iconos/emojis). Salidas: HTML estilizado (imprime a PDF desde el navegador para
# el mejor acabado) y un PDF (xelatex si está instalado; si no, LibreOffice como respaldo).
#
# Uso:  cd exports && ./build_manual.sh
# PDF de máxima calidad: instala  texlive-xetex texlive-fonts-recommended
#                                  texlive-latex-recommended texlive-latex-extra
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
TITLE="Chronosia — El Reino del Tiempo Fracturado"
SUBTITLE="Campaña de D&D 5e · Manual completo · v1.0-rc1"
OUT_MD="$HERE/Chronosia_Manual_Completo.md"
OUT_HTML="$HERE/Chronosia_Manual_Completo.html"
OUT_PDF="$HERE/Chronosia_Manual_Completo.pdf"
cd "$ROOT"

# --- Orden de lectura ---
FILES=()
add(){ local g; for g in $1; do [ -f "$g" ] && FILES+=("$g"); done; }
add "00_Indice_Campana.md"
add "01_Introduccion/*.md"
add "02_Guia_DM/01_Dirigir_Campana.md"
add "02_Guia_DM/06_Nexo_Planar_y_Continuaciones.md"
add "02_Guia_DM/05_La_Ascension_del_Conclave.md"
add "02_Guia_DM/07_Cronologia_Maestra_Campana.md"
add "02_Guia_DM/08_Por_Que_Derrotar_Lugartenientes.md"
add "02_Guia_DM/Eventos_Que_Siempre_Ocurren.md"
add "02_Guia_DM/DM_Screen_Una_Pagina.md"
add "02_Guia_DM/03_NPCs_Importantes.md"
add "02_Guia_DM/09_Cronopolis_Capa_Civil.md"
add "02_Guia_DM/02_Facciones/*.md"
add "02_Guia_DM/04_Cronofagos_Detallado/*.md"
add "03_Regiones/*.md"
add "04_Aventuras/00_Estructura_Campana.md"
add "04_Aventuras/Fase_0_Railroad_Inicial/*.md"
add "04_Aventuras/Fase_1_Robos_Traicion/*.md"
add "04_Aventuras/Fase_2_Sandbox_Inicial/*.md"
add "04_Aventuras/Fase_3_Sandbox_Avanzado/*.md"
add "04_Aventuras/Fase_4_Ritual_Completado/*.md"
add "04_Aventuras/Fase_5_Viaje_al_Pasado/*.md"
add "04_Aventuras/Fase_6_Batalla_Final/*.md"
add "05_Apendices/17_Monstruos_Enemigos.md"
add "05_Apendices/Bestiario_Regional/*.md"
add "06_Recursos/Tablas/*.md"
add "06_Recursos/Handouts/*.md"

# --- Concatenar: rutas de imagen absolutas + sin emojis ---
: > "$OUT_MD"
for f in "${FILES[@]}"; do
  sed -E "s#\]\((\.\./)*assets/#](${ROOT}/assets/#g" "$f" \
  | perl -CSD -pe '
      s/[\x{1F000}-\x{1FFFF}\x{2300}-\x{27BF}\x{2B00}-\x{2BFF}\x{FE00}-\x{FE0F}\x{2049}\x{203C}]//g; # emojis (se conservan flechas →)
      s/^(\#{1,6})\s+/$1 /;       # normaliza espacio tras almohadillas
      s/\*\*\s+/**/g;             # arregla "** Texto" tras quitar emoji
      s/[ \t]+$//;                # espacios finales
    ' >> "$OUT_MD"
  printf '\n\n---\n\n' >> "$OUT_MD"
done
echo "Markdown unificado: $OUT_MD ($(wc -w < "$OUT_MD") palabras)"

# --- HTML estilizado (recomendado: abrir e Imprimir -> Guardar como PDF) ---
pandoc "$OUT_MD" -f markdown -t html5 -s --toc --toc-depth=2 \
  -H "$HERE/dnd-style.html" \
  --metadata title="$TITLE" --metadata subtitle="$SUBTITLE" \
  -o "$OUT_HTML"
echo "HTML estilizado: $OUT_HTML  (ábrelo e 'Imprimir -> Guardar como PDF' para el mejor acabado)"

# --- PDF ---
if command -v xelatex >/dev/null; then
  echo "xelatex detectado -> PDF maquetado..."
  pandoc "$OUT_MD" -f markdown --pdf-engine=xelatex \
    -H "$HERE/dnd-latex-header.tex" \
    -V geometry:margin=1.6cm -V fontsize=10pt \
    --toc --toc-depth=2 --metadata title="$TITLE" --metadata subtitle="$SUBTITLE" \
    -o "$OUT_PDF" && echo "PDF (xelatex): $OUT_PDF"
elif command -v soffice >/dev/null || command -v libreoffice >/dev/null; then
  echo "Sin xelatex -> PDF de respaldo con LibreOffice (acabado más plano)..."
  SOFFICE="$(command -v soffice || command -v libreoffice)"
  "$SOFFICE" --headless --convert-to pdf --outdir "$HERE" "$OUT_HTML" >/dev/null 2>&1 \
    && echo "PDF (LibreOffice): $OUT_PDF" \
    || echo "AVISO: LibreOffice no pudo generar el PDF; usa el HTML e imprime a PDF."
else
  echo "Sin xelatex ni LibreOffice: usa el HTML e 'Imprimir -> Guardar como PDF'."
fi
