# 📊 Tablas de Tracking de la Campaña
## *Hojas de Seguimiento para el DM*

---

> **⚠️ PROPÓSITO DE ESTE DOCUMENTO:**
> Este documento contiene **TODAS las tablas de tracking** necesarias para gestionar el progreso de la campaña Chronosia.
> 
> **Copia y actualiza estas tablas después de cada sesión** para mantener un registro completo del estado de la campaña.

---

## 📋 **ÍNDICE DE TABLAS**

1. [Reloj del Ritual](#1-reloj-del-ritual)
2. [Desbloqueo de Regiones](#2-desbloqueo-de-regiones)
3. [Progresión de Niveles de los PJ](#3-progresión-de-niveles-de-los-pj)
4. [Estado de Lugartenientes](#4-estado-de-lugartenientes)
5. [Reliquias de los Lugartenientes](#5-reliquias-de-los-lugartenientes)
6. [Resumen General de Sesión](#6-resumen-general-de-sesión)

---

## 1. **RELOJ DEL RITUAL**

> Única cuenta de presión de la campaña. Marcador de **8 segmentos** (empieza en **2/8**) que mide la ascensión de Aethernus. A **8/8 la ascensión se consuma (derrota, Final D)**; la Torre se abre con la llave chroniana (Cap. 15). Fuente: [01_Como_Dirigir.md](../../01_Como_Dirigir.md).

### **⏳ Marcador**

```
[▓][▓][░][░][░][░][░][░]   ← empieza en 2/8
 0  1  2  3  4  5  6  7  8 → LA ASCENSIÓN SE CONSUMA (Final D — derrota)
```

### **⏳ Tracking por Sesión**

| **Sesión** | **Fecha** | **Segmento (X/8)** | **Movimiento esta sesión** | **Causa** | **Notas** |
|------------|-----------|--------------------|----------------------------|-----------|-----------|
| **1** | | 2/8 | — | Estado inicial | |
| **2-3** | | | | | |
| **4-5** | | | | Hito de Teach (Thyra → salto) | |
| **6** | | | | | |
| **7** | | | | | |
| **8** | | | | | |
| **9** | | | | | |
| **10** | | | | | |
| **11** | | | | | |
| **12** | | | | | |

### **📊 Qué mueve el Reloj:**

| **Movimiento** | **Causa** |
|----------------|-----------|
| ⬆️ **+1** | Explorar una región a fondo (≈+1 por arco resuelto) |
| ⬆️ **+1 / salto** | Hito de Teach (el asesinato de Thyra da un **salto**) · desatender a Teach (caza y absorbe otro lugarteniente → crece) |
| ⏸️ **Se estanca 2** | Derrotar a un lugarteniente **CRÍTICO** (Vorthak, Ignis o Teach → corta un canal divino): los **2 siguientes avances** no cuentan (Cap. 1) |
| ⏸️ **Congela 1** | Misión de sabotaje de los Anacronistas |
| ⬇️ **−1** | Sacrificio de Varrak (con el reloj en zona crítica ≥6/8) |
| 💀 **8/8** | La ascensión se consuma → **Final D** (la Torre NO se abre con el Reloj) |

### **🔎 El "hipo" del Contador:**
Toda muerte de lugarteniente corta un canal divino y el Contador lo acusa con un **parpadeo y un estancamiento momentáneo** (el Reloj nunca retrocede — la única excepción es el sacrificio de Varrak). Si **no** la causaron los PJ, los Anacronistas detectan la anomalía → los PJ investigan. Si la región **sigue rota** (no se restaura) = Teach interceptó el poder. Es la forma principal de destapar la caza de lugartenientes de Barbanegra.

### **🔮 ACCIÓN ESPECIAL: SACRIFICIO DE VARRAK**

El sacrificio ya **no** se dispara por desbalance, sino por una **relación construida** con Varrak a lo largo del sandbox y por el **reloj en zona crítica (≥6/8)**.

**Condiciones:**
- Reloj en zona crítica (≥6/8)
- Varrak vivo y **aliado** de los PJ (le dieron esperanza a lo largo de la campaña)
- Momento: en el funeral de Marcus, tras "La Traición de Serapis"

**Efecto:**
- Varrak se ofrece; el harakiri ritual libera su esencia temporal
- El monje manco la usa para recargar el artilugio y **revivir a Marcus** + dar un don a los PJ
- **El Reloj retrocede 1 segmento** (su muerte estabiliza el flujo)
- El Abismo de los Posibles se restaura

**Nota:** Si lo traicionaron, el momento cambia de tono (muere de otro modo o no ocurre). Ficha y diálogos en `02_Guia_DM/04_Cronofagos_Detallado/02_Varrak_El_Oraculo.md`.

### **📋 Registro de Muertes de Lugartenientes:**

| **Sesión** | **Fecha** | **Lugarteniente** | **¿Crítico?** | **Causa** | **Efecto en el Reloj** | **Notas** |
|------------|-----------|-------------------|---------------|-----------|------------------------|-----------|
| Fase 1 | | Thyra | No | Asesinada por Teach (hito fijo) | ⬆️ Salto | Poder robado por Teach |
| | | Varrak (sacrificio) | No | Voluntario, reloj ≥6/8 | ⬇️ −1 | 🔮 Revive a Marcus |
| | | | | | | |
| | | | | | | |

---

## 2. **DESBLOQUEO DE REGIONES**

### **🗺️ Tabla de Desbloqueo de Regiones**

| **Región** | **Lugarteniente** | **Tipo** | **Nivel** | **Puerta (qué la abre)** | **Fecha** | **Estado** | **Explorada** |
|-----------|------------------|----------|-----------|-------------------------|-----------|------------|---------------|
| **Cronópolis** (hub) | — | Centro Seguro | — | Siempre abierta | | ✅ Desbloqueada | |
| **La Espiral Inversa** | Serapis | Temporal | 4-7 | Entrada abierta · da el Núcleo del Rotor | | 🔓 Desbloqueada | |
| **Glacialis** | Ymir | Dimensional | 4-7 | Entrada abierta · da la Carcasa del Rotor | | 🔓 Desbloqueada | |
| **El Abismo de los Posibles** | Varrak | Temporal | 5-8 | Entrada abierta (más dura: entra con nivel) | | 🔓 Desbloqueada | |
| **El Jardín de los Tiempos Gemelos** | Medusa + Las Gemelas | Dimensional (×2) | 5-8 | Entrada abierta (más dura: entra con nivel) | | 🔓 Desbloqueada | |
| **El Archipiélago de Barbanegra** | Edward Teach | Híbrido (crítico) | 7-9 | Motor de Viento (Rotor: cualquier temporal + cualquier dimensional) | | 🔒 → 🔓 (Motor construido) | |
| **Las Ruinas del Tiempo Perdido** | Tempus | Temporal | 8-10 | Requiere una Arena del Tiempo (cualquier lugarteniente temporal) | | 🔒 | |
| **La Mansión de la Sed Eterna** | Vorthak | 🩸 Vida | 8-10 | Alto nivel (ver Mapa de Puertas) | | 🔒 | |
| **Las Calderas Dimensionales** | Ignis | Dimensional | 8-10 | Alto nivel (ver Mapa de Puertas) | | 🔒 | |
| **Las Llanuras de la Compresión** | Dimensionalis | Dimensional | 9-10 | Derrotar a Ignis | | 🔒 | |
| **La Ciudad Subterránea de Veldrisza** | Yrindra | Dimensional | 9-10 | Derrotar a Ignis (abre el ala profunda) | | 🔒 | |
| **Valle de la Aguja** | Thyra (caída) | Temporal | ≤10 | Inaccesible para los PJ (solo Teach); umbral de la Torre tras su muerte | | ⚰️ | |
| **Torre de la Eternidad** | Aethernus (Manshoon) | Clímax | 10 | Llave chroniana + entrada conocida (Cap. 15) | | 🔒 Hasta tener la llave | |

### **📝 Notas de Tracking:**
- **Total de Regiones:** 11 con lugarteniente + Cronópolis (hub) + Torre de la Eternidad (clímax)
- **Puerta:** razón in-world que abre la región (ver [Mapa de Puertas](../../01_Como_Dirigir.md)). El gating NO es "tras derrotar N lugartenientes" salvo donde la puerta lo indique
- **Regiones Desbloqueadas:** Marca con ✅ cuando se desbloquea
- **Regiones Exploradas:** Marca con ✅ cuando los PJ la visitan
- **Regiones Bloqueadas:** Marca con ⚰️ si el lugarteniente muere y la región se bloquea

---

## 3. **PROGRESIÓN DE NIVELES DE LOS PJ**

### **📈 Tabla de Progresión de Niveles**

| **Sesión** | **Fecha** | **Nivel Inicial** | **Nivel Final** | **Método de Subida** | **Notas** |
|------------|-----------|------------------|-----------------|----------------------|-----------|
| **1** | | 3 | 3 | Inicio de campaña | |
| **2** | | 3 | 4 | Investigación completa | |
| **3** | | 4 | 5 | Primer lugarteniente | |
| **4-5** | | 5 | 6 | Eventos de robos (XP narrativo) | |
| **6** | | 6 | 7 | Hito narrativo (la Traición de Serapis, Cap. 14) | |
| **7** | | 7 | 8 | Derrotar 1-2 lugartenientes | |
| **8** | | 8 | 9 | Derrotar 1-2 lugartenientes | |
| **9** | | 9 | 10 | Derrotar 1 lugarteniente (techo de nivel) | |
| **10-12** | | 10 | 10 | Revelaciones, Varrak, lugartenientes restantes (sin subir de nivel) | |
| **Clímax** | | 10 | 10 | Asalto a la Torre **cuando reúnan la llave chroniana y la entrada** — idealmente con el Reloj en 6-7/8. **A 8/8 la ascensión se consuma (Final D, derrota)**: la Torre nunca "se abre" por el Reloj | |

### **📝 Tracking Individual de PJ:**

| **PJ** | **Nivel Actual** | **Última Subida** | **Próxima Subida** | **Notas** |
|--------|------------------|-------------------|-------------------|-----------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

---

## 4. **ESTADO DE LUGARTENIENTES**

### **👑 Tabla de Estado de Lugartenientes**

| **Lugarteniente** | **Tipo**              | **Estado** | **Sesión de Cambio** | **Ubicación**             | **Notas**                     |
| ----------------- | --------------------- | ---------- | -------------------- | ------------------------- | ----------------------------- |
| **Thyra**         | Temporal (caída)      | ⚰️ Muerta  | Fase 1               | Valle de la Aguja         | Asesinada por Teach (hito fijo) |
| **Serapis**       | Temporal    | ✅ Activo   | —                    | La Espiral Inversa        | Bando Temporal                |
| **Varrak**        | Temporal    | ✅ Activo   | —                    | El Abismo de los Posibles | Neutral; elige en Fase 3, 🔮 puede sacrificarse si es aliado y el reloj ≥6/8 |
| **Vorthak**       | 🩸 Vida (drena años) | ✅ Activo   | —                    | La Mansión de la Sed Eterna | Líder del bando temporal por política, no conducto (crítico) |
| **Edward Teach**  | ⚓ Híbrido (poder robado) | ✅ Activo   | —                    | El Archipiélago de Barbanegra | Crítico, tiene Talismán; bando propio |
| **Dimensionalis** | Dimensional | ✅ Activo   | —                    | Las Llanuras de la Compresión | Independiente             |
| **Ignis**         | Dimensional | ✅ Activo   | —                    | Las Calderas Dimensionales | Líder Bando Dimensional (crítico) |
| **Yrindra**     | Dimensional | ✅ Activo   | —                    | La Ciudad Subterránea de Veldrisza | Aliada de Ignis      |
| **Las Gemelas**   | Dimensional | ✅ Activo   | —                    | El Jardín de los Tiempos Gemelos | Neutral; eligen en Fase 3 |
| **Medusa**        | Dimensional           | ✅ Activo   | —                    | El Jardín de los Tiempos Gemelos |                        |
| **Tempus**        | Temporal              | ✅ Activo   | —                    | Las Ruinas del Tiempo Perdido |                          |
| **Ymir**          | Dimensional           | ✅ Activo   | —                    | Glacialis                 |                               |
| **Aethernus Valcarys (Manshoon)** | BBEG | ✅ Recluido → ⚔️ Clímax | —                    | Torre de la Eternidad     | Ejecutando el ritual; el asalto llega **cuando los PJ reúnen la llave y la entrada** (a 8/8 ya es tarde: Final D) |

### **📝 Estados:**
- **✅ Activo:** Lugarteniente está vivo y activo
- **⚰️ Muerto:** Lugarteniente fue derrotado permanentemente
- **🤝 Aliado:** Lugarteniente se alió con los PJ
- **⚠️ Herido:** Lugarteniente está gravemente herido
- **🔒 Recluido:** Lugarteniente está aislado (Manshoon)

### **📋 Cambios de Estado:**

| **Sesión** | **Fecha** | **Lugarteniente** | **Cambio** | **Causa** | **Notas** |
|------------|-----------|-------------------|------------|-----------|-----------|
| Fase 1 | | Thyra | ⚰️ Muerta | Asesinada por Teach (hito fijo) | Poder robado |
| Fase 3 | | Varrak | Cambio de bando | Decisión de PJ | |
| Fase 3 | | Las Gemelas | Cambio de bando | Según bando ganador | |
| X | | Varrak | ⚰️ Muerto (Sacrificio) | Aliado + reloj ≥6/8 | 🔮 **Sacrificio voluntario: revive a Marcus y retrocede el Reloj −1** |

---

## 5. **RELIQUIAS DE LOS LUGARTENIENTES**

### **💍 Tabla de Botín (anillos y artefactos)**

Cada lugarteniente porta un **anillo de poder** (canalizador de Aethernus) y, en algunos casos, un artefacto regional. Son botín mágico potente. **Nota:** los anillos pierden su poder al cortarse la vinculación con Aethernus; preservarlos como objeto puede requerir el Talismán de Teach, pero **ya no son "combustible" de ninguna máquina del tiempo** — son recompensas y trofeos.

| **Lugarteniente** | **Tipo** | **Estado** | **Anillo Obtenido** | **Artefacto regional** | **Sesión** | **Notas** |
|-------------------|----------|------------|---------------------|------------------------|------------|-----------|
| **Serapis** | Temporal | Activo / Muerto | Sí / No | Arena del Tiempo · Núcleo (Rotor) | | |
| **Varrak** | Temporal | Activo / Muerto | Sí / No | Cristal Profético · Núcleo (destilable, aliado) | | Neutral/aliable |
| **Vorthak** | 🩸 Vida | Activo / Muerto | Sí / No | — (sin pieza de Rotor) | | Lugarteniente CRÍTICO |
| **Las Gemelas** | Dimensional | Activo / Muerto | Sí / No | Espejo de Realidad Fragmentada · Carcasa (Rotor) | | Neutrales/aliables |
| **Tempus** | Temporal | Activo / Muerto | Sí / No | Núcleo (Rotor) · Arena del Tiempo | | Reprogramable (vía pacífica) |
| **Ymir** | Dimensional | Activo / Muerto | Sí / No | Carcasa Dimensional (Rotor) | | |
| **Dimensionalis** | Dimensional | Activo / Muerto | Sí / No | Carcasa (Rotor) | | Independiente; vende información |
| **Ignis** | Dimensional | Activo / Muerto | Sí / No | Carcasa (Rotor) | | Lugarteniente CRÍTICO |
| **Yrindra** | Dimensional | Activo / Muerto | Sí / No | Carcasa (Rotor) · vende la entrada de la Torre | | |
| **Medusa** | Dimensional | Activo / Muerto | Sí / No | Carcasa (Rotor) | | Su "estasis" es disfraz de Voidar |
| **Edward Teach** | Híbrido (poder robado) | Activo / Muerto | Sí / No | Talismán de Interceptación (Cronómetro + Perla) | | Lugarteniente CRÍTICO; recupera Cronómetro y Perla |

> Detalle de cada objeto: [21_Objetos_Magicos_Reliquias.md](./21_Objetos_Magicos_Reliquias.md).

---

## 6. **RESUMEN GENERAL DE SESIÓN**

### **📋 Plantilla de Resumen de Sesión**

**Sesión #:** _____  
**Fecha:** _____  
**Nivel de PJ:** _____  
**Duración:** _____ horas

#### **Eventos Principales:**
- 
- 
- 

#### **Lugartenientes Enfrentados:**
- 
- 

#### **Regiones Exploradas:**
- 
- 

#### **Eventos Narrativos Importantes:**
- 
- 

#### **Urgencia Narrativa:**
- **Estado:** Baja / Media / Alta / Crítica
- **Indicadores:** (Gritos de dioses, distorsiones, acciones de lugartenientes)

#### **Reloj del Ritual:**
- **Segmento actual:** _____ /8
- **Movimiento esta sesión:** _____ (qué lo movió)
- **¿Lugarteniente crítico caído? ¿Hipo del Contador detectado?:** _____

#### **Artefactos:**
- 
- 

#### **Decisiones Críticas de los PJ:**
- 
- 

#### **Notas para Próxima Sesión:**
- 
- 

---

## 📝 **INSTRUCCIONES DE USO**

### **Cómo Usar Estas Tablas:**

1. **Antes de la Primera Sesión:**
   - Copia todas las tablas a un documento separado (o usa este mismo)
   - Inicializa todos los valores base (Sesión 1-6)

2. **Después de Cada Sesión:**
   - Actualiza el **Reloj del Ritual** (segmento actual y qué lo movió)
   - Marca regiones exploradas
   - Actualiza niveles de PJ (techo nivel 10)
   - Registra cambios de estado de lugartenientes
   - Evalúa urgencia narrativa según eventos
   - Completa el Resumen General de Sesión

3. **Cuando el Reloj se acerca a 8/8 (zona crítica):**
   - Sube la presión narrativa: hitos de Teach, gritos de los dioses, tormentas del ritual (opcional)
   - Si Varrak es aliado y el reloj ≥6/8, prepara su posible sacrificio (−1 al Reloj, revive a Marcus)
   - Recuerda a los PJ qué regiones/lugartenientes han quedado sin tocar (alimentan a Teach)

4. **Al llegar el Reloj a 8/8 (Fase 4: Clímax):**
   - **8/8: la ascensión se consuma → Final D** (la Llamada de los Dioses suena al reunir la llave, no a 8/8)
   - El final depende del estado del tablero: a quién derrotaron, si Teach llegó antes, si reunieron a Anacronistas + Oceánicos (ver finales en el Motor de Campaña)

5. **Durante la Sesión:**
   - Si derrotan a un lugarteniente, actualiza estado y el Reloj (¿era crítico? → se estanca **2 hitos**)
   - Si detectan un "hipo del Contador" que no provocaron, lánzalos a investigar (firma de Teach)
   - Si hay eventos aleatorios, úsalos narrativamente

6. **Revisión Periódica:**
   - Cada 3 sesiones, revisa que todo esté actualizado
   - Comprueba que el ritmo del Reloj acompaña el progreso de la mesa (ni cronómetro estricto ni regalado)
   - Evalúa la urgencia narrativa según los eventos ocurridos

---

## 🔗 **REFERENCIAS**

- **[07_Cronologia_Maestra_Campana.md](../../02_Guia_DM/07_Cronologia_Maestra_Campana.md)** - Timeline maestro y eventos de desbloqueo
- **[02_El_Semiplano.md](../../02_El_Semiplano.md)** - Información de regiones y desbloqueos
- **[01_Como_Dirigir.md](../../01_Como_Dirigir.md)** - Reloj del Ritual, puertas y finales (fuente única de estructura)
- **[21_Objetos_Magicos_Reliquias.md](./21_Objetos_Magicos_Reliquias.md#-sistema-de-anillos-de-poder-de-los-lugartenientes)** - Anillos y reliquias de los lugartenientes

---

*Estas tablas son herramientas vivas. Actualízalas constantemente y mantén un registro detallado del progreso de tu campaña.* 📊✨

