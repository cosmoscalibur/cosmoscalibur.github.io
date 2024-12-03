# *Distrohopping*: Cambiar de distribución Linux y no morir en el intento

Vengo de dos cambios de distribución Linux recientes, y eso me hizo pensar un
poco en el esfuerzo asociado y en como ese esfuerzo se puede reducir.
Igualmente, recordé el concepto asociado de "*distrohopping*" y las discusiones
alrededor de esta práctica, en la cual muchos terminan afirmando que realmente
es perder el tiempo y que aporta poco valor, pero yo no lo veo así y quiero
compartirles el valor que le veo y el como facilitarlo.

¿Qué he probado antes?: Mandriva (descontinuada), Open Suse, Ubuntu, Debian,
Antix, Lubuntu, Antergos, Arch, Gentoo, Funtoo, Linux Mint, Xubuntu, y ahora
Kubuntu y Manjaro KDE.

En cuáles he tenido periodos estables de años: Ubuntu, Lubuntu, Linux Mint y
Xubuntu. La transición este año a Kubuntu me enamoró de KDE (aquí aparece no
una necesidad sino un deseo, y es tener las opciones de configuración o gestión
que me sirven, de forma intuitiva, amigable, y con conjuntos de aplicaciones
preinstaladas que realmente me son útiles). Sobre el último detalle, también
deja un deseo y no necesidad, y es que lo preinstalado de la distribución sea
acorde a mis actividades. Los deseos son válidos, son parte de nuestra
experiencia positiva en una distribución, pero no deben ser el criterio de
selección.

## ¿Es buena idea hacer *distrohopping*?

Encontrarás muchos motivos para hacer *distrohopping*, lo interesante de lo
novedoso y querer probar la distro de la cual todos hablan, o el nuevo
gestor de paquetes que va a revolucionar la instalación, el mejor manejador
de controladores privativos, tener la distro que te permite usar todo el
beneficio de tu último computador o accesorio, o incluso motivos asociados a
aumentar más tu conocimiento y experiencia sobre el mundo Linux y las
distribuciones, o generar contenido variado sobre todas las opciones
disponibles, o condiciones laborales como la distro en la cual se encuentran
los servidores del servicio que ofrecen en tu trabajo como desarrollador.

Cada una de estas, encontrarás un foro o blog que la discute, y probablemente
te terminará indicando que perdiste el tiempo y que eso no generó valor para
ti, y te recomiendan que omitas la experiencia porque ellos en sus muchos años
de *distrohopping* concluyen que no necesitas probar de todo sino solo escoger
una desde el inicio que se ajuste a tu necesidad y quedarte allí.
¿Pero sabes algo? A ellos saber lo que buscaban y que eso existía les tomo
años.

El *distrohopping* es exactamente lo que hacemos cuando no sabemos muy bien lo
que necesitamos ni lo que existe para escoger, así que empezamos a probar. Y
así como sucede con el *smartphone*, el *smart tv*, el apartamento que
tomas en alquiler, el carro que compras o incluso el PC que compras, tus gustos
y necesidades cambian, haciendo que la decisión que tomaste ya no sea la mejor,
y está bien cambiar.

Cuando te enamoras de una distribución Linux, vas a considerar que nunca fue
necesario el *distrohopping* y que no te sirvió para lo que llegaste a
descubrir, pero es es una gran mentira. Tienes los elementos de comparación
porque te atreviste a probar, sabes que existía la distribución que elegiste
porque buscabas opciones cada que encontrabas detalles que no te agradaban de
la actual. Pero así como en los enamoramientos de prejas, también perdemos el
amor porque nosotros no somos los mismos siempre, y las distribuciones Linux
tampoco. Cambian continuamente aprovechando las revoluciones tecnológicas o por
sus definiciones necesarias para el autosostenimiento o *marketing*. Incluso,
las comunidades alrededor pueden cambiar y afectar la distribución.

Así que, adelante, es bueno hacer *distrohopping*, pero no te voy a mentir,
quienes afirman que es mala idea, tienen un punto importante, y es el esfuerzo
mental y físico que implica la transición. Así que, enfocaremos en como hacer
*distrohopping* reduciendo el impacto.

## ¿Qué me aporta hacer *distrohopping*?

Voy a detallar un poco esto, aprovechando los puntos que justamente terminan
detallando en muchos blogs sobre porque el *distrohopping* no aporta, y
finalizar con lo que a mi parecer, sí aporta.

