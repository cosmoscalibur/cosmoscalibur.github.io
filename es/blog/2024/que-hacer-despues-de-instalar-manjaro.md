---
date: 2024-12-05
tags: manjaro, arch, ubuntu, kubuntu, kde, pamac, flatpak
category: tecnología, linux
---

# ¿Qué hacer después de instalar Manjaro KDE 24?

Hace poco decidí pasarme a Manjaro KDE (24.1) y estoy muy contento del cambio.
Así que con motivo a esto, les cuento sobre las cosas por hacer después de
completar la instalación.

Aprovechando que vengo de una transición de Kubuntu (24.10) y Xubuntu (22.10),
haré paralelos de estos pasos, así que te servirá como una lista de "qué
hacer después de instalar Kubuntu 24.10".

Respecto a muchos paquetes populares y tradicionales con GUI, no veo problema
en el uso de ambientes tipo Flatpak si los nativos representan un problema o
potencial problema. Ejemplo, OBS no funciona si lo instalo nativo, pero sí en
flatpak, pero además, si está disponible como flatpak verificado prefiero esto
a un paquete disponible en el AUR. Un poco de esto lo discuto en
[](/es/blog/2024/distrohopping-cambiar-de-distribución-linux-y-no-morir-en-el-intento.md),
ya que esto me permite adecuar más rápido y compensar algo de estabilidad.

## Revisa los anuncios

