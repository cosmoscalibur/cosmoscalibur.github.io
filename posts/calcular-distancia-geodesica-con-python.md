<!--
.. title: Calcular distancia geodésica con Python
.. slug: calcular-distancia-geodesica-con-python
.. date: 2020-05-10 18:35:00-05:00
.. tags: python, gis, geoide, distancia geodésica, geopy
.. category: tecnología
.. link: 
.. description: Consideraciones para el cálculo de la distancia geodésica o distancia geográfica con Python (GeoPy).
.. type: text
.. author: Edward Villegas-Pulgarin
-->

Aunque una de las cosas que más ha rondado en mi desarrollo académico y laboral es la programación, y buena parte de los años en ello con Python, nunca había realizado una entrada al respecto en el blog (lo más cercano ha sido una entrada sobre {{% doc %}}crear-documentacion-de-un-proyecto-python-con-sphinx {{% /doc %}} y {{% doc %}}crear-contenedor-docker-aplicacion-gui-ealite {{% /doc %}}).  

A partir de ahora, y usando *notebooks* compartiré algunas entradas relacionadas con programación o algunas bibliotecas específicas. En esta ocasión, me interesa compartirles como calcular la distancia geodésica entre dos lugares con GeoPy (una biblioteca Python), una de las tantas cosas que por motivos laborales he necesitado en mi exploración con proyectos con sistemas de información geográfica y ruteos.

<!-- TEASER_END -->

# Geoide y geodésicas

¿Habían escuchado antes "geoide" y "geodésica"? Bueno, resulta que el concepto de distancia entre puntos es dependiente de la geometría sobre la cual sea válido el desplazamiento. Así, si ubicamos dos puntos sobre la superficie de la Tierra, uno podría pensar en tomar como distancia la separación en línea recta entre los dos puntos atravesando el interior de la Tierra, y sí, eso es una distancia pero es impráctica porque nadie por ahora atravesará el interior para desplazarse. A esta distancia la conocemos como distancia euclideana (supone una geometría plana, como nos enseñan en el colegio y para muchos en universidad, donde Pitágoras funciona para esta cuenta).  

Pues bien, si la distancia implica una restricción para moverse sobre una geometría en particular, las líneas rectas no son los caminos más cortos (sobre el cual se define la distancia) sino un tipo de líneas que llamaremos geodésicas. Así, la distancia sobre la superficie de la Tierra se mide sobre la geodésica que une los dos puntos de interés y a esa forma superficie de referencia de la Tierra es llamada geoide.

# Cálculo de distancia

El cálculo de la distancia sobre la Tierra debe hacerse suponiendo alguna condición sobre la geometría de la Tierra. Esto es por ejemplo, suponer una esfera, un elipsoide o un plano (y no, la Tierra no es plana, pero para distancias cortas es una buena aproximación). Estas suposiciones ya vienen incluidas y pueden ser parametrizadas en las bibliotecas de cómputo.  

