---
date: 2025-05-01
tags: manjaro, kde, pamac, flatpak, aur
category: tecnología, linux
---

# ¿Es Manjaro para novatos?

He usado Manjaro desde hace 7 meses, y me ha apasionado. Me gusta disponer de
las novedades rápido, sin el sacrificio de la estabilidad (cosa que me sucedía
en los intentos que tuve en Arch Linux), su gestor de *hardware* y de *núcleos
Linux* me parecen muy buenas utilidades. Además, {program}`pamac` es una
herramienta muy útil para gestionar paquetes en Manjaro, mucho más amigable que
{program}`pacman` de Arch Linux, y con cierta similitud con {program}`apt` de
Debian/Ubuntu. La documentación propia de Manjaro, sumada a la excelente
documentación de Arch Linux, hacen que sea una distribución muy fácil de usar, y
me atreveré a decir, que esta facilidad es extendida para novatos.

Te contaré mis pensamientos sobre Manjaro para novatos.

Bueno, me atrevo a decir que esta distribución tiene la estabilidad suficiente
para permitir el ingreso de usuarios nuevos al mundo Linux sin mayores
problemas. Recuerdo mis primeras experiencias en Linux, y no veo nada distinto.
Un par de problemas al inicio asociados al wifi, al controlador gráfico (
NVIDIA), el teclado externo y aprender la gestión de paquetes y leer cada que
algo se dañaba (uno nuevo reinstala varias veces).

Lo primero que uno quiere al moverse a Linux es tener una transición simple a
muchas aplicaciones que normalmente se tienen en Windows. Esto se logra con el
amplio repositorio oficial de Manjaro, se complementa bastante bien con Flatpak
y si se usa con moderación (y seleccionando aquellos con votos y las versiones
preferiblemente terminadas en -bin, si son la versión reciente), los paquetes
disponibles en el AUR (los problemas, nada diferente a usar PPA en Ubuntu y lo
que conlleva).

Esta oferta extendida con Flatpak y AUR nos deja con opciones de muchos paquetes
comunes, oficiales o no oficiales de versiones Windows, versiones recientes de
alternativas que ofrecen excelente compatibilidad o que sin ser compatibles son
una buena opción para cambiar el flujo de trabajo y usarlas. Pero también el
mundo de los videojuegos tiene en su ojo a la distribución Arch Linux, en la
cual se basa Steam Deck y por ende un potencial de beneficios en derivados de
Arch.

Si escoges un buen entorno de escritorio DE (esto es independiente de la
distribución Linux, sea desde Ubuntu hasta Manjaro), tendrás una ganancia en la
experiencia y este entorno recomendado si tienes buena RAM, es KDE. Y KDE tiene
en buena apreciación a Arch Linux, al punto que su proyecto de distro propia se
basa en este (proyecto Banana). Esto también implica que las soluciones de KDE
estarán muy probadas para Arch y derivados.

Que Manjaro disponga de su propio repositorio independiente de Arch Linux
permite tener la estrategia de pruebas de los paquetes y pensar en su
estabilidad antes de llegar a nosotros los usuarios finales. Y debo decir que
esto salvo por pequeños detalles que su propio foro advierte como corregir pasa
sin mayor novedad (mi transición inicial en Linux era a veces uno no saber ni
donde buscar como solucionar un daño). Esto si sabes seguir instrucciones lo
puedes hacer siendo novato en Linux. Esta separación implica que las novedades
se pueden dilatar típicamente entre 2 y 4 semanas, pero no tendrás que
sacrificar estabilidad y tiempo en arreglar tantos problemas como sucedería en
Arch Linux (al ser *mainstream* en lugar de *rolling release*). El repositorio
de Manjaro se separa en ramas inestables, de pruebas y estable. Si eres más
arriesgado, puedes usar las ramas inestables y de pruebas, y a su vez contribuir
para que Manjaro sea aún mejor.

Si decides usar Manjaro y siendo novato, con mayor razón la gestión de paquetes
recomendada es con {program}`pamac` en lugar de {program}`pacman`. Es más
amigable en los comandos y podrás recordarlos más fácil, y con ayuda de KDE
Discover incluso podrás gestionar la instalación de paquetes Flatpak de manera
gráfica.

El foro y recursos en general de Manjaro son muy buenos, muchos aptos para
cualquier nivel de usuario. Y sin duda, podrás encontrar también colaboración en
la red para apoyarte en como seguir este camino a la hora de migrar de Windows a
Linux, no solo a esta distribución sino a otras, en tu aventura de
[distrohopping](/es/blog/2024/distrohopping-cambiar-de-distribuci%C3%B3n-linux-y-no-morir-en-el-intento.md)
Y quedo atento a apoyar este camino.

## Recomendaciones

Ya he publicado en otras ocasiones temas relacionados con Manjaro, así que te
recomiendo dar un vistazo:

- [](/es/blog/2024/distrohopping-cambiar-de-distribuci%C3%B3n-linux-y-no-morir-en-el-intento.md)
- [](/es/blog/2024/que-hacer-despues-de-instalar-manjaro.md)
- [](/es/blog/2024/problemas-de-conexion-wifi-en-linux.md)
- [](/es/blog/2024/problema-de-wayland-y-graficos-hibridos-en-linux.md)
- [](/es/blog/2025/montar-disco-en-linux-y-error-de-volumen-sucio.md)
- [](/es/blog/2025/ecosistema-rust-para-la-terminal-linux.md)
- [](/es/blog/2024/configurar-starship-en-manjaro-y-zsh.md)
- [](/es/blog/2025/instalar-docker-en-manjaro.md)
