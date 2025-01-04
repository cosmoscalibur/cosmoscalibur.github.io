:date: 2019-10-22
:tags: linux, linux mint, paquetes snap, flatpak, appimage, apt, gestor de
    paquetes, instalación de software
:category: tecnología
:author: Edward Villegas-Pulgarin
:language: es

Instalando paquetes en Linux (Mint)
===================================

En Linux ahora tenemos muchas más opciones para instalar nuestros programas
favoritos y de uso diario, según los intereses personales en reducir espacio en
disco, aumentar estabilidad, mejorar seguridad, disponer siempre de la última
versión, tener muy buena integración con el sistema operativo o no requerir
permisos de administrador. Algunas de las estrategias, incluso facilitan que el
mismo mecanismo podemos usarlo en más de una distribución Linux y así disponer
de una transición más simple.

Este artículo es algo superficial sobre cada gestor, pero más adelante publicaré
artículos dedicados a cada uno de ellos con el fin de contarles más opciones y
trucos.

Programas generales
-------------------

Aunque no es una clasificación estricta, es la forma que veo para hablar de
estos paquetes de *software*. Son paquetes de uso general, lo suficiente para
ser de interés para disponer a través de medios de distribución para público
general. En ocasiones, esto puede incluir paquetes de uso científico o propio de
desarrollo, o de alguna disciplina particular.

Gestor de la distribución
~~~~~~~~~~~~~~~~~~~~~~~~~

La mayor parte de distribuciones Linux disponen de gestores de paquetes de
*software*, que son herramientas para la búsqueda, descarga, instalación y
configuración de estos. Los gestores se conectan a repositorios de paquetes
oficiales que son mantenidos por los desarrollados de la distribución,
asegurando que cumplan con estándares mínimos de compatibilidad y estabilidad.

También, algunos gestores pueden conectar a repositorios mantenidos por la
comunidad, dando la opción de extender el *software* disponible para instalación
por los usuarios de una manera simple, pero a riesgo de inestabilidad o
conflictos por la interacción con paquetes de los repositorios oficiales (no es
general, pero suele ocurrir). Estos repositorios de comunidad los recomiendo
como última opción.

En Ubuntu y Linux Mint, tienes la opción de usar el Centro de Software
(preinstalado) o Synaptic (preinstalado en Linux Mint), para realizar la gestión
de manera gráfica. Pero también puedes usar ``apt-get`` o ``apt`` (recomendado)
para la gestión a través de consola.

::

    sudo apt update -q
    sudo apt install -y okular

Ahora dispones del lector de archivos PDF en tu sistema. Puedes accederlo por el
menú o por comando (``okular``). La primera línea es recomendable para
actualizar las direcciones desde las cuales se descarga el software y los
metadatos para búsqueda. La segunda línea realiza la instalación sin solicitar
confirmación.

AppImage
~~~~~~~~

Me parece la mejor de las opciones entre las nuevas estrategias. Permite la
ejecución inmediata del programa (no requiere instalación), gestiona
actualización y no es necesario permisos de administrador al no requerir
instalar. En teoría, ejecuta en cualquier distribución Linux moderna.

Como el archivo ejecuta directamente, se pueden tener múltiples versiones del
mismo programa. Esto, es por el aislamiento que posee, es un tipo de contenedor,
tal como lo son las opciones de snap y flatpak, lo cual también evita conflictos
en el sistema (programas que puedan requerir la misma dependencia pero en
versiones diferentes, la dependencia no pueda gestionar múltiples instancias o
exponga una brecha de seguridad).

Usaremos Stellarium para dar un ejemplo, y puedes buscar en `AppImageHub
<https://appimage.github.io>`_ para ver una colección de AppImage disponibles.

.. _appimagecode:

Descargamos el `AppImage de Stellarium <https://stellarium.org/>`_ del sitio
oficial del software (el segundo pingüino).

::

    chmod 755 Stellarium-0.19.2-x86_64.AppImage
    ./Stellarium-0.19.2-x86_64.AppImage

La primera línea solo es necesario ejecutarla la primera vez.

Si queremos ejecutarlo de una manera más cómoda, podemos mover el archivo al
directorio de ejecución de binarios del usuario o a uno de ejecución de sistema
para estar disponible para todos los usuarios (``/usr/local/bin/``).

::

    mv Stellarium-0.19.2-x86_64.AppImage ~/.local/bin/stellarium
    stellarium

