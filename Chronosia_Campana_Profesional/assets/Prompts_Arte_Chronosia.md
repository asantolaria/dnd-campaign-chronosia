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

## 2 · Mapa general de Chronosia — ✅ **regenerado** (`00_mapa-general-chronosia.jpg`, nombres canónicos)

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

Marca también, SIN número y con UNA SOLA etiqueta: un pequeño VALLE HELADO al norte, con una torre-aguja solitaria, sellado por una barrera de escarcha; rotúlalo EXACTAMENTE «Valle de la Aguja», una sola vez. NO dibujes ni rotules la Torre de la Eternidad en este mapa (tiene el suyo propio).

Dibuja además, en línea fina punteada, las RUTAS desde Cronópolis a las regiones cercanas, y una ruta distinta sobre el mar (líneas de oleaje) que cruce el Mar Oriental hasta el Archipiélago de Barbanegra (8), para sugerir que solo se llega por mar; si la rotulas, escribe exactamente «Ruta marítima».

Añade rosa de los vientos y una cartela con el título «CHRONOSIA».

**REGLAS DE ROTULADO (estrictas):**
- **TODO el texto en ESPAÑOL.** Nada de inglés: usa «Mar Occidental» y «Mar Oriental» (NO «West/East Sea»), «Glaciares eternos» (NO «Eternal glacias»).
- **Una sola etiqueta por lugar** (no repitas ningún nombre).
- **Sin texto entre paréntesis** y **sin frases ni descripciones** dentro de la imagen: solo los nombres exactos de la lista (el texto largo se corrompe).
- Cuida la **ortografía** de los nombres propios: «Veldrisza» (no «Veldrixza»), «Subterránea» (no «Subterránnea»).
- El Valle de la Aguja se rotula EXACTAMENTE «Valle de la Aguja», UNA sola vez en todo el mapa; NUNCA escribas «Aeguja» ni ninguna otra variante, ni lo dupliques.

Si no puedes garantizar el texto correcto, genera el mapa **SOLO con los números 1-10** (sin nombres) y deja un recuadro de leyenda vacío en una esquina para rotular a mano. Formato vertical, proporción 2:3. Evita marcas de agua y estética de cómic.
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
Región: Las Ruinas del Tiempo Perdido (Chronosia), con distorsión TEMPORAL. Ciudad en ruinas atrapada fuera del tiempo: engranajes colosales semienterrados, relojería rota, fragmentos de piedra flotando inmóviles en el aire, un río que la cruza. MUY IMPORTANTE para el texto: en el MAPA marca SOLO con número (1 a 4) cuatro puntos, y pon los nombres en una caja de LEYENDA aparte titulada «Leyenda»: 1) El Archivo del Tiempo Astillado; 2) El Gran Engramaje Roto; 3) La Forja del Éter Eterno; 4) El Observatorio de las Estrellas Estáticas. Rotula además, con su nombre en cursiva y SIN número, tres lugares: «Refugio del Viajero» (zona segura de entrada), «El Río de los Segundos Perdidos» (el río) y «Los Cañones del Eco Temporal» (al fondo) — estos tres NO llevan número. Cada nombre aparece UNA sola vez. Etiquetas en español. Evita marcas de agua y estética de cómic.
```

### 5 · El Abismo de los Posibles *(Varrak — temporal · nv 7-8)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: El Abismo de los Posibles (Chronosia), con distorsión TEMPORAL. Gran cañón con peñascos e islas flotantes unidas por puentes; el mismo paisaje se repite ligeramente distinto en capas superpuestas y semitransparentes, como realidades paralelas solapadas. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 6 · Las Llanuras de la Compresión *(Dimensionalis — dimensional · nv 7-8 · → Avernus)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: Las Llanuras de la Compresión (Chronosia), con distorsión ESPACIAL. Llanura donde el espacio se pliega: distancias imposibles, caminos que se comprimen, estructuras estiradas o encogidas, horizonte curvado; al fondo, grietas con un resplandor infernal (presagio de Avernus). Rotula EXACTAMENTE seis puntos numerados, respetando tildes y ortografía (ATENCIÓN: se escribe «Encogido», con G — NUNCA «Encojido»): 1) Punto de Entrada Seguro (zona segura); 2) El Bosque de Árboles Encogidos; 3) El Mercado Retorcido; 4) El Puente Infinito y el Páramo Encogido; 5) La Grieta Temporal (las grietas con resplandor infernal hacia Avernus); 6) La Atalaya Comprimida. Al fondo, sin número: «Los Picos Estirados». Etiquetas en español. Evita marcas de agua y estética de cómic.
```

