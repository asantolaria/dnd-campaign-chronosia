# 🏰 Torre de la Eternidad
## *Asalto Final y Los Cuatro Finales*

---

> **📖 NAVEGACIÓN:**
> - [← Volver al Diagrama Principal](../00_Esquema_Campana_Mermaid.md)
> - [📊 Opciones en Sandbox](./01_Sandbox.md)
> - [⚔️ La Ascensión del Cónclave](./02_Ascension_Conclave.md)
> - [🎭 Decisiones Críticas](./04_Decisiones_Criticas.md)

---

## 🏰 **DIAGRAMA: TORRE DE LA ETERNIDAD**

Este diagrama muestra los 5 niveles del asalto final, las condiciones para cada uno de los 4 finales posibles, y las mecánicas del combate final.

```mermaid
flowchart TD
    ENTRADA[Entrada a la Torre<br/>Sesión 14<br/>Ritual al 98%] --> N1[Nivel 1: Sala de Ecos<br/>Simulacros de Manshoon<br/>Ecos de realidades]
    
    N1 --> N2[Nivel 2: Archivo de Clones<br/>Clones dormidos<br/>Grimorio flotante]
    
    N2 --> N3[Nivel 3: Prisión de los Fieles<br/>Prisioneros<br/>Llave de la Realidad]
    
    N3 --> N4[Nivel 4: Corazón del Tiempo<br/>Bucles temporales<br/>PJ del futuro]
    
    N4 --> N5[Nivel 5: Cámara de Ascensión<br/>Ritual en progreso<br/>Amaunator y Voidar encadenados]
    
    N5 --> TIMING{¿Ritual al 98-99%?}
    
    TIMING -->|Sí| CHECK_TEACH{¿Teach tiene Talismán?}
    TIMING -->|100%| FINAL_D[FINAL D: Demasiado Tarde<br/>Manshoon invencible<br/>CR 25+]
    
    CHECK_TEACH -->|Sí| CHECK_ARRIVAL{¿Quién llegó primero?}
    CHECK_TEACH -->|No| FINAL_A[FINAL A: Manshoon Ascendente<br/>Ritual al 98-99%<br/>CR 23]
    
    CHECK_ARRIVAL -->|Teach primero<br/>Ritual 95-98%| FINAL_B[FINAL B: Blackbeard Usurpador<br/>Teach intercepta poder<br/>CR 25]
    CHECK_ARRIVAL -->|PJ primero<br/>Ritual 98-99%| FINAL_A
    CHECK_ARRIVAL -->|Simultáneo<br/>Ritual 98%| FINAL_C[FINAL C: Carrera Divina<br/>3 bandos luchan<br/>Combate épico]
    
    FINAL_A --> COMBATE1[Combate vs Manshoon<br/>4 Fases de Combate<br/>Deben liberar dioses]
    FINAL_B --> COMBATE2[Combate vs Teach<br/>Teach en ascensión<br/>Manshoon moribundo ayuda]
    FINAL_C --> COMBATE3[Combate 3 bandos<br/>PJ vs Manshoon vs Teach<br/>Carrera al Cronosellado]
    
    COMBATE1 --> LIBERAR{¿Liberan dioses?}
    COMBATE2 --> LIBERAR
    COMBATE3 --> LIBERAR
    
    LIBERAR -->|Sí| VICTORIA[Victoria: Dioses liberados<br/>Chronosia se estabiliza<br/>PJ son héroes legendarios]
    LIBERAR -->|No| DERROTA[Derrota: Villano vencedor<br/>Conquista multiverso<br/>Mal final]
    
    style N1 fill:#e1f5ff
    style N2 fill:#e1f5ff
    style N3 fill:#e1f5ff
    style N4 fill:#e1f5ff
    style N5 fill:#ffe1e1
    style FINAL_A fill:#ffcccc
    style FINAL_B fill:#ccffcc
    style FINAL_C fill:#ccccff
    style FINAL_D fill:#ffccff
    style VICTORIA fill:#ccffcc
    style DERROTA fill:#ffcccc
```

---

## 📋 **INFORMACIÓN DETALLADA**

### **🏰 Los Cinco Niveles de la Torre:**

