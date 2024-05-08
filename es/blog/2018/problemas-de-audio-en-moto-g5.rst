:redirect: problemas-de-audio-en-moto-g5
:date: 2018-01-04 20:03:38
:tags: android, motorola, celulares, smartphone, audio, moto g5
:category: tecnología/trucos para android
:author: Edward Villegas-Pulgarin

Problemas de audio en Moto G5
=============================

Recién cambié mi celular Moto G3 por un Moto G5 y vaya susto el que me llevé
inicialmente. La verdad, como el cambio fue más bien un asunto de afán no
revisé foros previamente
(:doc:`ver recomendaciones a la hora de comprar </es/blog/2018/comprando-celular-para-personalizar>`)
sobre los problemas y me confié de los conocidos que tienen este celular y que
nunca les he escuchado de problemas.

El susto comenzó con la primera llamada (cuando lo compré no se hizo prueba de
llamada) y la sorpresa de encontrarme sin audio. Hice dos intentos adicionales
pensando que podía ser algún problema de señal pero persistía hasta que algo
se escucho cuando iba a cortar la llamada. Nuevamente probé, y el audio
empezaba 5 segundos después de conectarse la llamada.

Ante esto acudí al dios Google y me encontré una gran cantidad de noticias en
páginas de celulares y foros técnicos que reportaban no solo mi problema, sino
además otros problemas de audio (y otros problemas).

Problema y origen
-----------------

Del mes de mayo de 2017 (3 meses después de la fecha de lanzamiento) se
observan en esta búsqueda los primeros reportes de problemas de audio como
ausencia de sonido durante el inicio de las llamadas, mala calidad del audio e
incluso la apreciación de voz digitalizada. En algunos foros se encuentra
reportado como problemas específicos de algunos operadores móviles pero
realmente no es así, y ya entenderemos por que.

La razón de este error es que por defecto el Moto G5 viene habilitado con una
opción de mejora de audio a través de recursos LTE pero bueno, ¿es una mejora?

Esta mejora de audio con recursos LTE significa que la señal asociada al audio
de la llamada posee un procesamiento adicional con el fin de realizar el
filtrado de ruido y mejora del nivel de audio (volumen) pero esto significa
que hay un trabajo extra del procesador que no solo representa recurso de
procesamiento sino también de tiempo. Efectivamente en mis ensayos puedo decir
que percibí ligeramente un audio mucho más limpio con la mejora LTE pero nadie
espera que en una llamada toque gastar primero 5 segundos para iniciar el
audio, por lo cual resulta impráctico.

La voz digitalizada referida en los foros corresponde al efecto del
procesamiento de naturaleza digital y no analógica de la señal, algo que no
todos sentimos pero que al igual que en la música, algunos logran diferenciar
el sonido de un instrumento sintetizado de un instrumento tradicional
analógico. La mala calidad de audio podría ser un efecto no deseado del filtro.

Solución
--------

Bueno, sabiendo que la solución se encuentra en internet y no es difícil
encontrarla, decidí publicarla porque no siempre quien la necesita sabe inglés
así que esta es una forma de contribuir (al igual que las publicaciones de
ciencia) y bueno, a veces puedo dar detalles adicionales.

Necesitamos entrar a `Configuración` y en la sección de "Conexiones
inalámbricas y redes" seleccionamos `... Más`. Ahora nos dirigimos a
`Redes móviles` y deshabilitamos la opción `Modo 4G LTE mejorado`. Aunque nos
indica que se recomienda usarlo ya sabemos por experiencia que es el origen de
nuestro problema de audio.