### 7 · La Ciudad Subterránea de Veldrisza *(Veldrisza — dimensional · nv 8-9 · → Underdark)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: La Ciudad Subterránea de Veldrisza (Chronosia), con distorsión ESPACIAL. Caverna-ciudad drow del Underdark: arquitectura tallada en estalagmitas, telarañas colosales que conectan plataformas a distinta altura, un gran portal-telaraña hacia Menzoberranzan y hongos luminosos. MUY IMPORTANTE para el texto: en el MAPA marca los puntos SOLO con los números 1 a 6 (sin escribir nombres sobre el dibujo); pon todos los nombres en una caja de LEYENDA aparte, en una esquina, titulada «LEYENDA», con esta lista EXACTA (respeta tildes, NO mezcles ni repitas nombres): 1) Entrada de los Túneles Superiores (zona segura); 2) Mercado de las Sombras Luminosas; 3) El Gran Portal-Telaraña; 4) Círculo de la Torsión Espacial; 5) Templo del Abrazo de la Araña; 6) La Ciudadela Distorsionada. «Túneles» lleva tilde. Etiquetas en español. Evita marcas de agua y estética de cómic.
```

### 8 · Archipiélago de Barbanegra *(Edward Teach — dimensional · nv 8-9)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: Archipiélago de Barbanegra (Chronosia), con distorsión ESPACIAL. Islas dispersas en un mar antinaturalmente en calma, con vórtices y remolinos dimensionales, restos de naufragios, un fuerte pirata y faros, todo bajo una niebla baja. Etiquetas en español opcionales (revisa la ortografía). Evita marcas de agua y estética de cómic.
```

### 9 · La Mansión de la Sed Eterna *(Vorthak — temporal · nv 9 · → Barovia)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: La Mansión de la Sed Eterna (Chronosia), con distorsión TEMPORAL (drenaje de vida). Finca gótica solitaria envuelta en niebla espesa, con jardines marchitos, criptas y verja de hierro; la niebla se espesa hacia un borde que lleva a otro lugar (presagio de Barovia / Shadowfell). MUY IMPORTANTE para el texto: en el MAPA marca los puntos SOLO con los números 1 a 6, y pon los nombres en una caja aparte cuyo encabezado sea la palabra «Leyenda» en español (no «Map Key» ni nada en inglés). Una SOLA caja de leyenda, no dos. Lista: 1) Entrada Principal (zona segura, la verja); 2) Jardines Marchitos; 3) Fuente de Lágrimas Heladas; 4) El Observatorio Roto; 5) Criptas Familiares; 6) La Mansión (el edificio gótico central). En el borde, sin número, rotula «Niebla Eterna — Hacia Otro Lugar». Etiquetas en español. Evita marcas de agua y estética de cómic.
```

### 10 · Las Calderas Dimensionales *(Ignis — dimensional · nv 9-10 · → Plano del Fuego)*
```
Mapa regional dibujado a mano para mesa de D&D, estilo cartografía clásica de manual de rol: pergamino envejecido, tinta sepia, relieve a plumilla, retícula sutil, una "zona segura" de entrada y 3-5 puntos de interés marcados con iconos. Vista cenital, tono horror cósmico + épica, proporción 4:3.
Región: Las Calderas Dimensionales (Chronosia), con distorsión ESPACIAL. Cordillera volcánica con calderas y ríos de lava, portales ardientes abiertos sobre las bocas de fuego de los que asoma el Plano Elemental del Fuego, y huesos de dragón dispersos. Rotula EXACTAMENTE cinco puntos numerados, respetando tildes; las tres bocas de fuego centrales DEBEN llevar su rótulo: 1) Puesto de Guardia del Amanecer (zona segura); 2) La Aguja Temporal; 3) El Mausoleo de Fulgur; 4) La Grieta Primigenia; 5) Las Tres Calderas (las tres bocas/portales de lava, guarida del señor del fuego). Unidos por el «Camino de los Peregrinos» (un sendero). Etiquetas en español. Evita marcas de agua y estética de cómic.
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

