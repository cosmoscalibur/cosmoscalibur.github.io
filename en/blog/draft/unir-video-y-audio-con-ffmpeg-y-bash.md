---
date: 2024-10-20
tags: ffmpeg, bash scripting, vimeo, audio processing, video processing
category: technology, linux
language: en
---

# Unir video y audio con ffmpeg y bash

Recién mi novia me pidió el favor de ayudarle a descargar los videos de un curso
antes de que se venciera el acceso a la cuenta, y tocaba descargar los videos de
Vimeo. Pero el truco de descarga de estos videos, hace que luego toque unir el
audio y el video, así que les contaré como hacerlo con FFMPEG y Bash.

## Descargar video de Vimeo

Bueno, este es el punto inicial de la aventura, y es cómo descargar un video de
Vimeo a través de un sitio que posee autenticación. Resulta que si fuera
directamente de Vimeo, bastaría con la extracción con uso de _cookies_ que
ofrece [yt-dlp](https://github.com/yt-dlp/yt-dlp), pero como el video de Vimeo
está embebido en otro sitio, esto no funciona (o no encontré cómo, pues salía un
error de portal no reconocido para hacer el ingreso).

Al continuar la búsqueda, la única opción que encontré fue una extensión de
Chrome que se llama
[Free Vimeo Downloader](https://chromewebstore.google.com/detail/free-vimeo-downloader/migiikaijhclkmlpnnfficpopgmcpgia?hl=es-419),
que te habilita la opción de descarga desde el navegador de los videos de Vimeo
embebidos en cualquier portal. Te ofrece la opción de descargar los videos en
distintas calidades, aunque debes tener presente que el audio se descarga por
separado, y para poderlo descargar debes primero iniciar la reproducción.

```{attention}
Recuerda reproducir el video para habilitar la descarga del audio.
```

Los archivos descargados tienen como patrón, el nombre del video seguido de la
calidad de video, y en el caso del audio, seguido de `-audio`, ambos en formato
MP4. Ahora, ¿cómo unimos el video y el audio?

## Procesamiento con FFMPEG

Ahora, la tarea asociada al procesamiento para unir los archivos de audio con
los archivos de video, la vamos a delegar en
[FFMPEG](https://ffmpeg.org/download.html), una potente utilidad de línea de
comandos para el procesamiento de audio y video que es gratuita y de código
abierto.

Si usas Debian/Ubuntu o algún derivado, como yo, puedes instalar de la forma que
indico a continuación. Si no, puedes remitirte a la página oficial o también
instalarla con el gestor de paquetes {program}`conda` (aplica a todos los
sistemas operativos).

`````{tab-set}
````{tab-item} Ubuntu
```{code} bash
sudo apt install -y ffmpeg
```
````
````{tab-item} Manjaro
```{code} bash
sudo pamac install --no-confirm ffmpeg
```
````
`````

Para probar el concepto, usaremos uno de los pares de archivos.

```{code} bash
ffmpeg -i Modulo\ 2\ Clase\ 2\ Parte\ 5\ \(720p\ with\ 30fps\).mp4 -i Modulo\ 2\ Clase\ 2\ Parte\ 5-audio.mp4 -c copy output/Modulo\ 2\ Clase\ 2\ Parte\ 5.mp4
```

Como el audio y el video ya están en el mismo formato y codec, no es necesario
FFMPEG para aplicar transformaciones, sino solo para mantener el canal de video
del primer archivo y copiarle el canal de audio del segundo, para generar un
nuevo archivo de multimedia.

Observamos el parámetro `-i` que usamos para indicar un archivo fuente, ya sea
de audio, video o incluso imágenes y de texto. En este caso, lo usamos para
indicar el archivo de video y el archivo de audio que queremos emparejar (cada
archivo debe estar precedido de `-i`).

Si fuera necesario aplicar un _codec_ a estos, se debería indicar la opción
respectiva después de la ruta de cada archivo. En este caso, no nos interesa y
esto nos ayuda a que ejecute más rápido. De tal forma que simplemente indicamos
después del segundo archivo `-c copy` para indicar que se copia directamente,
preservando calidad y formato original.

Por último, se indica la ruta del archivo de salida, es decir, el archivo
resultado de nuestra unión de video y audio.

```{hint}
FFMPEG y su documentación, no es muy cómoda para alguien que no sea familiar
con la línea de comandos, por lo que si tienes dudas de donde empezar, te
recomiendo visitar los recetarios de
[ffmprovisr](https://amiaopensource.github.io/ffmprovisr/).
```

Podemos abrir el video, y veremos que el video con el audio incluido. Y ahora,
¿qué sucede si son 56 videos con sus 56 audios?

## Procesamiento en lote con Bash

Como los archivos tienen un patrón en sus nombres, y pueden ser listados en
orden, y el proceso que se ejecuta sobre cada par es el mismo, podemos crear una
rutina para este procesamiento en lote, y evitar así posibles errores como
omitir un par de archivos, mezclar un video con el audio de otro o errores de
digitación.

Necesitaremos almacenar los listados por separado de los archivos de video y
audio, de tal forma que iteremos de manera general sobre el total de videos y
avancemos en los dos listados, que al estar ordenados y con el patrón de nombre
iniciando por el nombre general del video, permitirá emparejarlos.

Luego, de manera cíclica obtenemos estas parejas, con las cuales formaremos los
archivos para los parámetros `-i` de {program}`ffmpeg`, y la asignación de la
ruta de salida.

Esto lo haremos en _bash_ (bueno, esto es para usuarios Linux, pero si usas
Windows, te invito a replicarlo en PowerShell o tu lenguaje favorito).

```{code-block} bash
---
name: bash-ffmpeg-unir
caption: Código *bash* para unir un conjunto de videos y audios con FFMPEG.
linenos:
---
#! /usr/bin/bash

OUTPUT=output
mkdir -p $OUTPUT
AUDIO_LIST=(*audio.mp4)
VIDEO_LIST=(*fps*.mp4)
LEN=${#AUDIO_LIST[*]}
echo "$LEN videos"
for ((i = 0; i < LEN; i++)); do
    echo "Procesando video: $((i + 1))"
    VIDEO_NAME="${VIDEO_LIST[$i]}"
    ffmpeg -i "$VIDEO_NAME" -i "${AUDIO_LIST[$i]}" -c copy "$OUTPUT/$VIDEO_NAME"
done
```

Te explico el código.

Línea 1, es una línea _shebang_ para indicar la ruta absoluta del interprete de
_shell_, en este caso, {program}`bash`.

En la línea 3, asignamos el nombre para el directorio de salida, que usaremos
para crear dicho directorio en la línea 4 y para formar la ruta completa de
salida en la línea 12.

En la línea 4 vemos la primera aparición de `$` que usamos para expandir un
resultado que puede ser de una variable como en este caso, o incluso de una
ejecución. Aquí, sobre {command}`mkdir -p` tenemos para decir que esto crea la
carpeta, y su opción `-p` es para que no falle en caso de ya existir.

Para obtener el listado de archivos podríamos usar `ls`, pero para convertir a
un arreglo tenemos que hacer ajustes en el `IFS`, y resulta más simple usar
directamente la expansión global de nombre de archivo, como lo hacemos en las
líneas 4 y 5.

La manera como nos referimos a un arreglo en Bash, es con `${ }` rodeando lo
requerido del arreglo, como la indicación a un elemento específico (`${ARR[0]}`)
usado en la línea 11 y 12, la totalidad de elementos (`${ARR[*]}` o `${ARR[@]}`)
o una variante con el símbolo `#` antes del nombre del arreglo para hacer el
conteo como se usa en la línea 7.

La sentencia `echo` la usamos para imprimir en la terminal, y vemos que el
mensaje está en comillas dobles, lo que evita que el resultado se intente
expandir (ejecutar), pues solo nos interesa hasta ese punto.

En las líneas 9 y 10 notamos la existencia de doble paréntesis, esto permite la
expansión aritmética. Siempre que necesitemos operaciones aritméticas, usamos
doble paréntesis. En particular, la línea 9 es el inicio del ciclo `for` en
Bash, que usa expansión aritmética con la asignación del valor inicial de la
variable para recorrer las listas, la condición del recorrido la cual es
mientras sea menor que la longitud de las listas y finalmente el avance en uno
para poder pasar al siguiente elemento. Luego sigue la indicación del `do` con
el bloque que repetiremos, y que depende de nuestra variable del ciclo (`i`). Y
para cerrar el ciclo, terminamos en `done`.

Bueno, con esto, estamos listos para ejecutar nuestro código que podemos
disponer en un archivo `unir_video.sh` y ejecutar como:

```{code} bash
bash unir_video.sh  # opción 1
. unir_video.sh  # opción 2
source unir_video.sh  # opción 3
```

Las últimas dos opciones son el motivo de usar el *shebang* de la línea 1, para
distinguir la _shell_ a usar.

Es hora de ejecutar, y deja que esto trabaje por ti con tu colección de videos.

```{hint}
Los 3 recursos que te recomiendo para Bash:

- [Explain Shell](https://explainshell.com/): Escribes una instrucción y te
  la explica.
- [Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls): Una compilación
  de errores comunes de los usuarios en Bash. Una forma de ver los
  antipatrones y ver las buenas prácticas.
- [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html)
  y [BASH Programming - Introduction HOW-TO](https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html):
  Los puntos iniciales de referencia que recomiendo para Bash, del proyecto de
  documentación de Linux, *TLDP*.
```
