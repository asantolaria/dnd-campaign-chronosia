# 🎨 Prompts de Arte — Chronosia

> Pack de prompts listos para generar el arte de la campaña, **optimizado para Gemini (Google)**. Sustituye al antiguo `Prompt_Mapa_ChatGPT.md` (que usaba regiones ya inexistentes).
>
> **Cada prompt es autocontenido:** ya lleva el ancla de estilo incrustada, así que solo tienes que **copiar el bloque entero y pegarlo** en Gemini. Es repetitivo a propósito.
>
> **Ventajas de Gemini para esto:** (1) rotula **texto dentro de la imagen** razonablemente bien — mejor que DALL·E/Midjourney —, así que puedes pedir nombres en español (revisa la ortografía); (2) es excelente **editando una imagen que le subas** (ideal para el restyle de criaturas: subes el PNG y pides el cambio conservando la pose).

---

## 0 · Cómo usarlo en Gemini

- **Copia un bloque ` ``` ` entero y pégalo.** No hace falta añadir nada delante: el estilo ya va dentro.
- **Texto/etiquetas:** Gemini escribe texto en imagen bastante bien. **Revisa la ortografía**; si falla, dile en el chat *"corrige el texto: pon exactamente «…»"* y reedita la misma imagen. Para texto 100 % fiable, pide la imagen **solo con números** y rotula tú con `mapa_general_chronosia.svg` (ya correcto).
- **Proporción:** va escrita en cada prompt en lenguaje natural (Gemini no usa flags).
- **Edición / restyle (lo mejor de Gemini):** sube el PNG y pega el prompt del §5; ya incluye *"conserva la pose y composición, cambia solo el acabado"*.
- **Coherencia:** trabaja en una sola conversación o sube una pieza ya aprobada como referencia (*"mismo estilo, paleta e iluminación que esta"*).

---

## 1 · Portada del manual *(NUEVO)*

> Para la home de la web y la tapa del PDF. Vertical, proporción 2:3. Gemini rotula texto regular: revisa la ortografía o pídela **sin texto** y rotula el título aparte.

```
Portada de manual de campaña de D&D, estilo key-art de tapa dura de Wizards of the Coast: ilustración pictórica épica, dramática y muy detallada, composición vertical de portada de libro, proporción 2:3. Acabado de pintura digital realista, no estilo cómic, sin marcas de agua.
Tema: CHRONOSIA, un semiplano donde el tiempo y el espacio se han fracturado. Escena central: una TORRE imposible que se alza hacia un cielo PARTIDO EN DOS — una mitad de sol dorado y relojería (el Tiempo), la otra de vacío púrpura estrellado (el Espacio) — con grietas de realidad recorriendo el firmamento. Alrededor de la torre flotan engranajes colosales, esferas de reloj rotas y fragmentos de tierra suspendidos fuera del tiempo. Abajo, en pequeño, la silueta de una ciudad amurallada con relojes (Cronópolis) y unas diminutas figuras de aventureros contemplando la escena, para dar escala épica. Paleta cohesionada en sepias y dorados contra púrpuras profundos; iluminación dramática, atmósfera de horror cósmico y maravilla.
Deja espacio limpio en la parte superior para el título y en la inferior para el subtítulo. Si rotulas: título «CHRONOSIA» grande y, debajo, «El Reino del Tiempo Fracturado». Evita estética de cómic y marcas de agua.
```

**Cuando la generes:** guárdala como `~/Descargas/portada.png` y dímelo — la optimizo para web, la pongo de cabecera en la home del sitio y la dejo lista para la tapa del PDF.

---

## 2 · Mapa general de Chronosia

> **Numeración canónica:** coincide con los 10 mapas regionales (§3) y los archivos `assets/mapas/01..10`. Úsala siempre. (El PNG antiguo del mapa general traía nombres obsoletos — «Colinas Remolino», «Ciudad de Hielo»…; este prompt lo corrige.)

```
Mapa de fantasía dibujado a mano, estilo cartografía clásica de manual de rol: papel/pergamino envejecido, tinta sepia, relieve sombreado a plumilla (montañas, bosques, costas), paleta apagada y cohesionada, cartela decorativa y borde ornamentado, rosa de los vientos. Aspecto de mapa real de campaña de D&D, legible y elegante. Vista cenital.

Tema: el semiplano fracturado de Chronosia (un limbo entre planos, no un reino al uso). Continente único y alargado en vertical, rodeado por dos mares (Mar Occidental al oeste, Mar Oriental al este). Gradiente: NORTE con altas montañas y glaciares eternos; CENTRO templado con una gran ciudad amurallada destacada en el corazón del continente; SUR árido y volcánico con un volcán activo.

En el CENTRO, sin número y como icono de ciudad-estrella destacado: CRONÓPOLIS, la capital amurallada con grandes relojes y puerto fluvial. **Rotúlala SOLO con la palabra «CRONÓPOLIS»** (no escribas descripciones en el mapa).

Marca 10 emplazamientos con un círculo numerado del 1 al 10 y rotúlalos con su nombre:
1 La Espiral Inversa — colinas templadas con un remolino/espiral grabado en el terreno, cerca de la capital.
2 El Jardín de los Tiempos Gemelos — jardín amurallado simétrico con estatuas y estanque-espejo, al este del centro.
3 Glacialis — ciudad de hielo entre los glaciares del norte.
4 Las Ruinas del Tiempo Perdido — ruinas con engranajes colosales semienterrados, en clima templado al oeste.
5 El Abismo de los Posibles — gran cañón con peñascos e islas flotantes, al oeste-centro.
6 Las Llanuras de la Compresión — llanura que se pliega, con grietas de resplandor infernal, al sureste-centro.
7 La Ciudad Subterránea de Veldrisza — una boca de caverna que baja al subsuelo (drow/Underdark), al sur-centro.
8 El Archipiélago de Barbanegra — islas piratas en un mar antinaturalmente en calma con vórtices, en el Mar Oriental.
9 La Mansión de la Sed Eterna — mansión gótica solitaria envuelta en niebla, al suroeste.
10 Las Calderas Dimensionales — calderas volcánicas con bocas de fuego, al sur junto al volcán.