### El Cronosellado *(canon: Cap. 15, la Cámara de Ascensión)*
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un artefacto mágico siniestro, render pictórico realista, iluminación dramática, resplandor mágico inquietante, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: el Cronosellado, el núcleo del ritual de ascensión — una semilla de luz flotante que es a la vez UN SOL DIMINUTO y UNA ESTRELLA NEGRA: un eclipse imposible donde una luz dorada solar y un vacío púrpura estrellado se drenan el uno en el otro en espiral, latiendo como un corazón a punto de pararse. Flota sobre un círculo ritual zodiacal grabado en piedra, con finas cadenas de luz dorada y de sombra violeta que convergen en él desde fuera de plano. Proporción 1:1.
```

### Contador del Ritual (monitor de la ascensión) *(propuesta — sin descripción en el lore)*
```
Ilustración de objeto/artilugio al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo, render pictórico realista, iluminación de estudio, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Contador del Ritual, artilugio gnomo de magia + tecnología que mide cuánto le falta a Aethernus para completar su ascensión divina. Propuesta: una columna-astrolabio de bronce y latón con una hilera vertical de 8 segmentos luminosos que se encienden uno a uno (de dorado a púrpura intenso) conforme avanza el ritual, coronada por una esfera graduada con agujas; algún segmento parpadea ("el hipo" cuando muere un lugarteniente). Versión de monitor público fijo en la plaza de Cronópolis, grande. Proporción 1:1. (Nota: aspecto interpretativo; el lore no lo describe.)
```

---

## 10 · Objetos de facción — inventos y reliquias por bando *(NUEVO)*

> Completa el códice visual del §9 (los 11 artefactos "héroe") con **lo que crearon las facciones**: la tecnología de cada pueblo y las reliquias del clímax. Mismo estilo de lámina de catálogo (objeto único, fondo neutro, sin personajes ni texto). **Paletas guía:** *Anacronistas / Ingenieros* = latón, oro envejecido y relojería gnoma; *Oceánicos de Abysara* = coral, nácar y bioluminiscencia turquesa; *Aethernus* = negro y oro con destellos dorados (Tiempo) y púrpuras (Espacio); *reliquias divinas* = dorado solar contra púrpura del vacío. Donde el lore no describe el objeto, va como **propuesta interpretativa** (marcado). Máquinas y armas largas van en 4:3; el resto en 1:1.

---

### 🌿 Anacronistas

#### Reloj de Estabilización Temporal
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, leve resplandor mágico, fondo neutro (pergamino), sin personajes, sin texto ni marcas de agua.
Objeto: el Reloj de Estabilización Temporal, un reloj gnomo de sobremesa de latón y oro envejecido bajo una cúpula de cristal; su péndulo central oscila sereno y perfecto mientras a su alrededor engranajes exteriores giran de forma caótica y desincronizada. Emite una burbuja de luz dorada tenue y estable a su alrededor (el aire dentro de ella parece "en calma"). Proporción 1:1.
```

#### Gafas de Percepción Temporal
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, leve resplandor mágico, fondo neutro (pergamino), sin personajes, sin texto ni marcas de agua.
Objeto: las Gafas de Percepción Temporal, unas gafas de relojero de montura de latón con varias lentes abatibles de aumento superpuestas; los cristales son de zafiro ahumado y, al mirar a través de ellos, muestran finas estelas doradas —ecos del pasado reciente— suspendidas en el aire. Proporción 1:1.
```

#### Brújula del Tiempo Verdadero
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, leve resplandor mágico, fondo neutro (pergamino), sin personajes, sin texto ni marcas de agua.
Objeto: la Brújula del Tiempo Verdadero, una brújula de bolsillo de latón con anillos concéntricos grabados con horas y símbolos de reloj en lugar de puntos cardinales; su aguja dorada no apunta al norte, sino a un pequeño sol grabado en la esfera (el "tiempo verdadero"). Tapa abierta, mecanismo visible. Proporción 1:1.
```

---

### 🌊 Oceánicos de las Profundidades (Abysara)

#### Amuleto de Respiración Acuática
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Amuleto de Respiración Acuática, un colgante oceánico de nácar y coral pulido que engarza una gota de agua marina encapsulada que nunca se vacía y ondula despacio en su interior; cordón de algas trenzadas. Brillo bioluminiscente turquesa. Proporción 1:1.
```

#### Tridente del Vacío
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un arma mágica, render pictórico realista del material, iluminación de estudio suave, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Tridente del Vacío, un tridente de las profundidades forjado en coral negro y hueso abisal, con las tres puntas grabadas con runas del dios Voidar; de sus dientes gotea una oscuridad estrellada (fragmentos de vacío) y el arma emite un aura fría púrpura-turquesa. Elegante y siniestro. Proporción 3:4.
```

#### Escama de Oceánico
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: la Escama de Oceánico, una gran escama iridiscente de un habitante de Abysara (tonos azul, verde y púrpura que cambian con la luz), montada como talismán/broche sobre una base de coral y plata; bioluminiscencia suave en los bordes. Proporción 1:1.
```

#### Cristal Estabilizador *(tecnología oceánica)*
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un único objeto mágico, render pictórico realista del material, iluminación de estudio suave, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Cristal Estabilizador, un cristal de azul profundo con matices turquesa que parece contener el océano en su interior; superficie lisa como el vidrio pero con textura orgánica de coral, emitiendo una luz tenue y constante azul verdosa. Transmite sensación de calma y protección. Proporción 1:1.
```

---

### ⚙️ La Resistencia (Ingenieros de Cronópolis)

