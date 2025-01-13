:date: 2019-11-08
:tags: gravity, newton
:category: science, physics
:language: en

Do we attract each other gravitationally?
=========================================

Gravitational interaction or what is commonly called gravitational force (let's
be clear about two different things here), usually appears in our imagination as
a dominant interaction that ultimately controls the movement of large celestial
bodies and keeps us attached to Earth. However, this interaction isn't exclusive
to stars; it exists between all objects with mass, and if so, why aren't we
attracted gravitationally by other people?

Gravity Force
-------------

Newton revealed in his *Philosophiæ naturalis principia mathematica* that all
bodies with mass (with no exceptions) have associated gravitational force
towards other objects, meaning that everybody with mass is attracted
gravitationally to others.

This attraction or force is the same reason why we're stuck to Earth, the same
reason why the planets in our Solar System orbit around the Sun, and the same
reason why an apple falls onto the ground.

The magnitude of this force can be mathematically described as: (assuming that
the bodies in question are point-like for calculation purposes)

.. math::

    F = - G \frac{m_1 m_2}{r^2},

where :math:`F` is the magnitude of the gravitational force between two masses
:math:`m_1` and :math:`m_2` separated by a distance :math:`r` between their
centers of mass. The negative sign indicates that the force is attractive, which
becomes more intense as the masses are greater (in the numerator) and decreases
with an increase in distance (in the denominator). :math:`G` is the Cavendish
constant or universal gravitational constant.

Let's assume for this case, a couple, where each individual has a mass of 100
kg, and they're separated by a distance of 10 cm (0.1 m) before they share a
kiss. Under these conditions, their gravitational attraction is:

.. math::

    F = - 6.674 \cdot 10^{-11} \frac{100 \cdot 100}{0.1^2} \text{N} = -0.00006674 \text{N}.

To give you an idea of this value, it's roughly the same force that would be
exerted by:

- 2-3 grains of rice on a balance scale due to their weight (gravity attraction
  towards the Earth)
- Even much less than the frictional force between two people's skin when
  they're in contact

To put it into perspective even further, if our couple were to share a kiss with
a force equal to their gravitational attraction towards each other, it would be
almost undetectable, like a whispered promise or a gentle touch.

Second Law of Newton
--------------------

Although this force is very weak, the second law of Newton allows us to
calculate the acceleration that will affect a body after applying a net force to
it. This enables us to see that if there is displacement (since the acceleration
won't be zero), we can determine the effect of a given force.

Let's apply the second law, assuming that one of the bodies remains stationary
and that the acceleration is constant (in reality, both bodies would move, and
the acceleration would increase as they approach each other):

.. math::

    a = \frac{F}{m} = \frac{-0.00006674}{100} \frac{\text{m}}{\text{s}^2} = -0.0000006674 \frac{\text{m}}{\text{s}^2}

Accelerating Motion
-------------------

As was mentioned, the acceleration is different from zero but very small.
However, that small acceleration is still enough to cause visible displacements
over a certain period of time. Let's note that it happens after 10 minutes (600
seconds):

.. math::

    d = \frac{at^2}{2} = \frac{-0.0000006674 \cdot 600^2}{2} \text{m} = 0.12 \text{m}.

Ten minutes would be enough to get the gravitational kiss (let's be real, they'd
happen way faster because the acceleration would keep increasing!), but that
doesn't happen. What's missing?

Force of Friction
-----------------

Don't worry, we're not going to get too technical here. We'll just use an
example to show how friction can slow down gravity at these small scales.

The force of friction is a force that opposes the movement of objects and comes
in two types: static (opposes the initial movement) and dynamic (during the
actual movement). Both cases are defined as a constant called the coefficient of
friction multiplied by the normal force (the component of weight that applies
perpendicular to the surface).

Friction originates from the irregularities on surfaces, which aren't perfectly
smooth and depend on the materials in contact and their surface finishes.

Let's assume our couple is standing on a horizontal floor, so the weight
(gravity) has the same magnitude as the normal force. We'll also assume the
surfaces in contact are rubbery (for shoes) and damp concrete (for the floor),
which means the static coefficient of friction is 0.3.

.. math::

    F_f = \mu_e N = 0.3 \cdot 9.76 \cdot 100 \text{N} = 292.8 \text{N}.

What now? If the force of static friction is not overcome by the applied force
(in this case, the force of gravity between the two bodies), the movement does
not start.

Conclusion
----------

Okay, so if we were in space, far away from any massive objects (so we wouldn't
have to deal with other bodies' effects), we'd basically eliminate any surface
or fluid contact effects (air resistance would also kick in and prevent the
attraction). In theory, we could still have a slow gravitational pull. But,
let's be real... when you're dealing with all these other interactions in
everyday life, gravity just doesn't cut it.

References
----------

- `Philosophiæ naturalis principia mathematica <https://en.wikipedia.org/wiki/Philosophi%C3%A6_Naturalis_Principia_Mathematica>`_,
      Wikipedia.
- `Newton's law of universal gravitation <https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation>`_,
      Wikipedia.
- `Friction <https://en.wikipedia.org/wiki/Friction>`_, Wikipedia.