Es importante revisar los [anuncios de liberación](https://forum.manjaro.org/t/stable-update-2024-10-10-kernels-pacman-7-0-kde-frameworks-6-6-virtualbox-7-1-2-mesa/169192/2),
en especial, para estar al tanto de los potenciales conflictos y errores que
tendremos, así como la opción para manejar el error. Ejemplo, en la versión
de liberación 24.1 que dispongo al momento de instalar, presenté los
siguientes errores documentados:

+ [Manjaro KDE no apaga y se queda la pantalla negra con el puntero](https://forum.manjaro.org/t/kde-dont-shut-down-anymore-since-last-update/168818/2):
  La solución a este caso es dirigirnos a "Sesión de escritorio" y en las
  opciones de "Restaurar sesión" seleccionar "Comenzar con una sesión
  vacía".
+ [Después de suspención el sistema queda congelado](https://bbs.archlinux.org/viewtopic.php?pid=2180537#p2180537):
  Este caso me sucedió, pero tras la actualización general no se replicó
  nuevamente así que no tuve oportunidad de probar la solución.

Un detalle extra, durante la instalación si inicias con los controladores
privativos de NVIDIA, puede que tu pantalla se quede gris. En mi caso, bastó
con esperar un tiempo un poco más prolongado para que el proceso retomara la
normalidad (comparativamente contra lo que observé al instalarlo en una VM y
en el PC que no tiene tarjeta gráfica dedicada).

## Actualiza réplicas del repositorio

Este paso es conveniente para que tengas descargas desde los servidores con
mejor tiempo de respuesta, pero además que se encuentren actualizados. En mi
caso me sucedió que la réplica usada comenzó a fallar, y con esto podemos
remover aquellas que ya no son funcionales.

```{code} bash
sudo pacman-mirrors --fasttrack
```

Este paso en Ubuntu no es nativo y representa una complejidad alta para el tipo
de público objetivo de la distribución.

## Actualizar el sistema

Nuestra herramienta de gestión de paquetes en Manjaro, es `pamac`. Es una
herramienta amigable, que no requiere el esfuerzo extra de memorizar las formas
de argumentos de una sola letra de `pacman`, y con cierta similitud a `apt` de
Ubuntu.

Usamos `-a` para indicar que se considera también la fuente del AUR. Esta
instrucción al mismo tiempo actualiza las fuentes de los paquetes (repositorio
oficial y AUR), no solo los paquetes.

El AUR es el equivalente de los PPA de Ubuntu, pero de una forma unificada,
contrario a la forma segmentado por mantenedor de Ubuntu que lleva fácilmente a
muchos más conflictos y representa archivos de configuración por PPA.

En general, en una distribución tipo _rolling release_ (RR) como Manjaro y
derivadas de Arch, es una buena práctica que esta actualización del sistema
sea frecuente para evitar conflictos de actualizaciones acumuladas.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code} bash
pamac upgrade -a
```

También puedes usar `update` en lugar de `upgrade`. Esto es la actualización
general de la distribución y no solo de los paquetes instalados.

:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
apt update -q && apt dist-upgrade -y
```

El primer paso actualiza el índice de los repositorios (incluyendo los PPA) y
el segundo paso actualiza en sí los paquetes instalados incluyendo cambios
propios del sistema que no necesariamente se relacionan con los paquetes
instalados.
:::
::::

Para la gestión general de paquetes desde el repo, nos interesa saber como
instalar desde el repositorio oficial, desde el AUR y remover paquetes.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code} bash
sudo pamac install PACKAGE --no-confirm # Repositorio oficial
pamac build PACKAGE_AUR --no-confirm # AUR
sudo pamac remove PACKAGE --no-confirm
pamac search -a KEY
pamac info PACKAGE
```

Hay una variante interesante de la instalación con la bandera `--as-deps` para
marcar explícitamente los paquetes instalados como dependencias en lugar de
instalación explícita. Así, cuando se remuevan los paquetes por los cuales
nos vimos en la necesidad de instalarlos, estos quedaran marcados como
huérfanos.

Puede que sea "irresponsable" el uso de `--no-confirm`, pero siendo la primera
instalación de los paquetes y que son casos previamente validados, estamos
bien. Sin embargo, esto debemos hacerlo con cuidado y en algunos casos se
podría requerir la validación e incluso cancelación de la transacción. Si
vas a actualizar o agregar paquetes posteriores a tu tanda inicial, puede ser
recomendable hacerlo en modo interactivo como chequeo y ya luego dejarlos para
tus rutinas sin la confirmación. Igual, te recomiendo no usarlo y que tomes
tus propias definiciones.

En caso de usar la instalación desde el AUR, mi recomendación es siempre
proceder sin `sudo` salvo que tengamos contexto que no se requiere clave GPG.
De otra forma, esta se intenta almacenar a nivel del administrador provocando
el error de "_tubería rota_", y es porque la clave debe almacenarse en un
usuario común. Ejemplo, esto sucede con Dropbox y Spotify.

:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code}
sudo apt install -y PACKAGE
sudo dpkg -i PACKAGE.deb  # Descarga manual
sudo apt remove -y PACKAGE
apt search KEY
apt show PACKAGE
```

En Ubuntu la instalación desde el PPA es igual, pero requiere un manejo previo
para agregar la fuente del PPA.

En ocasiones, al instalar desde un paquete _DEB_ o desde un PPA, puede ser
común problemas en los cuales no se disponen las dependencias o no se
resuelven adecuadamente, y es necesario aplicar al final `sudo apt install -f`.

:::
::::

## Instala dependencias para compilación de paquetes

Cuando usamos fuentes diferentes al repositorio oficial, será necesario
disponer de una serie de dependencias adicionales que nos ayudan a este
proceso. Esto sería el equivalente del `build-essential` de Ubuntu.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code}
pamac install base-devel --no-confirm
```

:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code}
sudo apt install -y build-essential curl git ca-certificates pkg-config
```

:::
::::

Es de resaltar que los paquetes adicionales indicados en el caso de Ubuntu,
vienen instalados por defecto en Manjaro al ser usados de forma directa por
`pamac`.

Como alternativa de instalación de paquetes, Manjaro viene con Flatpak
preconfigurado, así como Ubuntu viene con Snap preconfigurado.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

Flatpak está listo para usar.

:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
sudo apt install -y flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```
:::
::::

## Instala un núcleo estable

Aprovecha el último núcleo (*kernel*) disponible en Manjaro, pero es bueno
que instales un *kernel* estable (a la fecha, sería de la rama 6.6, pero
posiblemente 6.12 se perfile como estable también). Esto será necesario en
caso de tener una actualización de *kernel* que rompa el sistema, y sea
necesario usar uno anterior. Ten presente que parte de como sucede esto en
Manjaro, es que las versiones no estables son retiradas de los repositorios,
entonces no hay forma de volverlas a instalar y de ahí otro riesgo.

Puedes instalar el núcleo estable usando el "Gestor de configuración de
Manjaro" con la opción de "Núcleo".

Recuerda editar el archivo `/etc/default/grub` para cambiar el valor de las
líneas de estilo y tiempo de espera. Lo más importante es la opción de
*menu* en la variable de estilo.

```{code} text
GRUB_TIMEOUT=5

GRUB_TIMEOUT_STYLE=menu
```

De esta forma, tendremos el *grub* visible al inicio y podremos usar las
opciones avanzadas para cambiar de núcleo.

En Ubuntu debido a su estabilidad y que el núcleo en sí es parte de lo que se
vincula a la versión de la distribución, no es un paso de prevención a
considerar, y solo sería útil si por el soporte de hardware o alguna
característica muy específica lo requieres.

## Protege tus ojos

Selecciona un tema oscuro en el sistema. Puedes buscar por el menú la opción
de "Colores", y escoger entre "Breath Dark" o "Brisa oscuro". En mi caso me
agradó más la primera. Esta selección influye a lo largo de las aplicaciones
que permitan tomar el tema de sistema. También podemos buscar en el menú la
opción "Estilo de Plasma", podemos usar "Breath".

Si usas KDE Plasma como yo, puedes usar el modo de "Luz nocturna" ("Night
Color"). Puedes ajustar el modo de ubicación manual, seleccionas en el mapa y
configuras la temperatura de color que consideres adecuada. En mi caso, uso
4500 K para la luz diurna y 3700 K para la luz nocturna.

Si no usas KDE puedes instalar [RedShift](https://github.com/jonls/redshift),
pero ten presente que esta herramienta no soporta Wayland.

## Activar teclado numérico al arranque

Si deseas que el teclado numérico se active desde el arranque, vamos a
dirigirnos a la opción de bloqueo numérico de _hardware_ de teclado y
seleccionamos "Activar". Puedes acceder rápidamente a esta opción mediante el
buscador por "Teclado".

Esto es dependiente del entorno gráfico, por lo cual si no usas KDE Plasma te
sugiero revisar directamente la documentación de
[Arch: Activating numlock on bootup](https://wiki.archlinux.org/title/Activating_numlock_on_bootup).

## Prepara tus documentos

Durante la instalación de Manjaro, tenemos la opción de escoger entre
LibreOffice y OnlyOffice como paquete ofimático. Mi preferencia es por
[LibreOffice](https://wiki.archlinux.org/title/LibreOffice#Installation),
pero el paquete instalado de esta forma no es la versión más reciente, por lo
cual lo omito y lo instalo ahora.

Adicional, a veces requerimos de una alternativa compatible con Office, que en
mi caso ocurre por motivos laborales con Excel, y requiero usar WPS. Existen un
par de problemas que me afectaron y fue útil la documentación Arch sobre
[WPS Office: Troubleshooting](https://wiki.archlinux.org/title/WPS_Office#Troubleshooting).

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code} bash
sudo pamac install libreoffice-fresh --no-confirm
sudo pamac install --as-deps libreoffice-extension-texmaths libreoffice-fresh-es --no-confirm
pamac build wps-office-bin ttf-wps-fonts libtiff5 --no-confirm
```

:::
:::{tab-item} Ubuntu
:sync: ubuntu

