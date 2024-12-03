vincular entrada ffmpeg
vincular entrada obs-studio
Diccionario hunspell en admon informativa
En Chrome depósito de contraseñas kdewallet con blowfish. Si la contraseña es la misma de usuario y el login es manual, se habilita el depósito.


# ¿Qué hacer después de instalar Manjaro KDE?

Hace poco decidí pasarme a Manjaro KDE (24.1) y estoy muy contento del cambio.
Así que con motivo a esto, les cuento sobre las cosas por hacer después de
completar la instalación.

Debo aclarar que no soy de los usuarios Linux en modo fanático, así que las
cosas que verás aquí son acordes a mi facilidad para adecuar rápidamente el
equipo y solo resolver los problemas que realmente afectan la experiencia que
busco. Respecto a muchos paquetes populares y tradicionales con GUI, no veo
problema en el uso de ambientes tipo Flatpak o AppImage, pero el movimiento a
Manjaro lo realicé por utilidades más nuevas, algunas no muy populares
todavía y que su instalación en Ubuntu es usar un PPA, compilar o usar un
directorio comprimido. Así que, por el momento, no me complicaré con lo que
pueda saltarme el dolor de cabeza. Ejemplo, disponer del nuevo ecosistema de
utilidades que ha acompañado la onda de Rust (y no depender de descargar y
compilar con _cargo_). También un poco hacer un _desnapping_, empezando por no
ser forzado a usar Firefox en snap.

Para fines de estabilidad y consistencia, la preferencia por los paquetes
_flatpak_ es si estos son empaquetados oficiales o verificados.

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

## Actualizar el sistema

Nuestra herramienta de gestión de paquetes en Manjaro, es `pamac`. Es una
herramienta amigable, que no requiere el esfuerzo extra de memorizar las formas
de argumentos de una sola letra de `pacman`, y con cierta similitud a `apt` de
Ubuntu.

```{code} manjaro
pamac upgrade -a
```

Usamos `-a` para indicar que se considera también la fuente del AUR. El AUR es
el equivalente de los PPA de Ubuntu, pero de una forma unificada, contrario a
la forma segmentado por mantenedor de Ubuntu que lleva fácilmente a muchos
más conflictos. Pero el AUR tiene un soporte de primer nivel podríamos
decirlo, por lo cual a diferencia de los PPA no posee los continuos problemas
por GPG vencida o que su existencia sea un problema para actualizar la
distribución o problemas por repetición de fuentes.

Esta instrucción al mismo tiempo actualiza las fuentes de los paquetes
(repositorio oficial y AUR), no solo los paquetes.

```{code} ubuntu
apt update -q && apt dist-upgrade -y
```

En general, en una distribución tipo _rolling release_ (RR) como Manjaro y
derivadas de Arch, es una buena práctica que esta actualización del sistema
sea frecuente para evitar conflictos de actualizaciones acumuladas.

Para la gestión general de paquetes desde el repo, nos interesa saber como
instalar desde el repositorio oficial, desde el AUR y remover paquetes.

```{code}
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

```{code}
sudo apt install -y PACKAGE
sudo apt remove -y PACKAGE
apt search KEY
apt show PACKAGE
sudo dpkg -i PACKAGE.deb
```

En Ubuntu la instalación desde el PPA es igual, pero requiere un manejo previo
para agregar la fuente del PPA.

En ocasiones, al instalar desde un paquete _DEB_ o desde un PPA, puede ser
común problemas en los cuales no se disponen las dependencias o no se
resuelven adecuadamente, y es necesario aplicar al final `sudo apt install -f`.

## Instala dependencias para compilación de paquetes

Cuando usamos fuentes diferentes al repositorio oficial, será necesario
disponer de una serie de dependencias adicionales que nos ayudan a este
proceso. Esto sería el equivalente del `build-essential` de Ubuntu.

```{code}
pamac install base-devel --no-confirm
```

```{code}
sudo apt install -y build-essential curl git ca-certificates pkg-config
```

Es de resaltar que los paquetes adicionales indicados en el caso de Ubuntu,
vienen instalados por defecto en Manjaro al ser usados de forma directa por
`pamac`.

Como alternativa de instalación de paquetes, Manjaro viene con Flatpak
preconfigurado, así como Ubuntu viene con Snap preconfigurado.

```{code}
sudo apt install -y flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

## Protege tus ojos

Selecciona un tema oscuro en el sistema. Puedes buscar por el menú la opción
de "Colores", y escoger entre "Breath Dark" o "Brisa oscuro". En mi caso me
agradó más la primera. Esta selección influye a lo largo de las aplicaciones
que permitan tomar el tema de sistema. También podemos buscar en el menú la
opción "Estilo de Plasma", podemos usar "Breath".