#### Rifle Anti-Magia
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un arma de fuego (tecnología), render pictórico realista del material, iluminación de estudio, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Rifle Anti-Magia, un rifle largo de acero pavonado y latón con culata de madera oscura, cañón reforzado ceñido por anillos de cobre grabados con runas anti-hechizo, mira telescópica y recámara de cerrojo visible. Estética steampunk industrial de La Resistencia. Proporción 4:3.
```

#### Granada de Estabilidad
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un objeto (tecnología), render pictórico realista del material, iluminación de estudio, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: la Granada de Estabilidad, un explosivo esférico de latón con bandas remachadas y un pequeño cristal estabilizador engarzado en el centro que late azulado; pulsador/mecha superior y grabado de un reloj en calma. Proporción 1:1.
```

#### Escudo Tecnológico
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un objeto (tecnología), render pictórico realista del material, iluminación de estudio, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Escudo Tecnológico, un escudo de acero remachado con placas móviles y engranajes en el borde; un generador central proyecta una fina malla de energía anti-magia azulada sobre su superficie. Robusto y funcional, estética de La Resistencia. Proporción 1:1.
```

#### Trampa Mecánica Anti-Magia
```
Ilustración de objeto/artilugio al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un dispositivo (tecnología), render pictórico realista del material, iluminación de estudio, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: la Trampa Mecánica Anti-Magia, un dispositivo de suelo circular de latón y acero, plano y del tamaño de un escudo, con una placa de presión central grabada con runas anti-magia; unos brazos articulados con resortes rematan en barrotes de acero que, al activarse, se despliegan hacia arriba cerrándose en una cúpula-jaula que aísla a un lanzador de conjuros. Muéstralo en vista 3/4, ya disparado, con la jaula de barrotes formada y las runas emitiendo un tenue resplandor azulado que anula la magia dentro. Proporción 4:3.
```

#### Detector de Magia
```
Ilustración de objeto/artilugio al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un dispositivo (tecnología), render pictórico realista del material, iluminación de estudio, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Detector de Magia, un instrumento de mano de latón con diales graduados, agujas indicadoras y finas antenas de cobre; un cristal indicador en el centro parpadea con distinto color según el tipo de magia (temporal dorado, espacial púrpura). Estética de instrumento científico victoriano. Proporción 1:1.
```

#### Estabilizador Temporal *(portátil — versión de campo del Neutralizador)*
```
Ilustración de objeto/artilugio al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un dispositivo (tecnología + magia), render pictórico realista del material, iluminación de estudio, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Estabilizador Temporal, un dispositivo portátil de campo (versión reducida del Neutralizador de Cronópolis) del tamaño de un maletín/mochila de latón y acero, con patas plegables para clavarlo en el suelo, un péndulo pequeño y una esfera de reloj central; al desplegarse proyecta una cúpula-burbuja dorada de radio corto que estabiliza las distorsiones a su alrededor. Muéstralo desplegado y activo. Estética gnómica/steampunk. Proporción 1:1.
```

#### Cerrador de Portales *(antes «Compresor Dimensional» · portátil)*
```
Ilustración de objeto/artilugio al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un dispositivo (tecnología + magia), render pictórico realista del material, iluminación de estudio, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Cerrador de Portales, un dispositivo portátil de latón y acero del tamaño de un instrumento de campo, montado sobre un trípode plegable; en su frente lleva un pequeño iris mecánico (diafragma de placas) que se cierra como un obturador, con bobinas de cobre y una lente que proyecta un fino cono de energía que "cose" y apaga una grieta-portal púrpura. Estética gnómica/steampunk. Muéstralo desplegado sobre su trípode. Proporción 1:1.
```

#### Neutralizador de Campo *(instalación fija — escudo de Cronópolis)*
```
Ilustración de máquina mágica al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un artilugio grande (tecnología), render pictórico realista, iluminación de estudio, resplandor mágico frío, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Neutralizador de Campo, la mayor de las máquinas de los Ingenieros: una instalación fija y masiva de acero —anclada en Cronópolis— con bobinas y antenas de cobre en torno a un núcleo apagado (mate, sin brillo mágico) que proyecta hacia arriba una gran cúpula de energía anti-magia translúcida; es el escudo de la ciudad, e impide que la magia y las distorsiones de fuera penetren en su interior. Imponente, monumental. Proporción 4:3.
```

#### Motor de Viento Perpetuo
```
Ilustración de máquina mágica al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un artefacto grande, render pictórico realista, iluminación de estudio, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Motor de Viento Perpetuo, una gran máquina naval montada en un muelle o proa: una turbina/hélice colosal de latón impulsada por el Rotor Infinito engarzado en su corazón (un núcleo que pulsa energía dorada envuelto en una carcasa de hielo eterno con runas); genera un vendaval visible que hincha velas sobre un mar en calma muerta. Estética gnómica/steampunk. Proporción 4:3.
```

#### Prótesis Mecánica de Balthar
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de una prótesis (tecnología), render pictórico realista del material, iluminación de estudio, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: la Prótesis Mecánica de Balthar, un brazo protésico enano de latón y acero macizo con articulaciones expuestas y remaches; un cañón anti-magia integrado en el antebrazo y runas grabadas en las placas. Robusto, de armero. Proporción 1:1.
```

