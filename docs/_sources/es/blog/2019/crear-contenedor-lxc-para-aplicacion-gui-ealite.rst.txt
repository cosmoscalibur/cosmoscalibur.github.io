:redirect: crear-contenedor-lxc-para-aplicacion-gui-ealite
:date: 2019-11-11 18:21:26
:tags: contenedor, lxc, lxd, linux, wine, enterprise architect, ealite
:category: tecnología
:author: Edward Villegas-Pulgarin

Crear contenedor LXC para aplicación GUI - EALite
=================================================

El uso de contenedores en la industria del software se ha extendido ampliamente
y no es de extrañar, ofrece a los desarrolladores la posibilidad de mejorar el
aislamiento de sus servicios y de ahí hacerlo menos susceptible a errores por
colisiones con otros servicios o conflictos de dependencias. Al mismo tiempo,
son una alternativa más amigable en recursos respecto a las máquinas virtuales.

Múltiples proveedores de infraestructura para nube ofrecen la opción de
desplegar los servicios a partir de un contenedor, y sin duda, facilita la
distribución de entornos de desarrollo y aplicaciones.

Con estos beneficios (algo similar a lo discutido en
:doc:`instalando-paquetes-en-linux-mint`), procederemos a crear un contenedor
para la ejecución de Enterprise Architect (la versión del visor, pero es
aplicable a la versión completa). De manera oficial hay instrucciones para su
uso en Linux con Wine pero la receta está incompleta (hay que agregar una
instrucción más) y es mejor no ensuciar nuestro sistema de 64 bits con
bibliotecas de 32 bits de manera innecesaria. Así que empecemos.

Instalar LXD
------------

Nuestro primer paso será instalar el paquete LXD, el cual se encuentra
disponible a través de múltiples gestores de paquetes de las distribuciones
Linux pero también como paquete snap. Por facilidad, usaré el paquete snap.

.. code::

   sudo snap install lxd

Ahora, debemos inicializar (solo es necesario la primera vez tras instalar).

.. code::

   sudo lxd init

En mi caso, todos los valores que son preguntados los he dejado en su valor
por defecto. Personalmente, solo debería preocuparnos el tamaño de la unidad
usado (en caso de tener limitaciones en espacio de almacenamiento).

Crear perfil GUI
----------------

Por defecto, el comportamiento de los contenedores es para la ejecución de
servicios y aplicaciones de consola. Por eso, la ejecución de una aplicación
gráfica nos requiere una configuración adicional, que es realizar el paso al
sistema gráfico de nuestro sistema hospedador.

El perfil gráfico es definido con el siguiente código (copia y pega en un nuevo
archivo, :code:`lxdguiprofile.txt`).

.. code::

   config:
     environment.DISPLAY: :0
     raw.idmap: both 1000 1000
     user.user-data: |
       #cloud-config
       runcmd:
         - 'sed -i "s/; enable-shm = yes/enable-shm = no/g" /etc/pulse/client.conf'
         - 'echo export PULSE_SERVER=unix:/tmp/.pulse-native | tee --append /home/ubuntu/.profile'
       packages:
         - x11-apps
         - mesa-utils
         - pulseaudio
   description: GUI LXD profile
   devices:
     PASocket:
       path: /tmp/.pulse-native
       source: /run/user/1000/pulse/native
       type: disk
     X0:
       path: /tmp/.X11-unix/X0
       source: /tmp/.X11-unix/X0
       type: disk
     mygpu:
       type: gpu
   name: gui
   used_by:

Ahora, crearemos el perfil:

.. code::

   sudo lxc profile create gui
   cat lxdguiprofile.txt | sudo lxc profile edit gui

Este procedimiento, solo es necesario hacerlo la primera vez.

Obtener contenedor base
-----------------------

Una vez creado el perfil, lanzaremos un contenedor usando una imagen base, es
decir, sobre la cual desarrollaremos nuestra necesidad. Estas imágenes base se
encuentran disponibles en la página del proyecto y son bases de múltiples
distribuciones Linux, con versiones y arquitecturas diferentes.

