:redirect: blog/crear-version-de-windows-minima-con-msmg-toolkit
:date: 2020-07-09
:tags: msmg toolkit, microsoft windows
:category: tecnología
:author: Edward Villegas-Pulgarin
:language: es

Crear versión de Windows mínima con MSMG Toolkit
================================================

Reciente eliminé la partición de Windows de mi máquina por un problema en el
qué probé crear la tabla de partición de nuevo, pero me dio pereza instalar en
ese momento Windows porque mi sistema operativo principal es Linux. Además,
Windows no funcioba fluidamente en la máquina.

Ahora, consideré instalarlo en máquina virtual, lo que limita aún más los
recursos para Windows y decidí explorar como obtener un Windows que fuera
básicamente el sistema operativo sin tanta cosa preinstalada (muchas
asociadas a servicios que se ejecutan en segundo plano afectando el
rendimiento o que nunca uso).

Requisitos para crear la versión mínima
---------------------------------------

Además de nuestro equipo con Windows para poder ejecutar el software que nos
asistirá en el proceso, necesitamos dicho software y una imagen de Windows para
modificar.

Obtener imagen de Windows
~~~~~~~~~~~~~~~~~~~~~~~~~

Este es nuestro punto base, así que lo explicaremos primero. La forma de
obtener una imagen de Windows es a través de la página oficial [win10]_
(descarga gratuita pero no licenciada) seleccionando la edición, lenguaje y
arquitectura (si es un equipo reciente, estamos seguros que es 64 bits).

Una segunda opción, es a través de Media Creation Tool [mediacreation]_, una
utilidad de Microsoft para la descarga de la imagen de Windows. En esta
seleccionanos la misma información anterior.

Descargar MSMG Toolkit
~~~~~~~~~~~~~~~~~~~~~~

Ahora sigue la herramienta, *MSMG Toolkit* [msmg]_. Es una herramienta gratuita
para la personalización del instalador de Windows, lo cual se traduce en la
opción de reducir el impacto de los componentes preinstalados tanto en espacio
como en rendimiento, pero también hacer uno que otro ajuste estético.

En la página descargamos la herramienta :code:`MSMG Toolkit v10.1`, y
descargamos *MSMG Toolkit Packs* solo en caso de querer reinstalar algunas
componentes (es raro, pero la estrategia puede ser más rápida eliminando
colecciones y luego agregar una que otra componente, pero esto no lo
discutiré).

.. figure:: /images/crear-version-de-windows-minima-con-msmg-toolkit/descargar-msmg-toolkit.png
   :alt: Indicación del archivo a descargar de MSMG en Mega.
   :align: center
   :width: 800px
   :height: 400px

   Indicación del archivo a descargar de MSMG en Mega.

Ahora descomprimimos el archivo.

Ejecutar MSMG Toolkit
---------------------

El foco de esta publucación se encuentra en eliminar componentes, pues es justo
lo que impacta espacio de almacenamiento y rendimiento. La opción de
integración depende de los *packs* y consta de ubicar los instaladores en las
carpetas respectivas pero hacer el seguimiento de algunas dependencias para
ubicar los requeridos no me parece cómodo y prefiero sacrificarlos.

Inicializar imagen
~~~~~~~~~~~~~~~~~~

La imagen de Windows que obtuvimos la ubicamos en la carpeta ISO de la carpeta
generada al descomprimir la descarga de *MSMG Toolkit*.

También en la carpeta de *MSMG Toolkit*, encontraremos un archivo *batch*
llamado :code:`start`. Daremos doble clic y aceptamos la licencia de uso
ingresando :code:`A` y luego presionamos :code:`↩`.

.. note::

   Respecto a los ingresos de información, de ahora en adelante voy a referir
   al nombre de la opción y, debe entenderse como el número o letra que figura
   a su izquierda (al interior de los corchetes) en el menú y presionar
   :code:`↩` (enter).

