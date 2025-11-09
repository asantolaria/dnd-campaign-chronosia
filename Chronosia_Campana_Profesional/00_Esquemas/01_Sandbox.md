# 📊 Opciones en Sandbox
## *Exploración Libre y Sistema de Balance*

---

> **📖 NAVEGACIÓN:**
> - [← Volver al Diagrama Principal](../00_Esquema_Campana_Mermaid.md)
> - [⚔️ La Ascensión del Cónclave](./02_Ascension_Conclave.md)
> - [🏰 Torre de la Eternidad](./03_Torre_Eternidad.md)
> - [🎭 Decisiones Críticas](./04_Decisiones_Criticas.md)

---

## 🎯 **DIAGRAMA DETALLADO: OPCIONES EN SANDBOX**

Este diagrama muestra todas las opciones de exploración durante las Sesiones 6-12, incluyendo las regiones temporales y dimensionales, y cómo las decisiones afectan el sistema de balance crítico.

```mermaid
flowchart LR
    SANDBOX[Sandbox: Sesiones 6-12<br/>Exploración Libre] --> REGIONES[Regiones Desbloqueadas]
    
    REGIONES --> TEMP[Regiones Temporales]
    REGIONES --> DIM[Regiones Dimensionales]
    
    TEMP --> T1[Serapis<br/>Nivel 5-7]
    TEMP --> T2[Varrak<br/>Nivel 7-9]
    TEMP --> T3[Vorthak<br/>Nivel 9-11]
    TEMP --> T4[Medusa<br/>Nivel 8-9]
    TEMP --> T5[Tempus<br/>Nivel 10-12]
    
    DIM --> D1[Ymir<br/>Nivel 5-7]
    DIM --> D2[Edward Teach<br/>Nivel 11-13]
    DIM --> D3[Dimensionalis<br/>Nivel 9-11]
    DIM --> D4[Ignis<br/>Nivel 13-15]
    DIM --> D5[Veldrisza<br/>Nivel 11-13]
    DIM --> D6[Gemelas<br/>Nivel 9-11]
    
    T1 --> DEC1{¿Derrotar?}
    T2 --> DEC2{¿Derrotar/Aliarse?}
    T3 --> DEC3{¿Derrotar?}
    T4 --> DEC4{¿Derrotar?}
    T5 --> DEC5{¿Derrotar?}
    
    D1 --> DEC6{¿Derrotar?}
    D2 --> DEC7{¿Derrotar/Aliarse?}
    D3 --> DEC8{¿Derrotar/Aliarse?}
    D4 --> DEC9{¿Derrotar?}
    D5 --> DEC10{¿Derrotar/Aliarse?}
    D6 --> DEC11{¿Derrotar/Aliarse?}
    
    DEC1 --> BALANCE[⚖️ Sistema de Balance<br/>Temporales vs Dimensionales]
    DEC2 --> BALANCE
    DEC3 --> BALANCE
    DEC4 --> BALANCE
    DEC5 --> BALANCE
    DEC6 --> BALANCE
    DEC7 --> BALANCE
    DEC8 --> BALANCE
    DEC9 --> BALANCE
    DEC10 --> BALANCE
    DEC11 --> BALANCE
    
    BALANCE --> CONSEC{¿Desequilibrio?}
    CONSEC -->|Equilibrio| OK[Todo normal<br/>Sin penalizaciones]
    CONSEC -->|Desequilibrio 2| MENOR[Desbalance Menor<br/>1d4 efectos/sesión]
    CONSEC -->|Desequilibrio 3| MOD[Desbalance Moderado<br/>1d6 efectos/sesión]
    CONSEC -->|Desequilibrio 4+| CRIT[Desbalance Crítico<br/>1d8 efectos/sesión]
    
    style SANDBOX fill:#fff5e1
    style BALANCE fill:#ffe1e1
    style OK fill:#ccffcc
    style MENOR fill:#ffffcc
    style MOD fill:#ffcc99
    style CRIT fill:#ff9999
```

---

## 📋 **INFORMACIÓN DETALLADA**

### **⚖️ Sistema de Balance Crítico**

**Balance Inicial:**
- **Temporales Principales:** 3 (Serapis, Varrak, Vorthak)
- **Dimensionales Principales:** 5 (Teach, Dimensionalis, Ignis, Veldrisza, Gemelas)
- **Ya hay desequilibrio** favorable a lo dimensional (3 vs 5)

**Cálculo del Desbalance:**
- **Diferencia = |Temporales Derrotados - Dimensionales Derrotados|**
- **Ejemplo:** Si derrotan 2 temporales y 0 dimensionales → Diferencia = 2 (Desbalance Moderado)

### **🔴 Niveles de Desbalance:**

#### **🟢 EQUILIBRIO (Diferencia 0-1)**
- **Estado:** Todo funciona normalmente
- **Cronópolis:** Completamente seguro y estable
- **Viajes:** Sin problemas, portales funcionan al 100%
- **Descanso:** Descanso largo disponible sin restricciones

#### **🟡 DESBALANCE MENOR (Diferencia 2)**
- **Lanzamientos:** 1d4 efectos por sesión
- **Momento:** Al inicio de cada sesión
- **Efectos:** Ver [Tabla de Efectos por Desbalance](../../06_Recursos/Tablas/19_Tablas_Eventos.md#-tabla-de-efectos-por-desbalance)

#### **🟠 DESBALANCE MODERADO (Diferencia 3)**
- **Lanzamientos:** 1d6 efectos por sesión
- **Momento:** Al inicio + cada 2 horas
- **Efectos:** Ver [Tabla de Efectos por Desbalance](../../06_Recursos/Tablas/19_Tablas_Eventos.md#-tabla-de-efectos-por-desbalance)

#### **🔴 DESBALANCE CRÍTICO (Diferencia 4+)**
- **Lanzamientos:** 1d8 efectos por sesión
- **Momento:** Al inicio + cada hora + eventos importantes
- **Efectos:** Ver [Tabla de Efectos por Desbalance](../../06_Recursos/Tablas/19_Tablas_Eventos.md#-tabla-de-efectos-por-desbalance)
- **⚠️ ACCIÓN ESPECIAL:** Si el balance alcanza desbalance crítico (diferencia de 4+), Varrak del Horizonte (probablemente aliado de los PJ) se quitará la vida voluntariamente para equilibrar los poderes y evitar la catástrofe cósmica. Ver [02_Varrak_El_Oraculo.md](../../02_Guia_DM/04_Cronofagos_Detallado/02_Varrak_El_Oraculo.md) para detalles.

### **🎯 Estrategia Recomendada:**

**Para mantener el equilibrio:**
- Derrotar al menos 2 dimensionales antes de enfrentar más temporales
- Alternar entre temporales y dimensionales cuando sea posible
- Considerar alianzas en lugar de derrotas cuando el balance esté en riesgo

**Lugartenientes con opciones de alianza:**
- **Varrak** (Sesión 11): Puede unirse a los PJ
- **Edward Teach**: Puede negociar (peligroso)
- **Dimensionalis**: Puede vender información
- **Las Gemelas**: Pueden aliarse según circunstancias
- **Veldrisza**: Puede negociar (conexión con Jarlaxle)

---

*Este diagrama muestra cómo las decisiones de exploración afectan el balance crítico de Chronosia. Mantener el equilibrio es esencial para evitar catástrofes cósmicas.* ⚖️✨