Si usas KDE Plasma como yo (Manjaro KDE o Kubuntu), puedes usar el modo de "Luz
nocturna" ("Night Color"). Puedes ajustar el modo de ubicación manual,
seleccionas en el mapa y configuras la temperatura de color que consideres
adecuada. En mi caso, uso 4500 K para la luz diurna y 3700 K para la luz
nocturna.

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
[WPS: Troubleshooting](https://wiki.archlinux.org/title/WPS_Office#Troubleshooting).

```{code}
sudo pamac install libreoffice-fresh --no-confirm
sudo pamac install --as-deps libreoffice-extension-texmaths libreoffice-fresh-es --no-confirm
pamac build wps-office-bin ttf-wps-fonts libtiff5 --no-confirm
```

En el caso de Ubuntu, este viene con LibreOffice preinstalado. Y para instalar
WPS será necesario descargar manualmente el archivo _DEB_ de su
[sitio web](https://es.wps.com/office/linux/) e instalar con `dpkg`.

Instala la corrección de ortografía, en mi caso, de español Colombia.
Configura LibreOffice para usar Hunspell con este diccionario.

```{code}
sudo pamac install hunspell hunspell-es_co --no-confirm
```

```{code}
sudo apt install hunspell hunspell-es
```

## Instala Google Chrome

Tanto en Manjaro como en Ubuntu tendremos a Firefox como navegador por defecto,
pero es necesario reconocer que Google Chrome termina siendo necesario muchas
veces.

```{code}
pamac build google-chrome --no-confirm
```

```{code}
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install -f
```

Esto dejará configurado el PPA requerido para las actualizaciones.

Recuerda aplicar la sincronización de tu cuenta en ambos navegadores.

## Sincroniza tus archivos

Existen múltiples opciones de sincronización de archivos, pero sin duda
Dropbox sigue siendo un servicio común para muchos de nosotros al ofrecer una
alternativa gratuita alojada y con soporte para Linux del cliente de
escritorio.

```{code}
pamac build dropbox --no-confirm
```

```{code}
wget -O https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2024.04.17_amd64.deb
sudo dpkg -i dropbox_2024.04.17_amd64.deb
```

Una vez instalado, inicia la ejecución. En este punto vamos al administrador
de sesión de Dropbox y podremos vincular la cuenta.

## Listos para chatear

No solo chateamos desde nuestros celulares, así que es bueno que tengamos
nuestras opciones en el PC. Telegram y WhatsApp que las uso por motivos
personales, y Discord y Slack por motivos laborales.

```{code}
flatpak install flathub org.telegram.desktop
flatpak install flathub com.discordapp.Discord
pamac build whatsapp-for-linux slack-desktop --no-confirm
```

```{code}
flatpak install flathub org.telegram.desktop
flatpak install flathub com.discordapp.Discord
sudo snap install whatsapp-for-linux slack
```

## Toma pantallazos

KDE tiene una herramienta de capturas de pantalla muy buena y sofisticada
(*Spectacle*), pero esto último también me parece que desborda para el uso
rápido. Para esta labor prefiero típicamente _Flameshot_.

```{code}
sudo pamac install flameshot --no-confirm
```

```{code}
sudo snap install flameshot
```

## Listos para la creatividad

Para escribir una entrada en el blog, nuestro trabajo de grado, un informe de
laboratorio, el reporte ejecutivo, la presentación de _marketing_, el diagrama
de flujo de nuestro código o proceso, necesitamos hacer dibujos, diagramas,
videos, convertir formatos o ediciones básicas.

Así que por eso aquí queda nuestro combo creativo.

```{code}
pamac install imagemagick ffmpeg drawio-desktop --no-confirm
flatpak install -y flathub org.gimp.GIMP
flatpak install -y flathub org.inkscape.Inkscape
flatpak install -y flathub org.kde.krita
flatpak install -y flathub com.obsproject.Studio
```

```{code}
sudo apt install -y imagemagick ffmpeg
sudo snap install drawio
flatpak install -y flathub org.gimp.GIMP
flatpak install -y flathub org.inkscape.Inkscape
flatpak install -y flathub org.kde.krita
flatpak install -y flathub com.obsproject.Studio
```

Un ejemplo de lo que puedes hacer con _FFMPEG_ si no lo conoces lo comento en
[](/es/blog/2024/unir-video-y-audio-con-ffmpeg-y-bash.md).

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

```{code} manjaro
sudo pamac install steam --no-confirm
pamac build spotify --no-confirm  # GPG
flatpak install -y flathub com.stremio.Stremio
```

```{code} ubuntu
flatpak install -y flathub com.valvesoftware.Steam
flatpak install -y flathub com.stremio.Stremio
sudo snap install spotify
```

## Ahora mira el firmamento

Un pequeño _bonus_, es para los amantes de la astronomía.

La instalación del software planetario Stellarium y un software de
visualización 3D del universo, Gaia Sky.

```{code}
flatpak install flathub org.stellarium.Stellarium
flatpak install flathub de.uni_heidelberg.zah.GaiaSky
```