#### Brazo Mecánico de Lucienne
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de una prótesis (tecnología), render pictórico realista del material, iluminación de estudio, leve resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: el Brazo Mecánico de Lucienne, un brazo protésico más fino y preciso, de acero pulido y latón, con múltiples herramientas de artífice desplegadas en abanico (llaves, destornilladores, calibres) y cuchillas retráctiles asomando. Estética de ingeniera meticulosa. Proporción 1:1.
```

> *(El «Dispositivo de Detección de Kaoros» no lleva lámina propia: es el mismo objeto que el Detector de Magia en versión personal. Si quieres una variante, reusa el prompt del Detector añadiendo "más pequeño, con membranas y diapasones vibrantes en vez de esfera sonora".)*

#### Ferrocarril Universal *(concepto post-campaña — escena)*
```
Ilustración conceptual al estilo key-art de los manuales de Dungeons & Dragons 5e: escena épica, render pictórico realista, iluminación dramática, sin marcas de agua ni estética de cómic.
Escena: el Ferrocarril Universal, la obra final de los Ingenieros gnomos: vías de raíl de latón y acero que cruzan el semiplano fracturado de Chronosia, saltando entre fragmentos de tierra flotantes y engranajes colosales suspendidos; una locomotora de latón impulsada por el Rotor Infinito (núcleo dorado + carcasa de hielo) avanza hacia un gran portal-arco al final de las vías que se abre a una ciudad portuaria reconocible (Waterdeep/Faerûn). Paleta sepia-dorada contra púrpuras. Proporción 3:2 (apaisada). (Nota: aspecto interpretativo; el lore no lo describe en detalle.)
```

---

### 👑 Equipo de Aethernus Valcarys *(botín del clímax — Artefacto Único)*

> Todos comparten estética: **negro y oro** con venas de energía **dorada (Tiempo) y púrpura (Espacio)**, motivo de **eclipse** (sol dorado + estrella negra) y de **serpiente-infinito (∞)**. Son la regalía del BBEG: opulentos e imperiales.

#### Bastón de Mando de Aethernus
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un artefacto mágico, render pictórico realista del material, iluminación de estudio, resplandor mágico, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: el Bastón de Mando de Aethernus, un cetro de ébano negro con filigrana de oro rematado por una gema que es a la vez un sol dorado y una estrella negra (un eclipse), con finos engranajes y anillos orbitando la punta y desprendiendo destellos dorados y púrpuras. Imperial y amenazante. Proporción 3:4.
```

#### Corona de Aethernus
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un artefacto mágico, render pictórico realista del material, iluminación de estudio, resplandor mágico, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: la Corona de Aethernus, una corona de oro negro con puntas afiladas como agujas de reloj y cristales engarzados que laten como corazones —unos dorados (tiempo), otros púrpuras (espacio)—; el frontal muestra un motivo de eclipse. Opulenta y siniestra. Proporción 1:1.
```

#### Armadura de Aethernus
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un artefacto mágico, render pictórico realista del material, iluminación de estudio, resplandor mágico, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: la Armadura de Aethernus, una armadura de placas de metal negro con filigrana dorada y venas de energía dorada y púrpura recorriendo las junturas; hombreras en forma de engranajes y un peto con el motivo del eclipse. Presentada sobre soporte, imperial e imponente. Proporción 3:4.
```

#### Espada de Aethernus
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un arma mágica, render pictórico realista del material, iluminación de estudio, resplandor mágico, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: la Espada de Aethernus, una espada larga de acero oscuro cuyo filo parece "cortar el aire" dejando una estela doble, dorada (temporal) y púrpura (espacial); la guarda tiene forma de serpiente-infinito (∞) y la hoja está grabada con runas divinas. Proporción 3:4.
```

> *(No hay «Escudo de Aethernus»: es un mago y no usa escudo. El único escudo del clímax es el **Escudo de la División**, una reliquia de la Torre — su lámina está en «Reliquias divinas», más abajo.)*

---

### 🔮 Reliquias divinas *(Torre de la Eternidad — clímax)*

#### Fragmento de Amaunator
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de una reliquia sagrada, render pictórico realista, iluminación dramática, intenso resplandor mágico, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: el Fragmento de Amaunator, una esquirla de luz solar solidificada: un cristal dorado ardiente con forma de disco solar roto que flota e irradia calor y luz de mediodía; a su alrededor, eslabones de cadenas doradas rotas (el dios liberado). Proporción 1:1.
```

