# 🎲 Agente de Desarrollo - Campaña Chronosia
## *Configuración para Asistente de IA Especializado*

---

> **⚠️ PROPÓSITO:**
> Este archivo define cómo debe comportarse el agente de IA cuando trabaja en el desarrollo de la campaña **Chronosia - El Reino del Tiempo Fracturado**.

---

## 🎯 **CONTEXTO DE LA CAMPAÑA**

### **Información Básica:**
- **Nombre:** Chronosia - El Reino del Tiempo Fracturado
- **Sistema:** Dungeons & Dragons 5ª Edición
- **Niveles:** 3-15
- **Duración Estimada:** 15 sesiones
- **Tipo:** Sandbox con elementos de railroad
- **Tema Central:** Manipulación temporal/dimensional, guerra civil entre lugartenientes, ascensión divina

### **Estructura del Proyecto:**
```
Chronosia_Campana_Profesional/
├── 00_Esquemas/          # Diagramas Mermaid
├── 01_Introduccion/      # Resumen, guía rápida, creación de personajes
├── 02_Guia_DM/          # Documentos del DM (lugartenientes, sistemas, timeline)
├── 03_Regiones/         # Geografía y regiones de Chronosia
├── 04_Aventuras/        # Estructura por fases (0-4)
├── 05_Apendices/        # Monstruos, tesoros, recompensas
└── 06_Recursos/         # Tablas, mapas, handouts
```

---

## 📋 **REGLAS DE TRABAJO**

### **1. Gestión de Archivos y Referencias**

#### **Nomenclatura de Archivos:**
- **Guías Generales de Fase:** `00_Guia_General_Fase_X.md`
- **Sesiones Específicas:** `XX_Sesion_Y_[Titulo].md`
- **Documentos del DM:** `XX_[Nombre_Descriptivo].md`
- **Tablas:** `XX_Tablas_[Nombre].md`

#### **Referencias entre Documentos:**
- **SIEMPRE** usa rutas relativas desde el archivo actual
- **SIEMPRE** verifica que los enlaces apunten a archivos existentes
- **SIEMPRE** actualiza referencias cuando mueves o renombras archivos
- **Formato de enlaces:** `[Texto](../Ruta/Relativa/Archivo.md)` o `[Texto](./Archivo.md)`

#### **Estructura de Documentos:**
- **Índice de navegación** al inicio (si el documento es largo)
- **Referencias cruzadas** a documentos relacionados
- **Secciones claramente marcadas** con headers
- **Tablas formateadas** correctamente en Markdown

---

### **2. Gestión de Información Redundante**

#### **Principio de Fuente Única:**
- **NO duplicar información** - Si existe en un documento, referenciarlo
- **Tablas centralizadas** en `06_Recursos/Tablas/20_Tablas_Tracking_Campana.md`
- **Timeline maestro** en `02_Guia_DM/07_Cronologia_Maestra_Campana.md`
- **Información de lugartenientes** en `02_Guia_DM/04_Cronofagos_Detallado.md`

#### **Cuando Añadir Información:**
- **Nueva información:** Crear o actualizar el documento apropiado
- **Información relacionada:** Añadir referencia al documento fuente
- **Información duplicada:** Eliminar duplicado y añadir referencia

#### **Documentos Maestros (Fuentes de Verdad):**
- **Timeline:** `07_Cronologia_Maestra_Campana.md`
- **Sistema de Puntos:** `06_Eventos_Ascension_Conclave.md`
- **Tracking:** `20_Tablas_Tracking_Campana.md`
- **Lugartenientes:** `04_Cronofagos_Detallado.md`
- **Regiones:** `08_Geografia_y_Regiones_de_Chronosia.md`

---

### **3. Actualización de Documentos Relacionados**

#### **Cuando Modificas un Documento:**
1. **Verifica referencias cruzadas** - Actualiza documentos que referencian al modificado
2. **Actualiza índices** - Si hay cambios estructurales
3. **Actualiza navegación** - Si cambias rutas o nombres
4. **Mantén coherencia** - Asegúrate de que la información sea consistente

#### **Documentos que Deben Actualizarse Juntos:**
- **Timeline maestro** ↔ **Guías de fases** ↔ **Cronología de eventos**
- **Sistema de puntos** ↔ **Tablas de tracking** ↔ **Diagramas Mermaid**
- **Lugartenientes** ↔ **Regiones** ↔ **Misiones**
- **Resolución final** ↔ **Tablas de tracking** ↔ **Guías de clímax**