Para nuestro fin, usaremos una base de Ubuntu 18.04 para arquitectura i386, que
corresponde a 32 bits. Puedes usar otra distribución siempre y cuando disponga
de la forma de instalar los paquetes necesarios y en versiones recientes (entre
más reciente sea Wine, mejor).

.. code::

   sudo lxc launch --profile default --profile gui images:ubuntu/18.04/i386 ea

Cuando no requerimos la parte gráfica, podemos omitir
:code:`--profile default --profile gui`. Los dos perfiles son un proceso de
herencia, primero se carga el perfil por defecto y luego se añade lo necesario
para las aplicaciones gráficas.

Este procedimiento es la primera vez de cada contenedor. Si por error omitimos
el perfil gráfico, tendremos que volverlo a crear. Si por un error en la
especificación del contenedor lo deseamos eliminar, podemos ejecutar
:code:`sudo lxc rm ea --force`. El forzado es necesario para detener la
ejecución del contenedor, o igual podríamos detenerlo primero,
:code:`sudo lxc stop ea`.

Comandos en el contenedor
-------------------------

Para instalar nuestro programa en el contenedor, necesitamos ejecutar comandos
en este. Para ello, tenemos :code:`lxc exec {contenedor} -- {comando}`. Una
forma interactiva, adecuada para pruebas, es ejecutar bash.

.. code::

   sudo lxc exec ea -- /bin/bash

De esta manera podemos ejecutar los comandos de la misma manera que lo hacemos
en nuestro sistema, ya que estamos en el contenedor.

Si deseamos automatizar, nos interesará enviar directamente las instrucciones
en lugar de bash. Ejemplo, :code:`sudo lxc exec ea -- apt update -q`. Notemos
que se ha usado un comando que requiere privilegios de administrador, y es
porque por defecto el ingreso al contenedor es como administrador. Para hacer
uso del usuario estándar debemos indicarlo de forma explícita (por defecto,
tenemos el usuario ubuntu),
:code:`sudo lxc exec ea -- su - ubuntu -c 'echo $(uname -a)'`.

Gestionar archivos
------------------

La gestión de archivos es realizada con los comandos :code:`file pull` y
:code:`file push`.

Así, si deseamos enviar un archivo:

.. code::

   sudo lxc file push {archivo local} {contenedor}/{ruta contenedor}

Y si deseamos traer un archivo del contenedor:

.. code::

   sudo lxc file pull {contenedor}/{ruta contenedor} {archivo local}

Instalar EALite
---------------

Ahora que sabemos ejecutar comandos en el contenedor, instalaremos las
dependencias y finalmente EALite.

.. code::

   sudo lxc exec ea -- apt update -q
   sudo lxc exec ea -- apt install --install-recommends -y wine-stable winetricks
   sudo lxc exec ea -- apt install -y fonts-crosextra-carlito
   sudo lxc exec ea -- su - ubuntu -c 'winetricks --unattended msxml3'
   sudo lxc exec ea -- su - ubuntu -c 'winetricks --unattended msxml4'
   sudo lxc exec ea -- su - ubuntu -c 'winetricks --unattended msxml6'
   sudo lxc exec ea -- su - ubuntu -c 'winetricks --unattended mdac28'
   sudo lxc exec ea -- su - ubuntu -c 'winetricks --unattended jet40'
   wget http://www.sparxsystems.com.au/bin/EALite.exe
   sudo lxc file push EALite.exe ea/home/ubuntu/EALite.exe
   sudo lxc exec ea -- su - ubuntu -c 'wine msiexec /i EALite.exe'

En este punto, procederemos de manera gráfica a la instalación final de EALite.

.. figure:: /images/crear-contenedor-lxc-para-aplicacion-gui-ealite/instalacion-grafica-ealite-lxc.png
   :width: 480
   :align: center
   :alt: Ventana de instalación gráfica de EALite.

   Ventana de instalación gráfica de EALite.

Ahora, es necesario crear un mecanismo simple para la ejecución de EA.

