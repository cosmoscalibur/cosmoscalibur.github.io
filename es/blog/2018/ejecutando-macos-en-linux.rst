:redirect: blog/ejecutando-macos-en-linux
:date: 2018-01-18
:tags: linux, macos, máquina virtual, hackintosh, emulación
:category: tecnología
:author: Edward Villegas-Pulgarin
:language: es

Ejecutando macOS en Linux
=========================

Debo admitirlo, no me gusta Mac y sigue sin gustarme, pero en múltiples
ocasiones se hace necesario poder disponer de un Mac al igual que de un
Windows para efectos de pruebas o de correr software específico cuando no hay
de otra. Por este caso me di a la tarea de buscar como lograr ejecutar macOS
en mi equipo Asus que posee Linux instalado de la forma más fácil posible. A
continuación, como ejecutar macOS (específicamente hackintosh) en tu equipo
Linux (el procedimiento aplica también para Windows).

**Requisitos**: Conexión a internet estable, disco duro con más de 100 GB
disponibles, RAM superior a 6 GB, procesador de más de dos núcleos (preferible
Intel) y mucho tiempo.

Contexto
--------

Creo que no hay necesidad pero no hay que dar por obvias las cosas. El primer
punto al respecto de esto es que macOS en si mismo es "imposible" de piratear
porque el sistema operativo esta ligado al hardware. Así, la única manera de
obtener e instalar macOS es tener un equipo Mac. El tema se resuelve entonces
a través de una modificación del sistema operativo que da origen a iPC, OSX86
o Hackintosh, una variación del sistema que permite llevar macOS a equipos
tradicionales (PC).

El cómo se logra esto es elaborado y la verdad no veo interés en comentarlo
pues es el camino difícil, pero solo para resumir diré que el punto inicial
es que hay que tener un equipo Mac en el cual se ejecutan una serie de rutinas
para extraer los directorios del sistema y recrear los llamados del sistema
operativo a una forma entendible por los procesadores x86-64. La forma
sencilla es encontrar de donde obtener ya la imagen del sistema operativo
lista. Pero como podrán ver al googlear no solo un poco sino mucho, todo esta
dicho para quienes tienen Mac pero no para los mortales que no lo tenemos.

Descarga
--------

La verdad, creo que este es el punto más difícil y misterioso del proceso de
lograr la instalación de macOS (modificado). La razón de esta dificultad no
solo se asocia a la dificultad sino al tema legal (con Windows no sucede así
pues la imagen misma del sistema operativo es gratuita y el problema es
conseguir la licencia -salvo que no te importe el mensaje de copia no original
y la ausencia de actualizaciones-).

Después de muchos fracasos en descargas (largas descargas) que me llevaban a
depender de Mac, encontré dos opciones listas para usar que correspondían a
imágenes para máquina virtual (específicamente para VMWare/VirtualBox).
Difíciles de encontrar, recurren a descarga por enlace magnético y hay pocos
pares de descarga lo cual llega a un tiempo largo de descarga.

Necesitas para esto un cliente torrent (si usas Linux probablemente tendrás
por defecto transmission o si usas windows puedes instalar BitTorrent,
µTorrent o FrostWire), una buena conexión a internet y mucha paciencia. El
enlace magnético lo obtendrás de
`The Pirate Bay <https://thepiratebay.org/torrent/17986715/MacOS_Sierra_10.12_VirtualBox_VMWare_Virtual_Image_Preinstalled>`_
dando clic en donde dice *GET THIS TORRENT* (hay un símbolo de un imán al lado
izquierdo). Una vez lo hagas y si tienes correctamente instalado el cliente
torrent, este se abrirá (o el navegador solicitará permiso de abrirlo).

Ahora te esperan unas 12 horas de descarga (en mi caso el pico máximo de
velocidad que recuerdo fue de 120 kB y el mínimo fueron ratos donde no habían
pares de descarga).

Máquina Virtual
---------------

Mi recomendación es no intentar la instalación directa en el equipo (para
empezar, no pude encontrar una imagen para ello). El proceso de instalación
directo tiene sus pasos malucos y al parecer el soporte es básicamente es para
equipos con procesadores Intel (lo demás se hace con más trucos de lo normal y
para posiblemente perder el tiempo). Así, la mejor opción es una máquina
virtual, si fallas solo perdiste tiempo pero sigues con un sistema operativo
funcional montado para trabajar o dispersar.

En Linux me parece mucho más natural usar QEMU (usando la interfaz de
Virt-Manager) pero desafortunadamente este no tiene el soporte necesario y
nuevamente, nos llenamos de trucos bajo la manga si queremos hacerlo funcionar
de esa manera. Por ahora, QEMU es la mejor opción en Linux si deseas
virtualizar Windows u otra distribución linux, pero no macOS (tiene que ver
con el arranque, QEMU mantiene el sistema anterior -*LEGACY*- de arranque de
OSX). Así las cosas, una conversión de formato de la imagen no sirve (lo
intenté).

