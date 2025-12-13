# 🐉 Agente de Desarrollo - El Alzamiento de Tiamat - Sandbox
## *Configuración para Asistente de IA Especializado*

---

> **⚠️ PROPÓSITO:**
> Este archivo define cómo debe comportarse el agente de IA cuando trabaja en el desarrollo de la campaña **El Alzamiento de Tiamat - Sandbox**.

---

## 🎯 **CONTEXTO DE LA CAMPAÑA**

### **Información Básica:**
- **Nombre:** El Alzamiento de Tiamat - Sandbox
- **Sistema:** Dungeons & Dragons 5ª Edición
- **Niveles:** 8-16 (aproximadamente)
- **Duración Estimada:** Variable (depende de adaptación)
- **Tipo:** Sandbox político-militar
- **Tema Central:** Detener el regreso de Tiamat, Consejo de Guerra, decisiones estratégicas

### **Estructura del Proyecto:**
```
El alzamiento de Tiamat - Sandbox/
├── 01_Modificaciones_Personalizadas.md  # Cambios clave respecto a la original
├── 02_Resumen_Campana.md               # Resumen ejecutivo
├── 03_Referencias_Original.md          # Referencias a la campaña original
├── 04_Guia_DM/                         # Documentos del DM
│   ├── 00_Indice_Guia_DM.md
│   ├── 01_Dirigir_Campana.md
│   ├── 02_Facciones.md
│   ├── 03_NPCs_Importantes.md
│   ├── 04_Sistema_Tracking.md
│   ├── 05_Sistema_Consejo_Guerra.md
│   └── 06_Asistentes_Consejo.md
├── 05_Aventuras/                       # Aventuras y misiones
│   ├── 00_Estructura_Aventuras.md
│   ├── 01_Episodio_1_Consejo_Aguas_Profundas.md
│   ├── 04A-04C_Mision_Culto_Contraataca_*.md
│   ├── AO01-AO06_Mision_*.md  # Misiones adicionales oficiales
│   └── AN03-AN14_Mision_*.md  # Misiones adicionales no oficiales
└── 06_Recursos/                        # Tablas y recursos
    └── Tablas/
        ├── 00_Indice_Tablas.md
        ├── 01_Tabla_Puntuacion_Consejo.md
        └── 02_Tabla_Misiones_Consejo.md
```

---

## 📋 **REGLAS DE TRABAJO**

### **1. Gestión de Archivos y Referencias**

#### **Nomenclatura de Archivos:**
- **Episodios:** `01_Episodio_X_[Titulo].md`
- **Misiones Oficiales:** `04X_Mision_[Nombre].md` (04A, 04B, 04C)
- **Misiones Adicionales Oficiales:** `AOXX_Mision_[Nombre].md` (AO01-AO06)
- **Misiones Adicionales No Oficiales:** `ANXX_Mision_[Nombre].md` (AN03-AN14)
- **Documentos del DM:** `XX_[Nombre_Descriptivo].md`
- **Tablas:** `XX_Tabla_[Nombre].md`

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
- **Tablas centralizadas** en `06_Recursos/Tablas/`
- **Sistema de Tracking** en `04_Guia_DM/04_Sistema_Tracking.md`
- **Tabla de Puntuación** en `06_Recursos/Tablas/01_Tabla_Puntuacion_Consejo.md`
- **Tabla de Misiones** en `06_Recursos/Tablas/02_Tabla_Misiones_Consejo.md`

#### **Cuando Añadir Información:**
- **Nueva información:** Crear o actualizar el documento apropiado
- **Información relacionada:** Añadir referencia al documento fuente
- **Información duplicada:** Eliminar duplicado y añadir referencia

#### **Documentos Maestros (Fuentes de Verdad):**
- **Sistema del Consejo:** `04_Guia_DM/05_Sistema_Consejo_Guerra.md`
- **Sistema de Tracking:** `04_Guia_DM/04_Sistema_Tracking.md`
- **Tabla de Puntuación:** `06_Recursos/Tablas/01_Tabla_Puntuacion_Consejo.md`
- **Tabla de Misiones:** `06_Recursos/Tablas/02_Tabla_Misiones_Consejo.md`
- **Estructura de Aventuras:** `05_Aventuras/00_Estructura_Aventuras.md`
- **Facciones:** `04_Guia_DM/02_Facciones.md`
- **NPCs:** `04_Guia_DM/03_NPCs_Importantes.md`
- **Asistentes del Consejo:** `04_Guia_DM/06_Asistentes_Consejo.md`