En el menú, seleccionamos :code:`Source` y ahora
:code:`Extract Source from DVD ISO Image`. A continuación ingresamos el nombre
del archivo *ISO* sin extensión (ejemplo, si es :code:`Windows.iso` debemos
ingresar :code:`Windows`. Esta opción extrae los archivos del ISO de la imagen
y los ubica en la carpeta DVD.

En este momento debemos convertir el formato de imagen extraída de *ESD* a
*WIM*. Vamos a :code:`Convert` con la opción :code:`Convert Install ESD Image
to WIM Image`. Aquí debemos indicar el índice de nuestra versión de Windows,
que en mi caso corresponde a :code:`Windows 10 Home Single Language`.

.. figure:: /images/crear-version-de-windows-minima-con-msmg-toolkit/convert-windows-esd-wim.png
   :alt: Menú de convertir imagen ESD a WIM.
   :align: center
   :width: 400px
   :height: 600px

   Menú de conversión de imagen ESD a WIM con selección de la versión de Windows deseada.

Ahora volvemos a :code:`Source` y la opción :code:`Select Source
from <DVD> folder`. Aquí indicamos el único índice que tendremos disponible y
queda a decisión de cada quien las siguientes preguntas (no observé
diferencia).

Eliminar componentes
~~~~~~~~~~~~~~~~~~~~

Este es el paso importante del procedimiento y el más demorado. La forma más
rápida de proceder es eliminar por conjuntos de componentes y no a nivel de
detalle.

Para remover estas componentes vamos a :code:`Remove` y luego :code:`Remove
Windows Components`. Ahora tenemos un menú asociado a los distintos conjuntos
de componentes que podemos remover. Estos pueden ser removidos como conjunto
o removemos componentes individuales (una a una, lo cual lo hace un
procedimiento largo, aburridor y de mucha atención).

En mi caso he optado por remover todos los conjuntos de componentes ingresando
a cada opción de conjunto y allí indicando :code:`All XXX Components` (donde
:code:`XXX` es el nombre del conjunto de componentes) y luego aceptando que se
remueven todas las componentes (:code:`Removing All XXX Components Continue
...` y marcamos :code:`Y`).

Pero algo de detalle al respecto.

**Windows Apps**
   Perdemos *Windows Store* y la calculadora. Otros extrañarán *Cortana* y
   algunas componentes de *Xbox*.

**System Apps**
   Perderemos *Edge* y *OneDrive* entre otras aplicaciones. Recomendaría que
   conserven esta categoría para poder usar *Edge* como navegador web
   provisional.

**System**
   Perdemos *Paint*, *Wordpad* y la que más me duele, *Windows Subsystem For
   Linux*. Por este motivo, generé una versión en la cual removía todos los
   conjuntos menos este.

**Remoting**
   Realmente no extraño los elementos de este punto y creo que para la mayor
   parte de usuarios no son necesarios (*Home group*, *MultiPoint connector* y
   *Remote Assistence*).

**Privacy**
   Perdemos opciones como el uso del PIN para el ingreso de sesión o por
   reconocimiento facial.

**Multimedia**
   Perdemos *Windows Media Player* y *Windows Photo Viewer*.

**Internet**
   Perdemos *Internet Explorer* y *Adobe flash*.

Puedes hacerlo de esta forma, o componente a componente, pero advertencia,
algunas implican estar pendientes de dependencias de otros conjuntos.

Generar imagen de Windows mínima
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Terminado el proceso de eliminar las componentes no deseadas, accedemos a
:code:`Apply` y luego a :code:`Apply & Save Changes to Source Images`.
Terminada la aplicación de cambios procedemos a :code:`Target` y la opción
:code:`Make a DVD ISO Image` (pero también puedes aprovechar a crear la USB
para arranque :code:`Copy Source to USB Flash Drive`). Asignamos el nombre a
nuestra imagen y procedemos. En el caso de la USB se selecciona la unidad de la
USB.

Con nuestra imagen lista, ahora puedes quemarla o usarla para una máquina
virtual (carga directamente *ISO*).

Consideraciones finales
-----------------------

A diferencia de distintos sitios que "explican" el uso de MSMG, en este caso he
detallado adecuadamente las opciones, y en especial parte de selección de la
imagen de Windows que no suele decirse más que "una vez seleccionada".

Si como yo, decides remover todas las componentes posibles, vas a requerir
Powershell para instalar por comandos al menos el navegador y de ahí instalar
otros programas, o tener los instaladores listos en una USB. Mi sugerencia, es
aprovechar el gestor de paquetes *scoop* [scoop]_ que puede
instalarse con Powershell siguiendo los pasos del sitio web, y agregar el
repositorio de :code:`extras` para instalar paquetes como *Firefox*,
*Imageglass* y *LibreOffice* (más adelante haré una publicación al respecto).

Finalmente, es bueno un menú como *Open Shell* [shell]_ dado que perdimos las
opciones de búsqueda de Windows 10 y el menú básico no es muy cómodo.

.. figure:: /images/crear-version-de-windows-minima-con-msmg-toolkit/windows-minimal-openshell-scoop.png
   :alt: Windows mínimo en máquina Virtual.
   :align: center
   :width: 600px
   :height: 400px

   Windows mínimo en máquina virtual, haciendo uso de *Open Shell* y aplicaciones de *scoop*.

Debes tener en cuenta que algunas componentes pueden perderse de forma
definitiva (instalarlas es hacer reparación de instalación con el instalador
original o simplemente no hay forma). Y esto tiene un efecto en otros
posibles programas que ya no podrás instalar (en mi caso no puedo usar distros
Linux para Windows porque no tengo WSL).

Puedo decir que con 4 GB de RAM asignados a la máquina virtual tengo fluido
Windows cuando la instalación directa en la máquina con 8 GB de RAM hasta se
tostaba con solo tener abierto *Firefox* y *Word*.

.. [win10] `Download Windows 10 Disc Image (ISO File) <https://www.microsoft.com/en-us/software-download/windows10ISO>`_.
.. [mediacreation] `Media Creation Tool (direct download) <https://go.microsoft.com/fwlink/?LinkId=691209>`_.
.. [msmg] `MSMG Toolkit Downloads <https://msmgtoolkit.in/download.html>`_.
.. [scoop] `Scoop - A command-line installer for Windows <https://scoop.sh/>`_
.. [shell] `Open Shell Menu - GitHub <https://github.com/Open-Shell/Open-Shell-Menu/releases>`_.
