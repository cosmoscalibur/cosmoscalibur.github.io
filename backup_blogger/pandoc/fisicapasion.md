---
description: |
    Ciencia, física, matemáticas, biología, astronomía, linux, android,
    ubuntu, investigación, tecnología
generator: blogger
title: Física Pasión
viewport: width=1100
...

Este es un blog para hablar de ciencia en general. En lo posible
tendremos notas de actualidad científica, principalmente de ciencias
físicas pero no dejaremos a un lado el maravilloso panorama que nos
muestran otras áreas del saber y la investigación. Que viva la ciencia!
[Blog en Migración]

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=AdSense&widgetId=AdSense1&action=editWidget&sectionId=crosscol "Editar")

domingo, 20 de abril de 2014 {.date-header}
----------------------------

### [Con calma para SteamOS](http://fisicapasion.blogspot.com.co/2014/04/con-calma-para-steamos.html) {.post-title .entry-title itemprop="name"}

Bueno, es un poco raro que sin escribir hace mucho, lo primero que
escriba sea del mundo linux que del mundo de la ciencia y
particularmente de la física que es mi especialidad. Pero resulta que a
veces es un poco más fácil escribir sobre cosas que no toque justificar
tanto.\
\
 Soy usuario linux desde 2009, usando la distro Ubuntu con escritorio
