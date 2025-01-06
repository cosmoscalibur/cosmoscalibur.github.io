:date: 2020-01-06
:tags: python, sphinx, restructuredtext, documentación de software, sitio
    estático
:category: tecnología

Crear documentación de un proyecto Python con Sphinx
====================================================

Sin duda, una etapa importante en cualquier proyecto de desarrollo (y no solo de
*software*) es la generación de la documentación. En el caso de *software* es
posible asistirse de herramientas que ayudan a automatizar la generación de la
documentación mediante extracción de comentarios en el código, usar palabras
claves y lenguaje de marcado para modificación de estilo en el texto o inclusión
de otros elementos que no sean solo texto plano (imágenes, ecuaciones, enlaces
entre otros).

Algunas herramientas para este fin son `Doxygen <http://doxygen.nl/>`_ (habitual
para proyectos en C/C++), `Javadoc
<https://www.oracle.com/technetwork/java/javase/documentation/index-jsp-135444.html>`_
(para Java, pero habitual también en TypeScript), `ESDoc <https://esdoc.org/>`_
(para Javascript) y por supuesto, Sphinx, para Python.

En esta entrada instalaremos lo necesario para generar nuestra documentación de
un proyecto Python y haremos un pequeño ejemplo.

LaTeX
-----

Si deseamos generar documentación web, este paquete no es necesario, pero para
generar nuestra documentación en PDF es una dependencia obligatoria. La
instalación recomendada dependerá del sistema operativo que se use.

Mac
    Puedes usar `MacTex <https://www.tug.org/mactex/>`_ el cual incluye el
    compilador TeXLive y editores como TeXShop, y otras dependencias para el
    funcionamiento de LaTeX en Mac.

Windows
    La opción más cómoda es el compilador `MikTeX
    <https://miktex.org/download>`_, el cual permite de forma predeterminada la
    descarga automática de paquetes adicionales en la medida que sean requeridos
    (instalación *on the fly*).

    Es importante que en la configuración no cambies al modo silencioso, pues
    esto puede afectar la ejecución posterior en los casos que requieran de
    instalación.

    Si usas Anaconda, puedes incluirlo desde el canal de *conda-forge*, ``conda
    install -c conda-forge miktex``.

    En la primera forma de instalación requieres instalar Perl, en la segunda,
    este viene como dependencia instalada por el gestor de paquetes. También
    puedes usar `TeXLive <https://tug.org/texlive/acquire.html>`_ para Windows,
    el cual asegura la consistencia en el resultado entre los 3 sistemas
    operativos.

Linux
    En Linux usaremos TeXLive pero su instalación la haremos directamente del
    gestor de paquetes del sistema operativo. En la mayor parte de
    distribuciones Linux estará disponible a través del gestor.

    En el caso de las distribuciones basadas en Debian (Ubuntu y Linux Mint
    entre otras) puedes instalar de la siguiente manera:

    ::

        sudo apt install -y texlive texlive-latex-base texlive-latex-extra \
            texlive-lang-spanish latexmk

Sphinx
------

Si usamos Python a través de Anaconda podemos usar el gestor *conda* para la
instalación, así ``conda install sphinx``, en caso contrario, podemos usar el
gestor de paquetes *PIP*: ``pip install -U Sphinx``.

.. note::

    Si deseas una experiencia en Windows similar a Linux, usando el ``Makefile``
    tradicional y la posibilidad de usar en combinación con Bash, te recomiendo
    usar Git Bash, y si es en conjunto con Anaconda puedes leer mi publicación
    al respecto, :doc:`/es/blog/2019/usar-anaconda-python-en-git-bash` e
    instalar el paquete ``make`` con Anaconda (``conda install make``) o
    instalar `Mingw-w64 <http://mingw-w64.org/doku.php>`_.

Configuración de Sphinx
-----------------------

Abriremos una consola (si es Windows, debes tener en cuenta que para usar
paquetes de Anaconda debes usar las consolas Anaconda Prompt, Anaconda
PowerShell u otra si la configuraste -como el caso de Git Bash que mencioné en
la sección anterior-) y debemos ubicarnos en el directorio que destinaremos para
la documentación. Es habitual que en la estructura de nuestro proyecto
destinemos un directorio ``docs`` para este fin.