Para el cómputo de geodésicas en Python, en buena medida todo se resume en [GeographicLib](https://geographiclib.sourceforge.io/). Tanto [GDAL](https://gdal.org/), [PyProj](https://pyproj4.github.io/pyproj/stable/#) y [GeoPy](https://geopy.readthedocs.io/en/stable/#) recurren a la implementación de GeographicLib como método por defecto de cálculo.  

Para referencia, usaremos GeoPy (incluido también en GeoPandas) y que dispone de 3 métodos de cálculo de distancia que discutiremos.

Primer paso vamos a instalar GeoPy. Para este fin usaremos el gestor de paquetes *conda* de Anaconda, pero puedes usar *pip*.


```bash
%%bash
conda install -c conda-forge geopy
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


Ahora, importamos el módulo de [distancia de GeoPy](https://geopy.readthedocs.io/en/stable/#module-geopy.distance).


```python
import geopy.distance
```

Para referencia usaremos las coordenadas de Medellín (MDE) y Envigado (ENV) según son ubicadas por Google Maps.


```python
MDE = (6.2443695,-75.6512527)
ENV = (6.1663544,-75.5994392)
```

Para efectos de comparación, no solo presentaré la forma de uso de los métodos sino las distancias y los tiempos de ejecución.

## Método de círculo mayor

El [método de círculo mayor](https://en.wikipedia.org/wiki/Great-circle_distance) consiste en considerar la Tierra como una esfera perfecta de radio 6371.009 km (para el sistema de coordenadas geográficas [WGS-84](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84)). Con esta aproximación se puede tener un error máximo del 0.5%. A pesar del error, es un método de cálculo directo (es una fórmula para reemplazar) y por ende puede obtener un resultado muy rápido y tiene asegurado entregar siempre una aproximación.  

Es llamado círculo mayor porque en una esfera sabemos que el camino más corto es el descrito por el círculo de mayor radio sobre la esfera que contenga a los dos puntos.


```python
%timeit geopy.distance.great_circle(MDE, ENV)
print(geopy.distance.great_circle(MDE, ENV))
```

    14.9 µs ± 238 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    10.395180481810051 km


## Método de Vincenty

El [método de Vincenty](https://en.wikipedia.org/wiki/Vincenty%27s_formulae) es un método iterativo para la aproximación de la distancia geodésica sobre un elipsoide, en este caso, el elipsoide de referencia del sistema coordenado WGS-84. Este método presenta problemas de convergencia entre puntos antinodales y hoy su uso no es aconsejado (GeoPy aún lo presenta en la versión 1.21 pero está marcado como obsoleto).


```python
%timeit geopy.distance.vincenty(MDE, ENV)
print(geopy.distance.vincenty(MDE, ENV))
```

    /home/cosmoscalibur/anaconda/envs/geodesic/lib/python3.7/site-packages/ipykernel_launcher.py:1: DeprecationWarning: Vincenty is deprecated and is going to be removed in geopy 2.0. Use `geopy.distance.geodesic` (or the default `geopy.distance.distance`) instead, which is more accurate and always converges.
      """Entry point for launching an IPython kernel.


    29.7 µs ± 964 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    10.359310623929353 km


    /home/cosmoscalibur/anaconda/envs/geodesic/lib/python3.7/site-packages/ipykernel_launcher.py:2: DeprecationWarning: Vincenty is deprecated and is going to be removed in geopy 2.0. Use `geopy.distance.geodesic` (or the default `geopy.distance.distance`) instead, which is more accurate and always converges.
      


## Método de Karney

Este método al igual que el propuesto por Vincenty, es iterativo pero se asegura que siempre converge y con menor margen de error que Vincenty. Fue [propuesto en 2013](https://link.springer.com/article/10.1007/s00190-012-0578-z).  

La implementación disponible en GeoPy corresponde a la implementación C++ de GeographicLib.


```python
%timeit geopy.distance.distance(MDE, ENV)
print(geopy.distance.distance(MDE, ENV))
```

    231 µs ± 7.42 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    10.35931062438337 km



# Consideraciones

La interfaz incluida en GeographicLib no me pareció amigable, por lo cual no la recomiendo pero su uso asegura incluir solo las funciones especializadas para el tratamiento de la distancia geodésica. GeoPy incluye más utilidades pero posee una interfaz más simple. GDAL y PyProj poseen muchas más funcionalidades, por lo cual representa un aumento de almacenamiento innecesario. Esto, finalmente, para recomendar GeoPy para esta tarea (respecto a GeographicLib, aún te dará la opción de la aproximación de círculo mayor).  

Respecto al método, la divergencia de Vincenty para casos antinodales y la convergencia lenta en otros casos reportados, al igual que su marcado de obsolescencia en las implementaciones nos lleva a omitirlo de cualquier consideración futura. La aproximación de Karney posee el menor error de las 3 aproximaciones pero su tiempo de cómputo es alto si se considera la necesidad de calcular entre una gran cantidad de pares de puntos.  

Para mi caso de interés (problemas de ruteo), la distancia geodésica solo se usa como un primer aproximado para reducir el número de pares sobre los cuales se cálcula la distancia sobre la red vial (de lo cual hablaré en una próxima entrada) y por ende su valor no importa que tenga gran exactitud pero que sea decente para distancias cortas (se busca eliminar el cálculo de distancias largas sobre la red vial).  

Así, si la necesidad es de exactitud te recomiendo la aproximación de Karney pero si es solo una primera aproximación buscando menor tiempo de cómputo, la recomendación es el círculo mayor.
