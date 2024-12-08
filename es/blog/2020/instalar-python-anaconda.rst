:date: 2020-06-29
:tags: python, anaconda python, instalación de software, gestor de paquetes, conda
:category: tecnología
:author: Edward Villegas-Pulgarin
:language: es

Instalar Anaconda Python
========================

En los últimos años, una herramienta se ha popularizado no solo como una base
para el ecosistena de la analítica de datos ("ciencia de datos" como llaman
también algunos) sino también en general para el desarrollo en Python
(científico, web o de propósito general). Esta herramienta es Anaconda, que no
solo nos facilita un sistema de distribución de paquetes multiplataforma, un
repositorio principal con amplio soporte multiplataforma (canal *default* o
*anaconda*) sino un gestor de ambientes para permitir aislar nuestras
dependencias facilitando la reproducibilidad y evitando los conflictos.

Obtener instalador
------------------

Nuestro primer paso es obtener el instalador de Anaconda Python según nuestro
sistema operativo, modo de instalación y limitación de espacio de
almacenamiento o ancho de banda. Aunque Anaconda aún dispone de instaladores de
Python 2.7, no recomiendo su uso sino las versiones asociadas a Python 3.X
(Python 2 perdió soporte el 31 de diciembre de 2019).

Si tenemos limitación de espacio de almacenamiento o ancho de banda, podemos
usar el instalador de
`miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, el cual
corresponde a un instalador de alrededor de 60 MB en los 3 sistemas operativos.
Este instalador nos da mayor control sobre los paquetes instalados, y solo
incluye por defecto lo necesario para el interprete de Python y el gestor
Conda.

Si queremos una colección de paquetes listos para usar, iremos al instalador de
`Anaconda Python <https://anaconda.org/>`_ (seleccionamos *Download Anaconda*).
Ahora vamos a la sección de instaladores (*Anaconda Installers*) y escogeremos
el acorde a nuestra necesidad:

+ Instalador gráfico de 32 y 64 bits para Windows.
+ Instalador por línea de comandos para Windows (64 bits).
+ Instalador gráfico y por línea de comandos para Mac (64 bits).

Esta descarga es de alrededor de 500 MB para todos los casos.

Instalación por línea de comandos
---------------------------------

La instalación por línea de comandos aplica de la misma manera tanto para Mac
como para Linux, usando ambos un instalador basado en código bash (indiferente
si es Anaconda o Miniconda).

Para este caso nos basaremos en la instalación silenciosa [cmd]_ para evitar las
preguntas interactivas y así despreocuparnos durante la instalación. Invocamos
el instalador con Bash de la siguiente forma (asegurate de usar la ruta
completa y correcta del instalador :code:`sh` que usarás).

.. code:: bash

   bash Anaconda3-2020.02-Linux-x86_64.sh -b -p $HOME/anaconda
   echo ". $HOME/anaconda/etc/profile.d/conda.sh" >> $HOME/.bashrc
   source $HOME/.bashrc

En la invocación de Bash, el argumento :code:`-b` implica la aceptación de
licencias y con :code:`-p` indicamos la ruta para la instalación de Anaconda
(puedes cambiarla a tu deseo).

La segunda y tercera línea son específicas si usas una consola Bash. Esto
permite reconocer el gestor Conda por la consola cuando se inicia una nueva
sesión y la última línea que se aplique para la sesión actual.

Aunque no es mi preferencia y además puede generar potenciales conflictos, si
deseas que el entorno de Anaconda Python esté activado por defecto puedes
agregar en el :code:`.bashrc` la línea :code:`conda activate`.

.. youtube:: UFfsg56qigY
   :align: center

La versión de *Anaconda Navigator* incluida en 2020.02 en Linux presenta un
error, por lo cual, si al ejecutarlo ves el mensaje
:code:`UnboundLocalError: local variable 'DISTRO_NAME' referenced before assignment`
bastará con actualizar el paquete [navigator]_.

.. code:: bash

   conda update anaconda-navigator

Instalación gráfica
-------------------

La instalación en Windows con el instalador gráfico [gui]_ es sencilla. Las
opciones por defecto son justamente las recomendadas por lo cual solo es
necesario dar clic en "*Next*" siempre.

Es fuertemente recomendado usar la instalación con las opciones por defecto,
para evitar futuros conflictos. Esto es, instalar "*Just Me*" para no requerir
permisos de administrador, no agregar al :code:`PATH` (evitar conflictos con
programas que hagan uso de Python u otros paquetes incluidos en Anaconda) y
registrar Anaconda Python como Python por defecto (así será reconocido por los
editores de código que detectan Anaconda).

.. youtube:: zFk6beeQ-CU
   :align: center

La instalación gráfica en Mac puedes seguir también las opciones por defecto.

Verificar instalación
---------------------

Basta con validar la lista de paquetes incluidos para saber que funciona
adecuadamente Anaconda. Abrimos la consola Bash (Linux o Mac) o
*Anaconda Prompt* (Windows, o con abrir *Anaconda Navigator* es suficiente), y
ejecutamos :code:`conda list`. Si observamos la lista de paquetes, funciona.

Referencias
-----------

.. [cmd] `Installing in silent mode <https://conda.io/projects/conda/en/latest/user-guide/install/linux.html#installing-in-silent-mode>`_.
   conda.
.. [navigator] `UnboundLocalError: local variable 'DISTRO_NAME' referenced before assignment <https://github.com/ContinuumIO/anaconda-issues/issues/11662>`_. Anaconda issues.
.. [gui] `Installing on Windows <https://docs.anaconda.com/anaconda/install/windows/>`_. Anaconda.
