# 🎲 Sistema de Simulación de Campañas D&D
## *Herramienta Reutilizable para Simular Progresión de Campañas*

---

## 📋 **PROPÓSITO**

Este sistema permite simular el progreso de cualquier campaña de D&D basándose en:
- **Eventos automáticos** (cronología fija)
- **Acciones de los PJ** (decisiones variables)
- **Sistemas de balance** (mecánicas críticas)
- **Progresión de niveles** (desarrollo de personajes)
- **Desbloqueos** (acceso a contenido)

---

## 🎯 **COMPONENTES DEL SISTEMA**

### **1. 📅 Cronología Maestra**
- **Eventos Fijos**: Suceden independientemente de los PJ
- **Eventos Variables**: Dependen de las acciones de los PJ
- **Timing**: Cuándo ocurre cada evento
- **Dependencias**: Qué eventos requieren otros eventos previos

### **2. ⚖️ Sistemas de Balance**
- **Mecánicas Críticas**: Sistemas que afectan directamente a los PJ
- **Consecuencias**: Qué pasa cuando se rompe el balance
- **Restauraciones**: Cómo se puede restaurar el equilibrio
- **Escalado**: Cómo empeoran las consecuencias

### **3. 🗺️ Sistema de Desbloqueos**
- **Regiones/Contenido**: Qué se desbloquea y cuándo
- **Requisitos**: Qué se necesita para desbloquear
- **Progresión**: Orden lógico de desbloqueos
- **Alternativas**: Múltiples caminos para el mismo objetivo

### **4. 📊 Progresión de Niveles**
- **Puntos de Subida**: Cuándo y cómo suben de nivel
- **Requisitos**: Qué necesitan para subir
- **Escalado**: Cómo se ajusta la dificultad
- **Balance**: Mantener desafío apropiado

---

## 🔧 **HERRAMIENTAS DE SIMULACIÓN**

### **📝 Plantilla de Simulación**

```markdown
# 🎲 Simulación de [NOMBRE DE CAMPAÑA]

## 📊 Estado Inicial
- **Nivel de PJ**: [X]
- **Regiones Desbloqueadas**: [X]
- **Balance Actual**: [X]
- **Eventos Activos**: [X]

## 📅 Cronología de Eventos

### **Sesión [X] - [NOMBRE]**
- **Eventos Fijos**: [Lista]
- **Eventos Variables**: [Lista]
- **Acciones de PJ**: [Simuladas]
- **Consecuencias**: [Resultados]
- **Nuevo Estado**: [Actualización]

## ⚖️ Balance y Consecuencias
- **Desbalance Actual**: [X]
- **Efectos Activos**: [Lista]
- **Advertencias**: [NPCs que advierten]
- **Restauraciones**: [Cómo mejorar]

## 🗺️ Desbloqueos
- **Nuevos Desbloqueos**: [Lista]
- **Requisitos Cumplidos**: [Lista]
- **Próximos Desbloqueos**: [Lista]
- **Alternativas**: [Opciones]

## 📈 Progresión
- **Nivel Anterior**: [X]
- **Nivel Actual**: [X]
- **Método de Subida**: [Cómo]
- **Próximo Nivel**: [Cuándo]
```

### **🎲 Generador de Eventos Aleatorios**

```markdown
## 🎲 Tabla de Eventos Aleatorios (1d20)

| d20 | Evento Aleatorio | Tipo | Consecuencia |
|-----|------------------|------|--------------|
| 1 | [Evento 1] | [Tipo] | [Consecuencia] |
| 2 | [Evento 2] | [Tipo] | [Consecuencia] |
| ... | ... | ... | ... |
| 20 | [Evento 20] | [Tipo] | [Consecuencia] |

### **📊 Sistema de Lanzamientos**
- **Frecuencia**: Cada [X] sesiones
- **Modificadores**: [Condiciones que afectan]
- **Escalado**: [Cómo cambia la frecuencia]
```

### **⚖️ Sistema de Balance Genérico**

```markdown
## ⚖️ Sistema de Balance [NOMBRE]

### **🎯 Concepto Central**
[Descripción del balance crítico]

### **📊 Cálculo del Balance**
- **Fórmula**: [Cómo se calcula]
- **Ejemplo**: [Ejemplo práctico]

### **🔴 Niveles de Desbalance**

#### **🟢 EQUILIBRIO (Diferencia 0-1)**
- **Estado**: [Descripción]
- **Efectos**: [Lista de efectos]

#### **🟡 DESBALANCE MENOR (Diferencia 2)**
- **Lanzamientos**: [Frecuencia]
- **Efectos**: [Lista de efectos]

#### **🟠 DESBALANCE MODERADO (Diferencia 3)**
- **Lanzamientos**: [Frecuencia]
- **Efectos**: [Lista de efectos]

#### **🔴 DESBALANCE CRÍTICO (Diferencia 4+)**
- **Lanzamientos**: [Frecuencia]
- **Efectos**: [Lista de efectos]

### **👥 Explicadores del Balance**
- **[NPC 1]**: [Función y diálogos]
- **[NPC 2]**: [Función y diálogos]
- **[NPC 3]**: [Función y diálogos]
```

---

## 🎮 **PROCESO DE SIMULACIÓN**

### **1. 📋 Preparación**
1. **Definir Estado Inicial**: Nivel, regiones, balance
2. **Establecer Cronología**: Eventos fijos y variables
3. **Configurar Balance**: Mecánicas críticas
4. **Preparar Desbloqueos**: Requisitos y alternativas

