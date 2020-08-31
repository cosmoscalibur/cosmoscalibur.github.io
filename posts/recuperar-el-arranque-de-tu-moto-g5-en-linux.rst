.. title: Recuperar el arranque de tu Moto G5 en Linux
.. slug: recuperar-el-arranque-de-tu-moto-g5-en-linux
.. date: 2019-10-21 19:10:34-05:00
.. tags: android, motorola, smartphone, celulares, soft brick, flash, moto g5, fastboot, linux
.. category: trucos para android
.. link: 
.. description: Procedimiento y recursos para la recuperación del celular Moto G5 después de un soft brick, reinstalando android mediante fastboot en Linux.
.. type: text
.. author: Edward Villegas-Pulgarin

Recientemente, aunque cambié a un Moto G7, pensaba restaurar el celular de
fábrica pero salió mal el proceso (no siempre es fácil si pretendes eliminar
el acceso a `administrador <https://www.xda-developers.com/root/>`_ -*root*- y
el *recovery* personalizado -`TWRP <https://twrp.me/about/>`_-).

A raíz de esto, no funcionaba *play service* y por ende no era posible llegar
a la pantalla de ingreso de usuario ni omitirlo. Esto es un tipo de fallo
denominado *soft brick*, en el cual el celular es inservible a nivel de
sistema operativo (se distingue de un *hard brick*, en el cual el daño es
físico).

.. TEASER_END

A continuación, veremos como recuperar tu celular de este estado con Linux.

Instalación de herramientas Android
===================================

Nuestro primer paso es la instalación de las herramientas de software o
paquetes que necesitaremos para rescatar nuestro equipo. Este paso puede ser
realizado con la ayuda de los gestores de paquete de nuestra distribución
Linux pero por lo mismo dependerá de cual usemos.

En mi caso, uso Linux Mint 19, una distribución que es derivada de Ubuntu
18.04, compartiendo mucho de la base de paquetes en sus repositorios. Así,
en ambos casos, podremos proceder a instalar de la misma manera el SDK de
Android, ADB, Fastboot y Platform Tools.

.. code::

   sudo apt install -y android-sdk android-tools-fastboot android-tools-adb \
   android-sdk-platform-tools

Descargar *ROM* de fábrica
==========================

Como lo advertía en :doc:`comprando-celular-para-personalizar`, un detalle
importante al adquirir celular es revisar la existencia de la *ROM* de fábrica
(sistema operativo original) en los foros especializados como
`XDA <https://www.xda-developers.com/>`_. Pueden existir otras fuentes, pero
la recomendada es esta.

Descargaremos la *ROM* de la versión Android Oreo 8.1 para nuestro Moto G5.
`Descargar Android 8.1 Moto G5 cedric <https://mirrors.lolinet.com/firmware/moto/cedric/official/RETAIL/CEDRIC_RETAIL_8.1.0_OPP28.85-19-4-2_cid50_subsidy-DEFAULT_regulatory-DEFAULT_CFC.xml.zip>`_.

Una vez descargado el archivo, procedemos a descomprimirlo.


*Fastboot mode*
===============

Ya nos acercamos poco a poco. El siguiente paso es con nuestro celular.
Debemos pasar a modo *fastboot* y esto se logra de la siguiente manera.

1. Apagar el celular.
2. Presionar de manera sostenida la parte inferior de la tecla de volumen.
3. Mientras sostienes la tecla de volumen, presionar la tecla de prendido, y
   soltar.

En este momento, hemos ingresado al modo *fastboot* (o *bootloader*).
Conectamos el cable USB tanto al celular como a nuestro computador.

Podemos probar que todo vaya bien abriendo una terminal y ejecutando

.. code::

   fastboot devices

Y sabremos que funciona si muestra una secuencia alfanumérica y luego la
palabra *fastboot*. En mi caso es:

.. code::

   ZY3224RNMN	fastboot

Algunas veces puede fallar por permisos, en cuyo caso deberías probar la
ejecución con permiso de administrador.

.. code::

   sudo fastboot devices

Instalar sistema operativo
==========================

Finalmente, necesitamos instalar el sistema operativo. Vamos a requerir de
abrir una terminal y ubicarla en el directorio donde descomprimimos el sistema
operativo (algunos exploradores de archivos admiten poseen la opción de abrir
la terminal en el directorio abierto en el explorador o puedes moverte en la
terminal con el comando :code:`cd`).

Una vez ubicados en el directorio desde la terminal, procedemos a ejecutar

.. code::

   fastboot getvar max-sparse-size
   fastboot oem fb_mode_set
   fastboot flash partition gpt.bin
   fastboot flash bootloader bootloader.img
   fastboot flash modem NON-HLOS.bin
   fastboot flash fsg fsg.mbn
   fastboot erase modemst1
   fastboot erase modemst2
   fastboot flash dsp adspso.bin
   fastboot flash logo logo.bin
   fastboot flash boot boot.img
   fastboot flash recovery recovery.img
   fastboot flash system system.img_sparsechunk.0
   fastboot flash system system.img_sparsechunk.1
   fastboot flash system system.img_sparsechunk.2
   fastboot flash system system.img_sparsechunk.3
   fastboot flash system system.img_sparsechunk.4
   fastboot flash system system.img_sparsechunk.5
   fastboot flash system system.img_sparsechunk.6
   fastboot flash system system.img_sparsechunk.7
   fastboot flash system system.img_sparsechunk.8
   fastboot flash oem oem.img
   fastboot erase cache
   fastboot erase userdata
   fastboot erase DDR
   fastboot oem fb_mode_clear
   fastboot reboot

Muy bien, hemos terminado de instalar (si no hemos tenido ejecuciones
fallidas). Para iniciar el celular, con la tecla de volumen buscamos *restart*
y luego presionamos el botón de encendido. En este momento, es como si
estuviera nuevo el celular, por lo que tardará unos minutos que inicie.

¿Qué puede salir mal?
=====================

Bueno, esto no es un procedimiento seguro ni asegura el funcionamiento. El
primer detalle, es recordar que esto solo servirá si el problema era del
sistema operativo, o sea, si era un *soft brick*. En caso contrario,
*hard brick*, necesitarás un servicio técnico para el arreglo de tu equipo.

Otra opción para una posible falla en el proceso, es un cable USB deteriorado
o un puerto USB deteriorado. En estos casos, es posible perder la conexión
entre el celular y computador, y en muchas ocasiones no habrá una advertencia
visible (en mi caso, lo he notado con demoras superiores a las habituales).

Referencias
===========

+ `[FASTBOOT]CEDRIC_RETAIL_8.1.0_OPP28.85-19-4-2_cid50_subsidy-DEFAULT_regulatory-DEFAUL <https://forum.xda-developers.com/g5/development/fastboot-cedricretail8-1-0opp28-85-19-4-t3930448>`_.
+ `HardReset.info: Recovery Mode MOTOROLA Moto G5 <https://www.hardreset.info/devices/motorola/motorola-moto-g5/recovery-mode/>`_
+ `What Is Fastboot & How Do You Use It? <https://android.gadgethacks.com/how-to/know-your-android-tools-what-is-fastboot-do-you-use-it-0155640/>`_