### Aprender más sobre Linux: No

No seremos románticos, el *distrohopping* no te aporta nuevo conocimiento.
Realmente si quieres aprender, lo puedes hacer en cualquier distribución, solo
debes enfrentar los problemas en la forma difícil (toma el *hardway* de cada
cosa que consideres). Ejemplo, no uses mucho los elementos gráficos, los
botones u atajos, usa más comandos de la consola, y así obtendrás mayor
aprendizaje. No siempre instales el software desde repositorios, de vez en
cuando, anímate a instalarlo mediante compilación o desde un directorio
comprimido. No uses la casilla de verificación o el cuadro de texto de un
cuadro de diálogo para modificar una configuración, busca el archivo de texto
plano asociado a dicha configuración (si existe, en KDE Plasma y Wayland me he
encontrado muchas cosas que si existen en un archivo de configuración,
probablemente no están documentadas y definitivamente toca por los cuadros de
diálogo o opciones de la barra de tareas, porque ni siquiera un comando
asociado).

Lo que aprendes en una distribución específica, son justamente
herramientas específicas de la distribución y que por ende dicho conocimiento
no es universal o replicable, y no te será útil si cambias otra vez de
distribución o si tu amigo que usa otra distribución te pide ayuda.

### Mejor rendimiento del equipo: No

Tampoco nos aporta mayor rendimiento del equipo. En general el rendimiento lo
va a otorgar el *hardware*, el *software* para una tarea específica y el nivel
de depuración que tengamos. Todo esto se puede hacer actualizando el equipo,
cambiando el software usado para una tarea o depurando procesos que se activan
que no son necesarios, y desinstalando muchos paquetes preinstalados (o que
instalamos creyendo que algún día usaremos). ¿Y qué sucede si nuestro equipo es
viejo? En el *hardway* puedes hacer todo esto sobre cualquier distribución
Linux.

Así que, claramente tendrás mayor rendimiento si editas video con software que
acelera con GPU así es solo basado en CPU, o tu código Python ejecutará más
rápido si te pasas a Python 3.12 en lugar de continuar en Python 3.9, y tu
sistema operativo arrancará más rápido y tendrás un inicio de activa más fluido
si desactivas Dropbox y Discord del inicio de sesión. Esto no va a cambiar por
pasarte de Ubuntu a Arch. Fíjate en que muchas veces acumulamos mucha caché o
temporales, esto también requiere limpieza.

Si quieres mejor rendimiento debes aprovechar las optimizaciones que hacen en
versiones más actualizadas del software que usas (ejemplo, Python 3.12 ofrece
soporte experimental de JIT y del modo no GIL, que no existen en 3.9), o de un
software alternativo que optimiza el flujo que deseas más rápido (ejemplo,
pasar tu análisis de datos de Pandas a Polars o FireDucks). O considera si
estás en el límite de lo que otorga tu equipo si lleva varios años. Y sobre
todo, pon mucha atención en los servicios que se activan durante el arranque.