Marca también, SIN número: una TORRE solitaria y oculta tras las montañas del norte (la Torre de la Eternidad); y un pequeño VALLE HELADO cercano, sellado por una barrera de escarcha (el Valle de la Aguja).

Dibuja además, en línea fina punteada, las RUTAS desde Cronópolis a las regiones cercanas, y una ruta distinta sobre el mar (líneas de oleaje) que cruce el Mar Oriental hasta el Archipiélago de Barbanegra (8), para sugerir que solo se llega por mar; si la rotulas, escribe exactamente «Ruta marítima».

Añade rosa de los vientos y una cartela con el título «CHRONOSIA». **Rotula en español con etiquetas CORTAS y exactas (solo los nombres de la lista); NO escribas frases ni descripciones dentro de la imagen, porque el texto largo se corrompe.** Si el texto no sale fiable, genera el mapa SOLO con los números 1-10 y deja un recuadro de leyenda vacío en una esquina para rotular a mano. Formato vertical, proporción 2:3. Evita marcas de agua y estética de cómic.
```

---

## 2.1 · Cronópolis — mapa de ciudad (el hub) *(NUEVO)*

```
Mapa de ciudad dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, cartela con el título «CRONÓPOLIS» y una leyenda numerada de edificios. Vista cenital ligeramente isométrica, legible y elegante, proporción 4:3.
Tema: Cronópolis, la última ciudad libre y zona segura de Chronosia (un bastión estable en un semiplano roto, al estilo de una aldea gala asediada). Ciudad amurallada costera con puerto fluvial, faros y grandes relojes astronómicos por todas partes; arquitectura de relojería gnoma (engranajes, cúpulas de latón). Marca con números los puntos clave: 1 la Puerta y muralla; 2 la Plaza del Reloj con el CONTADOR DEL RITUAL (un gran marcador vertical de 8 segmentos luminosos que mide la cuenta atrás); 3 la Cámara del Tiempo de los Anacronistas (donde se guarda el Cronómetro de Realidades); 4 el cuartel de La Resistencia / fortaleza de acero; 5 el taller de los Ingenieros gnomos; 6 la taberna y el mercado de refugiados; 7 el templo; 8 el palacio de la Síndica / concejo; 9 el muelle con barcos. Ambiente de cobijo cálido frente al caos exterior. Etiquetas en español (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

---

## 2.2 · La Torre de la Eternidad — clímax *(NUEVO)*

```
Ilustración de mazmorra en CORTE VERTICAL (sección transversal) dibujada a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, cartela con el título «LA TORRE DE LA ETERNIDAD» y una leyenda lateral por niveles. Composición vertical alta y dramática, proporción 2:3.
Tema: la torre imposible donde Aethernus ejecuta su ascensión, alzándose entre las montañas heladas del norte hacia un cielo fracturado con grietas que muestran el cosmos. Muestra la torre abierta como una casa de muñecas, con 4 NIVELES apilados conectados por una gran escalera de caracol:
- Nivel 1 (base): cámara de acertijos con espejos y ecos de luz.
- Nivel 2: mansión lujosa de habitaciones con engranajes gigantes girando.
- Nivel 3: un puente estrecho sobre un abismo.
- Nivel 4 (cima): un ritual circular con dos dioses encadenados a pilares (uno dorado/solar, otro púrpura/vacío) y un marcador brillando.
Paleta sepia con acentos dorados (tiempo) y púrpuras (espacio/vacío). Tono épico y de horror cósmico.
**ROTULADO (importante):** etiqueta cada nivel SOLO con un título corto, exactamente: «Nivel 1 · Sala de Ecos», «Nivel 2 · Corazón del Tiempo», «Nivel 3 · Eliminatoria», «Nivel 4 · Cámara de Ascensión». **NO escribas frases ni párrafos descriptivos dentro de la imagen** — el texto largo se corrompe en galimatías. Si dudas, genera la imagen SIN texto y rotula tú. Evita marcas de agua y estética de cómic.
```

---

## 3 · Mapas por región (×10)

> Copia el bloque de la región que necesites. Todos van en proporción 4:3.

### 1 · La Espiral Inversa *(Serapis — temporal · nv 4-5)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: La Espiral Inversa (Chronosia), afectada por distorsión TEMPORAL. Valle en espiral donde el tiempo retrocede: vegetación que rebrota, ruinas que se reconstruyen solas, un pueblo cuyas calles se repiten en bucle concéntrico, bajo una luz dorada de atardecer perpetuo. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 2 · El Jardín de los Tiempos Gemelos *(Medusa + Las Gemelas — T/D · nv 5-7)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: El Jardín de los Tiempos Gemelos (Chronosia), con distorsión TEMPORAL y ESPACIAL. Jardín amurallado simétrico con setos-laberinto, estatuas inquietantes y estanques-espejo que reflejan un mundo invertido; una mitad detenida en estasis con escarcha cristalina, la otra reflejada como un espejo. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 3 · Glacialis *(Ymir — dimensional · nv 6-7 · → Plano del Agua)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: Glacialis (Chronosia), con distorsión ESPACIAL. Páramo glacial con portales de hielo translúcidos abiertos en el aire, grietas que filtran agua de otro plano, una ciudad de hielo y una red de umbrales helados unidos por senderos. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 4 · Las Ruinas del Tiempo Perdido *(Tempus — temporal · nv 6-7)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: Las Ruinas del Tiempo Perdido (Chronosia), con distorsión TEMPORAL. Ciudad en ruinas atrapada fuera del tiempo: engranajes colosales semienterrados, relojería rota, geometría ordenada de mecanismo de reloj, fragmentos de piedra flotando inmóviles en el aire. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 5 · El Abismo de los Posibles *(Varrak — temporal · nv 7-8)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: El Abismo de los Posibles (Chronosia), con distorsión TEMPORAL. Gran cañón con peñascos e islas flotantes unidas por puentes; el mismo paisaje se repite ligeramente distinto en capas superpuestas y semitransparentes, como realidades paralelas solapadas. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 6 · Las Llanuras de la Compresión *(Dimensionalis — dimensional · nv 7-8 · → Avernus)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: Las Llanuras de la Compresión (Chronosia), con distorsión ESPACIAL. Llanura donde el espacio se pliega: distancias imposibles, caminos que se comprimen, estructuras estiradas o encogidas, horizonte curvado; al fondo, grietas con un resplandor infernal (presagio de Avernus). Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 7 · La Ciudad Subterránea de Veldrisza *(Veldrisza — dimensional · nv 8-9 · → Underdark)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: La Ciudad Subterránea de Veldrisza (Chronosia), con distorsión ESPACIAL. Caverna-ciudad drow del Underdark: arquitectura tallada en estalagmitas, telarañas colosales que conectan plataformas a distinta altura, un gran portal-telaraña hacia Menzoberranzan y hongos luminosos. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 8 · Archipiélago de Barbanegra *(Edward Teach — dimensional · nv 8-9)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: Archipiélago de Barbanegra (Chronosia), con distorsión ESPACIAL. Islas dispersas en un mar antinaturalmente en calma, con vórtices y remolinos dimensionales, restos de naufragios, un fuerte pirata y faros, todo bajo una niebla baja. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 9 · La Mansión de la Sed Eterna *(Vorthak — temporal · nv 9 · → Barovia)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: La Mansión de la Sed Eterna (Chronosia), con distorsión TEMPORAL (drenaje de vida). Finca gótica solitaria envuelta en niebla espesa, con jardines marchitos, criptas y verja de hierro; la niebla se espesa hacia un borde que parece llevar a "otro lugar" (presagio de Barovia / Shadowfell). Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 10 · Las Calderas Dimensionales *(Ignis — dimensional · nv 9-10 · → Plano del Fuego)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: Las Calderas Dimensionales (Chronosia), con distorsión ESPACIAL. Cordillera volcánica con calderas y ríos de lava, portales ardientes abiertos sobre las bocas de fuego de los que asoma el Plano Elemental del Fuego, y huesos de dragón dispersos. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

---

## 4 · Retrato de Aethernus Valcarys (reemplaza el PNG roto)

```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica visible, anatomía y materiales naturalistas, iluminación cinematográfica y dramática con luz volumétrica, color rico, alto detalle. Fondo pictórico oscuro y atmosférico, foco total en el sujeto. Calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, estética de cómic/anime y aspecto 3D plastificado.

Sujeto: Aethernus Valcarys, archimago anciano y poderoso, villano final. Retrato de medio cuerpo. Rasgo distintivo: su rostro y cuerpo están partidos en dos mitades temporales — un lado joven y hermoso, el otro un anciano moribundo de piel arrugada y ojos hundidos. Viste una capa de "hilos temporales" que brillan tenues como estrellas; corona de cristales que laten con luz interior. Postura imperial, una mano alzada canalizando energía temporal (dorada) y espacial (violeta) entrelazadas. Expresión fría y megalómana, con un leve halo de poder divino robado. Proporción 3:4 (vertical).
```

---

## 5 · Criaturas y símbolo (estilo de los libros actuales de D&D)

> **Rasgos canónicos de los Cronófagos** (incluidos en los prompts):
> - **Máscara de médico de la peste con pico de cuervo, dorada, + lentes circulares oscuros** = seña de identidad de **tropa y sargentos** (rostro oculto, deshumanizados). **Oficiales y lugartenientes van SIN máscara** y revelan el rostro destrozado por el tiempo. *(Esta es la jerarquía visual: cuanto más arriba, más se ve el horror.)*
> - **Estética militar totalitaria de principios del s. XX:** gabán/túnica con correajes de cuero cruzados, botones dorados, cascos de acero (pickelhaube con pincho en sargentos), insignias, banderas púrpura con emblema de reloj de arena.
> - **Color por rango:** tropa = rojo · sargento = azul · oficial = púrpura.
> - **Distorsión visible:** TEMPORAL = un miembro mucho más viejo que el resto (y su ropa envejecida); ESPACIAL = partes del cuerpo semitransparentes / asimetrías imposibles.
> - **Emblema:** uróboros-infinito (serpiente en forma de ∞ mordiéndose la cola).
>
> **Para unificar el arte que ya tienes:** sube el PNG actual a Gemini y pega el bloque correspondiente; ya lleva la coletilla de "conserva la pose, cambia el acabado".

### 5.1 · Tropa Cronófaga (soldado raso)
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, anatomía y materiales naturalistas, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado. (Si subo una imagen de referencia: conserva la pose y composición, cambia solo el acabado y la iluminación a este estilo.)

Sujeto: soldado de infantería arcano-militar de los Cronófagos, cuerpo entero, estética militar totalitaria de principios del s. XX. Túnica militar ROJA con correajes de cuero cruzados y botones dorados, armadura de placas en los brazos, casco de acero mate. Lleva una MÁSCARA DE MÉDICO DE LA PESTE con pico de cuervo, dorada, y lentes circulares oscuros que le ocultan por completo el rostro (oculta un rostro infantil — contraste inquietante). Empuña dos espadas cortas gemelas. Señal de distorsión temporal: un brazo notoriamente más envejecido que el resto. Atmósfera sombría. Proporción 3:4 (vertical).
```

### 5.2 · Sargento Cronófago (suboficial)
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, anatomía y materiales naturalistas, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado. (Si subo una imagen de referencia: conserva la pose y composición, cambia solo el acabado y la iluminación a este estilo.)

Sujeto: suboficial (sargento) arcano-militar imponente, cuerpo entero, facción de los Cronófagos, estética militar totalitaria de principios del s. XX. Túnica militar AZUL con correajes de cuero cruzados y botones dorados; armadura de placas y casco de acero tipo pickelhaube (con pincho en el centro). Lleva una MÁSCARA DE MÉDICO DE LA PESTE con pico de cuervo, dorada con detalles plateados, y lentes circulares oscuros (rostro oculto). Bastón de mando rematado en cabeza de serpiente y un collar de uróboros-infinito; cristales de poder brillantes; insignias de sargento. Señal de distorsión espacial: parte del cuerpo semitransparente. Porte autoritario. Proporción 3:4 (vertical).
```

### 5.3 · Oficial Cronófago (comandante)
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, anatomía y materiales naturalistas, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado. (Si subo una imagen de referencia: conserva la pose y composición, cambia solo el acabado y la iluminación a este estilo.)

Sujeto: oficial comandante arcano-militar, cuerpo entero, jefe de élite de los Cronófagos, estética militar totalitaria de principios del s. XX. Túnica militar PÚRPURA con correajes de cuero cruzados, armadura de placas que cubre torso/brazos/piernas, botones dorados; gorra de plato militar (estilo soviético) del color del uniforme. SIN máscara: muestra un rostro distorsionado por el tiempo (mitades de distinta edad), con lentes circulares oscuros subidos sobre la gorra. Tatuaje de uróboros-infinito (serpiente en ∞ mordiéndose la cola) en la mano. Empuña un bastón de duelo que puede tornarse espada. Aura de poder espacio-temporal. Proporción 3:4 (vertical).
```

### 5.4 · Cronófago lanzador de conjuros
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, anatomía y materiales naturalistas, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado. (Si subo una imagen de referencia: conserva la pose y composición, cambia solo el acabado y la iluminación a este estilo.)

Sujeto: hechicero militar de los Cronófagos, cuerpo entero. Túnica-uniforme oscura; canaliza la distorsión: una mano que envejece y rejuvenece, hilos de tiempo dorados y grietas espaciales violetas a su alrededor. Ojos que brillan con visión de oráculo. Gestos arcanos. Proporción 3:4 (vertical).
```

### 5.5 · Símbolo de la facción Cronófaga
```
Emblema heráldico limpio para una facción de fantasía, al estilo de los símbolos de facción de los manuales actuales de Dungeons & Dragons: una SERPIENTE que forma el signo de infinito (∞) y se muerde la cola (uróboros), elegante y simétrica. Acabado de sigilo metálico grabado (bronce y acero envejecido) sobre fondo neutro, una o dos tintas, alto contraste, composición centrada, formato cuadrado 1:1, apto como icono. Sin texto ni marcas de agua.
```

---

## 6 · Retratos de los lugartenientes («los malos»)

> Un prompt autocontenido por jefe. Convención de color para que el set sea coherente: **energía temporal = dorada**, **dimensional = violeta**. El jefe final (Aethernus) está en el §4. Composición: medio cuerpo salvo los colosales (Ignis, Ymir, Tempus), que van a cuerpo entero.

### ⏰ Serapis el Retroceso *(Temporal · Elfo Eterno)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Serapis el Retroceso, elfo inmortal de porte sereno y antiquísimo. Viste túnicas de las que fluye arena HACIA ARRIBA (el tiempo invertido); sus ojos reflejan escenas del pasado. A su alrededor el tiempo retrocede: hojas que vuelven a la rama, una herida que se cierra sola. Energía temporal dorada. Medio cuerpo, proporción 3:4.
```

### ⏰ Varrak el Oráculo *(Temporal · Orco — suele ser aliado)*

> Varrak vive sus edades **a la vez**. Tienes su **forma verdadera** (fragmentada) y un **tríptico** de las 3 edades del mismo ser. Identidad fija para que se reconozca en las tres: orco de piel verde-grisácea, colmillos inferiores, una cicatriz vertical sobre la ceja izquierda, vestiduras de oráculo con motivos astrales, y ojos que brillan en dorado (visión de futuros).
> **Truco Gemini:** genera primero el **adulto**, y luego pídele *"el mismo orco pero de niño / muy anciano, misma cara, cicatriz y vestimenta"* para mantener la coherencia.

**Forma verdadera (fragmentada):**
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Varrak el Oráculo, orco vidente de piel verde-grisácea, colmillos inferiores y cicatriz vertical sobre la ceja izquierda, con vestiduras de oráculo de motivos astrales. Su cuerpo se fragmenta en VARIAS versiones superpuestas de sí mismo a la vez —niño, adulto y anciano simultáneos y semitransparentes, desfasados como ecos—; ojos que brillan en dorado al ver múltiples futuros. Aire profético y melancólico, no hostil. Energía temporal dorada. Medio cuerpo, proporción 3:4.
```

**1/3 — Varrak niño:**
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Varrak el Oráculo de NIÑO, orco joven de piel verde-grisácea con pequeños colmillos y una cicatriz vertical sobre la ceja izquierda; vestiduras de oráculo de motivos astrales (a su talla). Mirada demasiado sabia para su edad, ojos que brillan tenues en dorado. Energía temporal dorada. Retrato/medio cuerpo, proporción 3:4. (Es el mismo individuo que el adulto y el anciano: misma cara, cicatriz y vestimenta.)
```

**2/3 — Varrak adulto:**
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Varrak el Oráculo ADULTO, orco fornido en su plenitud, piel verde-grisácea, colmillos inferiores marcados y cicatriz vertical sobre la ceja izquierda; vestiduras de oráculo de motivos astrales. Porte sereno y profético, ojos que brillan en dorado con visión de futuros. Energía temporal dorada. Medio cuerpo, proporción 3:4. (Mismo individuo que el niño y el anciano.)
```

**3/3 — Varrak anciano:**
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Varrak el Oráculo ANCIANO, orco muy viejo de piel verde-grisácea apergaminada, colmillos desgastados y la misma cicatriz vertical sobre la ceja izquierda; vestiduras de oráculo de motivos astrales. Rostro surcado por mil vidas, ojos que arden en dorado, cargado de futuros vistos. Energía temporal dorada. Medio cuerpo, proporción 3:4. (Mismo individuo que el niño y el adulto.)
```

### ⏰ Lord Vorthak, el Sediento Eterno *(Temporal · Vampiro Ancestral — ápice)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico oscuro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Lord Vorthak, vampiro ancestral de aspecto noble pero demacrado, piel cérea, ojos rojos de hambre insaciable, vestiduras señoriales oscuras. A sus pies, secuaces prematuramente envejecidos y débiles. Ambiente gótico con niebla. Energía temporal dorada con tinte sanguíneo. Presencia de jefe poderoso. Medio cuerpo, proporción 3:4.
```

### ⏰ Medusa la Eterna *(Temporal · Medusa Ancestral)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Medusa la Eterna, medusa ancestral con cabellera de serpientes y mirada que petrifica en el tiempo. A su alrededor, víctimas a medio petrificar congeladas en el instante. Escamas, joyería antigua, porte regio y frío. Energía temporal dorada-verdosa. Medio cuerpo, proporción 3:4.
```

### ⏰ Tempus el Fragmentado *(Temporal · Constructo)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Tempus el Fragmentado, constructo antropomorfo hecho de fragmentos de tiempo: engranajes, esferas de reloj rotas y cristal flotando a su alrededor; partes de su cuerpo se repiten en bucle y se reensamblan. Energía temporal dorada. Cuerpo entero, proporción 3:4.
```

### 🌌 Edward Teach «Barbanegra» *(Dimensional · Humano pirata — ápice recurrente)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Edward Teach «Barbanegra», pirata humano de mediana edad con barba negra trenzada y abrigo de capitán. Poder de estasis robado: una mano envejece y rejuvenece, piel cristalina en zonas, micro-congelaciones del tiempo. Empuña un sable; a su alrededor, portales dimensionales y destellos de tiempo detenido. Carismático y peligroso. Energía mezcla dorada + violeta. Cuerpo entero, proporción 3:4.
```

### 🌌 Dimensionalis la Fracturada *(Dimensional · Tiefling)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Dimensionalis la Fracturada, tiefling de herencia infernal (cuernos, piel rojiza). Su cuerpo muestra múltiples versiones de sí misma en planos superpuestos, todas visibles a la vez, desfasadas como una fractura de la realidad. Laberinto espacial imposible a su alrededor. Energía dimensional violeta. Medio cuerpo, proporción 3:4.
```

### 🌌 Ignis el Devorador Espacial *(Dimensional · Dragón Rojo Ancestral — ápice)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica épica con luz volumétrica, color rico, alto detalle, fondo pictórico atmosférico, calidad de lámina de Monster Manual. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Ignis el Devorador Espacial, dragón rojo colosal y ancestral; escamas que brillan como lava fundida, ojos como pozos de fuego que reflejan otras dimensiones. Tras él se abren portales ardientes al Plano Elemental del Fuego. Pose imponente y amenazante. Cuerpo entero, lámina de criatura, proporción 4:3 horizontal.
```

### 🌌 Matrona Veldrisza, la Tejedora Dimensional *(Dimensional · Drow Matrona — ápice)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico oscuro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Matrona Veldrisza, drow anciana de porte regio. Vestiduras de seda negra con patrones de telaraña dimensional; cabello plateado que se extiende como hilos de telaraña. Iconografía de Lolth (arañas). Al fondo, un gran portal-telaraña hacia Menzoberranzan. Energía dimensional violeta. Medio cuerpo, autoridad imponente, proporción 3:4.
```

### 🌌 Las Gemelas del Espejo — Lyra y Nyx *(Dimensional · Humanas gemelas)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Las Gemelas del Espejo, dos hermanas humanas idénticas vestidas igual pero EN ESPEJO (peinado, joyas y complementos en lados opuestos; una con un ojo azul y otro marrón, la otra a la inversa). Una parece el reflejo perfecto de la otra; entre ambas, una superficie de espejo/portal que insinúa una dimensión invertida. Energía dimensional violeta. Doble retrato a medio cuerpo de ambas, proporción 3:4.
```

### 🌌 Ymir el Eterno Invierno *(Dimensional · Elemental de Hielo — llave del nexo)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook / Monster Manual 2024): fantasía heroica semirrealista, pincelada pictórica, iluminación cinematográfica épica con luz volumétrica, color rico, alto detalle, fondo pictórico atmosférico, calidad de lámina de Monster Manual. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Ymir el Eterno Invierno, gigante elemental de hielo cristalino de unos 6 metros; cuerpo formado por cristales de hielo con luz azulada interior, ojos como pozos de hielo. Su aliento congela el aire en esculturas; a su alrededor, portales de hielo al Plano Elemental del Agua. Cuerpo entero, lámina de criatura, proporción 3:4.
```

> **Opcional — Thyra la Suspendida (caída):** mujer de piel translúcida como cristal, movimientos congelados en el aire, atrapada fuera del tiempo; útil para flashbacks. Usa el mismo ancla + energía temporal dorada.

> **Villanos menores de región** (Cándano, Caelith, Velka, Magistrado Cerografo, Tessaly Bifronte, Karkesh, Zress'ynara, Capitán Móreve, Aurelius Crane, Capataz Drazhûl): sus descripciones están en `05_Apendices/Bestiario_Regional/`. Para retratarlos, usa el mismo ancla de estilo + su descripción del bestiario. Pídemelos y te los dejo también como bloques listos.

---

## 7 · Villanos menores de región (los mini-jefes)

> Uno por región; se combaten antes del lugarteniente. Mismo estilo de lámina de bestiario. Color: temporal = dorado, dimensional = violeta.

### 1 · Cándano el Penitente Eterno *(CR 4 · La Espiral Inversa)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Cándano el Penitente Eterno, humano de mediana edad alterado por el tiempo, antiguo sacristán enloquecido por vivir el mismo día miles de veces. Armadura de cuero tachonado; empuña una "daga de penitencia" cuyas heridas envejecen y pudren la carne. Mirada fanática, energía temporal dorada. Cuerpo entero, proporción 3:4.
```

### 2 · Caelith, el Jardinero a Medias *(CR 5 · Jardín de los Tiempos Gemelos)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Caelith, el Jardinero a Medias, humano horticultor atrapado a medio petrificar: la mitad izquierda es piedra agrietada que nunca cuaja, la derecha aún carne sangrante. Se mueve pesado arrastrando el lado pétreo y blande una gran podadera ("Podadera de Eras"). Energía temporal dorada con destellos de estasis. Cuerpo entero, proporción 3:4.
```

### 3 · Velka la Guardiana de Umbrales *(CR 5 · Glacialis)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Velka la Guardiana de Umbrales, humana transmutada por el frío, hechicera carcelera de portales. Porta un escudo de hielo; su sangre cristaliza al ser herida y conjura lanzas de helada desde umbrales gélidos. Energía dimensional violeta-azulada. Cuerpo entero, proporción 3:4.
```

### 4 · Magistrado Cerografo, el Engranaje Desfasado *(CR 5 · Ruinas del Tiempo Perdido)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Magistrado Cerografo, constructo de relojería modelado a imagen de los modrones, con caparazón de latón; juez mecánico enloquecido que ataca con un brazo-péndulo. Geometría ordenada, engranajes visibles. Energía temporal dorada. Cuerpo entero, proporción 3:4.
```

### 5 · Tessaly Bifronte, la Que Eligió Mal *(CR 6 · El Abismo de los Posibles)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Tessaly Bifronte, humana vidente fracturada: dos versiones de sí misma fusionadas en un cuerpo en guerra consigo mismo (apariencia superpuesta/parpadeante). Empuña una "Daga de los Dos Filos" (una hoja que apuñala y otra que ya apuñaló). Energía temporal dorada. Medio cuerpo, proporción 3:4.
```

### 6 · Karkesh el Cartógrafo de Cenizas *(CR 6 · Llanuras de la Compresión)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico neutro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Karkesh el Cartógrafo de Cenizas, tiefling cultista infernal pactado, agrimensor de la fractura. Armadura de tinta endurecida; traza mapas vivos en pergaminos de piel humana y ataca con punzones de tinta ardiente. Energía dimensional violeta con brasa infernal. Cuerpo entero, proporción 3:4.
```

### 7 · Zress'ynara, la Tejedora de Umbrales *(CR 7 · Ciudad de Veldrisza)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico oscuro/atmosférico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Zress'ynara, drider (torso de sacerdotisa drow caída, cuerpo de araña), maldecida por Lolth, con armadura natural quitinosa. Teje telarañas dimensionales negras y muerde con patas venenosas. Energía dimensional violeta. Cuerpo entero, proporción 3:4.
```

### 8 · Capitán Móreve "el Mascahoras" *(CR 7 · Archipiélago de Barbanegra)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico atmosférico marino, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Capitán Móreve "el Mascahoras", pirata no-muerto cronófago que devora tiempo; cuero tachonado de capitán, aspecto descarnado. Empuña un "sable cronófago" cuyas heridas envejecen a la víctima. Energía dimensional violeta con bruma. Cuerpo entero, proporción 3:4.
```

### 9 · Mayordomo Aurelius Crane *(CR 7 · Mansión de la Sed Eterna)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico gótico oscuro, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Mayordomo Aurelius Crane, vampiro noble no-muerto de cortesía perfecta, atado por un pacto de servidumbre. Librea de mayordomo reforzada, modales gélidos; ataca con garras drenantes que roban años (envejecen a la víctima). Energía temporal dorada con tinte sanguíneo. Cuerpo entero, proporción 3:4.
```

### 10 · Capataz Drazhûl, el Quemador de Fronteras *(CR 7 · Calderas Dimensionales)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico volcánico, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Capataz Drazhûl, humano cultista del fuego transmutado, capataz de las calderas con la piel medio carbonizada y escamas de ceniza. Blande un "Látigo de Escoria" ardiente y conjura fuego. Energía dimensional violeta entre llamas. Cuerpo entero, proporción 3:4.
```

---

## 8 · NPCs clave (mecenas y caras del hub)

> Los que el grupo ve en casi todas las sesiones. Mismo estilo de lámina de personaje.

### Din Goldgear *(artífice gnomo · mecenas)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook 2024): semirrealista, pincelada pictórica, iluminación cálida de taller, color rico, alto detalle, fondo pictórico neutro, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Din Goldgear, gnomo de los bosques joven, pequeña barba bien cuidada, gafas de aumento deslizándose por la nariz, delantal de cuero manchado de aceite con herramientas de artífice al cinto; mirada curiosa e inquieta. A su lado, un pequeño homúnculo de cristal temporal. Medio cuerpo, proporción 3:4.
```

### Capitán Marcus "el Inquebrantable" *(líder de la Resistencia · mecenas tecnológico)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook 2024): semirrealista, pincelada pictórica, iluminación dramática, color rico, alto detalle, fondo pictórico neutro, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Capitán Marcus, humano veterano de ~45 años, robusto, cabello castaño con canas prematuras, ojos grises penetrantes, cicatrices; su mano derecha es una prótesis mecánica compleja que él mismo diseñó. Estética anti-magia industrial (correajes, herramientas, un arma de fuego). Medio cuerpo, proporción 3:4.
```

### Cornelius "el Inmutable" *(relojero místico · mecenas)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook 2024): semirrealista, pincelada pictórica, iluminación cálida, color rico, alto detalle, fondo pictórico neutro con relojes, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Cornelius "el Inmutable", humano de mediana edad, cabello gris plateado despeinado, ojos azul profundo que parecen ver más allá del tiempo, delantal de cuero manchado de aceite con herramientas de relojería; sereno, inmune al caos temporal a su alrededor. Medio cuerpo, proporción 3:4.
```

### Galen *(líder de los Anacronistas · explicador del balance)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook 2024): semirrealista, pincelada pictórica, iluminación suave, color rico, alto detalle, fondo pictórico neutro, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Galen, humano anciano sabio, túnica azul de los Anacronistas, ojos que brillan con sabiduría temporal; porte de mentor sereno. Sutiles motivos de reloj/equilibrio en su vestimenta. Medio cuerpo, proporción 3:4.
```

### Síndica Maren Velasco *(autoridad civil de Cronópolis)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook 2024): semirrealista, pincelada pictórica, iluminación neutra, color rico, alto detalle, fondo pictórico neutro, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Síndica Maren Velasco, humana de mediana edad, administradora civil de un asentamiento sitiado: ropa sobria de funcionaria con cadena/insignia de cargo, gesto cansado pero digno e incorruptible. Lleva un fajo de documentos. Medio cuerpo, proporción 3:4.
```

### Bram "Dosjarras" Holderfast *(tabernero de La Última Hora)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook 2024): semirrealista, pincelada pictórica, iluminación cálida de taberna, color rico, alto detalle, fondo pictórico neutro, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Bram "Dosjarras" Holderfast, enano de las colinas, exsoldado bonachón con barba canosa; le falta una pierna y usa una prótesis mecánica de los Ingenieros. Mandil de tabernero, una jarra en cada mano. Medio cuerpo, proporción 3:4.
```

### Zephyr "el Saltamundos" *(comerciante interplanar)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook 2024): semirrealista, pincelada pictórica, iluminación con destellos estelares, color rico, alto detalle, fondo pictórico neutro, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Zephyr "el Saltamundos", genasi del aire de piel azul pálida y cabello que flota como nubes, ojos que brillan como mil estrellas, sonrisa contagiosa; ropajes de mercader exótico de muchos planos, baratijas mágicas colgando. Medio cuerpo, proporción 3:4.
```

### Jarlaxle *(líder de Bregan D'aerthe · aliado ambiguo)*
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Player's Handbook 2024): semirrealista, pincelada pictórica, iluminación dramática, color rico, alto detalle, fondo pictórico oscuro, calidad de lámina de sourcebook. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Jarlaxle, drow elegante y carismático, sombrero de ala ancha con una gran pluma, parche en un ojo, capa fina y multitud de joyas y objetos mágicos ocultos; sonrisa astuta. Medio cuerpo, proporción 3:4.
```

---

## 9 · Reliquias inventadas (objetos homebrew)

> Láminas de objeto único, fondo neutro (catálogo/códice), sin personajes. Las dos últimas no tienen descripción física en el lore: van como propuesta interpretativa.

### Cronómetro de Realidades
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, leve resplandor mágico, fondo neutro (pergamino), sin personajes, sin texto ni marcas de agua.
Objeto: el Cronómetro de Realidades, un reloj de bolsillo gnomo del tamaño de una mano, carcasa de oro envejecido con engranajes de mithril visibles tras un cristal de zafiro; los engranajes giran de forma anómala (hacia atrás, a saltos, en varias direcciones) y un pequeño cristal central pulsa con luz dorada. Proporción 1:1.
```

### Perla del Vacío Primordial
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: la Perla del Vacío Primordial, esfera del tamaño de un puño, superficie negra como obsidiana con iridiscencia púrpura cambiante; flota ingrávida y en su interior diminutas estrellas brillan y mueren en ciclos eternos. Proporción 1:1.
```

### Talismán de Interceptación Divina
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Talismán de Interceptación Divina, un medallón del tamaño de una mano: en el centro engarzada la Perla del Vacío Primordial (negra con iridiscencia púrpura), rodeada por los engranajes dorados del Cronómetro girando en múltiples direcciones; pulsa alternando luz dorada (temporal) y oscuridad púrpura (dimensional). Proporción 1:1.
```

### Contador del Ritual
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Contador del Ritual, reloj circular de gran tamaño (estilo astrolabio) con múltiples esferas superpuestas y engranajes en giro constante; fragmentos de cristal (aionita) incrustados en el borde que brillan, agujas doradas, y una esfera central que marca un avance creciente con un resplandor rojo de advertencia. Proporción 1:1.
```

### Espejo de Realidad Fragmentada
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Espejo de Realidad Fragmentada, espejo circular con marco de plata ornamentada; su superficie reflectante muestra múltiples realidades superpuestas, como si se mirara a través de varias dimensiones a la vez. Proporción 1:1.
```

### Arena del Tiempo Estabilizada
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: la Arena del Tiempo Estabilizada, un reloj de arena alto con estructura de bronce antiguo; la arena interior es dorada y brilla con luz temporal, y el cristal que la contiene refleja múltiples momentos a la vez. Proporción 1:1.
```

### Excavadora Dimensional
```
Ilustración de objeto/artilugio al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de una máquina mágica, render pictórico realista (metal, engranajes), iluminación de estudio, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: la Excavadora Dimensional, máquina de excavación del tamaño de un carro pequeño, de acero reforzado con engranajes de mithril, con múltiples taladros rotativos y dispositivos de compresión espacial; deja tras de sí un túnel dimensional estabilizado. Estética gnómica/steampunk. Proporción 4:3.
```

### Rotor Infinito
```
Ilustración de objeto/artilugio al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un artefacto mágico, render pictórico realista, iluminación de estudio, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Rotor Infinito, gran rotor circular con engranajes de mithril; núcleo interno que pulsa con energía temporal dorada, envuelto en una carcasa externa de hielo eterno tallado con runas dimensionales que nunca se derrite. Gira eternamente. Proporción 1:1.
```

### Anillos de Poder de los Lugartenientes
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de joyería mágica, render pictórico realista del metal, iluminación de estudio, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: los Anillos de Poder de los Lugartenientes, anillos de metal oscuro (hierro negro/adamantina) con forma de serpiente que se muerde la cola formando el símbolo del infinito (∞); escamas talladas con detalle y ojos que brillan con luz divina —dorada en los temporales, púrpura en los dimensionales—. Muestra dos o tres juntos (uno dorado, uno púrpura). Proporción 1:1.
```

### El Cronosellado *(propuesta — sin descripción en el lore)*
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un artefacto mágico siniestro, render pictórico realista, iluminación dramática, resplandor mágico inquietante, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: el Cronosellado, artefacto-prisión que captura y almacena el poder de una batalla divina. Propuesta: un dispositivo arcano-mecánico de metal negro y oro con dos cámaras enfrentadas (una dorada/solar = tiempo, otra púrpura/vacío = espacio) unidas por un sello central que contiene energía robada pulsante; cadenas rúnicas lo recorren. Es el corazón del ritual. Proporción 1:1. (Nota: aspecto interpretativo; el lore no lo describe.)
```

### Contador del Ritual (monitor de la ascensión) *(propuesta — sin descripción en el lore)*
```
Ilustración de objeto/artilugio al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo, render pictórico realista, iluminación de estudio, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Contador del Ritual, artilugio gnomo de magia + tecnología que mide cuánto le falta a Aethernus para completar su ascensión divina. Propuesta: una columna-astrolabio de bronce y latón con una hilera vertical de 8 segmentos luminosos que se encienden uno a uno (de dorado a púrpura intenso) conforme avanza el ritual, coronada por una esfera graduada con agujas; algún segmento parpadea ("el hipo" cuando muere un lugarteniente). Versión de monitor público fijo en la plaza de Cronópolis, grande. Proporción 1:1. (Nota: aspecto interpretativo; el lore no lo describe.)
```

---

## 10 · Flujo en Gemini (paso a paso)

1. **Una pieza por conversación** (o reusa la misma para variaciones y correcciones).
2. **Copia un bloque entero y pégalo.** Ya incluye estilo y proporción. Pide *"genera una sola imagen"*.
3. **Itera en el chat:** *"más oscuro"*, *"quita el texto de abajo"*, *"corrige la ortografía: «Glacialis»"*, *"el mismo personaje pero de cuerpo entero"*. Gemini reedita sobre el resultado.
4. **Restyle de criaturas:** sube el PNG actual (`cronófago …png`, `simbolo cronófagos.png`) y pega el bloque del §5 (ya trae la coletilla de conservar la pose).
5. **Coherencia:** cuando una criatura te convenza, súbela como referencia para las siguientes (*"mismo estilo, paleta e iluminación que esta"*).
6. **Reemplazo del PNG roto:** `Aethernus Valcarys - Manshoon.png` está corrupto (489 bytes, es un XML, no una imagen); sustitúyelo por el resultado del §4.
7. **Mapa con texto perfecto garantizado:** si Gemini falla con alguna etiqueta, genera el mapa solo con números y usa/edita `mapa_general_chronosia.svg` (ya trae los nombres correctos).

---

*Mantén un estilo y una paleta consistentes en todas las criaturas para que parezcan del mismo manual.*