Ahora ejecutamos ``sphinx-quickstart`` y respondemos las preguntas que saldrán.
Es necesario tener en cuenta, que si usas Windows debes agregar al comando la
terminación ``.exe``, ejemplo ``sphinx-quickstart.exe``.

::

    > Separate source and build directories (y/n) [n]: y
    > Project name: proyecto
    > Author name(s): Edward Villegas-Pulgarin
    > Project release []: 0.1.0
    > Project language [en]: es

Siempre recomiendo separar el directorio del código fuente de la documentación
del directorio de compilados de la misma. Respecto al esquema de versiones me
agrada el `versionamiento semántico <https://semver.org/>`_ que permite al
usuario final intuir un poco más sobre la madurez del proyecto con el número,
pero puedes usar el `esquema basado en fecha de liberación
<https://calver.org/>`_. En el lenguaje se especifica el lenguaje con el código
a dos letras internacional, acorde a los `soportados por Sphinx
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language>`_.

Aunque en la terminal nos indican que podemos continuar con el archivo
``index.rst``, debemos hacer unos pequeños cambios en el archivo ``conf.py`` que
encontraremos en ``docs/source``.

Puedes saber más opciones de configuración en la documentación de Sphinx sobre
`conf.py <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_.

Extensiones
~~~~~~~~~~~

Recomiendo incluir la extensión de Autodoc para extraer automáticamente la
documentación de la API, MathJax para el soporte de ecuaciones matemáticas en la
versión Web y Napoleon para el estilo de Numpy y Google en la documentación. Con
Coverage puedes validar que funciones se han documentado y dcotest integra
pruebas de código desde la documentación (comparar salidas con ejemplo de
documentación).

Modificar en el archivo.

::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.mathjax',
        'sphinx.ext.napoleon',
        'sphinx.ext.coverage',
        'sphinx.ext.doctest'
    ]

Importar tu proyecto
~~~~~~~~~~~~~~~~~~~~

Para actualizar automáticamente los metadatos desde el código (ejemplo, el autor
o la versión) puedes importar el paquete en el archivo de configuración. Dado
que estarás en modo de desarrollo, probablemente el paquete no ha sido instalado
y lo deberás hacer descomentando las tres primeras líneas de código en la
sección de *Path setup*. El punto que hay por defecto indica la misma carpeta de
``docs/source``, por lo cual es necesario reemplazar por ``../..`` que se
devuelve los dos niveles necesarios.

::

    import os
    import sys
    import datetime
    sys.path.insert(0, os.path.abspath('../..'))
    import proyecto

Ahora, puedes hacer cosas como la siguiente, si está disponible en tu código.

.. code-block:: python

    author = proyecto.__author__
    copyright = str(datetime.date.today().year) + ", " + author
    release = proyecto.__version__

Esto tiene un impacto respecto a algunas dependencias, que pueden provocar
fallos o si para la generación de la documentación no tenemos todas las
dependencias del paquete. En mi caso, he tenido problemas cuando tengo como
dependencia Tensorflow o cuando tengo ArcPy pero no tengo la licencia instalada.
En este caso, podemos hacer un falseo (*mock*) de los paquetes:

.. code-block:: python

    autodoc_mock_imports = ["tensorflow", "arcpy"]

Referencias cruzadas
~~~~~~~~~~~~~~~~~~~~

Para usar referencias cruzadas, es decir, numeración de tablas, figuras, códigos
y ecuaciones si poseen pie de objeto, y ser referenciados en el texto por el
número, se requiere configurar lo siguiente.

::

    numfig = True
    numfig_format = {'figure': 'Fig. %s', 'table': 'Tabla %s',
                     'code-block': 'Código %s', 'section': 'Sección %s'}
    numfig_secnum_depth = 1
    math_numfig = True
    math_eqref_format = 'Ec. {number}'

Así, es posible usar ``:label:`` para asignar una referencia a los objetos y
``:numref:`` y ``:eq:`` a la hora de mencionarlos. Con ``numfig_secnum_depth``
configuras la numeración de los objetos, si es continúa (0), por sección (1) y
subsección (2).

LaTeX
~~~~~

Hay una configuración básica para LaTeX que puedes agregar. El documento
maestro, el nombre del archivo TeX, el nombre de nuestra documentación, el
nombre del autor (que podemos usar la variable que ya definimos) y el tipo de
documento (cuya clase *manual* está definida por Sphinx).

::

    master_doc = 'index'
    latex_documents = [
        (master_doc, 'proyecto.tex', 'Documentación Proyecto',
         author, 'manual'),
    ]

Escritura en ReStructuredText
-----------------------------

Sobre esto, es referencia ver la documentación de `DocUtils
<https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html>`_ y de
Sphinx `ReStructuredText Primer
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.