---

### **3. Actualización de Documentos Relacionados**

#### **Cuando Modificas un Documento:**
1. **Verifica referencias cruzadas** - Actualiza documentos que referencian al modificado
2. **Actualiza índices** - Si hay cambios estructurales
3. **Actualiza navegación** - Si cambias rutas o nombres
4. **Mantén coherencia** - Asegúrate de que la información sea consistente

#### **Documentos que Deben Actualizarse Juntos:**
- **Tabla de Puntuación** ↔ **Sistema de Tracking** ↔ **Sistema del Consejo**
- **Tabla de Misiones** ↔ **Estructura de Aventuras** ↔ **Misiones individuales**
- **Facciones** ↔ **NPCs** ↔ **Asistentes del Consejo**
- **Modificaciones** ↔ **Resumen** ↔ **Referencias Originales**

---

### **4. Estructura de Misiones y Concilios**

#### **Concilios de la Campaña:**
- **Primer Concilio:** Nivel 8-9 (Inicio)
- **Segundo Concilio:** Nivel 9-11
- **Tercer Concilio:** Nivel 11-13
- **Cuarto Concilio y Final:** Nivel 13-16

#### **Tipos de Misiones:**
- **Oficiales:** Misiones principales de la campaña original (consultar PDF o 5e.tools)
- **Adicionales Oficiales (AO01-AO06):** Misiones secundarias de la original (consultar PDF o 5e.tools)
- **Adicionales No Oficiales (AN03-AN14):** Misiones nuevas desarrolladas en esta versión

#### **Al Trabajar con Misiones:**
- **Misiones oficiales** siempre están disponibles cuando corresponda
- **Misiones adicionales** pueden bloquearse mutuamente (sistema de nodos)
- **Cada misión** debe indicar su código, nivel, tipo y eventos del Consejo que afecta
- **Las misiones desarrolladas** están en `05_Aventuras/` con su código en el nombre

---

### **5. Sistema de Tracking y Puntuación**

#### **Tablas Centralizadas:**
- **Ubicación:** `06_Recursos/Tablas/`
- **Tabla de Puntuación:** `01_Tabla_Puntuacion_Consejo.md` - Medidores y eventos
- **Tabla de Misiones:** `02_Tabla_Misiones_Consejo.md` - Estado y disponibilidad

#### **Al Actualizar Tracking:**
- **NO crear tablas nuevas** en otros documentos
- **SÍ añadir referencias** a las tablas centralizadas
- **SÍ actualizar las tablas** cuando cambie información relevante
- **SÍ mantener coherencia** entre Sistema de Tracking y Tabla de Puntuación

---

### **6. Sistema de Ramificaciones de Misiones**

#### **Nodos de Decisión:**
Las misiones adicionales están organizadas en nodos donde elegir una bloquea otras:
- **Nodo 1:** Defensa del Norte (AN03, AN14)
- **Nodo 2:** Diplomacia (AN10, AN11)
- **Nodo 3:** Alianza Dracónica (AN05, AN12, AN06)
- **Nodo 4:** Inteligencia (AN04, AN07)
- **Nodo 5:** Preparación Final (AN09, AN08)

#### **Al Trabajar con Ramificaciones:**
- **Misiones oficiales** nunca se bloquean
- **Misiones adicionales oficiales (AO01-AO06)** nunca se bloquean
- **Misiones adicionales no oficiales (AN03-AN14)** pueden bloquearse dentro de su nodo
- **Actualizar tabla de misiones** cuando se bloqueen misiones

---

### **7. Referencias a la Campaña Original**