---

### **4. Estructura de Fases**

#### **Fases de la Campaña:**
- **Fase 0:** Sesiones 1-3 (Railroad Inicial)
- **Fase 1:** Sesiones 4-6 (Robos y Traición)
- **Fase 2:** Sesiones 6-9 (Sandbox Inicial)
- **Fase 3:** Sesiones 9-12 (Sandbox Avanzado)
- **Fase 4:** Sesiones 13-15 (Clímax)

#### **Al Trabajar con Fases:**
- **Cada fase tiene su carpeta** en `04_Aventuras/Fase_X_.../`
- **Cada fase tiene una guía general** `00_Guia_General_Fase_X.md`
- **Las sesiones individuales** están en archivos separados
- **El timeline maestro** referencia a las guías de fase

---

### **5. Sistema de Tracking**

#### **Tablas Centralizadas:**
- **Ubicación:** `06_Recursos/Tablas/20_Tablas_Tracking_Campana.md`
- **Contiene:** Puntos de ascensión, progresión del ritual, balance, regiones, niveles, artefactos, lugartenientes, resolución final

#### **Al Actualizar Tracking:**
- **NO crear tablas nuevas** en otros documentos
- **SÍ añadir referencias** a las tablas centralizadas
- **SÍ actualizar las tablas** cuando cambie información relevante

---

### **6. Diagramas Mermaid**

#### **Estructura Modular:**
- **Diagrama principal:** `00_Esquema_Campana_Mermaid.md`
- **Diagramas específicos:** `00_Esquemas/01_Sandbox.md`, `02_Ascension_Conclave.md`, etc.
- **Navegación:** Diagramas genéricos → Diagramas detallados

#### **Al Trabajar con Diagramas:**
- **Mantén la navegación** entre diagramas
- **Actualiza diagramas** cuando cambie la estructura
- **Referencia diagramas** en documentos relacionados

---

### **7. Gestión de Tareas**

#### **Archivo de Tareas:**
- **Ubicación:** `00_Plan_Desarrollo_Campana.md` (en la raíz de Chronosia_Campana_Profesional/)
- **Formato:** Lista de tareas con `[ ]` (pendiente) o `[x]` (completada)

#### **Al Identificar Tareas:**
- **Añadir inmediatamente** al plan de desarrollo
- **Organizar por categorías** (Simplificación, Expansión, Artefactos, etc.)
- **Marcar como completada** cuando se termine
- **Mover a "Tareas Completadas"** con fecha

---

## 🎭 **ESTILO Y TONO**

### **Para Documentos del DM:**
- **Claro y conciso** - Información práctica y accesible
- **Bien organizado** - Secciones claras, tablas formateadas
- **Referencias cruzadas** - Enlaces a documentos relacionados
- **Ejemplos prácticos** - Cuando sea útil para el DM

### **Para Contenido Narrativo:**
- **Inmersivo y evocador** - Descripciones ricas y detalladas
- **Original y único** - Evitar lo genérico
- **Enfocado en personajes** - Conexiones emocionales
- **Dilemas significativos** - Decisiones que importan

---

## 🔍 **BÚSQUEDA Y NAVEGACIÓN**

### **Documentos Clave para Consultar:**

#### **Estructura General:**
- `README.md` - Visión general de la campaña
- `04_Aventuras/00_Estructura_Campana.md` - Estructura de fases
- `02_Guia_DM/07_Cronologia_Maestra_Campana.md` - Timeline maestro

#### **Sistemas de Juego:**
- `02_Guia_DM/05_La_Ascension_del_Conclave.md` - Sistema de competencia + Resolución final
- `02_Guia_DM/06_Eventos_Ascension_Conclave.md` - Sistema de puntos
- `06_Recursos/Tablas/20_Tablas_Tracking_Campana.md` - Tablas de tracking

#### **Contenido Narrativo:**
- `02_Guia_DM/04_Cronofagos_Detallado.md` - Lugartenientes
- `03_Regiones/08_Geografia_y_Regiones_de_Chronosia.md` - Regiones
- `02_Guia_DM/09_Escenas_de_Revelacion.md` - Escenas de revelación

---

## ⚠️ **REGLAS CRÍTICAS**

### **NO Hacer:**
- ❌ **NO duplicar información** - Usar referencias en su lugar
- ❌ **NO crear tablas** fuera de `06_Recursos/Tablas/`
- ❌ **NO modificar el timeline maestro** sin actualizar guías de fase
- ❌ **NO cambiar nombres de archivos** sin actualizar referencias
- ❌ **NO crear documentos** sin verificar si la información ya existe

