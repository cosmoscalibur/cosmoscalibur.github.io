:redirect: blog/con-calma-para-steamos
:date: 2014-04-20
:tags: linux, steamos, videojuegos, steam
:category: tecnología
:author: Edward Villegas-Pulgarin
:language: es

Con calma para SteamOS
======================

Bueno, es un poco raro que sin escribir hace mucho, lo primero que
escriba sea del mundo linux que del mundo de la ciencia y
particularmente de la física que es mi especialidad. Pero resulta que a
veces es un poco más fácil escribir sobre cosas que no toque justificar
tanto.

Soy usuario Linux desde 2009, usando la distro Ubuntu con escritorio
gnome. Pero hace algún tiempo empece a comprar juegos en `Humble
Bundle <https://www.humblebundle.com/>`__. Muy buenos titulos,
excelentes gráficos y en otros excelentes historias, multiplataforma,
mejor dicho un paraíso *gamer* y al mejor precio (créanme! máximo he
pagado 15 dolares por 10 títulos en varias plataformas y sus audios).
Parte de estos títulos son de la corporación
`Valve <http://www.valvesoftware.com/>`__, desarrolladora de la
plataforma de videojuegos `Steam <http://store.steampowered.com/>`__.

Pero donde esta la gracia de este post... bueno, quienes saben de Steam
un poco más allá de sus juegos, sabrán del proyecto
`SteamOS <http://store.steampowered.com/livingroom/SteamOS/?l=spanish>`__.
Valve ahora apuesta al desarrollo de un sistema operativo exclusivo para
*gamers* optimizado para su plataforma. Se posee doble escritorio, uno
para la plataforma de juegos y otro para un escritorio linux tradicional
con gnome basado en Debian 7. En teoría todo lo que funcione en Debian 7
y Ubuntu 12.04 les funcionaría en SteamOS.

Y contrario a como encontrarán en otras publicaciones en internet (en inglés, no
hay por el momento en otros idiomas, o no que yo viera), comenzare por
una advertencia. A Valve no le interesa el problema de compatibilidad, y
por ello no empezaron un sistema operativo desde cero. La recomendación
de la tarjeta gráfica es NVIDIA (que están de hecho participando en el
proyecto), otras tarjetas según afirman funcionan pero puede presentar
problemas. Ese fue mi caso, la pantalla después de la instalación quedo
negra y por más truco de foros no revivió. Así que les recomiendo solo
intentarlo si poseen tarjeta NVIDIA. La restricción que indican de
espacio en disco realmente no es restrictiva, con menos solo implica
menos juegos. Igualmente, si desean conservar otro sistema operativo (su
distro anterior o Windows) el arranque múltiple esta aún en fase
experimental y de hecho grub no identificará algunas veces sus sistemas
anteriores (en mi caso, fue como si no tuviera instalado nada antes pero
si reconoce la tabla de partición). Paquetes de uso cotidiano deberán
instalarlos con el gestor (como esta basado en Debian encontrarán APT) y
frente a compatibilidad con dispositivos android modernos no podremos
hacer nada, más que probar suerte con compilar manualmente bibliotecas
como `libmtp <http://libmtp.sourceforge.net/>`__ para usuarios de
android 4 (¡que en `Ubuntu
14.04 <http://www.ubuntu.com/download/desktop>`__ ya esta integrado!).

Nuevamente un paso más anterior (o que ni siquiera esta junto en otras publicaciones)... si no quieren arriesgarse a instalar el sistema completo y
perder sus sistemas operativos anteriores, es posible instalar el
escritorio Steam para probar con más cuidado antes de dar el paso
completo, siempre y cuando nuestro sistema operativo sea Debian o uno
basado en él. Instalamos el cliente Steam (a través de APT *apt-get
install -y steam* o descargando el
`paquete <http://media.steampowered.com/client/installer/steam.deb>`__
de la página oficial). Luego debemos instalar los paquetes del
`compositor <http://repo.steampowered.com/steamos/pool/main/s/steamos-compositor/>`__ y
el `modeswitch
inhibitor <http://repo.steampowered.com/steamos/pool/main/s/steamos-modeswitch-inhibitor/>`__ (como
sabremos doble click y usar el centro de software o *dpkg -i \*.deb*).
Esto nos permitirá probar un poco Steam pero no con todas las
funcionalidades (los juegos Steam que no son linux no funcionarán), lo
que es equivalente a que solo instalemos el cliente.

Para terminar solo quiero comentar que me pareció algo genial del
instalador (lo único que pude ver) la opción de tomar pantallazos
durante la instalación, archivos que quedan guardados en
*/var/log/\*png*. Aún así, quien quiera correr riesgos, puede descargar
la versión 1.0 beta update 96 en el `repositorio
oficial <http://repo.steampowered.com/download/>`__.

Para seguir todos los anuncios oficiales te sugiero revisar
`aquí <http://steamcommunity.com/groups/steamuniverse#announcements>`__.