#### Fragmento de Voidar
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de una reliquia sagrada, render pictórico realista, iluminación dramática, resplandor mágico frío, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: el Fragmento de Voidar, una esquirla de vacío solidificado: un cristal negro-violáceo que contiene en su interior un cielo nocturno estrellado; sus bordes doblan y distorsionan el espacio a su alrededor. Junto a él, eslabones de cadenas púrpuras rotas. Proporción 1:1.
```

#### Cristal de Poder *(dorado / púrpura / multicolor)*
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de un componente mágico, render pictórico realista del material, iluminación de estudio, resplandor mágico, fondo neutro, sin personajes, sin texto ni marcas de agua.
Objeto: los Cristales de Poder, cristales brillantes que cristalizan de los estallidos de la batalla divina; muestra tres juntos que ilustran los tipos: uno dorado (poder temporal), uno púrpura (poder dimensional) y uno multicolor (ambos). Emiten una luz cálida y constante; se sienten llenos de energía. Proporción 1:1.
```

#### Cristal de la Batalla Eterna
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de una reliquia mágica peligrosa, render pictórico realista, iluminación dramática, resplandor mágico intenso, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: el Cristal de la Batalla Eterna, un gran cristal en el que el oro solar y el púrpura del vacío se entrelazan en espiral (un eclipse cristalizado); grietas de energía recorren su superficie y desprende un aura poderosa e inquietante (usar su poder daña al portador). Proporción 1:1.
```

#### Escudo de la División
```
Ilustración de objeto al estilo de los manuales actuales de Dungeons & Dragons 5e: lámina de catálogo de una reliquia/escudo, render pictórico realista del material, iluminación dramática, resplandor mágico, fondo neutro oscuro, sin personajes, sin texto ni marcas de agua.
Objeto: el Escudo de la División, un escudo antiguo partido literalmente por una línea central: una mitad dorada solar (Amaunator), la otra púrpura del vacío (Voidar), con el sello de la fractura del mundo grabado en el centro. Aura divina de ambos dioses. Proporción 1:1.
```

---

## 11 · Pendientes de la auditoría — mapas jugables y piezas nuevas *(NUEVO, sept 2026)*

> Lo que falta por generar tras la auditoría editorial y las ampliaciones: **battlemaps de la Torre (el clímax no tiene mapa jugable), mapa de jugador sin spoilers, battlemaps de Mansión y Galería de Azogue, y los retratos de Gorath y Tholassa.** Además, **regenera el mapa general con el prompt del §2** (el PNG actual conserva nombres antiguos).

### 11.1 · Mapa de JUGADOR del semiplano *(sin spoilers)* — ✅ **generado**: `assets/mapas/13_mapa-jugador-chronosia.jpg`
```
Mapa dibujado a mano para entregar a JUGADORES de D&D, estilo cartografía imperfecta de refugiados: pergamino muy envejecido, tinta sepia desigual, trazos de varias manos, anotaciones toscas, bordes rasgados, alguna mancha. Vista cenital, proporción 4:3.
Tema: el semiplano fracturado de Chronosia como lo conocen sus refugiados — diez regiones-esquirla flotando alrededor de una ciudad costera central, separadas por cortes negros (grietas) por donde no se puede viajar. MUY IMPORTANTE: marca las regiones SOLO con números 1-10 y la ciudad central con una estrella, y pon los nombres en UNA caja «Leyenda»: 1) La Espiral Inversa; 2) El Jardín de los Tiempos Gemelos; 3) Glacialis; 4) Las Ruinas del Tiempo Perdido; 5) El Abismo de los Posibles; 6) Las Llanuras de la Compresión; 7) La Ciudad de Veldrisza; 8) El Archipiélago (mar en calma muerta); 9) La Mansión de la Sed Eterna; 10) Las Calderas Dimensionales; ★ Cronópolis (refugio).
PROHIBIDO incluir (son secretos de DM): ninguna torre, ningún valle sellado al norte del centro, ninguna ciudad submarina, ninguna isla-fortaleza pirata destacada. En una esquina, una nota manuscrita: «No todo está en este mapa. — G.» Etiquetas en español. Evita marcas de agua y estética de cómic.
```

### 11.2 · Battlemaps de la Torre de la Eternidad *(4 planos jugables)* — ✅ **generados**: `assets/mapas/battlemap-torre-nivel1..4-*.jpg`

**Nivel 1 · Sala de Ecos**
```
Battlemap en VISTA EN PLANTA (plano de suelo arquitectónico visto desde arriba) para mesa de D&D, SIN NINGUNA CUADRÍCULA (la rejilla se añade luego en el tablero virtual), estilo pintado a mano de mapa de encuentro profesional (tipo mapas oficiales de WotC), iluminación dramática, sin texto ni marcas de agua, proporción 1:1.
Escenario: cámara circular de piedra oscura en la base de una torre arcana, convertida en un BOSQUE DE ESPEJOS: decenas de espejos de pie con marcos dorados y carcomidos, apoyados unos contra otros, colgando torcidos, formando pasillos laberínticos; algunos rotos en el suelo. Una gran escalera de caracol arranca en el extremo norte. Luz fría azulada con reflejos dorados imposibles en algunos cristales. Sin criaturas.
```

**Nivel 2 · Corazón del Tiempo**
```
Battlemap en VISTA EN PLANTA (plano de suelo arquitectónico visto desde arriba) para mesa de D&D, SIN NINGUNA CUADRÍCULA (la rejilla se añade luego en el tablero virtual), estilo pintado a mano de mapa de encuentro profesional, iluminación cálida y engañosamente acogedora, sin texto ni marcas de agua, proporción 4:3.
Escenario: planta de una mansión lujosa IMPOSIBLE incrustada dentro de una torre: salones opulentos con chimeneas encendidas, biblioteca, comedor servido, dormitorios perfectos — y entre las paredes, ENGRANAJES DORADOS GIGANTES que atraviesan habitaciones y pasillos, girando. Cada puerta está ligeramente desalineada con su marco. Escalera de caracol de subida al norte y de bajada al sur. Sin criaturas.
```

**Nivel 3 · Eliminatoria (el puente)**
```
Battlemap en VISTA EN PLANTA (plano de suelo arquitectónico visto desde arriba) para mesa de D&D, SIN NINGUNA CUADRÍCULA (la rejilla se añade luego en el tablero virtual), estilo pintado a mano de mapa de encuentro profesional, iluminación tenebrosa, sin texto ni marcas de agua, proporción 2:3 vertical.
Escenario: un PUENTE DE PIEDRA EN ESPIRAL, estrecho (10 pies), que cruza un abismo negro sin fondo dentro de una torre; del vacío suben zarcillos y tentáculos de sombra translúcida que rozan el puente sin tocarlo. Grietas y tramos sin barandilla. Plataforma de entrada al sur y arco de salida al norte, ambos de piedra rúnica. Sin criaturas.
```

**Nivel 4 · Cámara de Ascensión**
```
Battlemap en VISTA EN PLANTA (plano de suelo arquitectónico visto desde arriba) para mesa de D&D, SIN NINGUNA CUADRÍCULA (la rejilla se añade luego en el tablero virtual), estilo pintado a mano de mapa de encuentro profesional, iluminación de eclipse (oro contra púrpura), sin texto ni marcas de agua, proporción 1:1.
Escenario: la cima abierta de una torre arcana, una plataforma circular expuesta a un cosmos roto. En el centro, un GRAN CÍRCULO RITUAL ZODIACAL grabado en el suelo con una esfera de luz flotante que es a la vez un sol diminuto y una estrella negra. A izquierda y derecha, DOS PILARES colosales con grilletes y cadenas: unas cadenas gotean luz dorada, las otras sombra violeta, y ambas convergen en el centro. Escalera de llegada al sur. Bordes de la plataforma rotos hacia el vacío estrellado. Sin criaturas.
```

### 11.3 · Battlemap — La Mansión de la Sed Eterna *(interior por salas)* — ✅ **generado**: `assets/mapas/battlemap-mansion-sed-eterna.jpg`
```
Battlemap en VISTA EN PLANTA (plano de suelo arquitectónico visto desde arriba) para mesa de D&D, SIN NINGUNA CUADRÍCULA (la rejilla se añade luego en el tablero virtual), estilo pintado a mano de mapa de encuentro profesional, planta arquitectónica gótica, iluminación de candelabros, sin texto ni marcas de agua, proporción 4:3.
Escenario: planta noble de una mansión vampírica: un GRAN COMEDOR central con una mesa interminable servida para un banquete eterno (copas llenas, platos antiguos) y un trono de respaldo alto en la cabecera; alrededor, galería de retratos, escalinata doble, biblioteca, capilla profanada y acceso a una cripta-salón. Espejos de cuerpo entero en los pasillos, relojes de pie por todas partes, rosales secos en jardineras interiores. Sin criaturas.
```

### 11.4 · Battlemap — La Galería de Azogue y el Estanque de Lágrimas *(Cap. 5)* — ✅ **generado**: `assets/mapas/battlemap-galeria-azogue-estanque-lagrimas.jpg`
```
Battlemap en VISTA EN PLANTA (plano de suelo arquitectónico visto desde arriba) para mesa de D&D, SIN NINGUNA CUADRÍCULA (la rejilla se añade luego en el tablero virtual), estilo pintado a mano de mapa de encuentro profesional, iluminación plateada y espectral, sin texto ni marcas de agua, proporción 2:3 vertical.
Escenario en dos partes conectadas por una escalera: ARRIBA, una galería subterránea estrecha forrada de espejos de todos los tamaños a ambos lados (algunos vacíos, sin reflejo), con una puerta de doble cerradura al fondo, baldosas alternas marcadas y dos palancas enfrentadas a ambos lados de un espejo grande. ABAJO, la orilla de un ESTANQUE NEGRO perfectamente liso como obsidiana pulida que refleja un cielo sin estrellas, rodeado de hierba viva en una mitad y escarcha en la otra. Sin criaturas.
```

### 11.5 · Gorath el Gigante Mordido *(villano menor trágico · CR 6 · Mansión)* — ✅ **generado**: `assets/bestiario/villanos_menores/11_gorath-gigante-mordido.jpg`
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica con luz volumétrica, color rico, alto detalle, fondo pictórico gótico brumoso, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Gorath el Gigante Mordido, un gigante de las colinas vampirizado de 12 pies, corpulento pero desnutrido, la piel pálida grisácea CUBIERTA DE CICATRICES DE MORDISCOS (frescas y rojas unas, blancas y viejas otras, superpuestas en cuello y brazos). Colmillos desafilados, ojos rojos pero apagados y tristes, expresión confundida y mansa — un ser trágico, no amenazante: la reserva de sangre de su amo. Ropa noble vieja que le queda pequeña. Cuerpo entero, proporción 3:4.
```

