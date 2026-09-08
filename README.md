# 🌌 Chronosia — El Reino del Tiempo Fracturado

Campaña original y completa de **Dungeons & Dragons 5ª Edición**, escrita siguiendo los estándares de las campañas oficiales de Wizards of the Coast.

> *La campaña de "El Alzamiento de Tiamat" se ha movido a un repositorio aparte (`dnd-campaign-tyrany-dragons`). Aquí solo vive Chronosia.*

---

## 📖 La campaña

**Tipo:** Campaña original · **Niveles:** 3 → 10 · **Duración:** ~14-15 sesiones · **Estructura:** railroad inicial (Fase 0 en Waterdeep) → **sandbox con Reloj** → clímax guiado en la Torre de la Eternidad (4 finales) · **Tema:** tiempo y espacio rotos, dos dioses cautivos, un pueblo partido en dos, y un reloj de campaña que no espera a nadie.

Los PJ investigan un asesinato en Waterdeep que los arrastra a **Chronosia**, un semiplano fracturado anclado entre mundos. Toda la presión la marca **un único motor**: el **Reloj del Ritual** (8 segmentos — a 8/8 la ascensión de Aethernus se consuma y es la derrota). Once lugartenientes gobiernan diez regiones, pero **no hay que derrotarlos a todos**: hay que elegir, ganarse a los pueblos partidos (Anacronistas y Oceánicos), reunir la **llave chroniana** y asaltar la Torre antes de que el Reloj se agote — mientras el pirata Barbanegra intenta usurpar la ascensión por su cuenta. El villano es un clon de Manshoon; el epílogo puede convertir el limbo estabilizado en un **hub planar** (Underdark, Barovia, Avernus, Planos Elementales) para futuras campañas.

**➡️ Empieza por:** [`Chronosia_Campana_Profesional/index.md`](./Chronosia_Campana_Profesional/index.md) — o directamente [La Historia de Chronosia](./Chronosia_Campana_Profesional/00_La_Historia_de_Chronosia.md) y el [Capítulo 1 · Cómo dirigir](./Chronosia_Campana_Profesional/01_Como_Dirigir.md) (la fuente de verdad de las reglas de campaña).

**🌐 Manual navegable:** https://asantolaria.github.io/dnd-campaign-chronosia/ (se despliega solo con cada push a `main`).

---

## 📂 Estructura

```
Chronosia_Campana_Profesional/
├── index.md                        # Portada y navegación (empieza aquí)
├── 00_La_Historia_de_Chronosia.md  # El alma de la campaña
├── 01_Como_Dirigir.md              # El motor: Reloj, Mapa de Puertas, fases (FUENTE DE VERDAD)
├── 02_El_Semiplano.md              # El mundo + FAQ del DM
├── 01_Introduccion/                # Creación de personajes + Fase 0 (Waterdeep, dirigible)
├── 03_Cronopolis.md                # El hub
├── Capitulos_Regiones/             # Las 10 regiones del sandbox (Caps. 4-13)
├── 14_Arco_de_Barbanegra.md        # Los hitos de Teach + la Traición de Serapis
├── 15_Climax_La_Torre.md           # El clímax y los 4 finales
├── 02_Guia_DM/                     # Facciones, PNJs, fichas de lugartenientes, cronología, nexo planar
├── 05_Apendices/                   # Monstruos genéricos + Bestiario Regional
├── 06_Recursos/                    # Tablas, catálogo de objetos, 12 handouts, mapas
├── assets/                         # Arte (⚠️ originales ignorados por git; el espejo web/ sí se versiona)
└── exports/                        # build_manual.sh → manual completo en PDF/HTML
```

---

## 🎨 Arte y manual

- **Prompts de arte** (para Gemini): [`assets/Prompts_Arte_Chronosia.md`](./Chronosia_Campana_Profesional/assets/Prompts_Arte_Chronosia.md) · inventario en [`assets/00_Indice_Visual.md`](./Chronosia_Campana_Profesional/assets/00_Indice_Visual.md) y [`06_Recursos/Mapas/README.md`](./Chronosia_Campana_Profesional/06_Recursos/Mapas/README.md).
- **Las imágenes originales no se versionan** (pesan mucho); las copias optimizadas de `assets/web/` sí, y son las que usan la web y el PDF.
- **Manual en un único documento:** `cd Chronosia_Campana_Profesional/exports && ./build_manual.sh` genera el manual maquetado (PDF con xelatex + HTML). Ver [`exports/README.md`](./Chronosia_Campana_Profesional/exports/README.md).

---

*Uso personal y educativo; las referencias a D&D 5e pertenecen a Wizards of the Coast.*