#### **Documentos de Referencia:**
- **PDF Original:** `D&D El Alzamiento de Tiamat.pdf.pdf` (en la raíz)
- **Referencia Online:** https://5e.tools/adventure.html#rot,-1
- **Guía de Referencias:** `03_Referencias_Original.md`

#### **Al Referenciar la Original:**
- **Misiones oficiales** deben indicar que se consultan en PDF/5e.tools
- **NO desarrollar** misiones oficiales que ya existen en la original
- **SÍ desarrollar** misiones adicionales nuevas (AN03-AN14)
- **Mantener coherencia** con la narrativa de la original

---

## 🎭 **ESTILO Y TONO**

### **Para Documentos del DM:**
- **Claro y conciso** - Información práctica y accesible
- **Bien organizado** - Secciones claras, tablas formateadas
- **Referencias cruzadas** - Enlaces a documentos relacionados
- **Ejemplos prácticos** - Cuando sea útil para el DM

### **Para Contenido Narrativo:**
- **Inmersivo y épico** - Descripciones que reflejen la escala de la amenaza
- **Enfocado en decisiones** - Las elecciones de los jugadores importan
- **Consecuencias reales** - Las acciones tienen impacto en el mundo
- **Tensión política** - El Consejo de Guerra es un elemento central

---

## 🔍 **BÚSQUEDA Y NAVEGACIÓN**

### **Documentos Clave para Consultar:**

#### **Estructura General:**
- `README.md` - Visión general de la campaña
- `02_Resumen_Campana.md` - Resumen ejecutivo
- `01_Modificaciones_Personalizadas.md` - Cambios clave
- `05_Aventuras/00_Estructura_Aventuras.md` - Estructura de misiones

#### **Sistemas de Juego:**
- `04_Guia_DM/05_Sistema_Consejo_Guerra.md` - Sistema del Consejo
- `04_Guia_DM/04_Sistema_Tracking.md` - Sistema de tracking
- `06_Recursos/Tablas/01_Tabla_Puntuacion_Consejo.md` - Tabla de puntuación
- `06_Recursos/Tablas/02_Tabla_Misiones_Consejo.md` - Tabla de misiones

#### **Contenido Narrativo:**
- `04_Guia_DM/02_Facciones.md` - Facciones y organizaciones
- `04_Guia_DM/03_NPCs_Importantes.md` - Personajes clave
- `04_Guia_DM/06_Asistentes_Consejo.md` - Miembros del Consejo
- `05_Aventuras/` - Misiones desarrolladas

---

## ⚠️ **REGLAS CRÍTICAS**

### **NO Hacer:**
- ❌ **NO duplicar información** - Usar referencias en su lugar
- ❌ **NO crear tablas** fuera de `06_Recursos/Tablas/`
- ❌ **NO modificar la tabla de puntuación** sin actualizar el sistema de tracking
- ❌ **NO cambiar nombres de archivos** sin actualizar referencias
- ❌ **NO crear documentos** sin verificar si la información ya existe
- ❌ **NO desarrollar misiones oficiales** - Solo referenciarlas

### **SÍ Hacer:**
- ✅ **SÍ verificar referencias** antes de crear nuevos documentos
- ✅ **SÍ actualizar documentos relacionados** cuando modifiques uno
- ✅ **SÍ usar las tablas centralizadas** para tracking
- ✅ **SÍ mantener coherencia** entre sistemas
- ✅ **SÍ añadir enlaces** a misiones desarrolladas en las tablas
- ✅ **SÍ usar códigos de misión** en nombres de archivos (04A, AO01, AN03, etc.)

---

## 📊 **FLUJO DE TRABAJO RECOMENDADO**

### **Al Crear Nuevo Contenido:**
1. **Verificar** si la información ya existe
2. **Identificar** el documento apropiado o crear uno nuevo
3. **Añadir referencias** a documentos relacionados
4. **Actualizar índices** si es necesario
5. **Actualizar tablas** si afecta a tracking o misiones

### **Al Modificar Contenido Existente:**
1. **Leer el documento** completo para entender el contexto
2. **Identificar documentos relacionados** que puedan necesitar actualización
3. **Realizar cambios** manteniendo el formato y estilo
4. **Actualizar referencias cruzadas**
5. **Verificar coherencia** con tablas y sistemas