Una vez tienes las bases de ReStructuredText puedes editar lo básico. De ahí, y
para tener todo el provecho de Sphinx hay elementos como los roles, directivas y
dominios que debes aprender a usar, `Sphinx ReStructuredText
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.

¿Y por qué los dominios? Estos añaden sintaxis para manejar las relaciones con
el código, como enlazar a funciones relacionadas que se generaron con *autodoc*
y además la forma de como documentar la función (u otro elemento del código) en
su código fuente y que pueda ser extraída. Por ejemplo, el `dominio de Python
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain>`_.

¿Qué archivos debo editar?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Primero, editaremos ``docs/source/index.rst``, donde deberemos agregar los
nombres de los archivos que se incluyen en la documentación, tanto los generados
como los automáticos. Se agrega uno por línea, sin extensión y la posición es
relativa a la ubicación del archivo ``index.rst``.

Te recomiendo siempre un archivo ``README.rst`` que fija la generalidad e
intención del proyecto, ``history.rst`` para tener documentados los cambios
entre versiones (como un *changelog* pero a mano, más condensado), un
``usage.rst`` documentando el uso de nuestro proyecto, ``installation.rst`` con
instrucciones de instalación y adicional, agregar una ruta a la documentación de
la API (la misma ruta la debemos indicar más adelante). Puedes agregar más
archivos, por ejemplo, yo suelo usar un ``concepts.rst`` para detallar los
conceptos necesarios antes de usar el software o detallar teoría que ayuda a
interpretar resultados o que expande la información para que alguien pueda
analizar o continuar un desarrollo.

::

    .. toctree::
       :maxdepth: 3
       :caption: Contenido:

       README
       installation
       usage
       api/modules
       concepts
       history

Y podemos borrar las líneas posteriores de *Indices and tables*.

Vemos la mención a ``api/modules``, la cual es importante para incluir la
documentación automática extraída con Sphinx, que se explicará en la próxima
sección.

Ejecución de Sphinx
-------------------

Como estamos haciendo uso de *autodoc*, nuestro primer paso es generar la
extracción de la API.

::

    sphinx-apidoc -f -M -o source/api/ ../proyecto

Recordar que en Windows hay que agregar ``.exe`` (``sphinx-apidoc.exe``). ``-f``
es para forzar la regeneración de los archivos (importante si actualizamos la
documentación de la API), ``-M`` para ubicar primero la documentación de los
módulos (por defecto primero son las funciones, y esto no me parece natural).
Luego, es la ruta para la documentación de la API (uno de los archivos será el
``api/modules.rst``) y finalmente la ruta donde se encuentra el paquete. Ambas
rutas son relativas al directorio de documentación.

Ahora, solo es necesario generar la documentación: ``make latexpdf`` si es con
el *Makefile* o ``make.bat latexpdf`` si no instalaste *make* en Windows. Aquí
debemos devolvernos un nivel en la carpeta para ejecutarlo.

Publicar
--------

Ahora encontrarás en la carpeta *build* los archivos LaTeX, y uno de ellos será
el PDF que queremos. También puedes hacer compilación HTML (``make html``) y
usar esta para publicar como un `GitHub Pages <https://pages.github.com/>`_ o en
`ReadTheDocs
<https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_.
