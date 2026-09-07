# 🌌 Chronosia - El Reino del Tiempo Fracturado
## *Campaña de D&D 5e · nivel 3→10 · sandbox con Reloj y clímax en la Torre de la Eternidad*

---

## 📑 **POR DÓNDE EMPEZAR**

1. **[La Historia de Chronosia](00_La_Historia_de_Chronosia.md)** — el alma de la campaña; léela primero, entera.
2. **[Capítulo 1 · Cómo dirigir](01_Como_Dirigir.md)** — el motor: el Reloj del Ritual, el Mapa de Puertas, las fases y los villanos críticos. **Es la fuente de verdad de las reglas de campaña.**
3. **[index.md](index.md)** — la portada de la web/manual con la navegación completa.

---

## 📚 **ESTRUCTURA REAL DEL PROYECTO**

| Bloque | Dónde | Qué contiene |
|---|---|---|
| **Núcleo** | `00`–`03` | Historia, cómo dirigir, el semiplano, Cronópolis (hub) |
| **Regiones** | `Capitulos_Regiones/` (Caps. 4-13) | Las 10 zonas del sandbox, cada una con su pieza de la verdad |
| **Arcos** | `14`–`15` | El arco de Barbanegra + la Traición de Serapis, y el clímax en la Torre (4 finales) |
| **Guía del DM** | `02_Guia_DM/` | Facciones, PNJs, fichas de los Cronófagos (01-13), cronología, nexo planar |
| **Introducción** | `01_Introduccion/` | Creación de personajes |
| **Apéndices** | `05_Apendices/` | Monstruos genéricos y Bestiario Regional |
| **Recursos** | `06_Recursos/` | Tablas (eventos, tracking, objetos, encuentros, reconocimiento, rumores), handouts y mapas |
| **Arte** | `assets/` | Mapas, bestiario ilustrado, prompts de arte |
| **Semillas del DM** | `70_Ideas_Creativas_DM.md` | Ideas opcionales (no entra en el libro exportado) |

---

### **📕 Libro de campaña (un solo archivo)**

El script **`build_libro_campana.py`** genera un único archivo con toda la campaña, tipo libro, para búsqueda global (Ctrl+F) o lectura en un solo documento.

- **Uso:** `python build_libro_campana.py` → genera `Libro_Campana_Chronosia.md`
- **Con índice en navegador:** `python build_libro_campana.py --html` → genera además `.html` con índice clicable
- **PDF:** desde el `.md` puedes exportar con *pandoc*: `pandoc Libro_Campana_Chronosia.md -o libro.pdf --toc`

---

*Campaña completa y jugable. Las reglas de campaña (Reloj, puertas, hitos) tienen una sola fuente de verdad: el Capítulo 1.*