En el caso de Ubuntu, este viene con LibreOffice preinstalado. Y para instalar
WPS será necesario descargar manualmente el archivo _DEB_ de su
[sitio web](https://es.wps.com/office/linux/) e instalar con `dpkg`.
:::
::::

Instala la corrección de ortografía, en mi caso, de español Colombia. Configura
LibreOffice para usar Hunspell con este diccionario.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code} bash
sudo pamac install hunspell hunspell-es_co --no-confirm
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
sudo apt install hunspell hunspell-es
```
:::
::::

Ahora vamos a "Herramientas > Opciones" y en la sección de "Idiomas y regiones"
y "Generales", escogemos la variante de Idioma predeterminado para los
documentos. Y en "Ayudas de escritura" validamos que esté activo "Revisor
ortográfico Hunspell".

:::{attention}
Al tener un tema oscuro, LibreOffice por defecto no tendrá buena visibilidad de
los íconos. Para corregir esto vamos a "Herramientas > Opciones" y allí en la
sección de "Ver" evaluamos cual se ajusta mejor. En mi caso he escogido "Breeze
(SVG + Dark)"
:::

:::{note}
Si encuentras errores en las palabras detectadas o sugeridas por el diccionario
de *Hunspell* en español, lo puedes reportar en el repositorio GitHub de
[RLA ES](https://github.com/sbosio/rla-es), del cual
[soy contribuidor](/es/blog/2017/toponimos-colombianos-en-rla-es.rst).
:::

## Depósito de constraseñas

Cuando las aplicaciones comiencen a solicitar la creación de la cartera
*kdewallet*, vamos a aceptar la creación con *blowfish*. Además, si la
contraseña es la misma de nuestro inicio de sesión, este se activará
automáticamente.

## Instala Google Chrome

Tanto en Manjaro como en Ubuntu tendremos a Firefox como navegador por defecto,
pero es necesario reconocer que Google Chrome termina siendo necesario muchas
veces.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code} bash
pamac build google-chrome --no-confirm
```

:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install -f
```

Esto dejará configurado el PPA requerido para las actualizaciones.
:::
::::

Recuerda aplicar la sincronización de tu cuenta en ambos navegadores.

Instala la variante de idioma para corregir de tu interés en Firefox, en mi
caso, Español (Colombia) con la extensión
[Diccionario Ortográfico de Español Colombia](https://addons.mozilla.org/es/firefox/addon/diccionario-mozilla-es-co),
de la cual [soy mantenedor](https://github.com/cosmoscalibur/diccionario-mozilla-es-co)
(y pronto actualizaré versión).

## Sincroniza tus archivos

Existen múltiples opciones de sincronización de archivos, pero sin duda
[Dropbox](https://www.dropbox.com/referrals/AABBG1MmL-hedPRRiOrFIiDH6UePOg71THw?src=global9)
sigue siendo un servicio común para muchos de nosotros al ofrecer una
alternativa gratuita alojada y con soporte para Linux del cliente de escritorio.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code}
pamac build dropbox --no-confirm
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code}
wget -O https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2024.04.17_amd64.deb
sudo dpkg -i dropbox_2024.04.17_amd64.deb
```

Esto dejará configurado el PPA requerido para las actualizaciones.
:::
::::

Una vez instalado, inicia la ejecución. En este punto vamos al administrador
de sesión de Dropbox y podremos vincular la cuenta.

## Listos para chatear

No solo chateamos desde nuestros celulares, así que es bueno que tengamos
nuestras opciones en el PC. Telegram y WhatsApp que las uso por motivos
personales, y Discord y Slack por motivos laborales.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code}
sudo pamac install telegram-desktop discord --no-confirm
pamac build slack-desktop --no-confirm
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code}
flatpak install flathub org.telegram.desktop
flatpak install flathub com.discordapp.Discord
sudo snap install slack
```
:::
::::

## Toma pantallazos

KDE tiene una herramienta de capturas de pantalla muy buena y sofisticada
(*Spectacle*), pero esto último también me parece que desborda para el uso
rápido. Para esta labor prefiero típicamente _Flameshot_.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code}
sudo pamac install flameshot --no-confirm
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code}
sudo snap install flameshot
```
:::
::::

