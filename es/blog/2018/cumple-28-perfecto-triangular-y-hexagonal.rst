:redirect: blog/cumple-28-perfecto-triangular-y-hexagonal
:date: 2018-04-01
:tags: números, número perfecto, número triangular, número hexagonal, matemáticas
:category: ciencia
:author: Edward Villegas-Pulgarin
:language: es


Cumple 28: perfecto, triangular y hexagonal
===========================================

Bueno, después de algún tiempo vuelvo con entradas que por fin se relacionan
con algo que no sea tecnología. La motivación de esta publicación es el
particular mensaje de cumpleaños que me dejo mi hermano, y que dice así:

    ¡Felices 28 años! El 28 es un número perfecto, literalmente. Por serlo es
    también hexagonal y triangular. Es verdad que es el segundo número perfecto,
    pero también es el último que vas a cumplir. El siguiente está cerca de 500
    ¿sabrías encontrarlo?

Antes que nada, si quieren enviar de felicitaciones como este, pueden encontrar
en el blog Verne del 'El País' de España, los originales mensajes para edades
desde 1 año hasta 99 años: `Cómo felicitar el cumpleaños con datos matemáticos
hasta los 99
<https://verne.elpais.com/verne/2016/12/30/articulo/1483109720_864015.html>`_.

Secuencias numéricas
--------------------

Resulta que aparte de la clasificación de los números tradicionales que
conocemos desde la educación básica, como lo son los números enteros, es posible
designar nombres a distintas colecciones de números, asociadas a algunas
curiosidades (algunas útiles, otras no tanto).

En particular, las colecciones numéricas que me interesan para esta publicación
son secuencias numéricas. A diferencia de los tradicionales, estos no se generan
a partir de una mera definición basada en características que saltan a la vista
en la forma escrita (por ejemplo los reales los distinguimos fácilmente por el
separador decimal, los fraccionarios por la barra de división entre enteros, los
negativos por el símbolo negativo) sino por una formulación, una expresión
matemática que puede representar su valor o por algún patrón en general exhibido
por los valores (que no se asocia a su escritura o naturaleza).

Ahora, miremos porque el 28 cumple es perfecto, triangular y hexagonal.

Números perfectos
~~~~~~~~~~~~~~~~~

Los números perfectos cumplen con una propiedad bastante particular: es número
perfecto aquel número cuyos divisores propios positivos sumados tengan como
resultado el número mencionado [oeis_perfect]_ [wiki_perfect]_.

Esto es algo poco común, y el primer número perfecto es 6 y el segundo es 28.
Tal como menciona el mensaje indicado al inicio, el siguiente está alrededor de
500 (particularmente, 496). Veamos como lo sabemos de forma práctica.

n = 6
    Hallamos inicialmente los divisores propios de 6, que corresponde a: 1, 2 y
    1. A continuación: :math:`1+2+3=6` Como es igual, 6 es un número perfecto.
n = 28
    Hallamos nuevamente los divisores propios positivos: 1, 2, 4, 7 y 14. Y
    realizamos su suma: :math:`1+2+4+7+14=28`. Por lo cual, es número perfecto.

Por definición el 1 no se considera número perfecto, técnicamente no hay que
hacer una suma al ser un solo divisor propio positivo. ¿Cómo sabemos cuál es el
siguiente? Bueno, esa es la parte aburridora si lo quieres saber por tu cuenta.
Dado que no hay una expresión que lo genere sino un patrón asociado a una
característica del número, la única opción es revisar número por número si
cumple con la condición mencionada.

Números triangulares
~~~~~~~~~~~~~~~~~~~~

Los números triangulares son construcciones geométricas a partir de puntos, en
donde luego se cuentan los puntos y esa cantidad indica que el número pertenece
a este tipo. Igual aplica para el número hexagonal.

Me explico, se trata de usar puntos para construir la geometría, en este caso,
un triangulo equilátero. Así, se obtienen los números: 0, 1, 3, 6, 10, 15, 21,
28 y así sucesivamente [wiki_tri]_.