#### **Nivel 1: Sala de Ecos**
- **Encuentros:** Simulacros de Manshoon (versiones de diferentes realidades)
- **Mecánica:** Ecos de conversaciones de otras líneas temporales
- **Objetivo:** Encontrar el camino correcto entre múltiples realidades

#### **Nivel 2: Archivo de Clones**
- **Encuentros:** Clones dormidos de Manshoon (pueden despertar)
- **Tesoro:** Grimorio flotante con información sobre el ritual
- **Objetivo:** Evitar despertar a los clones o enfrentarlos estratégicamente

#### **Nivel 3: Prisión de los Fieles**
- **Encuentros:** Prisioneros leales a Manshoon (pueden ser liberados o interrogados)
- **Tesoro:** Llave de la Realidad (necesaria para liberar a los dioses)
- **Objetivo:** Obtener la llave sin alertar a Manshoon

#### **Nivel 4: Corazón del Tiempo**
- **Mecánica:** Bucles temporales donde los PJ pueden encontrarse con versiones futuras de sí mismos
- **Peligro:** Quedar atrapado en un bucle temporal
- **Objetivo:** Navegar los bucles sin quedar atrapado

#### **Nivel 5: Cámara de Ascensión**
- **Estado:** Ritual en progreso (98-100%)
- **Presentes:** Manshoon, Amaunator y Voidar encadenados
- **Objetivo:** Interrumpir el ritual y liberar a los dioses

### **⚔️ Los Cuatro Finales Posibles:**

#### **🔴 FINAL A: Manshoon Ascendente**
**Condiciones:**
- Los PJ llegan cuando el ritual está al 98-99%
- Edward Teach está ausente o fue derrotado previamente
- Manshoon está a MOMENTOS de completar la ascensión

**Combate:**
- **4 Fases:** Manshoon Mortal Potenciado → Ritual Acelera → Ascensión Parcial → El Dios Débil
- **CR 23** (Manshoon Ascendente)
- **Mecánica Crítica:** Los PJ DEBEN liberar a los dioses o perderán automáticamente

#### **🟢 FINAL B: Blackbeard el Usurpador**
**Condiciones:**
- Edward Teach tiene el Talismán de Interceptación
- Teach llega ANTES que los PJ
- El ritual está al 95-98%

**Combate:**
- **3 Fases:** Blackbeard Ascendente → El Dios Pirata → Furia Divina
- **CR 25** (Blackbeard Ascendant)
- **Giro Épico:** Manshoon cae al suelo, debilitado, y puede ayudar a los PJ

#### **🔵 FINAL C: La Carrera Divina**
**Condiciones:**
- Edward Teach y los PJ llegan SIMULTÁNEAMENTE
- El ritual está al 98%

**Combate:**
- **Mecánica Única:** Combate de tres bandos (PJ vs Manshoon vs Teach)
- **Objetivo:** Llegar primero al Cronosellado (centro del ritual)
- **Ritual avanza:** Cada 2 turnos, el ritual avanza 1%

#### **🟣 FINAL D: Demasiado Tarde**
**Condiciones:**
- Los PJ llegan cuando el ritual está al 100%
- Manshoon YA ascendió completamente

**Combate:**
- **CR 25+** (Manshoon completamente divino)
- **Casi invencible:** Los PJ solo pueden huir o sacrificarse heroicamente
- **Mal final:** El villano conquista el multiverso

### **🎯 Mecánicas del Combate Final:**

**Liberar a los Dioses:**
- **Requisito:** Llave de la Realidad (Nivel 3) + Acción de 1 turno
- **Efecto:** Amaunator y Voidar se liberan y atacan al villano
- **Crítico:** Sin liberar a los dioses, los PJ no pueden ganar

**Progresión del Ritual:**
- **Sesión 13:** Ritual al 98%
- **Sesión 14:** Ritual al 98-99% (durante el asalto)
- **Sesión 15:** Ritual al 98-100% (depende del timing)

**Edward Teach:**
- **Si tiene Talismán:** Puede llegar ANTES, DURANTE o DESPUÉS de los PJ
- **Si NO tiene Talismán:** Final B imposible

---

*El destino del multiverso se decide en estos momentos finales. Cada decisión, cada acción, cada segundo cuenta.* 🏰⚔️✨