## Listos para la creatividad

Para escribir una entrada en el blog, nuestro trabajo de grado, un informe de
laboratorio, el reporte ejecutivo, la presentación de _marketing_, el diagrama
de flujo de nuestro código o proceso, necesitamos hacer dibujos, diagramas,
videos, convertir formatos o ediciones básicas.

Así que por eso aquí queda nuestro combo creativo.

+ *Imagemagick*: Es útil para la conversión entre formatos de imagen.
+ *FFMPEG*: Utilidad de comandos para procesamiento de audio y video. Ejemplo:
  [](/es/blog/2024/unir-video-y-audio-con-ffmpeg-y-bash.md).
+ *OBS Studio*: Herramienta avanzada para grabación y edición de video.
+ *DrawIO*: Permite realizar diagramas y ofrece una gran cantidad de símbolos.
+ *InkScape*: Herramienta de dibujo vectorial. Una alternativa a Corel Draw.
+ *Krita*: Herramienta de dibujo y edición de mapas de bits. Es una
  alternativa a Photoshop. También puedes explorar *Gimp*.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

```{code}
pamac install imagemagick ffmpeg drawio-desktop inkscape krita --no-confirm
flatpak install -y flathub com.obsproject.Studio
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code}
sudo apt install -y imagemagick ffmpeg
sudo snap install drawio
flatpak install -y flathub org.inkscape.Inkscape
flatpak install -y flathub org.kde.krita
flatpak install -y flathub com.obsproject.Studio
```
:::
::::

Durante las pruebas de instalación con _pamac_, tuve problemas con OBS y esto
me motivó a usar los _flatpak_ en general para varios casos y así evitar el
manejo de dependencias opcionales o algunos problemas de controladores. En este
caso particular, OBS genera problemas con `DeckLink` que se relaciona con el
controlador `libva-vdpau-driver `. Acorde al mensaje de error, no se encuentra
instalado y por eso no puede configurar las [cámaras virtuales](/es/blog/2020/usar-la-camara-de-tu-celular-como-webcam.rst),
sin embargo el controlador sí estaba instalado. Esto viendo foros es un
problema común, pero no encontré algo que ayudara a solucionar.

## Momentos de ocio

Mi combo 3S de entretenimiento es Spotify, Stremio y Steam (en este orden de
uso). Spotify se volvió en mi opción para pasar el día a día mientras
trabajo desde casa y ante la ausencia de otros sonidos, necesito que por lo
menos haya música o un _podcast_. Stremio es mi alternativa a los servicios a
los servicios de Streaming ([](/es/blog/2024/la-mejor-alternativa-gratis-a-netflix.md))
y en Steam tengo buenos ratos de ocio sobre los cuales he comentado un poco ya
antes en el blog ([](/es/blog/2021/configurar-retroarch-en-steam.rst) y
[](/es/blog/2024/proton-modo-de-compatibilidad-de-steam.md)).

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro
```{code}
sudo pamac install steam --no-confirm
pamac build spotify --no-confirm
flatpak install -y flathub com.stremio.Stremio
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu
```{code}
flatpak install -y flathub com.valvesoftware.Steam
flatpak install -y flathub com.stremio.Stremio
sudo snap install spotify
```
:::
::::

## Ahora mira el firmamento

Un pequeño _bonus_, es para los amantes de la astronomía.

La instalación del software planetario Stellarium y un software de
visualización 3D del universo, Gaia Sky.

```{code}
flatpak install flathub org.stellarium.Stellarium
flatpak install flathub de.uni_heidelberg.zah.GaiaSky
```
