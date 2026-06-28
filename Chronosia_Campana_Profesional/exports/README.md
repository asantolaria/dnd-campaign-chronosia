# 📦 Exports — Manual de Chronosia

Genera el manual de la campaña (texto + imágenes) en **dos documentos** para que
cada uno tenga un tamaño manejable:

- **Chronosia_Manual_Nucleo** — el "libro base": lore, guías del DM, el motor de
  campaña (Reloj y puertas), regiones, facciones, lugartenientes, bestiario,
  objetos y tablas. Es lo que se lee para **entender y dirigir** la campaña.
- **Chronosia_Apendice_Sesiones** — el "módulo de aventura": la prep **sesión a
  sesión** (Fases 0-4).

## Uso

```bash
cd exports
./build_manual.sh
```

Produce (ignorados por git, se regeneran) para cada documento:
- `*.md` — el documento concatenado en Markdown.
- `*.html` — versión estilizada **a dos columnas**.
- `*.pdf` — PDF maquetado (xelatex), a **una columna**.

## Dos densidades de PDF

- **PDF xelatex (una columna):** el que genera el script automáticamente. Robusto,
  las tablas siempre caben. El núcleo ronda las ~300 páginas.
- **PDF a dos columnas (densidad tipo *Curse of Strahd*, ~mitad de páginas):** abre
  el `*.html` en el navegador e **Imprimir → Guardar como PDF**. El HTML ya está
  maquetado a dos columnas (A4). Es el camino recomendado para el acabado más
  compacto y bonito. *(No se hace en xelatex porque las `longtable` de pandoc no
  conviven con el modo de dos columnas.)*

## Requisitos

- **pandoc** (Markdown → HTML/PDF).
- **xelatex** (`texlive-xetex texlive-fonts-recommended texlive-latex-recommended
  texlive-latex-extra`) para el PDF maquetado. Si falta, el script usa LibreOffice
  de respaldo o, en último caso, deja el HTML para imprimir a PDF.

## Notas

- El script resuelve las rutas de imagen a absolutas (las ilustraciones se
  incrustan). Los mapas en PNG de alta resolución hacen que el núcleo pese decenas
  de MB; el apéndice de sesiones es ligero.
- El orden y el reparto de capítulos (núcleo vs sesiones) están en las listas
  `NUCLEO` y `SESIONES` de `build_manual.sh`; edítalas para mover secciones.