Necesariamente necesitas de VMWare o de VirtualBox. En mi caso, y es la opción
más simple desde Linux, podemos usar VirtualBox (esta en los repositorios de
varias distribuciones) y en Windows, igual por ser gratuito te lo recomiendo
(`descargar <https://www.virtualbox.org/wiki/Downloads>`_).

Instalación
-----------

Nuestro primer paso es descomprimir el archivo que descargamos (un archivo
:code:`rar`). De los archivos que encontrarás solo es necesario el archivo con
extensión :code:`vmdk` (puedes renombrar el archivo si deseas). Ahora abrimos
VirtualBox y seleccionamos el botón de nuevo.

Ahora vamos a seleccionar el sistema operativo, indicando como se ve en la
imagen y luego asignamos la RAM deseada (2 GB son el mínimo del sistema pero
hay que considerar que además es una máquina virtual, lo cual conviene asignar
más para un comportamiento más fluido) considerando que debes dejar al menos
2 GB disponibles para el sistema operativo del equipo.

.. figure:: /images/ejecutando-macos-en-linux/maquina-virtual-seleccionar-macos.png
   :alt: Selección del sistema operativo
   :scale: 50 %
   :align: center

   Selección del sistema operativo y versión a instalar.

Finalmente debemos indicar que se creara a partir de una imagen de disco
existente y seleccionamos el símbolo de carpeta para buscar el archivo
:code:`vmdk`.

.. figure:: /images/ejecutando-macos-en-linux/maquina-virtual-disco-existente.png
   :alt: Selección de disco existente
   :scale: 50 %
   :align: center

   Selección de crear máquina virtual a partir de disco existente.

Aquí hemos creado ya la máquina en si misma pero debemos configurar antes un
par de cosas. En configuración de la máquina debemos ir a la sección de
sistema (*system*) y luego placa madre (*Motherboard*) y habilitar las
características extendidas (*Extended features*) y elegir *USB Tablet* en el
puntero (*Pointing device*). En la misma sección vamos a la pestaña de
procesador (*Processor*) e indicamos al menos 2 CPU. Por último, en la sección
de monitor (*Display*) vamos a la pestaña *Screen* y asignamos 128 MB a la
memoria de video (*Video Memory*).

Ahora, pasamos a la consola (powershell o CMD en Windows) y ejecutamos lo
siguiente (si es Windows hay que poner :code:`VBoxManage.exe` estando en el
directorio de VirtualBox -:code:`cd "C:Program FilesOracleVirtualBox"`-):

.. code:: bash

   VBoxManage modifyvm "macos" --cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff
   VBoxManage setextradata "macos" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac11,3"
   VBoxManage setextradata "macos" "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"
   VBoxManage setextradata "macos" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Iloveapple"
   VBoxManage setextradata "macos" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"
   VBoxManage setextradata "macos" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1

Tras esto estamos listos para encender la máquina virtual e instalar el
sistema operativo en ella (nombre, usuario, contraseña, idioma, teclado). Lo
único problemático aquí es que tendrás problema con el teclado pues esta
pensado para los teclados Mac. Como cualquier instalación de sistema operativo
es algo lento y más considerando que es una máquina virtual.

.. figure:: /images/ejecutando-macos-en-linux/maquina-virtual-idioma-macos.png
   :alt: Selección de idioma en macOS.
   :scale: 80 %
   :align: center

   Selección de idioma en macOS.

Después
-------

No soy usuario Mac y mi propósito de hacer esto era muy específico, validar
compatibilidad de códigos que uso, desarrollo o contribuyo. Pero en este
mismo sentido, algo que recomiendo hacer, es instalar
`Homebrew <https://brew.sh/index_es.html>`_ con el fin de tener listo nuestro
macOS para pruebas y poder instalar distintos paquetes comunes a la hora de
programar.

Para ello debes abrir la consola que encontrarás en aplicaciones y ejecutar lo
siguiente:

.. code:: bash

   ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Tendrás que tener paciencia pues el proceso me tomó 45 minutos (en foros
reportan la instalación de *homebrew* de casi 2 horas) y necesitas estar
pendiente pues hay dos solicitudes de tu contraseña.

.. figure:: /images/ejecutando-macos-en-linux/maquina-virtual-homebrew-macos.png
   :alt: Instalación de homebrew en macOS
   :align: center
   :scale: 60 %

   Instalación por consola de homebrew en macOS.

Una vez instalado, puedes aprovechar a dejar listo python (actualiza la
versión por defecto e instala el gestor pip). Igualmente es conveniente
instalar otros paquetes de uso común por otras aplicaciones .

.. code:: bash

   brew install pkg-config # Ayuda a determinar la lista de paquetes existentes
   brew install python3 # Python3 no viene por defecto
   brew install python2 # Actualiza la versión existente. En ambos casos se instala pip (pip2 y pip3)
   brew install freetype # Requerido para la manipulación de fuentes -por ejemplo en matplotlib-
   brew install libpng # Requerido para la manipulación de imágenes png -por ejemplo en matplotlib-
   brew install pygtk # Binding de GTK para python. Interfaces en pygtk son comunes.
