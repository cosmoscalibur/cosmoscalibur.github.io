:date: 2018-04-01
:tags: numbers, perfect number, triangular number, hexagonal number, mathematics
:category: science
:author: Edward Villegas-Pulgarin
:language: en


Turning 28: perfect, triangular and hexagonal
=============================================

Well, after some time I return with posts that are finally related
to something other than technology. The motivation for this publication is the
particular birthday message that my brother left me, which says:

    Happy 28th! 28 is a perfect number, literally. Because of that it is
    also hexagonal and triangular. It is true that it is the second perfect number,
    but it is also the last one you will celebrate. The next one is near 500.
    Could you find it?

First of all, if you want to send congratulations like this, you can find
original messages for ages from 1 year to 99 years in the Verne blog of 'El País' of Spain: `Cómo felicitar el cumpleaños con datos matemáticos
hasta los 99
<https://verne.elpais.com/verne/2016/12/30/articulo/1483109720_864015.html>`_.

Numerical sequences
-------------------

It turns out that apart from the classification of traditional numbers that
we know from basic education, such as integers, it is possible
to assign names to different collections of numbers, associated with some
curiosities (some useful, others not so much).

In particular, the numerical collections that interest me for this publication
are numerical sequences. Unlike traditional ones, these are not generated
from a mere definition based on characteristics that are obvious
in the written form (for example, we easily distinguish real numbers by the
decimal separator, fractionals by the division bar between integers,
negatives by the negative symbol) but by a formulation, a mathematical expression
that can represent their value or by some general pattern exhibited
by the values (which is not associated with their writing or nature).

Now, let's look at why turning 28 is perfect, triangular, and hexagonal.

Perfect numbers
~~~~~~~~~~~~~~~

Perfect numbers meet a rather particular property: a perfect number
is that number whose positive proper divisors added together result in
the mentioned number [oeis_perfect]_ [wiki_perfect]_.

This is somewhat uncommon, and the first perfect number is 6 and the second is 28.
As the message indicated at the beginning mentions, the next one is around
500 (specifically, 496). Let's see how we know it practically.

n = 6
    We initially find the proper divisors of 6, which correspond to: 1, 2, and
    3. Then: :math:`1+2+3=6`. Since it is equal, 6 is a perfect number.
n = 28
    We find again the positive proper divisors: 1, 2, 4, 7, and 14. And
    we perform their sum: :math:`1+2+4+7+14=28`. Therefore, it is a perfect number.

By definition, 1 is not considered a perfect number; technically there is no
sum to make as it is a single positive proper divisor. How do we know which is the
next one? Well, that is the boring part if you want to know it on your own.
Since there is no expression that generates it but a pattern associated with a
characteristic of the number, the only option is to check number by number if
it meets the mentioned condition.

Triangular numbers
~~~~~~~~~~~~~~~~~~

Triangular numbers are geometric constructions from points, where
the points are then counted, and that quantity indicates that the number belongs
to this type. The same applies to the hexagonal number.

I explain: it is about using points to build geometry, in this case,
an equilateral triangle. Thus, the numbers obtained are: 0, 1, 3, 6, 10, 15, 21,
28, and so on [wiki_tri]_.

Note that with 0 points we form a triangle whose sides have a length of 0
points (yes, curiously the definition includes 0). With one point, we form a
triangle whose sides are 1 point. With 3 points we form a triangle whose
sides are 2 points (since the corners are shared, that's why it is 3 points in
total), 6 points are triangles with sides of 3 points (3 vertices that are
shared and 3 that are in the middle of the sides—one on each side—) and
10 has sides of 4 points (3 shared vertices, 2 points on each side and 1
interior point of the triangle since the previous triangle is accumulated).

.. code::

   .   .      .           .
      . .    . .         . .
            . . .       . . .
                       . . . .

From the mathematical point of view, triangular numbers are the partial sums of
the sequence of positive integers :math:`T_{n} = \sum\limits_{i=1}^{n}i`,
or equivalently the Newton binomials of the form [wiki_tri]_ [oeis_tri]_

.. math::
   T_{n} = \begin{pmatrix}n+1 \\ 2\end{pmatrix} = \frac{n(n+1)}{2}

Note that :math:`28 = 1+2+3+4+5+6+7`.

Hexagonal number
~~~~~~~~~~~~~~~~

As I mentioned earlier, the hexagonal number can also be seen as a
geometric arrangement of points forming a regular polygon (these numbers are
generally called polygonal numbers). In this case the geometric arrangement
corresponds to forming a regular hexagon with the points. Just like the
triangular one, the points of the previous hexagon must be accumulated and reused
(in this way there are two edges that share their points with the new hexagon)
[wiki_hex]_.

.. code::

   .    ..         ...
       .  .       .  ..
        ..       .  .  .
                  .  ..
                   ...

Like the triangular ones, it also has a mathematical expression that
can generate the sequence: :math:`n(2n-1)` [wiki_hex]_ [oeis_hex]_.

What is the next one?
---------------------

Well, at this time I'm already getting a bit sleepy, so I will give the answer
in an update of the publication or in a new entry in which I can
take the opportunity to explain some things about Python such as generators.

But what does programming have to do with it? Given the pattern exhibited by the
numbers, it is not possible to simply substitute into an equation to find out
the answer to the message's question (but it can be quickly checked in
the OEIS [oeis]_), and it is necessary to make a code that verifies the condition for
each number in an orderly manner.

To learn more
-------------

.. [wiki_perfect] Wikipedia, `Perfect number <https://en.wikipedia.org/wiki/Perfect_number>`_.
.. [oeis_perfect] The On-Line Encyclopedia of Integer Sequences, `Hexagonal numbers <http://oeis.org/A000384>`_.
.. [wiki_tri] Wikipedia, `Triangular number <https://en.wikipedia.org/wiki/Triangular_number>`_.
.. [oeis_tri] The On-Line Encyclopedia of Integer Sequences, `Triangular numbers <http://oeis.org/A000217>`_.
.. [wiki_hex] Wikipedia, `Hexagonal number <https://en.wikipedia.org/wiki/Hexagonal_number>`_.
.. [oeis_hex] The On-Line Encyclopedia of Integer Sequences, `Perfect numbers <http://oeis.org/A000396>`_.
.. [oeis] `The On-Line Encyclopedia of Integer Sequences <http://oeis.org/wiki/Welcome>`_.
