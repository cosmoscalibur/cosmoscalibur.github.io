:redirect: usar-anaconda-python-en-git-bash
:date: 2019-12-31 14:43:50
:tags: git, anaconda python, git bash, instalación de software, gestor de paquetes, conda
:category: tecnología
:author: Edward Villegas-Pulgarin

Usar Anaconda Python en Git Bash
================================

Recientemente, por motivos laborales he tenido que trabajar en Windows y es
por esto que tuve la necesidad de buscar una opción cómoda de usar `Git <https://git-scm.com/>`_
en Windows, con soporte de `Bash <https://www.gnu.org/software/bash/>`_ a lo
que estoy acostumbrado en Linux y con Python Anaconda reconocido. De alguna
manera, la versión mínima de como usar Windows sin morir en el intento.

Anaconda Python
---------------

Lo primero es proceder a instalar Anaconda Python desde su sitio oficial, pero
recomiendo revisar primero la necesidad real de tener todo lo incluido en
Anaconda o usar algo minimalista como Miniconda. Anaconda representará una
instalación y descarga de casi 500 MB, y por ende un mayor tiempo en ambos
pasos. Por otro lado, Miniconda solo instala lo mínimo requerido para tener
Python y el gestor de paquetes Conda. Esta última opción es recomendable si
posees poco espacio en disco, deseas instalar rápidamente, solo deseas probar
lo básico de Python o el equipo es de bajas características (recuerdo casos en
los cuales mis estudiantes -épocas de docente- la sola instalación de Anaconda
bloqueaba el equipo y lo reiniciaba).

Si usas Anaconda para tus proyectos de desarrollo y usando buenas prácticas,
seguramente estarás acostumbrado a usar ambientes y en ese caso no necesitas
tener tantas cosas en el base, siendo buena opción Miniconda también.

Descarga `Anaconda <https://www.anaconda.com/distribution/>`_ o
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ según tu
necesidad e instala como cualquier programa de Windows. Lo importante durante
la instalación es indicar que sea solo para el usuario actual y que no se
asocie el :code:`PATH`. Seguir este consejo les evitará dolores de cabeza en el
futuro.

.. update:: 2020-07-02 12:00:00

   Para saber mayor detalle del proceso de instalación puedes consultar mi
   publicación :doc:`/es/blog/2020/instalar-python-anaconda`.

Git Bash
--------

Si bien puedes descargarlo desde el sitio del proyecto, aprovecharemos el
gestor Conda para facilitar la tarea de descarga, instalación y configuración.

Abriremos Anaconda PowerShell o Anaconda Prompt, y ejecutaremos lo siguiente:

.. code:: bash

   conda create -n gitbash -c conda-forge git=2.24.0

Es importante el uso de :code:`-c conda-forge` porque de este canal vendrá la
versión de Git que usaremos. Si se usa el canal por defecto, se instala solo el
cliente de consola, mientras que en esta opción viene Git Bash. He indicado
también el :code:`-n gitbash` para evitar posibles conflictos entre los
paquetes requeridos para usar Git y los paquetes disponibles en el ambiente
base. En alguna publicación posterior hablaré sobre Conda para profundizar en
esto.

Una vez terminada la instalación, puedes abrir el menú de Windows y buscar Git
Bash, el cual ya contará con Conda reconocido. Ahora solo debes empezar a
usarlo, :code:`conda activate base`.

.. note::

   En este momento, nuestro ambiente por defecto será gitbash. Si instalas sin
   indicar el ambiente, tendrás el base por defecto habilitado pero con
   posibles conflictos.

¿Y qué pasa si ya teníamos instalado Git Bash? Git Bash soporta los archivos
típicos de Bash, como el :code:`bashrc`. Así, podemos usar la configuración que
habitualmente se usa en Linux.

Abrimos Git Bash, y ejecutamos:

.. code:: bash

   cd $HOME
   echo ". /c/Users/USUARIO/ANACONDA/etc/profile.d/conda.sh" >> .bashrc
   source .bashrc

Con la primera línea aseguramos ir al directorio del usuario. En la segunda
línea, crearemos o editaremos el archivo de configuración, pero debes
reemplazar :code:`USUARIO` por la carpeta de tu usuario y :code:`ANACONDA` por
la carpeta de Anaconda (habitualmente :code:`Anaconda3` o :code:`Miniconda3` si
usaste Miniconda). La tercera línea actualiza la configuración en la sesión
actual de la consola permitiendo usar de forma inmediata Conda. Para la próxima
apertura de Git Bash ya no tendrás que configurar nada, solo empezar a usar
Conda (aún no hay ambiente activado).

