# 🌌 Chronosia — El Reino del Tiempo Fracturado

Campaña original y completa de **Dungeons & Dragons 5ª Edición**, escrita siguiendo los estándares de las campañas oficiales de Wizards of the Coast.

> *La campaña de "El Alzamiento de Tiamat" se ha movido a un repositorio aparte (`dnd-campaign-tyrany-dragons`). Aquí solo vive Chronosia.*

---

## 📖 La campaña

**Tipo:** Campaña original · **Niveles:** 3 → 10 · **Estructura:** railroad inicial → sandbox → clímax (6 fases) · **Tema:** tiempo y espacio rotos, guerra entre lugartenientes, ascensión divina y un **nexo entre planos**.

Los PJ investigan un asesinato en Waterdeep que los arrastra a **Chronosia**, un semiplano fracturado anclado entre mundos. Deben derrotar a los 12 lugartenientes manteniendo el **balance temporal/dimensional**, descubrir que el villano es un clon de Manshoon, y decidir el destino del limbo — que al estabilizarse se convierte en un **hub planar** (puertas al Underdark, Barovia, Avernus y los Planos Elementales) desde el que lanzar futuras campañas.

**➡️ Empieza por:** [`Chronosia_Campana_Profesional/00_Indice_Campana.md`](./Chronosia_Campana_Profesional/00_Indice_Campana.md)

---

## 📂 Estructura

```
Chronosia_Campana_Profesional/
├── 00_Indice_Campana.md          # Índice maestro (empieza aquí)
├── 01_Introduccion/              # Resumen, guía rápida, creación de personajes
├── 02_Guia_DM/                   # Dirigir la campaña, facciones, lugartenientes,
│                                 #   nexo planar, NPCs, capa civil de Cronópolis
├── 03_Regiones/                  # Geografía y regiones
├── 04_Aventuras/                 # 6 fases (Fase 0–6), sesión a sesión
├── 05_Apendices/                 # Monstruos + Bestiario_Regional (villanos, bestias, NPCs)
├── 06_Recursos/                  # Tablas, objetos mágicos, handouts
├── assets/                       # Arte (mapas, lugartenientes, NPCs, reliquias) + prompts
│                                 #   ⚠️ imágenes ignoradas por git; ver Prompts_Arte_Chronosia.md
└── exports/                      # build_manual.sh → manual completo en PDF/HTML
```

---

## 🎨 Arte y manual

- **Prompts de arte** (para Gemini): [`assets/Prompts_Arte_Chronosia.md`](./Chronosia_Campana_Profesional/assets/Prompts_Arte_Chronosia.md) · índice visual en [`assets/00_Indice_Visual.md`](./Chronosia_Campana_Profesional/assets/00_Indice_Visual.md).
- **Las imágenes no se versionan** (pesan mucho); viven en el vault y se regeneran con los prompts.
- **Manual en un único documento:** `cd Chronosia_Campana_Profesional/exports && ./build_manual.sh` genera el manual maquetado estilo libro D&D (PDF con xelatex + HTML). Ver [`exports/README.md`](./Chronosia_Campana_Profesional/exports/README.md).

---

## 🛠️ Configuración

- [`.cursorrules`](./.cursorrules) — reglas del asistente de IA para desarrollo de campañas.

---

*Estado: **v1.0-rc1**. Uso personal y educativo; las referencias a D&D 5e pertenecen a Wizards of the Coast.*
