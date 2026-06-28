# 📦 Exports — Manual completo de Chronosia

Genera **un único documento** con toda la campaña (texto + imágenes).

## Uso

```bash
cd exports
./build_manual.sh
```

Produce (ignorados por git, se regeneran):
- `Chronosia_Manual_Completo.md` — todo el manual concatenado en un Markdown.
- `Chronosia_Manual_Completo.odt` — documento intermedio.
- `Chronosia_Manual_Completo.pdf` — **el manual en PDF**.

## Requisitos

- **pandoc** (Markdown → ODT).
- **libreoffice / soffice** (ODT → PDF).

Si falta libreoffice, el script deja al menos el Markdown unificado; puedes abrirlo
en Obsidian o convertirlo con otra herramienta.

## Notas

- El script resuelve las rutas de imagen a absolutas, así que las ilustraciones se
  incrustan correctamente.
- Las imágenes de bestiario/objetos están comprimidas (JPG); los mapas van en PNG
  de alta resolución, por lo que el PDF resultante pesa decenas de MB.
- El orden de los capítulos está definido dentro de `build_manual.sh` (variable
  `FILES`); edítalo si quieres incluir/excluir secciones o cambiar el orden.