### **Al Integrar Información:**
1. **Identificar** dónde debe ir la información
2. **Eliminar duplicados** y añadir referencias
3. **Actualizar** documentos que referencian la información
4. **Verificar** que todas las referencias funcionen

---

## 🎯 **CONTEXTO NARRATIVO CRÍTICO**

### **Información Clave (Solo para el DM):**
- **El Culto del Dragón** busca resucitar a Tiamat mediante rituales
- **El Consejo de Aguas Profundas** coordina la respuesta
- **Las decisiones de los jugadores** afectan los medidores del Consejo
- **El ritual avanza** con el tiempo si no se detiene
- **Múltiples frentes** requieren que los jugadores elijan prioridades

### **Sistemas Críticos:**
- **Medidores del Consejo:** 16 medidores (10 oficiales + 6 nuevos)
- **Sistema de Eventos:** Eventos que modifican los medidores
- **Sistema de Ramificaciones:** Nodos de decisión para misiones adicionales
- **Progreso del Ritual:** Avanza si no se detiene
- **Resolución Final:** Depende de los medidores del Consejo

---

## 🔗 **REFERENCIAS RÁPIDAS**

### **Documentos Maestros:**
- **Sistema del Consejo:** `04_Guia_DM/05_Sistema_Consejo_Guerra.md`
- **Sistema de Tracking:** `04_Guia_DM/04_Sistema_Tracking.md`
- **Tabla de Puntuación:** `06_Recursos/Tablas/01_Tabla_Puntuacion_Consejo.md`
- **Tabla de Misiones:** `06_Recursos/Tablas/02_Tabla_Misiones_Consejo.md`
- **Estructura de Aventuras:** `05_Aventuras/00_Estructura_Aventuras.md`

### **Guías del DM:**
- **Índice:** `04_Guia_DM/00_Indice_Guia_DM.md`
- **Dirigir Campaña:** `04_Guia_DM/01_Dirigir_Campana.md`
- **Facciones:** `04_Guia_DM/02_Facciones.md`
- **NPCs:** `04_Guia_DM/03_NPCs_Importantes.md`
- **Asistentes del Consejo:** `04_Guia_DM/06_Asistentes_Consejo.md`

### **Información General:**
- **Modificaciones:** `01_Modificaciones_Personalizadas.md`
- **Resumen:** `02_Resumen_Campana.md`
- **Referencias Original:** `03_Referencias_Original.md`
- **README:** `README.md`

### **Misiones Desarrolladas:**
- **Episodio 1:** `05_Aventuras/01_Episodio_1_Consejo_Aguas_Profundas.md`
- **Culto Contraataca I:** `05_Aventuras/04A_Mision_Culto_Contraataca_I_Emboscadas.md`
- **Culto Contraataca II:** `05_Aventuras/04B_Mision_Culto_Contraataca_II_Ofensiva.md`
- **Culto Contraataca III:** `05_Aventuras/04C_Mision_Culto_Contraataca_III_Desesperacion.md`
- **Misiones Adicionales Oficiales:** `05_Aventuras/AO01_Mision_*.md` a `AO06_Mision_*.md`
- **Misiones Adicionales No Oficiales:** `05_Aventuras/AN03_Mision_*.md` a `AN14_Mision_*.md`

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
- Enlaces a misiones desarrolladas en tablas

### **Formato de Secciones:**
- Headers con emojis para identificación visual
- Índices de navegación en documentos largos
- Referencias cruzadas claras

### **Códigos de Misiones:**
- **Oficiales:** 01, 02, 03, 04A, 04B, 04C, 05, 06, 07, 08
- **Adicionales Oficiales:** AO01, AO02, AO03, AO04, AO05, AO06
- **Adicionales No Oficiales:** AN03, AN04, AN05, AN06, AN07, AN08, AN09, AN10, AN11, AN12, AN13, AN14

---

*Este agente está configurado para mantener la coherencia, evitar redundancia y facilitar el desarrollo de la campaña El Alzamiento de Tiamat - Sandbox.* 🐉✨

