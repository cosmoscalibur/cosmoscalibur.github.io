.. title: Instalar paquetes snap en Linux Mint 20
.. slug: instalar-paquetes-snap-en-linux-mint-20
.. date: 2020-06-29 18:16:35-05:00
.. tags: linux, linux mint, paquetes snap, instalación de software, gestor de paquetes
.. category: tecnología
.. link: 
.. description: Linux Mint 20 tiene deshabilitada la instalación de Snap por defecto y es necesario cambiar la configuración de apt para poderlo hacer.
.. type: text
.. author: Edward Villegas-Pulgarin

¿Ya tienes Linux Mint 20 y deseas
:doc:`instalar paquetes Snap <instalando-paquetes-en-linux-mint#snap>`? Mint ha
decidido deshabilitar la instalación de Snap por defecto y es necesario cambiar
la configuración de apt para poderlo hacer.

.. TEASER_END

Si prefieres la versión en video:

.. youtube:: i2GjXP8iB1I
   :align: center

El problema
===========

Si ya cuentas con Linux Mint 20 observarás que al intentar instalar el paquete
:code:`snapd` (el gestor snap), nos llevaremos la sorpresa de no poderlo
instalar. Encontraremos un mensaje como el siguiente:

.. raw:: html

    <pre><font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#739FCF"><b>~</b></font>$ apt install snapd
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    Package snapd is not available, but is referred to by another package.
    This may mean that the package is missing, has been obsoleted, or
    is only available from another source

    <font color="#EF2929"><b>E: </b></font>Package &apos;snapd&apos; has no installation candidate</pre>

    <pre><font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#739FCF"><b>~</b></font>$ apt show snapd
    Package: snapd
    State: not a real package (virtual)
    <font color="#C4A000">N: </font>Can&apos;t select candidate version from package snapd as it has no candidate
    <font color="#C4A000">N: </font>There is 1 additional record. Please use the &apos;-a&apos; switch to see it
    <font color="#C4A000">N: </font>No packages found</pre>

La razón
========

Este problema es originado por una modificación en las preferencias de
:code:`apt` que lo engaña haciendo creer que no hay un paquete disponible que
cumpla la solicitud. Esto es provocado por el comportamiento asociado al
instalador de *Chromium*, el cual, para su fácil mantenimiento por parte del
equipo de Ubuntu, han decidido usar un paquete DEB cuya única función es
invocar la instalación desde snap (instalando snap si este no lo está).

En lo personal no lo veo problemático, para mi el caso ideal es tener ojalá
gestores de paquetes que terminen de instalar componentes desde otro gestor de
forma automática en lugar de yo encargarme del trabajo sucio. Pero el equipo de
Mint encuentra una falta de transparencia con sus usuarios que no son
advertidos de esto e incluso considerar como una falla de seguridad [snap-mint]_.

La solución
===========

Para solventar este problema, basta con eliminar o comentar las líneas de un
archivo: :code:`/etc/apt/preferences.d/nosnap.pref`. En mi caso, no veo razón
de mantenerlo, así que procedo a eliminarlo y posteriormente a instalar el
gestor de snaps. Si te sientes más cómodo, puedes comentar las líneas y una vez
instalado el gestor volver a descomentarlas [snap-install]_.

.. code:: bash

   sudo rm /etc/apt/preferences.d/nosnap.pref
   sudo apt install -y snapd
   snap help

Ahora puedes instalar tus paquetes snap en la forma como lo expliqué en un
:doc:`artículo anterior <instalando-paquetes-en-linux-mint#snap>`.


Referencias
===========

.. [snap-mint] Snapping at Canonical's Snap: Linux Mint team says no to Ubuntu
   store 'backdoor'.
   `The register, 2 Jun 2020 <https://www.theregister.com/2020/06/02/linux_mint_team_snap/>`_.
.. [snap-install] How To Enable Snap And Install Snap Packages On Linux Mint 20?
   `fossbytes, June 12, 2020 <https://fossbytes.com/how-to-enable-snap-and-install-snap-packages-on-linux-mint-20/>`_