Nuevamente, la primera línea es solo la primera vez.

.. _instalando-paquetes-en-linux-mint#snap:

Snap
~~~~

Los snap son el mecanismo de instalación promovido por Canonical
(desarrolladores de Ubuntu). Sigue siendo un mecanismo centralizado, que
requiere aprobación de Canonical para ser admitido el paquete y requiere ser
administrador para la instalación.

En Ubuntu viene preinstalado pero en Linux Mint es necesario instalarlo.

::

    sudo apt install -y snapd

Una vez instalado, podemos proceder a instalar un paquete snap.

::

    sudo snap install code --classic
    snap run code # Ejecuta

La ejecución con ``snap run`` es necesaria si tras instalar no reconoce el
paquete. Después de la primera ejecución o tras abrir una nueva terminal o
reiniciar el equipo, será ya reconocido el paquete sin problema para ejecutarse
directamente con el nombre (``code``) o por el menú.

Puedes buscar más paquetes en `snapcraf <https://snapcraft.io/store>`_.

.. update:: 2020-07-02 12:00:00

    A partir de Linux Mint 20 debes primero configurar APT para poder instalar
    Snap. Puedes revisar mi publicación
    :doc:`/es/blog/2020/instalar-paquetes-snap-en-linux-mint-20` para saber como.

Flatpak
~~~~~~~

El caso de flatpak no es muy cómodo, tiene cierta centralización como snap, pero
con fines de indexación. Un desarrollador puede crear su propio repositorio
flatpak. Y al igual que AppImage, no requiere permisos de administrador.

En Linux Mint viene preconfigurado a partir de la versión 18.3, pero si usas
Ubuntu necesitas instalarlo. Desde la 18.10 se encuentra en los repositorios
oficiales.

::

    sudo apt install flatpak
    sudo apt install gnome-software-plugin-flatpak
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

La primera línea instala el gestor de flatpak. La segunda línea permite usar
flatpak con el Centro de Software de Gnome. Y la tercera línea agrega el
repositorio de paquetes flatpak más popular, `flathub
<https://flathub.org/home>`_.

Para ejemplificar, instalaremos el paquete peek

::

    flatpak install -y flathub com.uploadedlobster.peek
    flatpak run com.uploadedlobster.peek

Desafortunadamente la ejecución es siempre así, pero puedes crear un archivo que
te facilite la labor.

::

    echo "flatpak run com.uploadedlobster.peek" > ~/.local/bin/peek
    chmod 755 ~/.local/bin/peek
    peek

A nivel gráfico, por defecto si es agregado al menú.

Compilación y binarios
~~~~~~~~~~~~~~~~~~~~~~

Estas opciones, no son parte de la historia. La compilación sigue siendo
fundamental para la optimización de código crítico o de alto rendimiento como es
necesario en la computación científica. La compilación saca provecho de la
arquitectura del procesador usado.

En este caso, será típico el uso de :program:`configure` y :program:`make`. Para
más información, es necesario leer el archivo :file:`README` que deberías
encontrar, el cual explicará el detalle del proceso de instalación.

En los paquetes con binarios, se obtiene un precompilado que es genérico
respecto al procesador u optimizado no necesariamente para el procesador que se
usa en nuestra máquina.

Una vez tenemos el binario (precompilado o por compilación en nuestra máquina)
debemos dar permiso de ejecución al binario (``chmod 755``) y añadirlo a un
directorio que pertenezca al ``path`` (ejemplo, a :file:`$HOME/.local/bin/`).

Rutinas de instalación
~~~~~~~~~~~~~~~~~~~~~~

En ocasiones encontraremos archivos :file:`.run` o :file:`.sh` que asisten la
instalación, descargando componentes o codificando los distintos archivos en un
solo archivo.

Para este caso, es necesario conferir permiso de ejecución al archivo y proceder
a ejecutarlo. Este procedimiento, es el mismo expuesto en las `primeras dos
líneas de AppImage <#appimagecode>`_.

Referencias
-----------

- `AppImage <https://appimage.org/>`_.
- `Flatpak <https://www.flatpak.org/>`_.
- `Snap <https://snapcraft.io/>`_.
- `Gnome Software Center <https://wiki.gnome.org/Apps/Software>`_.
- `Ubuntu APT <https://help.ubuntu.com/lts/serverguide/apt.html>`_.
