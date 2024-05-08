:redirect: viendo-carga-molecular
:date: 2012-02-28 11:22:00
:tags: afm, microscopía, nanotecnología, fuerza atómica, ibm
:category: tecnología
:author: Edward Villegas-Pulgarin

Viendo carga molecular
======================


Científicos de IBM fueron capaz de medir por primera vez la distribución
de carga de una molécula individual. Este logro permitirá dar nuevas
luces acerca de la formación de enlaces
entre átomos y moléculas, así como el estudio de
distribución electrónicas con estructuras moleculares funcionales.

Esta observación se logro mediante el uso de una modificación de la
técnica de microscopia de fuerza atómica (AFM por sus siglas en ingles).
Esta técnica usa una muy pequeña punta (cuya terminación es de
tamaño atómico) que interactúa con las nubes de carga de la superficie
de interés experimentando repulsión/atracción conforme nos acercamos. 

Esta fuerza sobre la punta no es medida directamente pero se establece
a través de la medición de la deflexión de la ménsula en el cual se
apoya la punta y se obtiene usando el modelo de resortes (Ley de Hooke)
:math:`F=-kz`, donde :math:`k` corresponde a la constante de resorte de la ménsula
(asociada a sus propiedades elásticas, como el modulo de Young). Usando
esta fuerza junto con la curva de calibración de fuerza vs distancia del
instrumento, es posible reconstruir (estas técnicas no nos permiten
observar por lentes, debemos observar una reconstrucción matemática de
la información a través del monitor de nuestro pc) la topografía de una
superficie, y en este caso particular la estructura molecular en sí.

.. figure:: /images/viendo-carga-molecular/stm-esquematico.png
   :width: 320px
   :height: 257px
   :align: center

   Esquemático de un STM.

La técnica usada, resultado de la modificación de la anterior,
denominada KPFM (*Kelvin probe force microscopy*),
es sensible adicionalmente a la carga. Esto se logra ya que la
adaptación realizada esta basada en el uso de un STM (*Scanning Tunneling
Microscopy*, o Microscopia de Efecto Túnel) la cual aplica una diferencia
de potencial al montaje, volviendo este sensible a las
propiedades eléctricas y conductivas de la muestra. Esta técnica esta
basada en el efecto de tunelamiento de la mecánica cuántica, que en este
caso se produce cuando se acerca mucho una punta conductora a la
superficie de interés. En este momento, surge una diferencia de
potencial entre la punta y la superficie, que puede causar la emisión de
electrones con una cierta probabilidad y por ende inducir una corriente
de tunelamiento. Esta corriente de tunelamiento es función de la
posición de la punta, la diferencia de potencial aplicada y la densidad
local de estados (LDOS) asociada a la densidad electrónica.

Las siguientes micrografías son etapas del procesamiento de imagen de
una observación de la tautomerización de la naftalocianina. La imagen en
escala de grises corresponde a la micrografía original, donde se
evidencian tonalidades claras y oscuras asociadas a distribuciones de
carga más negativas o más positivas (no es directamente la medición de
la carga, pero si de la intensidad del campo eléctrico, produciendo los
fuertes contrastes debido a cambios en la dirección del
campo eléctrico y no solo de su magnitud). Posteriormente se cambia el
mapa de color, y por último se realizan suavizados de la imagen.

.. figure:: /images/viendo-carga-molecular/micrografia-naftalocianina.jpg
   :width: 320px
   :height: 257px
   :align: center

   Micrografía de naftalocianina.

**Referencias**

1. `Scientists image the charge distribution within a single molecule for the first time <http://www.physorg.com/news/2012-02-scientists-image-molecule.html>`__. Physorg. February 22, 2012.

2. `Atomic force microscopy <http://en.wikipedia.org/wiki/Atomic_force_microscopy>`__. Wikipedia.

3. `Atomic Force Microscopy <http://www.nanoscience.com/education/AFM.html>`__. Nanoscience.

4. `Scanning tunneling microscope <http://en.wikipedia.org/wiki/Scanning_tunneling_microscope>`__. Wikipedia.
