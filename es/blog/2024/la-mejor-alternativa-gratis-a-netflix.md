---
date: 2024-10-21
tags: netflix, stremio, torrents, películas, series, aplicaciones para linux, aplicaciones para android, aplicaciones para windows
category: entretenimiento, películas y series
---

# Ver películas gratis con Stremio y Torrentio

¿Cansado de que las cuentas de _streaming_ que requieres para ver todo tu
contenido favorito sean ese gasto hormiga que te desangra hasta más no poder?
Espero que no, pero igual, te daré un truco para ver todo ese contenido de forma
cómoda, segura y gratis. Así que te hablaré de Stremio y una extensión que te
permitirá obtener el contenido a partir de *torrents*.

## Stremio

[Stremio](https://www.stremio.com/) es un agregador de contenido multimedia que
permite la búsqueda de proveedores para la reproducción del contenido de
interés. Esta búsqueda de proveedores se realiza por medio de un sistema de
extensiones a distintos servicios (puedes vincular tus cuentas de _streaming_
como Netflix, Disney+, Prime Video, Apple TV) y así tener unificado en un único
centro de multimedia. Pero como esto se basa en extensiones, también es posible
obtener extensiones para la reproducción de contenido desde índices de torrents,
por lo cual puedes tener acceso a contenido gratis y seguro. Un detalle extra
para resaltar, es que está disponible para Linux, Mac, Windows,
[Android](https://play.google.com/store/apps/details?id=com.stremio.one&hl=es_CO)
e incluso [Web](https://web.stremio.com/).

Es importante, que aunque Stremio se puede ejecutar sin tener cuenta creada,
crees la cuenta. De esta forma podrás sincronizar no solo el contenido que ves,
los contenidos en lista, el avance del contenido, sino también las extensiones
instaladas, y esto es clave para luego poder usar Stremio con la extensión para
*torrents* en el móvil o en el televisor.

`````{tab-set}
````{tab-item} Linux
En Linux, puedes instalar el paquete de forma cómoda con la versión oficial
dispuesta como flatpak.

```{code} bash
flatpak install -y flathub com.stremio.Stremio
```
````
````{tab-item} Windows
En [Windows](https://www.stremio.com/downloads), disponemos el tradicional
`.exe` para la instalación.
````
`````

### Torrentio

La magia para ver gratis películas y series viene de una extensión, que te
permite reproducir el contenido de *torrents* en Stremio y posee disposición de
varios servidores de *torrents*, de los cuales voy a destacar *The Pirate Bay*,
*Torrent Galaxy* (estos para contenido en inglés), *Cinecalidad* (para audio
latino) y *Mejor Torrent* (para audio español) y *Nyaasi* (para anime).

Para instalar Torrentio, usaremos este
[enlace](https://torrentio.strem.fun/providers=yts,eztv,rarbg,1337x,thepiratebay,kickasstorrents,torrentgalaxy,magnetdl,horriblesubs,nyaasi,tokyotosho,anidex,mejortorrent,wolfmax4k,cinecalidad%7Csort=seeders%7Clanguage=spanish,latino%7Cqualityfilter=cam/configure)
el cual ya dispone de la configuración que recomiendo. Lo especial de la
configuración es:

1. *Providers*: Excluimos *Rutor*, *Rutracker*, *Comando*, *BluDV* y *Torrent9*.
   Al excluir estos, removemos los casos que poseen contenido principalmente en
   ruso, portugués e italiano. Nos queda el contenido en inglés, español y
   japonés (el ánime)
2. *Sorting*: Aplicaremos *By seeders*, de esta forma le damos preferencia al
   contenido que potencialmente se va a reproducir mejor. Si posee pocos
   *seeders* puede no reproducir y más si es un archivo pesado, pero a veces hay
   sorpresas así que puedes intentar casos incluso de pocos *seeders*.
3. *Priority foreign language*: *Spanish* y *Latino*. Esto ubica de primero el
   contenido en español, siguiendo el ordenamiento de *seeders* y luego
   nuevamente por *seeders* pero ya en cualquier otro lenguaje. Lo habitual es
   que el lenguaje declarado corresponde al lenguaje del audio disponible.
4. *Exclude qualities/resolutions*: *CAM*, no vas a querer ver este contenido.
   Estos son los grabados con cámara sobre una reproducción en cine o casera. La
   imagen y el audio son perversos.

Si consideras modificar algo, adelante, y luego das clic en el botón de
*INSTALL*.

En mi experiencia, hay buena oportunidad de encontrar contenido popular en
español latino y español España (este en particular), pero siempre es mejor
estar dispuesto a ver el contenido en inglés para ir a la fija y con
reproducción fluida. Gracias a la extensión de OpenSubtitles v3 y OpenSubtitles
(ambos oficiales), podemos disponer de un repositorio de subtítulos para
nuestros contenidos, así estos no existan embebidos (si es embebido, mucho
mejor).

### Instalar en TV

Sí, Stremio y sus extensiones funcionan en Android, por lo cual no solo podrás
disponer de esta opción en tu móvil, sino también en tu Android TV. Es
importante como lo advertí previamente, que hayas creado la cuenta en Stremio
porque en TV no hay opción de formulario de ingreso y deberás usar un enlace de
ingreso o QR para acceder desde el móvil o el computador.

La instalación es la mejor opción, pero si no está disponible Stremio para tu TV
también puedes transmitir desde el móvil o conectar el computador o móvil por
cable al TV.

## Extra: Pluto TV

Esta no es precisamente una buena alternativa para un reemplazo de tus cuentas
de _streaming_, pero sí encontrarás buen contenido gratuito y en español latino.
Si creas la cuenta, puedes optar por opciones de sincronización del estado de
avance. [Pluto TV](https://www.pluto.tv/welcome) está disponible en web, Android
y iOS.
