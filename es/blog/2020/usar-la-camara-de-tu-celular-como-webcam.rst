:date: 2020-05-17
:tags: linux, android, webcam, cámara, droidcam, aplicaciones android
:category: tecnología
:author: Edward Villegas-Pulgarin
:language: es

Usar la cámara de tu celular como webcam
========================================

Con la nueva normalidad que vivimos alrededor de la virtualidad, el uso de
videollamadas se ha incrementado y muchas cámaras incorporadas en los
equipos no poseen buenas características (o son ausentes). Adicional, el
soporte de opciones como usar el celular, una buena alternativa para no
comprar una cámara web, es amplio en Windows pero no en Linux.

Así que, por ese motivo hoy les compartiré como usar la cámara del celular
(Android o iOS) como cámara web en Linux.

DroidCam
--------

Sin hacer muchos rodeos y comparaciones, en este asunto seré muy práctico.
La primera aplicación que me cumplió con las características y que
funcionó adecuadamente, es DroidCam [droidcam_]. Esta utilidad nos permite
usar la cámara del celular para reemplazar los incorporados del equipo, y
se puede hacer comunicación tanto por wifi como por el cable USB
(instalando ADB).

Instalación en Linux
~~~~~~~~~~~~~~~~~~~~

El procedimiento de instalación puede seguirse en la página web de
DroidCam [linux_] pero lo lustraré para el caso de Linux Mint
(aplicable para Debian y derivados). El aspecto dependiente de la
distribución es la instalación de las 3 dependencias requeridas (GCC, Make
y Linux Headers).

.. raw:: html

    <pre><font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#729FCF"><b>/tmp</b></font>$  wget https://files.dev47apps.net/linux/droidcam_latest.zip
    --2020-05-12 19:03:30--  https://files.dev47apps.net/linux/droidcam_latest.zip
    Resolving files.dev47apps.net (files.dev47apps.net)... 104.28.5.185, 104.28.4.185, 2606:4700:3037::681c:4b9, ...
    Connecting to files.dev47apps.net (files.dev47apps.net)|104.28.5.185|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 933306 (911K) [application/zip]
    Saving to: ‘droidcam_latest.zip’
    droidcam_latest.zip 100%[===================&gt;] 911,43K  2,45MB/s    in 0,4s
    2020-05-12 19:03:30 (2,45 MB/s) - ‘droidcam_latest.zip’ saved [933306/933306]
    <font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#729FCF"><b>/tmp</b></font>$  echo &quot;5ff0e772a76befba4e37e03101b611d7 droidcam_latest.zip&quot; | md5sum -c --
    droidcam_latest.zip: OK
    <font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#729FCF"><b>~/tmp</b></font>$ sudo apt install -y gcc make linux-headers-`uname -r`
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    make is already the newest version (4.1-9.1ubuntu1).
    gcc is already the newest version (4:7.4.0-1ubuntu2.3).
    linux-headers-5.3.0-51-generic is already the newest version (5.3.0-51.44~18.04.2).
    <font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#729FCF"><b>/tmp</b></font>$  unzip droidcam_latest.zip -d droidcam &amp;&amp; cd droidcam
    Archive:  droidcam_latest.zip
      inflating: droidcam/LICENCE
      inflating: droidcam/Makefile
      inflating: droidcam/README.md
      inflating: droidcam/droidcam
      inflating: droidcam/droidcam-cli
      inflating: droidcam/install
      creating: droidcam/src/
      inflating: droidcam/uninstall
      creating: droidcam/v4l2loopback/
      inflating: droidcam/v4l2loopback/v4l2loopback-dc.c
      inflating: droidcam/v4l2loopback/Makefile
      inflating: droidcam/v4l2loopback/test-mmap.c
      inflating: droidcam/v4l2loopback/test.c
    <font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#729FCF"><b>/tmp/droidcam</b></font>$  sudo ./install
    [sudo] password for cosmoscalibur:
    Webcam parameters: &apos;640&apos; and &apos;480&apos;
    Building v4l2loopback-dc.ko
    make: Entering directory &apos;/tmp/droidcam/v4l2loopback&apos;
    make -C /lib/modules/`uname -r`/build M=`pwd`
    make[1]: Entering directory &apos;/usr/src/linux-headers-5.3.0-51-generic&apos;
      CC [M]  /tmp/droidcam/v4l2loopback/v4l2loopback-dc.o
      Building modules, stage 2.
      MODPOST 1 modules
      CC      /tmp/droidcam/v4l2loopback/v4l2loopback-dc.mod.o
      LD [M]  /tmp/droidcam/v4l2loopback/v4l2loopback-dc.ko
    make[1]: Leaving directory &apos;/usr/src/linux-headers-5.3.0-51-generic&apos;
    make: Leaving directory &apos;/tmp/droidcam/v4l2loopback&apos;
    Moving driver and executable to system folders
    + cp v4l2loopback/v4l2loopback-dc.ko /lib/modules/5.3.0-51-generic/kernel/drivers/media/video/
    + cp droidcam /usr/bin/
    + cp droidcam-cli /usr/bin/
    + set +x
    Registering webcam device
    Running depmod
    make: Entering directory &apos;/tmp/droidcam/v4l2loopback&apos;
    make -C /lib/modules/`uname -r`/build M=`pwd` clean
    make[1]: Entering directory &apos;/usr/src/linux-headers-5.3.0-51-generic&apos;
      CLEAN   /tmp/droidcam/v4l2loopback/Module.symvers
    make[1]: Leaving directory &apos;/usr/src/linux-headers-5.3.0-51-generic&apos;
    make: Leaving directory &apos;/tmp/droidcam/v4l2loopback&apos;
    Adding uninstall script
    Adding driver to /etc/modules
    Done
    <font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#729FCF"><b>/tmp/droidcam</b></font>$ lsmod | grep v4l2loopback_dc
    <font color="#EF2929"><b>v4l2loopback_dc</b></font>        24576  0
    videodev              208896  5 v4l2_common,videobuf2_v4l2,<font color="#EF2929"><b>v4l2loopback_dc</b></font>,uvcvideo,videobuf2_common
    </pre>

