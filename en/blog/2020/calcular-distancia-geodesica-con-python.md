---
date: 2020-05-10
tags: python, geodesic, geopy
category: technology
language: en
---

# Computing Geodesic Distance with Python

I'd like to share how to compute the geodesic distance between two places using
GeoPy (a Python library), one of the many things I've needed for my exploration
in projects related to geographic information systems and routing.

## Geoid and Geodesics

Ever heard of a "geoid" or a "geodesic"? Well, it turns out that the concept of
distance between two points depends on the shape of the surface you're measuring
on. So, if you pick two spots on Earth, you might think the shortest distance
between them is a straight line that goes through the center of the planet. And
yeah, that's technically a distance, but it's not very practical since nobody's
going to burrow through the Earth to get from one place to another. We call that
kind of distance a Euclidean distance (because it's based on flat geometry, like
you learned in school).

But if distance is about moving along a specific surface, then straight lines
aren't always the shortest paths. Instead, we have these things called
geodesics. So, the distance on Earth's surface is measured along the geodesic
that connects the two points you're interested in. And that surface that we use
as a reference for Earth's shape is called the geoid.

## Computing Distance on Earth

The computation of distance on Earth must be performed under certain conditions
regarding the geometry of Earth. For example, assuming a sphere, an ellipsoid,
or a plane (and not, the Earth is not flat, but for short distances it's a good
approximation). These assumptions are already included and can be parameterized
in computer libraries.

For Python computations, most computations boil down to
[GeographicLib](https://geographiclib.sourceforge.io/). Most of
[GDAL](https://gdal.org/), [PyProj](https://pyproj4.github.io/pyproj/stable/#),
and [GeoPy](https://geopy.readthedocs.io/en/stable/#) rely on GeographicLib as
the default method for distance computations.

For reference, we'll use GeoPy (also included in GeoPandas) with three methods
of distance computation that we'll discuss.

First, we'll install GeoPy using {program}`conda` from Anaconda, but you can
also use {program}`pip`.

```bash
%%bash
conda install -c conda-forge geopy
```

```
Collecting package metadata (current_repodata.json): ...working... done
Solving environment: ...working... done

## Package Plan ##

  environment location: /home/cosmoscalibur/anaconda/envs/geodesic

  added / updated specs:
    - geopy


The following NEW packages will be INSTALLED:

  geographiclib      conda-forge/noarch::geographiclib-1.50-py_0
  geopy              conda-forge/noarch::geopy-1.21.0-py_0

The following packages will be UPDATED:

  ca-certificates     pkgs/main::ca-certificates-2020.1.1-0 --> conda-forge::ca-certificates-2020.4.5.1-hecc5488_0

The following packages will be SUPERSEDED by a higher-priority channel:

  certifi              pkgs/main::certifi-2020.4.5.1-py37_0 --> conda-forge::certifi-2020.4.5.1-py37hc8dfbb8_0
  openssl              pkgs/main::openssl-1.1.1g-h7b6447c_0 --> conda-forge::openssl-1.1.1g-h516909a_0


Proceed ([y]/n)?
Preparing transaction: ...working... done
Verifying transaction: ...working... done
Executing transaction: ...working... done
```

Now, import the
[*distance* module of GeoPy](https://geopy.readthedocs.io/en/stable/#module-geopy.distance).

```python
import geopy.distance
```

For reference, we will be using the coordinates of Medellín (MDE) and Envigado
(ENV) as per their locations on Google Maps.

```python
MDE = (6.2443695,-75.6512527)
ENV = (6.1663544,-75.5994392)
```

For comparison purposes, I will not only present the usage of the methods, but
also the distances and execution times as well.

### Great Circle Method

The [Great Circle Distance](https://en.wikipedia.org/wiki/Great-circle_distance)
method consists of considering the Earth as a perfect sphere with a radius of
6371.009 km (for the geographical coordinate system WGS-84). With this
approximation, an error of up to 0.5% can be achieved. Despite the error, it is
a direct computation method (a formula that can replace) and therefore obtains a
very fast result, guaranteed to always provide an approximation.

It is called the "Great Circle" method because in a sphere, we know that the
shortest path is the one described by the circle with the largest radius over
the sphere that contains the two points.

```python
%timeit geopy.distance.great_circle(MDE, ENV)
print(geopy.distance.great_circle(MDE, ENV))
```

```
14.9 µs ± 238 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
10.395180481810051 km
```

### Vincenty Method

The [Vincenty Formulae](https://en.wikipedia.org/wiki/Vincenty%27s_formulae) is
an iterative method for approximating the geodesic distance over an ellipsoid,
in this case, the reference ellipse of the WGS-84 coordinate system. This method
presents convergence issues between antipodal points and is no longer
recommended for use (GeoPy still presents it in version 1.21, but it is marked
as obsolete).

```python
%timeit geopy.distance.vincenty(MDE, ENV)
print(geopy.distance.vincenty(MDE, ENV))
```

```
/home/cosmoscalibur/anaconda/envs/geodesic/lib/python3.7/site-packages/ipykernel_launcher.py:1: DeprecationWarning: Vincenty is deprecated and is going to be removed in geopy 2.0. Use `geopy.distance.geodesic` (or the default `geopy.distance.distance`) instead, which is more accurate and always converges.
  """Entry point for launching an IPython kernel.


29.7 µs ± 964 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
10.359310623929353 km


/home/cosmoscalibur/anaconda/envs/geodesic/lib/python3.7/site-packages/ipykernel_launcher.py:2: DeprecationWarning: Vincenty is deprecated and is going to be removed in geopy 2.0. Use `geopy.distance.geodesic` (or the default `geopy.distance.distance`) instead, which is more accurate and always converges.
```

### Karney Method

This method is also iterative, like Vincenty's method, but it guarantees
convergence and has a smaller margin of error than Vincenty. It was
[proposed in 2013](https://link.springer.com/article/10.1007/s00190-012-0578-z).

The implementation available in GeoPy corresponds to the C++ implementation of
GeographicLib.

```python
%timeit geopy.distance.distance(MDE, ENV)
print(geopy.distance.distance(MDE, ENV))
```

```
231 µs ± 7.42 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
10.35931062438337 km
```

## Considerations

The interface included in GeographicLib did not seem user-friendly to me, so I
do not recommend it. However, its use ensures that only specialized functions
for computing geodesic distance are used. GeoPy includes more utilities, but has
a simpler interface. GDAL and PyProj have many more features, which makes them
take up unnecessary storage space. This, ultimately, leads to recommending GeoPy
for this task (in comparison to GeographicLib, you will still have the option of
using the Great Circle method).

Regarding the method, the divergence of Vincenty for antipodal cases and the
slow convergence in other cases, as well as its marked obsolescence in
implementations, lead us to omit it from any future consideration. The Karney
approximation has the smallest error among the three approximations, but its
computation time is high if considering the need to compute between many point
pairs.

For my specific interest (routing problems), the geodesic distance is used only
as an initial approximation to reduce the number of pairs of points for which
the distance on the road network is computed (which I will discuss in a future
entry) and therefore its value does not matter if it has high accuracy, but is
decent for short distances (the goal is to eliminate the computation of long
distances over the road network).

Thus, if exactness is required, I recommend the Karney approximation, but if
only an initial approximation seeking less computation time is needed, the Great
Circle method is recommended.
