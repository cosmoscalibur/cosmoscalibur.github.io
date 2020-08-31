.. title: ¿Nos atraemos gravitacionalmente?
.. slug: nos-atraemos-gravitacionalmente
.. date: 2019-11-08 19:40:26-05:00
.. tags: física, fuerza de gravedad, atracción gravitacional, gravedad
.. category: ciencia/curiosidades físicas
.. link: 
.. description: La atracción gravitacional actúa sobre todos los cuerpos con
                masa, pero aparentemente no somos atraídos por otras personas
                por la gravedad. En este artículo se explica porque no es
                apreciable el efecto de la fuerza gravitacional entre los
                cuerpos cotidianos.
.. type: text
.. author: Edward Villegas-Pulgarin
.. has_math: true

La interacción gravitacional o mal llamada fuerza gravitacional (hablamos de
dos cosas diferentes), suele verse en nuestro imaginario como una interacción
dominante, finalmente, controla el movimiento de los grandes astros y nos ata
a la Tierra. Pero, esta interacción no es exclusiva de los astros, existe
entre todos los cuerpos con masa, y si es así, ¿por qué no somos atraídos
gravitacionalmente por otras personas?

.. TEASER_END

Fuerza de gravedad
==================

Newton en los *Philosophiæ naturalis principia mathematica* nos expone que
todos los cuerpos con masa (sin excepción) poseen asociada fuerza
gravitacional sobre otros, es decir, todos los cuerpos con masa se atraen
gravitacionalmente.

Esta atracción o fuerza, es la misma por la cual nos encontramos atados a la
Tierra, la misma por la cual los planetas del Sistema Solar "giran" alrededor
del sol y la misma por la cual una manzana cae al suelo.

La magnitud de esta fuerza se puede describir matemáticamente como (suponemos
que los cuerpos de esta pareja son puntuales para el cálculo):

.. math::

   F = - G \frac{m_1 m_2}{r^2},

donde :math:`F` es la magnitud de la fuerza gravitacional ejercida entre dos
masas :math:`m_1` y :math:`m_2` separadas a una distancia :math:`r` entre sus
centros de masa. El signo negativo indica el carácter atractivo de la fuerza,
que es más intensa en la medida que las masas son mayores (al estar en el
numerador) y decae con el aumento de la distancia (al estar en el denominador).
:math:`G` es la constante de Cavendish o de gravitación universal.


Vamos a suponer para el caso, una pareja, donde cada individuo posee una masa
de 100 kg, y están separados a una distancia de 10 cm (0.1 m) antes de darse un
beso. Con estas condiciones, su atracción gravitacional es:

.. math::

   F = - 6.674 \cdot 10^{-11} \frac{100 \cdot 100}{0.1^2} \text{N} = -0.00006674 \text{N}.

Para hacernos a una idea de este valor, es la fuerza que harán 2 o 3 granos de
arroz sobre una báscula por efecto de su peso (atracción gravitacional por la
Tierra).

Segunda ley de Newton
=====================

Aunque dicha fuerza es muy débil, la segunda ley de Newton, que nos permite
llegar a la aceleración que afectará a un cuerpo tras aplicar una fuerza neta
sobre este, nos permite ver que si existirá desplazamiento (pues la aceleración
será distinta de cero).

Apliquemos la segunda ley, suponiendo que uno de los cuerpos se queda fijo y
que la aceleración es constante (realmente los dos cuerpos se moverían y la
aceleración aumentaría en la medida que se acerquen):

.. math::

   a = \frac{F}{m} = \frac{-0.00006674}{100} \frac{\text{m}}{\text{s}^2} = -0.0000006674 \frac{\text{m}}{\text{s}^2}

Movimiento acelerado
====================

Como se advirtió, la aceleración es distinta de cero pero muy pequeña. Aún así,
esa pequeña aceleración es suficiente para provocar desplazamientos visibles
tras un tiempo dado. Notemos que sucede tras 10 minutos(600 segundos):

.. math::

   d = \frac{at^2}{2} = \frac{-0.0000006674 \cdot 600^2}{2} \text{m} = 0.12 \text{m}.

Diez minutos serían suficientes para lograr el beso por atracción
gravitacional (realmente serían menos porque la aceleración aumentaría cada
vez), pero eso no sucede. ¿Qué nos falta incluir?

Fuerza de fricción
==================

No vamos a complicarnos mucho, y vamos a incluir para ejemplificación, solo uno
de tantos factores capaz de frenar a la gravedad en estas escalas. La fuerza de
fricción.

Esta es una fuerza que se opone al desplazamiento de los cuerpos, y hay dos
tipos: estática (se opone al inicio del movimiento) y dinámica (durante el
movimiento). Ambos casos se definen como una constante denominada coeficiente
de fricción multiplicado por la fuerza normal, que corresponde a la componente
del peso que aplica perpendicularmente sobre la superficie.

La fuerza de fricción se origina en las irregularidades de las superficies, las
cuales no son perfectamente lisas y, dependen de los materiales de las
superficies en contacto y acabado de las mismas.

Supondremos para este caso, que nuestra pareja se encuentra sobre un suelo
horizontal, de manera que el peso (la fuerza con la que son atraídos por la
Tierra) posee la misma magnitud que la fuerza normal. También supondremos que
las superficies en contacto son caucho (para el calzado) y cemento húmedo
(para el suelo), de forma que el coeficiente de fricción estático es 0.3.

.. math::

   F_f = \mu_e N = 0.3 \cdot 9.76 \cdot 100 \text{N} = 292.8 \text{N}.

¿Y ahora qué? Si la fuerza de fricción estática no es superada por la fuerza
aplicada (en este caso, la fuerza de gravedad entre los dos cuerpos), el
movimiento no inicia.

Conclusión
==========

Efectivamente si estuviéramos en el espacio distante a cualquier cuerpo masivo
(para no poner en medio efectos de otros cuerpos), se elimine efectos de
contacto con superficies o fluidos (la resistencia del aire también evitaría la
atracción), y otras posibles interacciones (como acumulación de carga estática),
podría darse la lenta atracción. Sin embargo, ante la presencia de múltiples
interacciones en nuestra experiencia cotidiana, la atracción gravitacional
resulta débil en comparación a todas ellas.

Referencias
===========

+ `Philosophiæ naturalis principia mathematica <https://en.wikipedia.org/wiki/Philosophi%C3%A6_Naturalis_Principia_Mathematica>`_,
   Wikipedia.
+ `Newton's law of universal gravitation <https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation>`_,
   Wikipedia.
+ `Friction <https://en.wikipedia.org/wiki/Friction>`_, Wikipedia.