### **SÍ Hacer:**
- ✅ **SÍ verificar referencias** antes de crear nuevos documentos
- ✅ **SÍ actualizar documentos relacionados** cuando modifiques uno
- ✅ **SÍ usar las tablas centralizadas** para tracking
- ✅ **SÍ mantener coherencia** con el timeline maestro
- ✅ **SÍ añadir tareas** al plan de desarrollo cuando se identifiquen

---

## 📊 **FLUJO DE TRABAJO RECOMENDADO**

### **Al Crear Nuevo Contenido:**
1. **Verificar** si la información ya existe
2. **Identificar** el documento apropiado o crear uno nuevo
3. **Añadir referencias** a documentos relacionados
4. **Actualizar índices** si es necesario
5. **Añadir tareas** al plan de desarrollo si quedan pendientes

### **Al Modificar Contenido Existente:**
1. **Leer el documento** completo para entender el contexto
2. **Identificar documentos relacionados** que puedan necesitar actualización
3. **Realizar cambios** manteniendo el formato y estilo
4. **Actualizar referencias cruzadas**
5. **Verificar coherencia** con el timeline maestro

### **Al Integrar Información:**
1. **Identificar** dónde debe ir la información
2. **Eliminar duplicados** y añadir referencias
3. **Actualizar** documentos que referencian la información
4. **Verificar** que todas las referencias funcionen

---

## 🎯 **CONTEXTO NARRATIVO CRÍTICO**

### **Información Ultra-Secreta (Solo para el DM):**
- **Manshoon está recluido** ejecutando ritual de ascensión divina
- **NO sabe** de las traiciones entre lugartenientes
- **Edward Teach** es el único que sospecha y puede robar poder
- **La Ascensión del Cónclave** surgió orgánicamente, no fue planeada

### **Sistemas Críticos:**
- **Balance Temporal/Dimensional:** Debe mantenerse equilibrado
- **Sistema de Puntos:** 15 puntos = Supremo (máximo 3)
- **Progresión del Ritual:** Avanza constantemente (85% → 100%)
- **Resolución Final:** Se calcula antes de Sesión 13

---

## 🔗 **REFERENCIAS RÁPIDAS**

### **Documentos Maestros:**
- Timeline: `02_Guia_DM/07_Cronologia_Maestra_Campana.md`
- Tracking: `06_Recursos/Tablas/20_Tablas_Tracking_Campana.md`
- Lugartenientes: `02_Guia_DM/04_Cronofagos_Detallado.md`
- Sistema de Competencia: `02_Guia_DM/05_La_Ascension_del_Conclave.md`

### **Guías de Fases:**
- Fase 0: `04_Aventuras/Fase_0_Railroad_Inicial/00_Guia_General_Fase_0.md`
- Fase 1: `04_Aventuras/Fase_1_Robos_Traicion/00_Guia_General_Fase_1.md`
- Fase 2: `04_Aventuras/Fase_2_Sandbox_Inicial/00_Guia_General_Fase_2.md`
- Fase 3: `04_Aventuras/Fase_3_Sandbox_Avanzado/00_Guia_General_Fase_3.md`
- Fase 4: `04_Aventuras/Fase_4_Climax/00_Guia_General_Fase_4.md`

### **Diagramas:**
- Principal: `00_Esquema_Campana_Mermaid.md`
- Sandbox: `00_Esquemas/01_Sandbox.md`
- Ascensión: `00_Esquemas/02_Ascension_Conclave.md`
- Torre: `00_Esquemas/03_Torre_Eternidad.md`
- Decisiones: `00_Esquemas/04_Decisiones_Criticas.md`

---

## 📝 **CONVENCIONES DE CÓDIGO**

### **Formato de Tablas:**
- Usar formato Markdown estándar
- Encabezados claros
- Datos consistentes
- Referencias a otras tablas cuando sea apropiado

### **Formato de Enlaces:**
- Rutas relativas desde el archivo actual
- Texto descriptivo en el enlace
- Verificar que los archivos existan

### **Formato de Secciones:**
- Headers con emojis para identificación visual
- Índices de navegación en documentos largos
- Referencias cruzadas claras

---

*Este agente está configurado para mantener la coherencia, evitar redundancia y facilitar el desarrollo de la campaña Chronosia.* 🎲✨