gnome. Pero hace algún tiempo empece a comprar juegos en [Humble
Bundle](https://www.humblebundle.com/). Muy buenos titulos, excelentes
gráficos y en otros excelentes historias, multiplataforma, mejor dicho
un paraíso *gamer* y al mejor precio (créanme! máximo he pagado 15
dolares por 10 títulos en varias plataformas y sus audios). Parte de
estos títulos son de la corporación
[Valve](http://www.valvesoftware.com/), desarrolladora de la plataforma
de videojuegos [Steam](http://store.steampowered.com/).\
\

[![](https://scontent-b-mia.xx.fbcdn.net/hphotos-prn2/t1.0-9/10157196_653805448000130_1403643270930494879_n.jpg)](https://scontent-b-mia.xx.fbcdn.net/hphotos-prn2/t1.0-9/10157196_653805448000130_1403643270930494879_n.jpg)

Pero donde esta la gracia de este post... bueno, quienes saben de Steam
un poco más allá de sus juegos, sabrán del proyecto
[SteamOS](http://store.steampowered.com/livingroom/SteamOS/?l=spanish).
Valve ahora apuesta al desarrollo de un sistema operativo exclusivo para
*gamers* optimizado para su plataforma. Se posee doble escritorio, uno
para la plataforma de juegos y otro para un escritorio linux tradicional
con gnome basado en Debian 7. En teoría todo lo que funcione en Debian 7
y Ubuntu 12.04 les funcionaría en SteamOS.\
\
\
\
 Y contrario a como encontrarán en otros posts en internet (en inglés,
no hay por el momento en otros idiomas, o no que yo viera), comenzare
por una advertencia. A Valve no le interesa el problema de
compatibilidad, y por ello no empezaron un sistema operativo desde cero.
La recomendación de la tarjeta gráfica es NVIDIA (que están de hecho
participando en el proyecto), otras tarjetas según afirman funcionan
pero puede presentar problemas. Ese fue mi caso, la pantalla después de
la instalación quedo negra y por más truco de foros no revivió. Así que
les recomiendo solo intentarlo si poseen tarjeta NVIDIA. La restricción
que indican de espacio en disco realmente no es restrictiva, con menos
solo implica menos juegos. Igualmente, si desean conservar otro sistema
operativo (si distro anterior o windows) el booteo múltiple esta aún en
fase experimental y de hecho grub no identificará algunas veces sus
sistemas anteriores (en mi caso, fue como si no tuviera instalado nada
antes pero si reconoce la tabla de partición). Paquetes de uso cotidiano
deberán instalarlos con el gestor (como esta basado en Debian
encontrarán APT) y frente a compatibilidad con dispositivos android
modernos no podremos hacer nada, más que probar suerte con compilar
manualmente bibliotecas como [libmtp](http://libmtp.sourceforge.net/)
para usuarios de android 4 (¡que en [Ubuntu
14.04](http://www.ubuntu.com/download/desktop) ya esta integrado!).\
\
 Nuevamente un paso más anterior (o que ni siquiera esta junto en otros
posts)... si no quieren arriesgarse a instalar el sistema completo y
perder sus sistemas operativos anteriores, es posible instalar el
escritorio Steam para probar con más cuidado antes de dar el paso
completo, siempre y cuando nuestro sistema operativo sea Debian o uno
basado en él. Instalamos el cliente Steam (a través de APT *apt-get
install -y steam* o descargando el
[paquete](http://media.steampowered.com/client/installer/steam.deb) de
la página oficial). Luego debemos instalar los paquetes del
[compositor](http://repo.steampowered.com/steamos/pool/main/s/steamos-compositor/) y
el [modeswitch
inhibitor](http://repo.steampowered.com/steamos/pool/main/s/steamos-modeswitch-inhibitor/) (como
sabremos doble click y usar el centro de software o *dpkg -i \*.deb*).
Esto nos permitirá probar un poco Steam pero no con todas las
funcionalidades (los juegos Steam que no son linux no funcionarán), lo
que es equivalente a que solo instalemos el cliente.\

[![](https://scontent-b-mia.xx.fbcdn.net/hphotos-prn2/t1.0-9/1374940_653805424666799_6737258560863111281_n.jpg)](https://scontent-b-mia.xx.fbcdn.net/hphotos-prn2/t1.0-9/1374940_653805424666799_6737258560863111281_n.jpg)\
 Para terminar solo quiero comentar que me pareció algo genial del
instalador (lo único que puse ver) la opción de tomar pantallazos
durante la instalación, archivos que quedan guardados en
*/var/log/\*png*. Aún así, quien quiera correr riesgos, puede descargar
la versión 1.0 beta update 96 en el [repositorio
oficial](http://repo.steampowered.com/download/).\
\
 Para seguir todos los anuncios oficiales te sugiero revisar
[aquí](http://steamcommunity.com/groups/steamuniverse#announcements).\
\

Publicado por [Edward Yesid Villegas
Pulgarin](https://plus.google.com/111158383854036411781 "author profile")
en
[13:21](http://fisicapasion.blogspot.com.co/2014/04/con-calma-para-steamos.html "permanent link")

  --------------
  Reacciones: 
  --------------

[Enlaces a esta
entrada](http://fisicapasion.blogspot.com.co/2014/04/con-calma-para-steamos.html#links)
[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post.g?blogID=6963194434005030045&postID=3809502476916451846 "Enviar entrada por correo electrónico")
[![](//img2.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=6963194434005030045&postID=3809502476916451846&from=pencil "Editar entrada")

[Enviar por correo
electrónico](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3809502476916451846⌖=email "Enviar por correo electrónico")[Escribe
un
blog](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3809502476916451846⌖=blog "Escribe un blog")[Compartir
con
Twitter](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3809502476916451846⌖=twitter "Compartir con Twitter")[Compartir
con
Facebook](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3809502476916451846⌖=facebook "Compartir con Facebook")[Compartir
en
Pinterest](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3809502476916451846⌖=pinterest "Compartir en Pinterest")

Etiquetas:
[Gamer](http://fisicapasion.blogspot.com.co/search/label/Gamer),
[Linux](http://fisicapasion.blogspot.com.co/search/label/Linux),
[SteamOS](http://fisicapasion.blogspot.com.co/search/label/SteamOS)

lunes, 11 de noviembre de 2013 {.date-header}
------------------------------

### [El debate Cuero - Bernal](http://fisicapasion.blogspot.com.co/2013/11/el-debate-cuero-bernal.html) {.post-title .entry-title itemprop="name"}

Si bien la ciencia en esencia es imparcial, la objetividad de ella
tiende a perderse cuando desconocemos mucho del medio o cuando sólo por
nuestra condición humana dejamos que la ciencia deje su ideal. Y en
ello, se crean discusiones de carácter casi absurdo por falta de
definiciones adecuadas y de una cultura general en ciencia y tecnología,
y su impacto no sólo en la comunidad general sino incluso, hasta en los
mismos académicos. Recientemente, y aún en continua discusión en los
medios, el caso del científico colombiano Dr. [Raúl
Cuero](http://es.wikipedia.org/wiki/Ra%C3%BAl_Cuero), nos enseño la
falta de cultura y de criterio de nuestro periodismo científico y de la
falta de ética en la investigación científica de algunos casos, sin
desmeritar en ningún momento sus competencias en ciencia. Todo sale a la
luz en un artículo del Dr. [Rodrigo
Bernal](http://es.wikipedia.org/wiki/Rodrigo_Bernal) que salió en El
Espectador, [Los dudosos honores del científico colombiano Raúl
Cuero](http://www.elespectador.com/noticias/actualidad/el-dudoso-idolo-de-cuero-articulo-454167),
a lo cual siguieron distintos debates y posiciones de respaldo tanto a
Bernal
([ejemplo](http://www.elespectador.com/noticias/actualidad/cientificos-respaldan-rodrigo-bernal-quien-desenmascaro-articulo-454563) en
El Espectador que hace una recopilación, y [carta de defensa de Carolina
Murcia](http://www.elespectador.com/noticias/actualidad/carta-carolina-murcia-articulo-454842)
indicando los logros del Dr. Bernal) como a Cuero
([ejemplo](http://lasillavacia.com/content/raul-cuero-y-rodrigo-bernal-una-discusion-impar-46053) en
La Silla Vacía, el cual me duele por pretende un fuerte apoyo de
criterios objetivos, pero sin saberlos usar, y su
[autodefensa](http://www.elespectador.com/noticias/actualidad/no-he-sido-deshonesto-raul-cuero-articulo-454168)).\
\
 Sin duda, el caso de la ética profesional del Dr. Cuero no lo voy a
discutir, pues es obvio para quienes somos detractores de él ([opiniones
de investigadores en
Medellín](http://delaurbe.udea.edu.co/2013/10/28/cuero-encontro-el-ambiente-perfecto-para-engrandecerse/))
como para quienes lo favorecen, que infló sus logros para aparentar más
de lo que era, destacando de manera popular por sobre otros científicos
colombianos, sin tener mérito real (es uno más entre el montón de los
que hace algo) y sus contradicciones develadas en los debates ([W
Radio](http://www.wradio.com.co/escucha/archivo_de_audio/rodrigo-bernal-y-el-cientifico-raul-cuero-debatieron-sobre-investigaciones/20131024/oir/2001080.aspx),
[El
Colombiano](http://www.elcolombiano.com/BancoConocimiento/R/round_cientifico_entre_rodrigo_bernal_y_raul_cuero/round_cientifico_entre_rodrigo_bernal_y_raul_cuero.asp))
en donde argumenta que las cosas contradictorias son cuestión de
semántica lingüística siguiendo con sus juegos de palabras de
post-modernismo, como en su texto para el programa de la gobernación de
["Antioquia la más
educada"](http://www.parquedelacreatividad.org/prensa/documentos/revista_debates/educacion_contemporanea_cultura_creatividad.html),
que en un aparte reza "En el pasado, el paso de la antología a la
epistemología era teórico.", lo cual no dice absolutamente nada (y como
mi colega [+Nicolas
Guarin](http://plus.google.com/115230888269190537809) lo hace notar,
hasta con errores de ortografía se fue dicho texto de Cuero), pero se
acerca al "confunde y reinarás" como indicó el físico Cesar Díaz tras la
[cátedra de Cuero en el
SENA](http://www.elespectador.com/noticias/actualidad/catedra-de-raul-cuero-articulo-455105).\
\
 Ahora al grano... la ciencia de cada quien, ya que ahora la discusión
se volvió en decir si el Dr. Bernal tenía el nivel indicado para dudar
de Cuero y si Cuero tiene efectivamente un nombre distinguido en el
mundo de la ciencia o si es alguien más del montón. Quienes están a
favor del Dr. Cuero se basan en el impacto que posee su trabajo, y el
número de publicaciones en el área y que esta en las fronteras de la
ciencia. Sin embargo, en este tema hay algo que puede dar unas
referencias mucho más claras de su impacto. Si bien, tal como lo indican
sus defensores, posee mayor número de citaciones que el Dr. Bernal, al
igual que mayor número de documentos registrados en
[Scopus](http://es.wikipedia.org/wiki/Scopus), existen situaciones que
deben atenuarse para compararlos adecuadamente.\
\

[![](http://1.bp.blogspot.com/-OaW31yVATCc/UoEwBherM5I/AAAAAAAAHO4/v1oD7Eaz1Fg/s200/Screenshot+from+2013-11-11+10:53:36.png)](http://1.bp.blogspot.com/-OaW31yVATCc/UoEwBherM5I/AAAAAAAAHO4/v1oD7Eaz1Fg/s1600/Screenshot+from+2013-11-11+10:53:36.png)[![](http://1.bp.blogspot.com/-sT-qCknMsks/UoEwBcusFlI/AAAAAAAAHO0/WSdiYPaiT-4/s200/Screenshot+from+2013-11-11+10:53:41.png)](http://1.bp.blogspot.com/-sT-qCknMsks/UoEwBcusFlI/AAAAAAAAHO0/WSdiYPaiT-4/s1600/Screenshot+from+2013-11-11+10:53:41.png)

\

El Dr. Bernal comienza a publicar en 1980, fecha desde la cual Scopus
posee un registro de 22 documentos citados 341 veces y ha sido buscado
en su motor de búsqueda 1120 veces. Ahora, intentaremos una demostración
por contradicción. Si el Dr. Cuero se encuentra en la frontera de la
ciencia y sus trabajos tienen gran impacto, debería estar radicalmente
lejos de un investigador "común" colombiano, como el Dr. Bernal. El Dr.
Bernal comienza a publicar en 1995 y cuenta con un registro de 21
documentos en Scopus, citados 179 veces y ha sido buscado en dicho motor
15856 veces. El número de registros es comparable y el número de
búsquedas al Dr. Bernal es significativamente superior al Dr. Cuero. Sin
embargo, en la ciencia nos importa es que tanto repercute nuestro
trabajo en otros, y allí aparentemente Cuero gana. Pero, no es su
victoria. El Dr. Cuero posee 341 citaciones en 33 años de trabajo,
mientras que Bernal cuenta con 179 en 18 años, lo cual deja una
diferencia de citaciones por año a favor del Dr. Cuero por apenas 0.38.
Pero el Dr. Bernal no profana decir ser una autoridad, y esta a la par
del Dr. Cuero. Pero en *La Silla Vacía* dicen que la mayor parte de las
citaciones de Cuero son después de 2000, lo cual es falso revisando
Scopus, donde solo indica 29, en comparación a las 72 del Dr. Bernal
(así que mucho menos la afirmación de que la cantidad absoluta en dicho
periodo supera al Dr. Bernal).\
\

[![](http://2.bp.blogspot.com/-7tzDd0zg_qo/UoEvsOQyTQI/AAAAAAAAHOk/3FJtrN-Z6dM/s200/Screenshot+from+2013-11-11+11:02:20.png)](http://2.bp.blogspot.com/-7tzDd0zg_qo/UoEvsOQyTQI/AAAAAAAAHOk/3FJtrN-Z6dM/s1600/Screenshot+from+2013-11-11+11:02:20.png)[![](http://1.bp.blogspot.com/-whAMNVMRSvA/UoEvsYcpRII/AAAAAAAAHOo/rqVnqSNtsJQ/s200/Screenshot+from+2013-11-11+11:02:30.png)](http://1.bp.blogspot.com/-whAMNVMRSvA/UoEvsYcpRII/AAAAAAAAHOo/rqVnqSNtsJQ/s1600/Screenshot+from+2013-11-11+11:02:30.png)

\

Aún así este análisis muestra poco sobre sus impactos. La
[bibliometría](http://es.wikipedia.org/wiki/Bibliometr%C3%ADa), un área
que estudia el impacto de las publicaciones de la ciencia, nos muestra
que hay más elementos de análisis. Un elemento adicional, es el
denominado [factor de
impacto](http://es.wikipedia.org/wiki/Factor_de_impacto), que dice que
tan citados son sus artículos en promedio\*, en lo cual el Dr. Cuero
saca una ventaja al Dr. Bernal de 15.5 a 8.5 citas por publicación (pero
lleva 15 años más de trabajo, casi el doble... el doble en su factor de
impacto). Si ponemos en igual periodo de productividad, nuevamente Cuero
cae, ya que sus citaciones desde el periodo de productividad del Dr.
Bernal son 101, luego el factor de impacto de Cuero a 17 años - factor
de impacto 1996-2013 - es de 5.94 en comparación a los 10.53 del Dr.
Bernal.\
\
 Pero, algunas veces existen trabajos cuyas citaciones pueden inflarse a
raíz de compartir el trabajo con co-autores de gran impacto (una mala
práctica en el bajo mundo del trafico de citas) o porque efectivamente
se posee un trabajo pionero y/o de gran importancia. Por ello, existen
otras indices que atenúan los factores del golpe de suerte (tipo
Macarena del duo español musical Los del río, que fue su único éxito) o
esas publicaciones excepcionalmente buenas o trafico con algunos
co-autores, como lo es el índice *h*.\
\
 El [índice *h*](http://es.wikipedia.org/wiki/%C3%8Dndice_h) nos indica
un poco más sobre la regularidad del impacto que posee cada publicación
del autor (o sea, de su impacto a lo largo de su trayectoria). Se define
como el número mínimo de artículos publicados que cuentan con mínimo un
número de citaciones iguales a los artículos considerados (gráficamente
es la intersección de las citaciones ordenadas de mayor a menor con la
recta *y=x*). Así, un índice *h* de 4 (el cual posee Cuero) indica que
posee 4 artículos que como mínimo han sido citados 4 veces cada uno.
Pero el Dr. Bernal posee un índice *h* de 6, lo cual nos habla que ha
poseído un mayor impacto en su trayectoria. Si miramos el referente
temporal de *La Silla Vacía*, Scopus nos muestra nuevamente que el Dr.
Bernal ha impactado justo en el periodo 2000-2013 con un índice *h* de
5, en comparación al índice *h* de 2 para el Dr. Cuero en el mismo
periodo. Estos valores en el párrafo incluyen autocitaciones.\
\

[![](http://4.bp.blogspot.com/-kIDJaStneZI/UoEvcLTUHnI/AAAAAAAAHOU/t0L1FtxLpFk/s200/Screenshot+from+2013-11-11+11:01:06.png)](http://4.bp.blogspot.com/-kIDJaStneZI/UoEvcLTUHnI/AAAAAAAAHOU/t0L1FtxLpFk/s1600/Screenshot+from+2013-11-11+11:01:06.png)[![](http://1.bp.blogspot.com/-rJ-k7J118tc/UoEvcBzPPrI/AAAAAAAAHOY/m6kUWfQSH9I/s200/Screenshot+from+2013-11-11+11:01:09.png)](http://1.bp.blogspot.com/-rJ-k7J118tc/UoEvcBzPPrI/AAAAAAAAHOY/m6kUWfQSH9I/s1600/Screenshot+from+2013-11-11+11:01:09.png)

\

Cuando un trabajo impacta fuertemente un área de estudio, es evidente
que sus citaciones serán significativamente altas, sin embargo, el
trabajo más citado del Dr. Cuero cuenta con 34 citaciones, y solo 6 de
sus 22 documentos han sido citados, mientras que el Dr. Bernal posee un
artículo 62 veces y 13 de sus publicaciones han sido citadas. Nuevamente
deja ver que el Dr. Bernal ha impactado mucho más a la comunidad
académica que el Dr. Cuero.\
\
 El Dr. Cuero así como sus defensores, argumentan que el área de
trabajo, biología sintética, al ser reciente justifica el bajo número de
citaciones y publicaciones. Sin embargo, una rápida búsqueda en google
academico para notar que los autores prominentes en el tema (solo
contando los que poseen perfil en google academico y que explicitamente
tengan en su perfil que es su área de trabajo) poseen hasta 20055
citaciones\*\* a lo largo de su trayectoria, en comparación a las 341
del Dr. Cuero. Tampoco es excusa la novedad del trabajo particular o del
tópico de trabajo.\
\
 La tabla a continuación muestra un resumen de los indicadores de la
contienda (pero incluye autocitacitaciones en la mención de factor de
impacto e índice *h*).\

\

\

Indicador

Cuero

Bernal

Primera publicación

1980

1995

Publicaciones

22

21

Citaciones

341

179

Desde 1996

101

179

Indice h

5

7

Búsquedas

1120

15856

Artículo más citado

34

65

Rango temporal (años)

33

18

Citaciones por año

10.3333333333

9.9444444444

Factor de impacto

15.5

8.5238095238

IF 1996

5.9411764706

10.5294117647

Artículos citados

6

13

\
 \* Por facilidad en este post, he flexibilizado la definición de
*Factor de impacto* ya que en Scopus no esta automatizado consultar las
citaciones en un periodo de tiempo asociada a publicaciones en el mismo
periodo de tiempo, que es como se calcula el factor de impacto. Así que
solo he considerado citaciones totales en el periodo de tiempo entre las
publicaciones de cualquier momento.\
 \*\* Andrew Ellington, quien en Scopus registra 329 documentos con
13285 citaciones e índice *h* de 51 en el periodo 1996-2013,\
\
\

Publicado por [Edward Yesid Villegas
Pulgarin](https://plus.google.com/111158383854036411781 "author profile")
en
[14:51](http://fisicapasion.blogspot.com.co/2013/11/el-debate-cuero-bernal.html "permanent link")

  --------------
  Reacciones: 
  --------------

[Enlaces a esta
entrada](http://fisicapasion.blogspot.com.co/2013/11/el-debate-cuero-bernal.html#links)
[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post.g?blogID=6963194434005030045&postID=6314747162192694149 "Enviar entrada por correo electrónico")
[![](//img2.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=6963194434005030045&postID=6314747162192694149&from=pencil "Editar entrada")

[Enviar por correo
electrónico](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=6314747162192694149⌖=email "Enviar por correo electrónico")[Escribe
un
blog](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=6314747162192694149⌖=blog "Escribe un blog")[Compartir
con
Twitter](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=6314747162192694149⌖=twitter "Compartir con Twitter")[Compartir
con
Facebook](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=6314747162192694149⌖=facebook "Compartir con Facebook")[Compartir
en
Pinterest](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=6314747162192694149⌖=pinterest "Compartir en Pinterest")

Etiquetas:
[Bibliometría](http://fisicapasion.blogspot.com.co/search/label/Bibliometr%C3%ADa),
[Ciencia](http://fisicapasion.blogspot.com.co/search/label/Ciencia),
[Raúl
Cuero](http://fisicapasion.blogspot.com.co/search/label/Ra%C3%BAl%20Cuero),
[Rodrigo
Bernal](http://fisicapasion.blogspot.com.co/search/label/Rodrigo%20Bernal)

martes, 18 de junio de 2013 {.date-header}
---------------------------

### [Orden y origen del cosmos griego](http://fisicapasion.blogspot.com.co/2013/06/orden-y-origen-del-cosmos-griego.html) {.post-title .entry-title itemprop="name"}

Segundo artículo especial para el blog oficial del grupo [Veil
Nebula](http://www.veilnebula.org/10/post/2013/06/orden-y-origen-del-cosmos-griego.html),
basado en mi charla de "Cosmogonía y cosmología griega" de astronomía en
el parque de [+Planetario Jesús Emilio Ramírez
González](http://plus.google.com/106401720425500095803) ([+Parque
Explora](http://plus.google.com/114863977465169963907)) en el Parque de
los Deseos del 14 de mayo de 2013.

Tales de Mileto, el primer filosofo griego, incorporó las primeras
nociones no mitológicas a la descripción y explicación del mundo, he
intento aclarar el misterio de la sustancia primera, considerándola el
agua. El mundo para Tales era un disco circular flotando en el océano.\
 Anaximandro (segundo filosofo jónico) abandonaría la visión de Tales y
del arjé, y asignaría como principio el infinito o lo indefinido. Por
simetría, la Tierra debería ser plana o una forma convexa, y en
equilibrio con el centro del universo. La naturaleza de los cielos es el
fuego y es esférico en forma. Los cuerpos del cielo ubicados a
diferentes distancias, siendo el sol más distante que la esfera de
estrellas fijas. Los cuerpos celestes son agujeros que permiten ver el
fuego del cielo.\
 Anaxímenes (tercer filosofo jónico), encontró el principio en el aire,
que por compresión o rarefacción conduciría a la creación de todo. La
Tierra tiene su origen en el aire denso. La Tierra, al igual que la
luna, el sol y los planetas son planos, y las estrellas fijas son como
clavos en un sólido.\
 Jenófanes, el fundador de la escuela eleática, consideró el principio
en la Tierra. La Tierra es plana y enclavada en el infinito mientras el
sol, los cometas y estrellas son nubes incandescentes. El sol y las
estrellas son formadas diariamente de nubes de partículas ardientes
mientras que la luna es una nube comprimida cuyo brillo viene de una luz
inherente que se extingue mensualmente.\
 A Parménides, virtual fundador de la escuela eleática, corresponde la
primera distinción de una Tierra esférica. Considera el universo entero
por capas esféricas concéntricas alrededor de la estacionaria Tierra. Es
la primera concepción de esferas concéntricas. Consideró el brillo de la
luna por reflexión de la luz del sol, y el origen de estos a partir de
materiales residuales de la vía láctea. Al igual que Anaximandro, comete
el mismo error de poner las estrellas fijas más cerca que el sol.\
 Heráclito consideraría como principio el fuego basado en que todo
llegara a fluir. El sol se formaría a partir de exhalaciones de la
Tierra.\
 Anaxágoras afirma que el universo contiene solo dos cosas: infinito
número de pequeñas partículas (átomos) y el vacío que se extiende al
infinito. Los átomos son hechos de lo mismo pero difieren en forma y
tamaño. Incorpora el principio de causalidad de Leucipo. Demócrito
afirma que las sombras de la luna reflejan la existencia de montañas,
perdiendo la naturaleza perfecta la luna. Estos constituyen el atomismo
griego, y los tres en conjunto apoyan una Tierra plana.\
 Para los estoicos el cosmos es finito y rodeado por un vacío infinito.
Esta en un estado de flujo, como pulsante en tamaño de forma periódica.\
 Aristóteles planteó una Tierra esférica rodeada de esferas celestes
concéntricas entre las cuales las primeras alrededor de la tierra son
los elementales en el orden tierra, agua, aire y fuego. El universo
existe sin cambios a través de la eternidad. Contiene un quinto elemento
denominado éter sobre el cual se hallan los cuerpos celestes.\
 Aristarco introduce la primera mención al sol en el centro, en el cual
siguiendo la linea de pensamiento de Filolao (pitagórico que plantea el
primer modelo no geocéntrico con un fuego central) identificó en el
fuego central al sol y asignó las posiciones correctas a los planetas.
La Tierra rota y órbita alrededor del sol. La esfera de las estrellas
fijas es tan distante que es imposible detectar paralaje.\

**Fuentes**

[The cosmological ideas among the
Greeks](http://articles.adsabs.harvard.edu//full/1916PA.....24..358M/0000358.000.html).
Hector MacPherson, Popular Astronomy, Vol. 24, p.358 (1916).\
 [La evolución en los
griegos](http://fisicapasion.blogspot.com/2012/05/la-evolucion-en-los-griegos.html).
Blog Física pasion de Edward Villegas, Mayo 13 de 2012.\
 [Arche](http://en.wikipedia.org/wiki/Arche). Wikipedia (english
version). June 18, 2013.

Publicado por [Edward Yesid Villegas
Pulgarin](https://plus.google.com/111158383854036411781 "author profile")
en
[13:48](http://fisicapasion.blogspot.com.co/2013/06/orden-y-origen-del-cosmos-griego.html "permanent link")

  --------------
  Reacciones: 
  --------------

[Enlaces a esta
entrada](http://fisicapasion.blogspot.com.co/2013/06/orden-y-origen-del-cosmos-griego.html#links)
[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post.g?blogID=6963194434005030045&postID=2556208115886760426 "Enviar entrada por correo electrónico")
[![](//img2.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=6963194434005030045&postID=2556208115886760426&from=pencil "Editar entrada")

[Enviar por correo
electrónico](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=2556208115886760426⌖=email "Enviar por correo electrónico")[Escribe
un
blog](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=2556208115886760426⌖=blog "Escribe un blog")[Compartir
con
Twitter](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=2556208115886760426⌖=twitter "Compartir con Twitter")[Compartir
con
Facebook](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=2556208115886760426⌖=facebook "Compartir con Facebook")[Compartir
en
Pinterest](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=2556208115886760426⌖=pinterest "Compartir en Pinterest")

Etiquetas:
[Arjé](http://fisicapasion.blogspot.com.co/search/label/Arj%C3%A9),
[Cosmología](http://fisicapasion.blogspot.com.co/search/label/Cosmolog%C3%ADa),
[Grecia](http://fisicapasion.blogspot.com.co/search/label/Grecia),
[Historia](http://fisicapasion.blogspot.com.co/search/label/Historia)

### [¿Tetraquark?](http://fisicapasion.blogspot.com.co/2013/06/tetraquark.html) {.post-title .entry-title itemprop="name"}

Bueno, resulta que el mundo de la física de partículas viene en un
continuo agitar, y nuevos datos y modelos surgen a partir de los
experimentos realizados en los grandes aceleradores de partículas (esos
túneles enormes en los cuales se hace que partículas a muy alta
velocidad colisionen).\
 Lo último en este revuelo, concierne a una nueva partícula que apoya el
modelo molecular de quarks, en el cual se pueden presentar mesones
híbridos, que son partículas constituidas por combinación de mesones,
siendo así partículas constituidas por 4 quarks.\
 Nuestros modelos tradicionales de física de partículas nos permite
ubicar en el mundo de las partículas formadas por quarks (a lo que
denominamos hadrones) los mesones y los bariones. Los mesones,
partículas formadas por pares de quarks (quark y antiquark, pero no
necesariamente el respectivo antiquark) y bariones formados por 3
quarks. Es aquí donde la noticia toma tanta importancia, mostrando una
nueva variedad de hadrones, como el recién descubierto (aún en estudios
preliminares) Z\_c(3900).\

[![](http://cdn.physorg.com/newman/gfx/news/2013/twocolliderr.png)](http://cdn.physorg.com/newman/gfx/news/2013/twocolliderr.png)

La literatura nos referencia este tetraquark como una partícula tipo
charmonium, que corresponden a un tipo especial de mesones en los que se
forma el mesón a partir del quark encando y su respectivo antiquark
(corresponden a los quarkonios, de los cuales solo existen charmonium y
bottomonium). ¿Y por que es de este tipo? Es un tetraquark tipo
charmonium porque en su estructura de quarks se evidencia la estructura
de los mesones charmonium acompañado de un mesón pi.\
 Este descubrimiento abre puertas a evidenciar nuevas y exóticas formas
de materia, al igual que a nuevas extensiones de la física de
partículas.\
\
 **Fuentes**\
 [Two collider research teams find evidence of new particle
Zc(3900)](http://phys.org/news/2013-06-collider-teams-evidence-particle-z3900.html).
Physorg June 18, 2013.

[Observation of the Charged Hadron Zc(3900) at sqrt(s)=4170
MeV](http://arxiv.org/abs/1304.3036). T. Xiao, S. Dobbs, A. Tomaradze,
Kamal K. Seth. ArXiv. April 10, 2013.

[Z\_c(3900) - what is inside?](http://arxiv.org/abs/1304.0380) M.B.
Voloshin. ArXiv. April 1, 2013.

[Quarkonium](http://en.wikipedia.org/wiki/Quarkonium). Wikipedia
(english version). June 18, 2013.

[Meson](http://en.wikipedia.org/wiki/Meson). Wikipedia (english
version). June 18, 2013.

[Hadron](http://en.wikipedia.org/wiki/Hadron). Wikipedia (english
version). June 18, 2013.

[Baryon](http://en.wikipedia.org/wiki/Baryon). Wikipedia (english
version). June 18, 2013.

Publicado por [Edward Yesid Villegas
Pulgarin](https://plus.google.com/111158383854036411781 "author profile")
en
[10:42](http://fisicapasion.blogspot.com.co/2013/06/tetraquark.html "permanent link")

  --------------
  Reacciones: 
  --------------

[Enlaces a esta
entrada](http://fisicapasion.blogspot.com.co/2013/06/tetraquark.html#links)
[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post.g?blogID=6963194434005030045&postID=8394500596505489170 "Enviar entrada por correo electrónico")
[![](//img2.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=6963194434005030045&postID=8394500596505489170&from=pencil "Editar entrada")

[Enviar por correo
electrónico](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=8394500596505489170⌖=email "Enviar por correo electrónico")[Escribe
un
blog](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=8394500596505489170⌖=blog "Escribe un blog")[Compartir
con
Twitter](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=8394500596505489170⌖=twitter "Compartir con Twitter")[Compartir
con
Facebook](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=8394500596505489170⌖=facebook "Compartir con Facebook")[Compartir
en
Pinterest](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=8394500596505489170⌖=pinterest "Compartir en Pinterest")

Etiquetas: [Física de
partículas](http://fisicapasion.blogspot.com.co/search/label/F%C3%ADsica%20de%20part%C3%ADculas),
[Tetraquark](http://fisicapasion.blogspot.com.co/search/label/Tetraquark),
[Zc(3900)](http://fisicapasion.blogspot.com.co/search/label/Zc%283900%29)

domingo, 2 de junio de 2013 {.date-header}
---------------------------

### [El planeta de Einstein](http://fisicapasion.blogspot.com.co/2013/06/el-planeta-de-einstein.html) {.post-title .entry-title itemprop="name"}

[![](http://www.cfa.harvard.edu/image_archive/2013/49/hires.jpg)](http://www.cfa.harvard.edu/image_archive/2013/49/hires.jpg)*El
planeta de Einstein* como ha sido llamado el exoplaneta
[Kepler-76b](http://en.wikipedia.org/wiki/Kepler-76b) es la muestra de
la reutilización de los datos del proyecto
[Kepler](http://www.blogger.com/) para búsqueda de nuevos exoplanetas.\
 Se trata de un gigante gaseoso caliente (un júpiter caliente) a 2200 K
de dos masas de júpiter y periodo orbital de 1.5 días. Se encuentra en
la constelación de Cygnus a 2000 años luz.\
 Su descubrimiento fue confirmado por *[Trans-Atlantic Exoplanet
Survey](http://en.wikipedia.org/wiki/Trans-Atlantic_Exoplanet_Survey)*,
arreglo de 3 telescopios Schmidt de 10 cm dedicados a la exploración del
espacio para búsqueda de exoplanetas por método de tránsito alrededor de
estrellas muy brillantes del Monte Palomar, y con el *[SOPHIE échelle
spectrograph](http://en.wikipedia.org/wiki/SOPHIE_%C3%A9chelle_spectrograph)*,
espectrógrafo de alta resolución instalado en un telescopio reflector de
1.93 m en el Observatorio Haute-Provence.\

[![](http://english.tau.ac.il/sites/default/files/styles/reaserch_main_image_580_x_330/public/planet580.jpg)](http://english.tau.ac.il/sites/default/files/styles/reaserch_main_image_580_x_330/public/planet580.jpg)

Su apodo, *el planeta de Einstein*, corresponde a que es el primer
planeta descubierto usando la relatividad especial. El método de
detección combina 3 fenómenos que modifican la luminosidad de la
estrella. Uno es la luz reflectada por el planeta, otro es la variación
por la modificación del área visible de la estrella (a mayor área
exhibida más luminosa) y el tercero es efecto de la relatividad
especial, conocido como [impulso
Doppler](http://en.wikipedia.org/wiki/Relativistic_beaming) o radiación
relativista.\

[![](http://upload.wikimedia.org/wikipedia/en/4/4d/AGN_Jet_Dilation.png)](http://upload.wikimedia.org/wikipedia/en/4/4d/AGN_Jet_Dilation.png)El
impulso Doppler lo podemos entender como un efecto causado por la
dilatación temporal cuando la fuente luminosa se desplaza, disminuyendo
el espaciamiento temporal entre los pulsos de luz y por ende aumentado
la intensidad luminosa percibida. En este caso, las velocidades
relativistas están asociados a un chorro generado desde el planeta
debido a su super-rotación.\
\
\
\
 [Kepler-76b](http://en.wikipedia.org/wiki/Kepler-76b). Wikipedia
(english).\
 [New Method of Finding Planets Scores its First
Discovery](http://kepler.nasa.gov/news/nasakeplernews/index.cfm?FuseAction=ShowNews&NewsID=266).
NASA Kepler. May 13 2013.\

[BEER analysis of Kepler and CoRoT light curves: I. Discovery of
Kepler-76b: A hot Jupiter with evidence for
superrotation](http://arxiv.org/abs/1304.6841). Accepted to The
Astrophysical Journal. Simchon Faigler, Lev Tal-Or, Tsevi Mazeh, Dave W.
Latham, Lars A. Buchhave. May 2013.

[TAU team takes part in discovering new
planet](http://english.tau.ac.il/news/discovering_new_planet). Tel Aviv
University News. May 13 2013.\

[Relativistic
beaming](http://en.wikipedia.org/wiki/Relativistic_beaming). Wikipedia
(english).

Publicado por [Edward Yesid Villegas
Pulgarin](https://plus.google.com/111158383854036411781 "author profile")
en
[17:29](http://fisicapasion.blogspot.com.co/2013/06/el-planeta-de-einstein.html "permanent link")

  --------------
  Reacciones: 
  --------------

[Enlaces a esta
entrada](http://fisicapasion.blogspot.com.co/2013/06/el-planeta-de-einstein.html#links)
[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post.g?blogID=6963194434005030045&postID=140764318457684011 "Enviar entrada por correo electrónico")
[![](//img2.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=6963194434005030045&postID=140764318457684011&from=pencil "Editar entrada")

[Enviar por correo
electrónico](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=140764318457684011⌖=email "Enviar por correo electrónico")[Escribe
un
blog](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=140764318457684011⌖=blog "Escribe un blog")[Compartir
con
Twitter](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=140764318457684011⌖=twitter "Compartir con Twitter")[Compartir
con
Facebook](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=140764318457684011⌖=facebook "Compartir con Facebook")[Compartir
en
Pinterest](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=140764318457684011⌖=pinterest "Compartir en Pinterest")

Etiquetas:
[Astronomía](http://fisicapasion.blogspot.com.co/search/label/Astronom%C3%ADa),
[Exoplanetas](http://fisicapasion.blogspot.com.co/search/label/Exoplanetas),
[Kepler-76b](http://fisicapasion.blogspot.com.co/search/label/Kepler-76b),
[Relatividad
especial](http://fisicapasion.blogspot.com.co/search/label/Relatividad%20especial)

domingo, 26 de mayo de 2013 {.date-header}
---------------------------

### [Cosmogonía griega](http://fisicapasion.blogspot.com.co/2013/05/cosmogonia-griega.html) {.post-title .entry-title itemprop="name"}

[![](http://2.bp.blogspot.com/-UkTmjytTfyY/UaKViPf8ozI/AAAAAAAAFw0/7P4hSEvI_OA/s200/ofion.png)](http://2.bp.blogspot.com/-UkTmjytTfyY/UaKViPf8ozI/AAAAAAAAFw0/7P4hSEvI_OA/s1600/ofion.png)*Artículo
especial para el blog del grupo de astronomía recreativa [Veil
Nebula](http://www.veilnebula.org/4/post/2013/05/cosmogona-griega.html).*\
 *\
* La cosmogonía y cosmología de los antiguos griegos se encuentra
profundamente vinculada. Sus elementos cosmológicos si bien prescinden
de la mitología desde los razonamientos del primer filosofo griego,
[Tales de Mileto](http://es.wikipedia.org/wiki/Tales_de_Mileto), se
puede rastrear el origen de algunos de estos en ella.\
 Los relatos de la cosmogonía griega pueden ubicarse en los textos de
[Homero](http://es.wikipedia.org/wiki/Homero) y la
[Teogonía](http://es.wikipedia.org/wiki/Teogon%C3%ADa) de
[Hesíodo](http://es.wikipedia.org/wiki/Hesiodo), en los que se ilustra
la estructura de su universo y sus dioses.\

[![](http://4.bp.blogspot.com/-YFwf7spYRMw/UaKV5eZ0ZQI/AAAAAAAAFw8/pTKlYdccXGE/s200/urano+y+gea.jpg)](http://4.bp.blogspot.com/-YFwf7spYRMw/UaKV5eZ0ZQI/AAAAAAAAFw8/pTKlYdccXGE/s1600/urano+y+gea.jpg)\
 Para los griegos, el universo surge del
[caos](http://es.wikipedia.org/wiki/Caos_(mitolog%C3%ADa)), del cual una
fuerza creadora empieza a tomar forma y se manifiesta como
[Eurínome](http://es.wikipedia.org/wiki/Eur%C3%ADnome_(oce%C3%A1nide)).
Eurínome, adoptando forma de paloma deposita un huevo que es calentado
por [Ofión](http://es.wikipedia.org/wiki/Ofi%C3%B3n), la serpiente
primigenia. Una vez el huevo eclosiona, surge el universo, y de ahí
[Urano](http://es.wikipedia.org/wiki/Urano_(mitolog%C3%ADa)) (el cielo)
y [Gea](http://es.wikipedia.org/wiki/Gea) (la Tierra). Estos,
constituyen la primera generación de dioses de la teogonía. Una vez
creado el universo, Eurínome y Ofión se radican en el [monte
Olimpo](http://es.wikipedia.org/wiki/Olimpo), pero al atribuirse Ofión
la creación del universo, Eurínome lo castiga enviándolo al
[Tártaro](http://es.wikipedia.org/wiki/T%C3%A1rtaro_(mitolog%C3%ADa))
(inframundo).\

\

[![](http://3.bp.blogspot.com/-VIIQXq1xZNg/UaKWFIvDhhI/AAAAAAAAFxE/iMoqFKyviaM/s320/universo+biblia.jpg)](http://3.bp.blogspot.com/-VIIQXq1xZNg/UaKWFIvDhhI/AAAAAAAAFxE/iMoqFKyviaM/s1600/universo+biblia.jpg)Del
matrimonio de la primera generación de dioses, su acto copulativo genera
todas las formas de la Tierra y el firmamento, así como a las primeras
razas de la tierra, los [titanes](http://es.wikipedia.org/wiki/Titanes)
y titánides. La Tierra creada es de forma circular, y rodeada
completamente por el gran río
[Océanos](http://es.wikipedia.org/wiki/Oc%C3%A9ano_(mitolog%C3%ADa)). La
superficie separaba dos mundos, el inframundo debajo, y arriba el
firmamento como concebido a forma de un cascarón sólido. Este último
concepto, rastreable en culturas cristianas y judaicas se refleja en la
separación del bien y el mal, de la perfección y lo imperfecto. La
Tierra y el inframundo se caracteriza por el mal y la imperfección,
motivo por el cual existe la vida humana, y su superficie esta
accidentada. El firmamento, representación de los designios de sus
dioses (las constelaciones y astros eran gobernados por estos, y en sus
formas y movimientos se reflejaba su naturaleza de vida) era perfecto,
con formas circulares y esféricas, y de naturaleza de fuego.

\

[Myths &
Legends](http://www.dk.co.uk/nf/Book/BookDisplay/0,,9781405335522,00.html).
Philip Wilkinson. Dorling Kindersley, London 2009.\
 Articulos Wikipedia enlazados.

Publicado por [Edward Yesid Villegas
Pulgarin](https://plus.google.com/111158383854036411781 "author profile")
en
[18:10](http://fisicapasion.blogspot.com.co/2013/05/cosmogonia-griega.html "permanent link")

  --------------
  Reacciones: 
  --------------

[Enlaces a esta
entrada](http://fisicapasion.blogspot.com.co/2013/05/cosmogonia-griega.html#links)
[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post.g?blogID=6963194434005030045&postID=3837260600645729722 "Enviar entrada por correo electrónico")
[![](//img2.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=6963194434005030045&postID=3837260600645729722&from=pencil "Editar entrada")

[Enviar por correo
electrónico](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3837260600645729722⌖=email "Enviar por correo electrónico")[Escribe
un
blog](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3837260600645729722⌖=blog "Escribe un blog")[Compartir
con
Twitter](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3837260600645729722⌖=twitter "Compartir con Twitter")[Compartir
con
Facebook](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3837260600645729722⌖=facebook "Compartir con Facebook")[Compartir
en
Pinterest](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=3837260600645729722⌖=pinterest "Compartir en Pinterest")

Etiquetas:
[Cosmogonía](http://fisicapasion.blogspot.com.co/search/label/Cosmogon%C3%ADa),
[Grecia](http://fisicapasion.blogspot.com.co/search/label/Grecia),
[Mitología](http://fisicapasion.blogspot.com.co/search/label/Mitolog%C3%ADa)

jueves, 17 de enero de 2013 {.date-header}
---------------------------

### [Asimov en la ciencia](http://fisicapasion.blogspot.com.co/2013/01/isaac-asimov-en-la-ciencia.html) {.post-title .entry-title itemprop="name"}

[![](https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-prn1/150072_462073923839951_1869148884_n.jpg)](https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-prn1/150072_462073923839951_1869148884_n.jpg)Isaac
Asimov si bien por el común de la gente es conocido solo como un
escritor de ciencia ficción y misterio (esta ultima temática menos
conocida por el común) y como un gran divulgador de la ciencia, también
fue un científico.

\
 Isaac Asimov, o la forma literal rusa *Isaak Yudovich Ozimov*, nació el
2 de enero de 1920 en Petrovichi, Rusia. Asimov obtuvo titulo de
pregrado, maestría y doctorado en química de la *Columbia University* en
la ciudad de Nueva York. Recordando un poco, los títulos a nivel de
posgrado te confieren las habilidades de investigador (o lo popularmente
conocido como científico).\
\
 Para obtener un doctorado es necesario aportar nuevo conocimiento sobre
un tema, particularmente su tesis doctoral fue en bioquímica (área en la
que se desempeño también como profesor titular en *Boston University*)
con la tesis "*Kinetics of the Reaction Inactivation of Tyrosinase
During Its Catalysis of the Aerobic Oxidation of Catechol*". Fue
investigador químico (científico) de la naval y posteriormente de la
armada, en la cual participo de las pruebas de la bomba atómica en
Bikini. Igualmente publico libros no precisamente de divulgación, sino
textos de carácter formal y científico, como el más conocido de estos
"*Modern Biology*" (1961). Igualmente publico otros textos científicos,
como "*Biochemistry and Human Metabolism*" (1952), el primer texto que
no era ciencia ficción, en compañía de 2 de sus colegas de trabajo de
la *Boston University School of Medicine* y "*The Human Body*" (1963). Y
en la sección "*Letters*" de la revista *Science* también fue
contribuyente frente a debates de gran impacto en la década de los 60 y
70 en biología.\

\

[Isaac Asimov](http://en.wikipedia.org/wiki/Isaac_Asimov). Wikipedia in
english.

[Biography for Isaac Asimov](http://www.imdb.com/name/nm0001920/bio).
IMDb.\

[Isaac Asimov](http://www.biography.com/people/isaac-asimov-9190737).
Biography True Story.

[Isaac Asimov
Biography](http://www.notablebiographies.com/An-Ba/Asimov-Isaac.html#ixzz2Hp8BaOVW).
Notable Biographies.\

\

\

\

\

Publicado por [Edward Yesid Villegas
Pulgarin](https://plus.google.com/111158383854036411781 "author profile")
en
[21:06](http://fisicapasion.blogspot.com.co/2013/01/isaac-asimov-en-la-ciencia.html "permanent link")

  --------------
  Reacciones: 
  --------------

[Enlaces a esta
entrada](http://fisicapasion.blogspot.com.co/2013/01/isaac-asimov-en-la-ciencia.html#links)
[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post.g?blogID=6963194434005030045&postID=5575350967711260358 "Enviar entrada por correo electrónico")
[![](//img2.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=6963194434005030045&postID=5575350967711260358&from=pencil "Editar entrada")

[Enviar por correo
electrónico](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=5575350967711260358⌖=email "Enviar por correo electrónico")[Escribe
un
blog](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=5575350967711260358⌖=blog "Escribe un blog")[Compartir
con
Twitter](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=5575350967711260358⌖=twitter "Compartir con Twitter")[Compartir
con
Facebook](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=5575350967711260358⌖=facebook "Compartir con Facebook")[Compartir
en
Pinterest](https://www.blogger.com/share-post.g?blogID=6963194434005030045&postID=5575350967711260358⌖=pinterest "Compartir en Pinterest")

Etiquetas: [Ciencia
Ficción](http://fisicapasion.blogspot.com.co/search/label/Ciencia%20Ficci%C3%B3n),
[Historia](http://fisicapasion.blogspot.com.co/search/label/Historia),
[Isaac
Asimov](http://fisicapasion.blogspot.com.co/search/label/Isaac%20Asimov)

[Entradas
antiguas](http://fisicapasion.blogspot.com.co/search?updated-max=2013-01-17T21:06:00-05:00&max-results=7 "Entradas antiguas")
[Página principal](http://fisicapasion.blogspot.com.co/)

Suscribirse a: [Entradas
(Atom)](http://fisicapasion.blogspot.com/feeds/posts/default)

No encuentras lo que buscas? Prueba el buscador de Google {.title}
---------------------------------------------------------

Cargando...

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=CustomSearch&widgetId=CustomSearch1&action=editWidget&sectionId=sidebar-right-1 "Editar")

Páginas
-------

-   [Página principal](http://fisicapasion.blogspot.com.co/)
-   [Recursos Bibliográficos y
    Software](http://fisicapasion.blogspot.com.co/p/bases-de-datos-y-repositorios.html)
-   [Linux y Software
    Libre](http://fisicapasion.blogspot.com.co/p/linux-y-software-libre.html)
-   [Física
    Computacional](http://fisicapasion.blogspot.com.co/p/fisica-computacional.html)
-   [Edward Villegas](https://sites.google.com/site/edwardyvillegas/)

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=PageList&widgetId=PageList1&action=editWidget&sectionId=sidebar-right-1 "Editar")

Archivo del blog
----------------

-   [▼ ](javascript:void(0))
    [2014](http://fisicapasion.blogspot.com.co/search?updated-min=2014-01-01T00:00:00-05:00&updated-max=2015-01-01T00:00:00-05:00&max-results=1)
    (1)
    -   [▼ ](javascript:void(0))
        [abril](http://fisicapasion.blogspot.com.co/2014_04_01_archive.html)
        (1)
        -   [Con calma para
            SteamOS](http://fisicapasion.blogspot.com.co/2014/04/con-calma-para-steamos.html)

-   [► ](javascript:void(0))
    [2013](http://fisicapasion.blogspot.com.co/search?updated-min=2013-01-01T00:00:00-05:00&updated-max=2014-01-01T00:00:00-05:00&max-results=7)
    (7)
    -   [► ](javascript:void(0))
        [noviembre](http://fisicapasion.blogspot.com.co/2013_11_01_archive.html)
        (1)

    -   [► ](javascript:void(0))
        [junio](http://fisicapasion.blogspot.com.co/2013_06_01_archive.html)
        (3)

    -   [► ](javascript:void(0))
        [mayo](http://fisicapasion.blogspot.com.co/2013_05_01_archive.html)
        (1)

    -   [► ](javascript:void(0))
        [enero](http://fisicapasion.blogspot.com.co/2013_01_01_archive.html)
        (2)

-   [► ](javascript:void(0))
    [2012](http://fisicapasion.blogspot.com.co/search?updated-min=2012-01-01T00:00:00-05:00&updated-max=2013-01-01T00:00:00-05:00&max-results=6)
    (6)
    -   [► ](javascript:void(0))
        [noviembre](http://fisicapasion.blogspot.com.co/2012_11_01_archive.html)
        (1)

    -   [► ](javascript:void(0))
        [septiembre](http://fisicapasion.blogspot.com.co/2012_09_01_archive.html)
        (1)

    -   [► ](javascript:void(0))
        [agosto](http://fisicapasion.blogspot.com.co/2012_08_01_archive.html)
        (1)

    -   [► ](javascript:void(0))
        [mayo](http://fisicapasion.blogspot.com.co/2012_05_01_archive.html)
        (1)

    -   [► ](javascript:void(0))
        [febrero](http://fisicapasion.blogspot.com.co/2012_02_01_archive.html)
        (2)

-   [► ](javascript:void(0))
    [2011](http://fisicapasion.blogspot.com.co/search?updated-min=2011-01-01T00:00:00-05:00&updated-max=2012-01-01T00:00:00-05:00&max-results=16)
    (16)
    -   [► ](javascript:void(0))
        [septiembre](http://fisicapasion.blogspot.com.co/2011_09_01_archive.html)
        (1)

    -   [► ](javascript:void(0))
        [julio](http://fisicapasion.blogspot.com.co/2011_07_01_archive.html)
        (4)

    -   [► ](javascript:void(0))
        [mayo](http://fisicapasion.blogspot.com.co/2011_05_01_archive.html)
        (1)

    -   [► ](javascript:void(0))
        [abril](http://fisicapasion.blogspot.com.co/2011_04_01_archive.html)
        (2)

    -   [► ](javascript:void(0))
        [marzo](http://fisicapasion.blogspot.com.co/2011_03_01_archive.html)
        (1)

    -   [► ](javascript:void(0))
        [febrero](http://fisicapasion.blogspot.com.co/2011_02_01_archive.html)
        (3)

    -   [► ](javascript:void(0))
        [enero](http://fisicapasion.blogspot.com.co/2011_01_01_archive.html)
        (4)

-   [► ](javascript:void(0))
    [2010](http://fisicapasion.blogspot.com.co/search?updated-min=2010-01-01T00:00:00-05:00&updated-max=2011-01-01T00:00:00-05:00&max-results=7)
    (7)
    -   [► ](javascript:void(0))
        [diciembre](http://fisicapasion.blogspot.com.co/2010_12_01_archive.html)
        (7)

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=BlogArchive&widgetId=BlogArchive1&action=editWidget&sectionId=sidebar-right-1 "Editar")

@cosmoscalibur {.title}
--------------

[Seguir a @cosmoscalibur](https://twitter.com/cosmoscalibur)

[Tweet](https://twitter.com/share)

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=HTML&widgetId=HTML4&action=editWidget&sectionId=sidebar-right-1 "Editar")

Me gusta Cosmoscalibur {.title}
----------------------

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=HTML&widgetId=HTML2&action=editWidget&sectionId=sidebar-right-1 "Editar")

+Cosmoscalibur {.title}
--------------

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=HTML&widgetId=HTML5&action=editWidget&sectionId=sidebar-right-1 "Editar")

Comentarios (Usuarios Facebook) {.title}
-------------------------------

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=HTML&widgetId=HTML3&action=editWidget&sectionId=footer-1 "Editar")

Entradas populares
------------------

-   [La Tierra cambio después del terremoto de
    Japón](http://fisicapasion.blogspot.com.co/2011/03/la-tierra-cambio-despues-del-terremoto.html)
    Tal vez el título del post dice poco, porque la Tierra siempre esta
    en un cambio continuo así no lo percibamos. Constantemente la masa
    de la...
-   [![](http://1.bp.blogspot.com/_sydA_xCOkr0/S7NZECWr-XI/AAAAAAAAAc8/ZXAg0xJsCxM/s72-c/hubble+dark+matter+map+3D.jpg)](http://fisicapasion.blogspot.com.co/2011/04/la-antimateria-seria-anti-materia.html)
    [La antimateria sería
    anti-materia](http://fisicapasion.blogspot.com.co/2011/04/la-antimateria-seria-anti-materia.html)
    La antimateria sería verdadera anti-materia. Probablemente suene
    extraño esto, pero no lo es. La antimateria había sido hasta el
    momento ma...
-   [Gravitomagnetismo y Gravity Probe
    B](http://fisicapasion.blogspot.com.co/2011/07/gravitomagnetismo-y-gravity-probe-b.html)
    Una de las teorías de mayor impacto, no solo a
    nivel científico sino también del "saber popular" ha sido la teoría
    de la relativid...
-   [Asimov en la
    ciencia](http://fisicapasion.blogspot.com.co/2013/01/isaac-asimov-en-la-ciencia.html)
    Isaac Asimov si bien por el común de la gente es conocido solo como
    un escritor de ciencia ficción y misterio (esta ultima temática
    menos c...
-   [Calculan masa del agujero negro mas
    grande](http://fisicapasion.blogspot.com.co/2011/01/calculan-masa-del-agujero-negro-mas.html)
    El astrónomo Karl Gebhardt de la University of Texas, Austin,
    presento los resultados de su equipo de investigación el 12 de enero
    en el enc...
-   [La evolución en los
    griegos](http://fisicapasion.blogspot.com.co/2012/05/la-evolucion-en-los-griegos.html)
    Hablando un poco de la evolución biológica el día de ayer, dando
    inicio a las actividades del ciclo de astrobiología en el Club
    Orión, se g...
-   [![](http://2.bp.blogspot.com/-UkTmjytTfyY/UaKViPf8ozI/AAAAAAAAFw0/7P4hSEvI_OA/s72-c/ofion.png)](http://fisicapasion.blogspot.com.co/2013/05/cosmogonia-griega.html)
    [Cosmogonía
    griega](http://fisicapasion.blogspot.com.co/2013/05/cosmogonia-griega.html)
    Artículo especial para el blog del grupo de astronomía recreativa
    Veil Nebula . La cosmogonía y cosmología de los antiguos griegos se
    encu...
-   [El último tránsito de
    Venus](http://fisicapasion.blogspot.com.co/2012/02/el-ultimo-transito-de-venus.html)
    Retomando el blog después de cierto tiempo de abandono por diversos
    motivos, volvemos con las cosas que nos gustan,
    ciencia, tecnología y ot...
-   [Viendo carga
    molecular](http://fisicapasion.blogspot.com.co/2012/02/viendo-carga-molecular.html)
    Punta de medición de un AFM. La zona de medición corresponde al
    final del filamento delgado de la imagen. Científicos de IBM fuer...

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=PopularPosts&widgetId=PopularPosts1&action=editWidget&sectionId=footer-1 "Editar")

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=AdSense&widgetId=AdSense3&action=editWidget&sectionId=footer-1 "Editar")

  --
  --

Edward Villegas COPYRIGHT 2010-2016 (Blog en migración). Plantilla
Awesome Inc.. Con la tecnología de [Blogger](https://www.blogger.com).

[![](//img1.blogblog.com/img/icon18_wrench_allbkg.png)](//www.blogger.com/rearrange?blogID=6963194434005030045&widgetType=Attribution&widgetId=Attribution1&action=editWidget&sectionId=footer-3 "Editar")