### **2. 🎲 Simulación Sesión por Sesión**
1. **Revisar Eventos Fijos**: ¿Qué debe ocurrir?
2. **Simular Acciones de PJ**: ¿Qué harían típicamente?
3. **Calcular Consecuencias**: ¿Qué resultados?
4. **Actualizar Estado**: Balance, desbloqueos, niveles
5. **Preparar Próxima Sesión**: Eventos futuros

### **3. 📊 Análisis de Resultados**
1. **Progresión General**: ¿Cómo avanza la campaña?
2. **Puntos de Decisión**: ¿Dónde pueden cambiar las cosas?
3. **Consecuencias del Balance**: ¿Cómo afecta a los PJ?
4. **Desbloqueos Críticos**: ¿Qué es esencial desbloquear?

---

## 🔄 **CASOS DE USO**

### **📚 Para Campañas Existentes**
- **Validar Diseño**: ¿Funciona la progresión?
- **Identificar Problemas**: ¿Dónde hay cuellos de botella?
- **Optimizar Balance**: ¿Está bien calibrado?
- **Preparar Contingencia**: ¿Qué pasa si los PJ toman decisiones inesperadas?

### **🆕 Para Campañas Nuevas**
- **Prototipar Mecánicas**: ¿Son viables?
- **Calibrar Dificultad**: ¿Es apropiada?
- **Planificar Progresión**: ¿Es lógica?
- **Testear Sistemas**: ¿Funcionan como esperado?

### **🎯 Para Sesiones Específicas**
- **Preparar Encuentros**: ¿Qué puede pasar?
- **Anticipar Decisiones**: ¿Qué opciones tienen los PJ?
- **Calcular Consecuencias**: ¿Qué resultados posibles?
- **Planificar Contingencias**: ¿Qué hacer si...?

---

## 📝 **EJEMPLOS DE IMPLEMENTACIÓN**

### **🎲 Ejemplo 1: Campaña de Investigación**
```markdown
## ⚖️ Sistema de Balance: Pistas vs Tiempo
- **Fórmula**: |Pistas Encontradas - Tiempo Transcurrido|
- **Crítico**: Si el tiempo supera las pistas por 5+
- **Consecuencia**: El villano escapa o completa su plan
```

### **🎲 Ejemplo 2: Campaña de Supervivencia**
```markdown
## ⚖️ Sistema de Balance: Recursos vs Amenazas
- **Fórmula**: |Recursos Disponibles - Amenazas Activas|
- **Crítico**: Si las amenazas superan los recursos por 3+
- **Consecuencia**: Los PJ no pueden sobrevivir
```

### **🎲 Ejemplo 3: Campaña Política**
```markdown
## ⚖️ Sistema de Balance: Aliados vs Enemigos
- **Fórmula**: |Aliados Ganados - Enemigos Creados|
- **Crítico**: Si los enemigos superan a los aliados por 4+
- **Consecuencia**: Los PJ son exiliados o ejecutados
```

---

## 🛠️ **HERRAMIENTAS ADICIONALES**

### **📊 Calculadora de Balance**
```markdown
## ⚖️ Calculadora de Balance

**Estado Actual:**
- [Factor A]: ___
- [Factor B]: ___
- **Diferencia**: |A - B| = ___
- **Nivel**: [Equilibrio/Menor/Moderado/Crítico]

**Efectos Activos:**
- [ ] [Efecto 1]
- [ ] [Efecto 2]
- [ ] [Efecto 3]

**Próximos Lanzamientos:**
- **Frecuencia**: [X] por sesión
- **Momento**: [Cuándo]
- **Cantidad**: [Cuántos]
```

### **🎯 Generador de Escenarios**
```markdown
## 🎯 Generador de Escenarios

**Tipo de Sesión**: [Exploración/Combate/Diplomacia/Investigación]
**Nivel de PJ**: [X]
**Regiones Disponibles**: [Lista]
**Balance Actual**: [Estado]

**Escenarios Posibles:**
1. [Escenario 1] - Probabilidad: [X]%
2. [Escenario 2] - Probabilidad: [X]%
3. [Escenario 3] - Probabilidad: [X]%

**Recomendación**: [Escenario más probable]
```

---

## 📚 **DOCUMENTACIÓN ADICIONAL**

### **🔗 Enlaces Útiles**
- [Plantilla de Simulación Básica](#plantilla-de-simulación)
- [Sistema de Balance Genérico](#sistema-de-balance-genérico)
- [Proceso de Simulación](#proceso-de-simulación)
- [Casos de Uso](#casos-de-uso)

### **📝 Notas de Uso**
- **Flexibilidad**: Adapta el sistema a cualquier campaña
- **Escalabilidad**: Funciona desde sesiones individuales hasta campañas completas
- **Reutilización**: Una vez configurado, se puede usar múltiples veces
- **Personalización**: Cada campaña puede tener sus propias mecánicas

---

## 🎉 **CONCLUSIÓN**

Este sistema de simulación proporciona:
- **Herramientas reutilizables** para cualquier campaña
- **Métodos estructurados** para simular progresión
- **Sistemas de balance** adaptables
- **Procesos claros** para análisis y preparación

**¡Úsalo para simular Chronosia, cualquier otra campaña, o crear nuevas aventuras!**

---

*Última actualización: Diciembre 2025 - Sistema de simulación reutilizable creado*