### 11.6 · Tholassa de la Corriente Honda *(aliada oceánica · emisaria de la Reina Nereia)* — ✅ **generado**: `assets/bestiario/npcs/tholassa-de-la-corriente-honda.jpg`
```
Ilustración pintada digital, estilo de los manuales oficiales actuales de Dungeons & Dragons 5e (Monster Manual 2024): semirrealista, pincelada pictórica, iluminación cinematográfica submarina, color rico, alto detalle, fondo pictórico de arrecife en penumbra, calidad de lámina de bestiario. Evita texto, logotipos, marcas de agua, cómic/anime y aspecto 3D plastificado.
Sujeto: Tholassa de la Corriente Honda, una oceánica noble y solemne del pueblo de las profundidades: humanoide acuática de piel nacarada iridiscente, OJOS LUMINOSOS SIN PÁRPADOS, aletas elegantes en antebrazos y sienes, vestiduras de coral y seda de anémona con una insignia real. Porte de embajadora en luto: digna, antigua, con una ira fría contenida. Empuña un bastón-tridente de coral. Cuerpo entero, proporción 3:4.
```

### 11.7 · Prop — el pergamino de la profecía de Varrak *(opcional)* — ✅ **generado**: `assets/handouts/prop-profecia-de-varrak.jpg`
```
Fotografía cenital realista de un PROP de rol: un pergamino envejecido y manchado de círculos de taza de té, escrito a mano en tinta sepia con siete estrofas en caligrafía cuidada de escriba, sobre una mesa de madera oscura junto a una taza de té humeante. La TERCERA estrofa está QUEMADA: un agujero de bordes carbonizados se come el texto. Sin texto legible necesario (puede ser pseudoescritura); luz cálida de vela, proporción 3:4, sin marcas de agua.
```