.. code::

   sudo lxc exec ea -- su - ubuntu -c 'mkdir $HOME/.local/bin'
   sudo lxc exec ea -- su - ubuntu -c 'echo "wine $HOME/.wine/drive_c/Program\ Files/Sparx\ Systems/EA\ LITE/EA.exe" > $HOME/.local/bin/ealite'
   sudo lxc exec ea -- su - ubuntu -c 'chmod 755 $HOME/.local/bin/ealite'

Ejecutar EALite
---------------

Ahora, podemos usar el visor de Enterprise Architect.

.. code::

   sudo lxc exec ea -- su - ubuntu -c 'ealite'

Cuando iniciemos el sistema operativo, requerimos de iniciar el contenedores
antes de ejecutar la instrucción anterior, :code:`sudo lxc start ea`.

.. figure:: /images/crear-contenedor-lxc-para-aplicacion-gui-ealite/ealite-inicio-lxc.png
   :width: 480
   :align: center
   :alt: EA Viewer abierto.

   EA Viewer abierto.

.. figure:: /images/crear-contenedor-lxc-para-aplicacion-gui-ealite/ealite-abrir-proyecto-lxc.png
   :width: 480
   :align: center
   :alt: Acceso al sistema de archivos del contenedor y no solo de la unidad de Wine.

   Acceso al sistema de archivos del contenedor y no solo de la unidad de Wine.

Puedes asegurar una forma simple de ejecutar EALite creando una rutina de
lanzamiento con las dos líneas anteriores en un archivo que sea reconocido en
el :code:`path`.

.. code::

   mkdir -p $HOME/.local/bin
   cat << EOF > $HOME/.local/bin/ealite
   sudo lxc start ea
   sudo lxc exec ea -- su - ubuntu -c 'ealite'
   EOF
   chmod 755 $HOME/.local/bin/ealite

La ejecución con :code:`sudo` puede omitirse si se añade el usuario a un grupo
que permita la ejecución de lxc. Más adelante, haré una publicación sobre como
hacerlo. Por ahora, diviértete ejecutando :code:`ealite` e ingresando la
contraseña de administrador.

Para abrir un proyecto, recuerda usar :code:`file push` y explorar dentro del
contenedor.

Compartir
---------

Para compartir el contenedor, puedes publicarlo y exportar la imagen.

.. code::

   sudo lxc publish ea --alias ealite
   sudo lxc image export ealite

La imagen exportada es un archivo :code:`tar.gz` con el nombre asociado al
*fingerprint* (una secuencia alfanumérica). Luego se debe importar la imagen
y hacer :code:`launch` nuevamente con el perfil.

También puedes exportar directamente el contenedor, lo cual es recomendable
porque lleva con ello la configuración del perfil GUI y es listo para usar
una vez hagas la importación.

.. code::

   sudo lxc export ea ea.tar.gz --optimized-storage 

Referencias
-----------

+ `EA Viewer <https://www.sparxsystems.eu/enterprisearchitect/ea-lite-edition/>`_.
+ `can't run “glxgears” in root on lxc 2.0 container <https://askubuntu.com/questions/827070/cant-run-glxgears-in-root-on-lxc-2-0-container/827146>`_.
  Solución a un posible error usando GUI en LXC.
+ `How to easily run graphics-accelerated GUI apps in LXD containers on your Ubuntu desktop <https://blog.simos.info/how-to-easily-run-graphics-accelerated-gui-apps-in-lxd-containers-on-your-ubuntu-desktop/>`_.
+ `LXD Getting started - command line <https://linuxcontainers.org/lxd/getting-started-cli/>`_.
+ `Image server for LXC and LXD <https://us.images.linuxcontainers.org/>`_.
+ `Installing Enterprise Architect under Linux <https://www.sparxsystems.com/enterprise_architect_user_guide/14.0/product_information/enterprise_architect_linux.html>`_
+ `Winetricks <https://wiki.winehq.org/Winetricks>`_.
+ `How do I export a lxc container? <https://stackoverflow.com/questions/31228191/how-do-i-export-a-lxc-container>`_