Notemos que con 0 puntos formamos un triángulo cuyos lados tienen longitud de 0
puntos (si, curiosamente la definición incluye el 0). Con un punto, formamos un
triángulo cuyos lados son de 1 punto. Con 3 puntos formamos un triángulo cuyos
lados son de 2 puntos (como las esquinas son compartidas por eso son 3 puntos en
total), 6 puntos son triángulos de lado de 3 puntos (3 vértices que son
compartidos y 3 que se encuentran en medio de los lados -uno en cada lado-) y el
10 son lados de 4 puntos (3 vértices compartidos, 2 puntos en cada lado y 1
punto interior del triángulo ya que se acumula el triángulo anterior).

.. code::

   .   .      .           .
      . .    . .         . .
            . . .       . . .
                       . . . .

Desde la forma matemática, los números triangulares son las sumas parciales de
la sucesión de números enteros positivos :math:`T_{n} = \sum\limits_{i=1}^{n}i`,
o equivalentemente los binomios de Newton de la forma [wiki_tri]_ [oeis_tri]_

.. math::
   T_{n} = \begin{pmatrix}n+1 \\ 2\end{pmatrix} = \frac{n(n+1)}{2}

Notemos que :math:`28 = 1+2+3+4+5+6+7`.

Número hexagonal
~~~~~~~~~~~~~~~~

Como mencione anteriormente, el número hexagonal también puede verse como un
arreglo geométrico de puntos formando un polígono regular (a estos números, se
les denomina en general números poligonales). En este caso el arreglo geométrico
corresponde a formar con los puntos un hexágono regular. Al igual que el
triangular, se deben acumular los puntos del hexágono anterior y reusarlos
(de esa forma hay dos aristas que comparten sus puntos con el nuevo hexágono)
[wiki_hex]_.

.. code::

   .    ..         ...
       .  .       .  ..
        ..       .  .  .
                  .  ..
                   ...

Al igual que los triangulares, también cuenta con una expresión matemática que
puede generar la secuencia: :math:`n(2n-1)` [wiki_hex]_ [oeis_hex]_.

¿Cuál es el siguiente?
----------------------

Bueno, a esta hora ya me esta dando algo de sueño, por lo cual daré respuesta
en una actualización de la publicación o en una nueva entrada en la cual puedo
aprovechar a explicar algunas cosas de python como lo son los generadores.

Pero, ¿que tiene que ver la programación? Dado el patrón exhibido por los
números no es posible simplemente reemplazar en una ecuación para saber cual es
la respuesta a la pregunta del mensaje (pero se puede consultar rápidamente en
el OEIS [oeis]_) y es necesario hacer un código que verifique la condición para
cada número en forma ordenada.

Para saber más
--------------

.. [wiki_perfect] Wikipedia, `Número perfecto <https://es.wikipedia.org/wiki/N%C3%BAmero_perfecto>`_.
                  Consultado: 1 de abril de 2018.
.. [oeis_perfect] The On-Line Encyclopedia of Integer Sequences, `Hexagonal numbers <http://oeis.org/A000384>`_.
                Consultado: 1 de abril de 2018.
.. [wiki_tri] Wikipedia, `Número triangular <https://es.wikipedia.org/wiki/N%C3%BAmero_triangular>`_.
                  Consultado: 1 de abril de 2018.
.. [oeis_tri] The On-Line Encyclopedia of Integer Sequences, `Triangular numbers <http://oeis.org/A000217>`_.
                Consultado: 1 de abril de 2018.
.. [wiki_hex] Wikipedia, `Número hexagonal <https://es.wikipedia.org/wiki/N%C3%BAmero_hexagonal>`_.
              Consultado: 1 de abril de 2018.
.. [oeis_hex] The On-Line Encyclopedia of Integer Sequences, `Perfect numbers <http://oeis.org/A000396>`_.
                Consultado: 1 de abril de 2018.
.. [oeis] `The On-Line Encyclopedia of Integer Sequences <http://oeis.org/wiki/Welcome>`_.
                  Consultado: 1 de abril de 2018.