---

## 12 · Flujo en Gemini (paso a paso)

1. **Una pieza por conversación** (o reusa la misma para variaciones y correcciones).
2. **Copia un bloque entero y pégalo.** Ya incluye estilo y proporción. Pide *"genera una sola imagen"*.
3. **Itera en el chat:** *"más oscuro"*, *"quita el texto de abajo"*, *"corrige la ortografía: «Glacialis»"*, *"el mismo personaje pero de cuerpo entero"*. Gemini reedita sobre el resultado.
4. **Restyle de criaturas:** sube el PNG actual (`cronófago …png`, `simbolo cronófagos.png`) y pega el bloque del §5 (ya trae la coletilla de conservar la pose).
5. **Coherencia:** cuando una criatura te convenza, súbela como referencia para las siguientes (*"mismo estilo, paleta e iluminación que esta"*).
6. **Reemplazo del PNG roto:** `Aethernus Valcarys - Manshoon.png` está corrupto (489 bytes, es un XML, no una imagen); sustitúyelo por el resultado del §4.
7. **Mapa con texto perfecto garantizado:** si Gemini falla con alguna etiqueta, genera el mapa solo con números y usa/edita `mapa_general_chronosia.svg` (ya trae los nombres correctos).

---

*Mantén un estilo y una paleta consistentes en todas las criaturas para que parezcan del mismo manual.*
