:redirect: blog/usar-ubuntu-en-windows
:date: 2020-10-05
:tags: windows, linux, wsl, wsl2, ubuntu, windows subsystem for linux
:category: tecnología
:author: Edward Villegas-Pulgarin
:language: es

Usar Ubuntu en Windows con WSL2
===============================

Como contaba en una que otra publicación, por motivos laborales mantengo mucho
en Windows pero es necesario en ocasiones tener Linux a la mano. Sin duda a
nivel de desarrollo Linux toma cada vez mayor relevancia y es notorio cuando
Microsoft le da relevancia al soporte de Linux en su ecosistema, no solo en
despliegues en nube sino también en el mismo escritorio. En esto último,
referimos a WSL (*Windows Subsystem for Linux*) [wsl]_.

WSL es el componente de Windows que nos permite cumplir la promesa de este
artículo, ejecutar distribuciones Linux desde Windows y con rendimiento alto
(no se trata de una emulación sino la ejecución de un kernel Linux real) e
incluso, vincula adecuadamente con la GPU (solo para
*Microsoft Windows Insider Program* [cuda]_) y permite hacer uso de Docker en Windows
Home [docker]_.

Veremos como instalar una distribución Linux en Windows con WSL y es importante
realizarlo en el orden mencionado.

Habilitar WSL
-------------

Nuestro primer paso es abrir la consola de Power Shell en modo administrador y
a continuación ejecutaremos:

.. code::
    
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

Actualizar a WSL2
-----------------

Si disponemos de un sistema de 64 bits (*x64*), podemos actualizar a WSL2
siempre y cuando la versión sea 1903 o superior, con número de compilación
18362 o superior. Podemos verificar ejecutando :code:`winver` y verificar en
la ventana que despliega.

En caso contrario, podemos recurrir al asistente de *Windows Update* para
tener dicha versión. Una vez con este requisito, podemos ejecutar:

.. code::

   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   $wsl_file="wsl_update_x64.msi"
   $wsl_file_path=$pwd.Path + "\" + $wsl_file
   Invoke-WebRequest -Uri https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi -OutFile $wsl_file_path -UseBasicParsing
   Start-Process $wsl_file_path
   wsl --set-default-version 2

El procedimiento anterior es mi versión de ejecución por línea de comandos,
pero la documentación oficial dispone para descarga e instalación manual.
Asumo el interés en usar la WSL2 como versión por defecto, por lo cual es
necesario ejecutar la última línea del bloque.

Instalar distribución Linux
---------------------------

A través de la tienda de aplicaciones podemos continuar con la instalación de
la distribución Linux deseada, pero si te interesa continuar con el uso de la
consola, procedemos a revisar la dirección de descarga de nuestra distribución
acorde a la lista disponible en la sección de descarga manual de la
documentación oficial [wsl-manual]_. En nuestro ejemplo, instalaremos Ubuntu
20.04 (cambiar el número de la versión LTS soportada en la URL si te interesa
otra).

.. code::

   Invoke-WebRequest -Uri https://aka.ms/wslubuntu2004 -OutFile Ubuntu.appx -UseBasicParsing
   Add-AppxPackage .\Ubuntu.appx
   ubuntu2004.exe
   
Una vez se complete el proceso, debemos inicializar la distribución para que la
configuración termine. Puedes hacerlo lanzando la distribución desde la
aplicación o con el comando desde la consola como en este ejemplo.

Concluido el proceso, será como estamos acostumbrados, creamos un usuario y
contraseña durante la configuración inicial, podemos usar el gestor de paquetes
e incluso lanzar algunas aplicaciones gráficas habilitando el servidor X11.

Finalmente, actualicemos nuestra distribución (en el paso anterior la consola
ha quedado ubicada en Ubuntu).

.. code::

   sudo apt update -q
   sudo apt dist-upgrade -y

Hay que tener en cuenta que no todo funcionará, uno de esos detalles es la
instalación de paquetes snap al igual que docker.

Estamos listos para usar Ubuntu en Windows. Para este fin podemos abrir
nuevamente desde PowerShell y ejecutar :code:`ubuntu2004.exe`, abrir el
lanzador de Ubuntu en el menú, usar la consola Ubuntu de Windows Terminal
(lo recomiendo y la reconocerá de forma inmediata) o VSCode con la extensión de
*Remote - WSL*.

Aplicaciones gráficas
---------------------

Para cerrar este tema, falta que lancemos nuestras aplicaciones gráficas. Para
esto será necesario modificar el archivo :code:`.bashrc` [ubuntu-wiki]_.

.. code::

   echo "export DISPLAY=$(awk '/nameserver / {print $2; exit}' /etc/resolv.conf 2>/dev/null):0" >> $HOME/.bashrc
   echo "export LIBGL_ALWAYS_INDIRECT=1" >> $HOME/.bashrc

.. note::

   En ningún sitio encontré referencia a necesitar reiniciar o hacer algún
   procesimiento adicional, pero en mi caso al intentar tras la ejecución no me
   funcionó, pero me funcionó después de reiniciar la máquina.

Ahora, instalamos `VcXsrv <https://sourceforge.net/projects/vcxsrv/>`_.
Lanzamos *XLaunch*, opción *Multiple Windows*, *Start no client* y finalmente
habilitamos *Disable access control*. Este paso es necesario para iniciar el
servidor X (cada que se requiera una aplicación gráfica si no lo hemos hecho
durante la sesión respectiva de Windows). Para hacerlo de forma rápida, puedes
guardar la configuración y lanzarlo desde dicho archivo.

Para probar, puedes instalar instalar :code:`x11-apps` y lanzar :code:`xclock`.

Errores comunes
---------------

Estos errores comunes son basados en lo natural que se ve ir a la tienda de
aplicaciones y escoger instalar nuestra distribución.

Al intentar abrir la distribución de esta manera nos encontraremos con el error
siguiente:

.. code::

    Installing, this may take a few minutes...
    WslRegisterDistribution failed with error: 0x8007019e
    The Windows Subsystem for Linux optional component is not enabled. Please enable it and try again.
    See https://aka.ms/wslinstall for details.
    Press any key to continue...

Esto requiere ejecutar el paso de instalación de habilitación de WSL. Una vez
habilitado, debemos reinstalar la distribución, de otra manera veremos el
siguiente error:

.. code::

    Installing, this may take a few minutes...
    WslRegisterDistribution failed with error: 0x800700b7
    The distribution installation has become corrupted.
    Please select Reset from App Settings or uninstall and reinstall the app.
    Error: 0x800700b7 Cannot create a file when that file already exists.

Por esta misma razón, nuestra distro estará en WSL1 y será necesario convertir.

.. code::

   wsl -l -v
   wsl --set-version Ubuntu 2

Con la primera línea verificamos la versión asignada y con el segundo
convertimos.

Referencias
-----------

.. [wsl] `Windows Subsystem for Linux Installation Guide for Windows 10 <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_.
.. [cuda] `CUDA on WSL User Guide <https://docs.nvidia.com/cuda/wsl-user-guide/index.html#abstract>`_.
.. [docker] `Docker Desktop WSL 2 backend <https://docs.docker.com/docker-for-windows/wsl/>`_.
.. [wsl-manual] `Manually download Windows Subsystem for Linux distro packages <https://docs.microsoft.com/en-us/windows/wsl/install-manual>`_.
.. [ubuntu-wiki] `WSL - Ubuntu Wiki <https://wiki.ubuntu.com/WSL>`_.