La última instrucción es solo para efectos de validación. Si sale
:code:`v4l2loopback_dc`, estamos bien.

Instalación en Android
~~~~~~~~~~~~~~~~~~~~~~

Para instalar en Android, buscamos DroidCam en Google Play [android_].
Encontrarán dos versiones, una gratuita y una paga. Podemos usar la
gratuita para la funcionalidad requerida, siendo única limitación la
resolución máxima a la que transmite.

Una vez instalada, procedemos a abrir y seguir los siguientes pasos:

1. Mensaje de agradecimiento, presionamos "Próximo".
2. Instrucciones para cámara web, presionamos "Obtener".
3. En la siguiente vista obtenemos la IP y el puerto que debemos
   configurar en nuestro equipo.

.. figure:: /images/usar-la-camara-de-tu-celular-como-webcam/droidcam-activo-ip-puerto.jpg
   :align: center
   :width: 300px
   :alt: DroidCam activo (información de IP y puerto).

   DroidCam activo (información de IP y puerto).

En la parte superior derecha, accedemos a la configuración. La
configuración importante para nosotros está en la sección "CÁMARA", y es
el límite de FPS (ayuda a ahorrar batería) y la cámara que se usará (en
"Cámara" podemos seleccionar cuál de las cámaras).

Ejecutar
--------

Finalmente, para hacer uso de DroidCam en Linux, debemos ejecutar en la
consola :code:`droidcam` y esto abrirá un GUI para ingresar la IP y el
puerto que usaremos.

.. raw:: html

    <pre><font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#729FCF"><b>/tmp/droidcam</b></font>$ droidcam
    Device: USB2.0 VGA UVC WebCam: USB2.0 V
    Device: USB2.0 VGA UVC WebCam: USB2.0 V
    Device: Droidcam
    Found driver: /dev/video2 (fd:7)
    connecting to 192.168.1.2:4747
    </pre>

.. figure:: /images/usar-la-camara-de-tu-celular-como-webcam/droidcam-linux-gui.png
   :align: center
   :width: 400px
   :alt: Cliente GUI de DroidCam en Linux.

   Cliente GUI de DroidCam en Linux. Aquí ingresamos IP y puerto.

Una vez configurado, presionamos "Connect". En este momento DroidCam del
celular activará la vista de la cámara y podremos configurar la aplicación
que requiera de la cámara.

Para ejemplo, tomaré Skype, pero será igual con toda aplicación que
soporte selección de cámara (aplica para Hangout, OBS, Teams, entre otras).
En el menú respectivo, seleccionamos "DroidCam" y estamos listos.

.. figure:: /images/usar-la-camara-de-tu-celular-como-webcam/droidcam-seleccion-skype.jpg
   :align: center
   :width: 400px
   :alt: Selección de DroidCam como cámara en Skype.

   Selección de DroidCam como cámara en las aplicaciones.

Comparemos ahora la calidad incluyendo las dos vistas (DroidCam e
incorporada) con OBS.

.. figure:: /images/usar-la-camara-de-tu-celular-como-webcam/droidcam-vs-integrada.png
   :align: center
   :width: 600px
   :alt: Comparación de cámara DroidCam y cámara integrada.

   Comparación incorporando la vista de DroidCam (izquierda) y la cámara integrada de mi equipo (derecha) en OBS.

Referencias
-----------

.. [droidcam] DroidCam Wireless Webcam https://www.dev47apps.com/ .
.. [linux] DroidCam Linux Install https://www.dev47apps.com/droidcam/linuxx/ .
.. [android] DroidCam Wireless Webcam (Android) https://play.google.com/store/apps/details?id=com.dev47apps.droidcam
