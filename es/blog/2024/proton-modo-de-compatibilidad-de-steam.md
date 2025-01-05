---
date: 2024-06-04
tags: videojuegos para linux, steam, steam proton, steam play, aplicaciones para linux, juego brawlhalla
category: entretenimiento
---

# Proton: Modo de compatibilidad de Steam

¿Quieres jugar ese videojuego Steam que es soportado en Windows, pero no en
Linux? Te cuento como usar el modo de compatibilidad de Steam en todos los
juegos.

Así es, tengo un lado _gamer_ y ya antes les he contado un poco sobre Steam
([](/es/blog/2021/configurar-retroarch-en-steam.rst) y
[](/es/blog/2014/con-calma-para-steamos.rst)), que es la plataforma de mi
predilección (entre otras, porque muchos de los juegos ofrecidos en
[Humble Bundle](https://www.humblebundle.com/) son para esta). Y es común en los
juegos que he comprado en los paquetes o algunos _free to play_ que me han
llamado la atención, no tener la opción de Linux que es mi sistema operativo
principal. Pero Steam, tiene una solución, o al menos, una alternativa que vale
la pena intentar antes de olvidar.

## Proton

En el mundo Linux, seguramente conocerás una herramienta que nos permite
intentar ejecutar programas Windows en Linux, que se llama
[Wine](https://www.winehq.org/), de la cual también les conté en el pasado
cuando necesitaba usar
[_Enterprise Architect_ desde Linux](/es/blog/2019/crear-contenedor-lxc-para-aplicacion-gui-ealite.rst).
Resulta que Wine es justamente la solución por defecto, y cuando no, es una
solución que aplica modificaciones sobre lo ya existente de Wine. Así es como
surge, Proton, la solución desarrollada por _Valve_ (los desarrolladores de
_Steam_) para permitir dar portabilidad de los juegos Windows a un público
amante de videojuegos, que cada vez es mayor usando Linux.

[Proton](https://github.com/ValveSoftware/Proton) usa como base Wine, y adiciona
una serie de componentes y parches adicionales para dar compatibilidad a los
juegos desarrollados para Steam con soporte original para Windows, en Linux. Y
esto ha sido de gran importancia para el proyecto de
[Steam Deck](https://store.steampowered.com/steamdeck), la consola portátil de
Steam basada en Linux.

## Steam Play

Si queremos entonces instalar videojuegos en nuestro PC Linux que son soportados
en Windows y no Linux, ya la opción de compatibilidad, la cual se llama _Steam
Play_, viene activada por defecto. Pero, esto solo para el catálogo oficialmente
soportado.

Sin embargo, existen juegos que sin ser soportados oficialmente, puedes darles
un vistazo y funcionan perfectamente. Justamente esta semana, para una partida
con mis compañeros de trabajo, decidimos jugar
[Brawlhalla](https://store.steampowered.com/app/291550/Brawlhalla/), y la
sorpresa, no está soportado en Linux.

Así que, el proceso cuando no tenemos habilitado un juego es dirigirnos al menú
de la barra superior, seleccionamos _Steam_, _Configuración_, _Compatibilidad_ y
en el cuadro que nos muestra esta sección, veremos que la primera opción ya está
habilitada (la de títulos soportados), pero la opción para todos los títulos no.
Ahora, adelante, habilitamos que sea para todos los títulos y aceptamos el
reinicio de _Steam_. Una vez regresemos a _Brawlhalla_, veremos que el botón de
instalar ya se encuentra habilitado.

Una vez termine la instalación e iniciemos el juego, veremos un solo mensaje de
error, del cual no hay que preocuparse, lo saltamos y podemos jugar sin
inconvenientes.