Aprovecha los gestores de limpieza, paquetes y procesos de tu distribución, o
usa un software de optimización y monitoreo como [Stacer](https://oguzhaninan.github.io/Stacer-Web/).

### Software actualizado: No

Es claro que existen distribuciones con software más actualizado, esto es la
diferencia que se ofrecen entre los modelos de liberación continúa
(_rolling release_), liberación periódica o las liberaciones de soporte largo
(LTS). Si deseamos algo muy nuevo, la preferencia sería una liberación
continúa, pero su estabilidad puede estar comprometida. Si queremos mayor
estabilidad, usaremos una LTS, pero fácilmente esto implica retraso de años en
el uso de nuevo software o de mejorar soporte de hardware. Un punto intermedio
son las liberaciones periódicas (que acorde al compromiso con la estabilidad de
las distribuciones, algunas periódicas pueden ser más o menos lentas para
actualizar paquetes, ejemplo, Ubuntu es lenta).

Sin embargo, los repositorios oficiales no son el único mecanismo para tener
software actualizado. Puedes usar fácilmente _snap_ si estás en Ubuntu o
derivados (en otras distribuciones puede no ser tan natural) o _flatpak_ (la
cual en algunas distribuciones viene preinstalado, o instalarlo). También
puedes usar los AppImage que no implican instalación en el sistema (es un tipo
de aplicación portable para Linux), aunque estas no poseen un repositorio
centralizado de gran tamaño, entonces se vuelve una gestión manual cada
AppImage. Estas opciones no solo te permiten obtener las últimas versiones (si
son las versiones oficiales), sino también omitir problemas asociados a
dependencias. Ejemplo, en Manjaro en mi equipo con tarjeta gráfica NVIDIA tengo
problemas para instalar OBS Studio con _pamac_ por una dependencia (aclaro la
tarjeta gráfica porque el problema no es replicable si lo instalo en un equipo
con tarjeta gráfica integrafa), pero si uso _Flatpak_ lo tengo funcional sin
problema.

También existen opciones de instalación simples de usar a través de los
gestores de paquetes de los lenguajes de desarrollo en los cuales se
implementaron. Ejemplo, puedes instalar el emulador de terminal Alacritty en
su última versión con *cargo* (Rust) o instalar la utilidad de descarga de
videos *YT DLP* con *PIP/UV* (Python).

Y como siempre, está el *hardway*, puedes descargar el archivo *tar.gz* que
muchos suministran (ejemplo, Dropbox, y así evitar el PPA en Ubuntu) o
descargar el código fuente desde un sitio web o repositorio GitHub y manejar
las dependencias de compilación.

### Consistencia filosófica (fanatismo o purismo incluído): No

Muchos cambian o escogen una distribución por consistencia filosófica. Pero
esto realmente tampoco lo otorga.

Si no quieres software privativo, puedes desinstalarlo y buscar las
alternativas, y luego instalarlas. Si no estás de acuerdo con el uso por
defecto de Firefox como _snap_ en Ubuntu y de otros paquetes, puedes
desinstalar el software, bloquear el redireccionamiento a _snap_ de los
gestores de paquetes o tienda de software, y luego volver a instalar ya con la
versión *DEB* (has logrado el *desnapping* de Ubuntu).

Quieres tener la libertad de elección, puedes desinstalar cualquier componente
e instalar la componente que te haga sentir bien.

La consistencia filosófica o purismo lo puedes alcanzar a través de acciones
específicas sobre la distribución.

### Comodidad y facilidad (ley de mínimo esfuerzo): Sí

Esto es lo realmente importante cuando escogemos un producto y servicio, y
aplica cuando seleccionamos una distribución Linux. Debe ser cómodo para
nosotros, no para los demás, debe ser fácil para nosotros, no para los demás.

Queremos que las actividades de nuestro día a día se hagan de una forma
placentera, que los tipos de inconvenientes se solucionen fácilmente y que las
labores de volver a montar la distribución desde cero si cambiamos de equipo o
si nos vemos en la necesidad de reinstalar, nos tome poco tiempo. Pero estos
detalles son detalles personales que se ajustan a la expectativa, necesidad y
experiencia de cada usuario, y estos elementos cambian en nosotros a lo largo
del tiempo, así como lo que encontramos en las distribuciones.

Esto hace que todos los puntos que anteriormente indiqué que eran posibles en
el *hardway* se cumplan en un *easyway* cuando cambias de distribución Linux.
Cada distribución Linux está diseñada para un tipo de usuario y fin específico,
y por ende ese enfoque se encuentra natural y optimizado. Pero hay tanta
variedad de usuarios y fines, que por ende, la variedad de distribuciones Linux
también es igual de amplia y saber la existencia de aquella que se ajusta como
amor a primera vista, como pareja perfecta, nos puede tomar años (para luego
cambiar de intereses e iniciar un nuevo proceso de búsqueda).

El problema es que este proceso de transición entre nuestro anterior amor y el
nuevo amor, en las distribuciones Linux, tiene un alto costo.

## Facilita la transición: *distrohopping sano*

Lo que no es habitual encontrar en las publicaciones sobre *distrohopping* es
el modo fácil de hacerlo. Incluso una vez leí sobre como hacer *distrohopping*
fácil, y el enfoque fue en las distribuciones que "permitían" esto (de alguna
forma, distribuciones sencillas de usar).

Pero si queremos probar incluso las distribuciones difíciles, ¿hay una forma
sana y simple de hacerlo?

### Evalúa tus necesidades

El primer punto que voy a resaltar, es que debemos tener clara la necesidad del
cambio. Esto nos permite saltar a una distribución con una evaluación previa de
lo que vamos a encontrar y de las capacidades que se requieren para ello. Estas
necesidades debemos tener presente que no se trata solo de las necesidades no
satisfechas, sino también de las necesidades ya satisfechas, ya que de otra
forma tenemos una alta probabilidad de hacer un salto perdiendo algo necesario.

En mi caso, mis necesidades no satisfechas son:

+ Disponibilidad de software nuevo (en esencia, del ecosistema de alternativas
  en Rust): Las podría instalar mediante compilación con *cargo*, pero esto
  aumenta el tiempo de la instalación total, en algunos casos la compilación
  genera alto esfuerzo en el equipo y comienza a calentarse mientras lo uso, y
  su integración en el sistema no es simple.
+ Disponibilidad de software actualizado: En el software popular, típicamente
  con GUI, no tengo problema con encontrar opciones en Flatpak que sean
  oficiales o con buen soporte, y que dispongan toda la funcionalidad. Sin
  embargo, para usos avanzados me ha pasado que software con GUI en paquetes
  Flatpak o Snap no exponen todas las opciones de utilidades de línea de
  comandos, o que por el nivel de aislamiento no se integran adecuadamente o
  incluso no pueden conectar con otros servicios del sistema operativo. En mi
  experiencia, también he visto mucho problema con las utilidades de línea de
  comandos o con elementos que requieran notificaciones u otros monitoreos de
  su actividad.
+ Libertad de elección en el mecanismo de instalación: Como usuario de Ubuntu y
  derivadas, mi Firefox está en _snap_. Pero muchos paquetes está vinculados
  _snap_ y esto no es claro al momento de decidir la instalación y debido a lo
  que no exponen al ser _snap_ a veces he tenido problemas. Igualmente, con los
  _snap_ ya he tenido problemas de inicialización que no suceden con sus
  versiones del repositorio oficial o incluso el equivalente en _flatpak_. Pero
  el bloqueo de _snap_ puede tener el riesgo oculto de generar otros fallos de
  integración de los cuales Ubuntu espera tener el _snap_.

Y mis necesidades satisfechas:

+ Software y controladores privativos: Sin duda, con derivadas de Ubuntu tengo
  una buena experiencia a este nivel, ya que al tener la comunidad más grande,
  es la comunidad en la cual más se enfocan las empresas al generar versión
  oficial. Ejemplo, mi experiencia con NVIDIA solo ha sido buena en Ubuntu y
  derivados (y esto me impacta en el uso de Wayland también).
+ Estabilidad: Si bien tengo experiencia en Linux y con conocimientos de nivel
  medio o avanzado, no quiero tener que solucionar problemas continuamente, y
  tener el temor a cada actualización o instalación.
+ Excelente documentación o comunidad: En caso de tener problemas, o querer
  validar información previa a probar algo, o consultar como se hace algo,
  quiero disponer de buenas opciones para consultar o preguntar. Esto se logra
  con una buena documentación del proyecto o con una comunidad muy activa o de
  buen tamaño.

Y por último, una que me genera sentimientos encontrados:

+ Soporte de *hardware*: En Ubuntu y derivados, esto ha sido un problema cuando
  cambio de equipo (generalmente, equipo nuevo). El periodo de transición para
  poderlo usar me toca típicamente quedarme en Windows porque el núcleo que
  viene no es muy actualizado, y por ende no soporta el procesador, o los
  controladores privativos no están actualizados. En general hay un buen
  soporte, pero hay que esperar hasta la siguiente liberación periódica
  (6 meses). Cuando he probado otras distribuciones en modelos de liberación
  continúa tras los cambios de equipo, tengo ese soporte, pero típicamente
  perdía el sistema a los días o semanas, o el tiempo demandado en procesos de
  instalación era alto.

Es importante que en el proceso, tengamos claro en las necesidades, cuales son
sacrificables. En mi caso, puedo perder un poco la libertad de elección del
mecanismo de elección si esta me favorece, y perder los controladores y software
privativo, si dispongo de alternativas.

Con estas necesidades claras, es posible indagar un poco en los foros, blogs y
[DistroWatch](https://distrowatch.com/), los posibles candidatos.



### Crea un entorno de pruebas o un plan de respaldo



### Crea una transición uniforme


+ No seas fanático o purista.
+ Resuelve los conflictos que realmente te generan valor.
    + Extensiones solo disponibles para VSCode y no para Code (OSS).
    + Errores de instalación con el gestor y repositorio oficial de paquetes disponibles en mecanismos más simples.
