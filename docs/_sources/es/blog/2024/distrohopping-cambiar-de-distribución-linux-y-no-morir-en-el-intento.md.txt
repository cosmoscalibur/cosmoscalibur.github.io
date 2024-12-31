---
date: 2024-12-03
tags: distrohopping, distribución linux, ubuntu, manjaro, kde
category: tecnología, linux
---

# *Distrohopping*: Cambiar de distribución Linux y no morir en el intento

Vengo de dos cambios de distribución Linux recientes, y eso me hizo pensar un
poco en el esfuerzo asociado y en como ese esfuerzo se puede reducir.
Igualmente, recordé el concepto asociado de "*distrohopping*" y las discusiones
alrededor de esta práctica, en la cual muchos terminan afirmando que realmente
es perder el tiempo y que aporta poco valor, pero yo no lo veo así y quiero
compartirles el valor que le veo y el cómo facilitarlo.

¿Qué he probado antes?: Mandriva (descontinuada), Open Suse, Ubuntu, Debian,
Antix, Lubuntu, Antergos, Arch, Gentoo, Funtoo, Linux Mint, Xubuntu, y ahora
Kubuntu y Manjaro KDE.

En cuáles he tenido periodos estables de años: Ubuntu, Lubuntu, Linux Mint y
Xubuntu. La transición este año a Kubuntu me enamoró de KDE y se convierte en mi
escritorio (*DE*) favorito.

## ¿Es buena idea hacer *distrohopping*?

Encontrarás muchos motivos para hacer *distrohopping*, lo interesante de lo
novedoso y querer probar la distro de la cual todos hablan, o el nuevo gestor de
paquetes que va a revolucionar la instalación, el mejor manejador de
controladores privativos, tener la distro que te permite usar todo el beneficio
de tu último computador o accesorio, o incluso motivos asociados a aumentar más
tu conocimiento y experiencia sobre el mundo Linux y las distribuciones, o
generar contenido variado sobre todas las opciones disponibles, o condiciones
laborales como la distro en la cual se encuentran los servidores del servicio
que ofrecen en tu trabajo como desarrollador.

Cada una de estas, encontrarás un foro o blog que la discute, y probablemente te
terminará indicando que perdiste el tiempo y que eso no generó valor para ti, y
te recomiendan que omitas la experiencia porque ellos en sus muchos años de
*distrohopping* concluyen que no necesitas probar de todo, sino solo escoger una
desde el inicio que se ajuste a tu necesidad y quedarte allí. ¿Pero sabes algo?
A ellos saber lo que buscaban y que eso existía les tomo años.

El *distrohopping* es exactamente lo que hacemos cuando no sabemos muy bien lo
que necesitamos ni lo que existe para escoger, así que empezamos a probar. Y así
como sucede con el *smartphone*, el *smart tv*, el apartamento que tomas en
alquiler, el carro que compras o incluso el PC que compras, tus gustos y
necesidades cambian, haciendo que la decisión que tomaste ya no sea la mejor, y
está bien cambiar.

Cuando te enamoras de una distribución Linux, vas a considerar que nunca fue
necesario el *distrohopping* y que no te sirvió para lo que llegaste a
descubrir, pero es una gran mentira. Tienes los elementos de comparación porque
te atreviste a probar, sabes que existía la distribución que elegiste porque
buscabas opciones cada que encontrabas detalles que no te agradaban de la
actual. Pero así como en los enamoramientos de parejas, también perdemos el amor
porque nosotros no somos los mismos siempre, y las distribuciones Linux tampoco.
Cambian continuamente aprovechando las revoluciones tecnológicas o por sus
definiciones necesarias para el autosostenimiento o *marketing*. Incluso, las
comunidades alrededor pueden cambiar y afectar la distribución.

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
cosa que consideres). Ejemplo, no uses mucho los elementos gráficos, los botones
u atajos, usa más comandos de la consola, y así obtendrás mayor aprendizaje. No
siempre instales el software desde repositorios, de vez en cuando, anímate a
instalarlo mediante compilación o desde un directorio comprimido. No uses la
casilla de verificación o el cuadro de texto de un cuadro de diálogo para
modificar una configuración, busca el archivo de texto plano asociado a dicha
configuración (si existe, en KDE Plasma y Wayland me he encontrado muchas cosas
que si existen en un archivo de configuración, probablemente no están
documentadas y definitivamente toca por los cuadros de diálogo o opciones de la
barra de tareas, porque ni siquiera un comando asociado).

Lo que aprendes en una distribución específica, son justamente herramientas
específicas de la distribución y que por ende dicho conocimiento no es universal
o replicable, y no te será útil si cambias otra vez de distribución o si tu
amigo que usa otra distribución te pide ayuda.

### Mejor rendimiento del equipo: No

Tampoco nos aporta mayor rendimiento del equipo. En general el rendimiento lo va
a otorgar el *hardware*, el *software* para una tarea específica y el nivel de
depuración que tengamos. Todo esto se puede hacer actualizando el equipo,
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
software alternativo que optimiza el flujo que deseas más rápido (ejemplo, pasar
tu análisis de datos de Pandas a Polars o FireDucks). O considera si estás en el
límite de lo que otorga tu equipo si lleva varios años. Y sobre todo, pon mucha
atención en los servicios que se activan durante el arranque.

Aprovecha los gestores de limpieza, paquetes y procesos de tu distribución, o
usa un software de optimización y monitoreo como
[Stacer](https://oguzhaninan.github.io/Stacer-Web/).

### Software actualizado: No

Es claro que existen distribuciones con software más actualizado, esto es la
diferencia que se ofrecen entre los modelos de liberación continúa (_rolling
release_), liberación periódica (*fixed release* o *point release*) o las
liberaciones de soporte largo (LTS). Si deseamos algo muy nuevo, la preferencia
sería una liberación continúa, pero su estabilidad puede estar comprometida. Si
queremos mayor estabilidad, usaremos una LTS, pero fácilmente esto implica
retraso de años en el uso de nuevo software o de mejorar soporte de hardware. Un
punto intermedio son las liberaciones periódicas (que acorde al compromiso con
la estabilidad de las distribuciones, algunas periódicas pueden ser más o menos
lentas para actualizar paquetes, ejemplo, Ubuntu es lenta).

Sin embargo, los repositorios oficiales no son el único mecanismo para tener
software actualizado. Puedes usar fácilmente _snap_ si estás en Ubuntu o
derivados (en otras distribuciones puede no ser tan natural) o _flatpak_ (la
cual en algunas distribuciones viene preinstalado, o instalarlo). También puedes
usar los AppImage que no implican instalación en el sistema (es un tipo de
aplicación portable para Linux), aunque estas no poseen un repositorio
centralizado de gran tamaño, entonces se vuelve una gestión manual cada
AppImage. Estas opciones no solo te permiten obtener las últimas versiones (si
son las versiones oficiales), sino también omitir problemas asociados a
dependencias. Ejemplo, en Manjaro en mi equipo con tarjeta gráfica NVIDIA tengo
problemas para instalar OBS Studio con _pamac_ por una dependencia (aclaro la
tarjeta gráfica porque el problema no es replicable si lo instalo en un equipo
con tarjeta gráfica integrada), pero si uso _Flatpak_ lo tengo funcional sin
problema.

También existen opciones de instalación simples de usar a través de los gestores
de paquetes de los lenguajes de desarrollo en los cuales se implementaron.
Ejemplo, puedes instalar el emulador de terminal Alacritty en su última versión
con *cargo* (Rust) o instalar la utilidad de descarga de videos *YT DLP* con
*PIP/UV* (Python).

Y como siempre, está el *hardway*, puedes descargar el archivo *tar.gz* que
muchos suministran (ejemplo, Dropbox, y así evitar el PPA en Ubuntu) o descargar
el código fuente desde un sitio web o repositorio GitHub y manejar las
dependencias de compilación.

### Consistencia filosófica (fanatismo o purismo incluido): No

Muchos cambian o escogen una distribución por consistencia filosófica. Pero esto
realmente tampoco lo otorga.

Si no quieres software privativo, puedes desinstalarlo y buscar las
alternativas, y luego instalarlas. Si no estás de acuerdo con el uso por defecto
de Firefox como _snap_ en Ubuntu y de otros paquetes, puedes desinstalar el
software, bloquear el redireccionamiento a _snap_ de los gestores de paquetes o
tienda de software, y luego volver a instalar ya con la versión *DEB* (has
logrado el *desnapping* de Ubuntu).

Quieres tener la libertad de elección, puedes desinstalar cualquier componente e
instalar la componente que te haga sentir bien.

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

Esto hace que todos los puntos que anteriormente indiqué que eran posibles en el
*hardway* se cumplan en un *easyway* cuando cambias de distribución Linux. Cada
distribución Linux está diseñada para un tipo de usuario y fin específico, y por
ende ese enfoque se encuentra natural y optimizado. Pero hay tanta variedad de
usuarios y fines, que por ende, la variedad de distribuciones Linux también es
igual de amplia y saber la existencia de aquella que se ajusta como amor a
primera vista, como pareja perfecta, nos puede tomar años (para luego cambiar de
intereses e iniciar un nuevo proceso de búsqueda).

El problema es que este proceso de transición entre nuestro anterior amor y el
nuevo amor, en las distribuciones Linux, tiene un alto costo.

## Facilita la transición: *distrohopping sano*

Lo que no es habitual encontrar en las publicaciones sobre *distrohopping* es el
modo fácil de hacerlo. Incluso una vez leí sobre como hacer *distrohopping*
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

- Disponibilidad de software nuevo (en esencia, del ecosistema de alternativas
  en Rust): Las podría instalar mediante compilación con *cargo*, pero esto
  aumenta el tiempo de la instalación total, en algunos casos la compilación
  genera alto esfuerzo en el equipo y comienza a calentarse mientras lo uso, y
  su integración en el sistema no es simple.
- Disponibilidad de software actualizado: En el software popular, típicamente
  con GUI, no tengo problema con encontrar opciones en Flatpak que sean
  oficiales o con buen soporte, y que dispongan toda la funcionalidad. Sin
  embargo, para usos avanzados me ha pasado que software con GUI en paquetes
  Flatpak o Snap no exponen todas las opciones de utilidades de línea de
  comandos, o que por el nivel de aislamiento no se integran adecuadamente o
  incluso no pueden conectar con otros servicios del sistema operativo. En mi
  experiencia, también he visto mucho problema con las utilidades de línea de
  comandos o con elementos que requieran notificaciones u otros monitoreos de su
  actividad.
- Libertad de elección en el mecanismo de instalación: Como usuario de Ubuntu y
  derivadas, mi Firefox está en _snap_. Pero muchos paquetes están vinculados
  _snap_ y esto no es claro al momento de decidir la instalación y debido a lo
  que no exponen al ser _snap_ a veces he tenido problemas. Igualmente, con los
  _snap_ ya he tenido problemas de inicialización que no suceden con sus
  versiones del repositorio oficial o incluso el equivalente en _flatpak_. Pero
  el bloqueo de _snap_ puede tener el riesgo oculto de generar otros fallos de
  integración de los cuales Ubuntu espera tener el _snap_.

Y mis necesidades satisfechas:

- Software y controladores privativos: Sin duda, con derivadas de Ubuntu tengo
  una buena experiencia a este nivel, ya que al tener la comunidad más grande,
  es la comunidad en la cual más se enfocan las empresas al generar versión
  oficial. Ejemplo, mi experiencia con NVIDIA solo ha sido buena en Ubuntu y
  derivados (y esto me impacta en el uso de Wayland también).
- Estabilidad: Si bien tengo experiencia en Linux y con conocimientos de nivel
  medio o avanzado, no quiero tener que solucionar problemas continuamente, y
  tener el temor a cada actualización o instalación.
- Excelente documentación o comunidad: En caso de tener problemas, o querer
  validar información previa a probar algo, o consultar como se hace algo,
  quiero disponer de buenas opciones para consultar o preguntar. Esto se logra
  con una buena documentación del proyecto o con una comunidad muy activa o de
  buen tamaño.

Y por último, unas que me generan sentimientos encontrados:

- Soporte de *hardware*: En Ubuntu y derivados, esto ha sido un problema cuando
  cambio de equipo (generalmente, equipo nuevo). El periodo de transición para
  poderlo usar me toca típicamente quedarme en Windows porque el núcleo que
  viene no es muy actualizado, y por ende no soporta el procesador, o los
  controladores privativos no están actualizados. En general hay un buen
  soporte, pero hay que esperar hasta la siguiente liberación periódica (6
  meses). Cuando he probado otras distribuciones en modelos de liberación
  continúa tras los cambios de equipo, tengo ese soporte, pero típicamente
  perdía el sistema a los días o semanas, o el tiempo demandado en procesos de
  instalación era alto.
- Software preinstalado acorde a mis actividades: Esto no debe ser un criterio
  principal porque si es fácil instalarlo, lo puedo hacer, pero sin duda, si hay
  software preinstalado puedo empezarlo a usar más rápido. Además, esto evita
  tener que configurar la integración de estos paquetes.

Es importante que en el proceso, tengamos claro en las necesidades, cuáles son
sacrificables. En mi caso, puedo perder un poco la libertad de elección del
mecanismo de elección si esta me favorece, y perder los controladores y software
privativo, si dispongo de alternativas.

Con estas necesidades claras, es posible indagar un poco en los foros, blogs y
[DistroWatch](https://distrowatch.com/), los posibles candidatos.

Algunas conclusiones en el caso de mis necesidades:

- Distribución con modelo de liberación continuo: Me permite disponer de
  software nuevo y actualizado, y estoy dispuesto al monitoreo de información y
  ajustes que puede venir de algo de inestabilidad. Para compensar, se puede
  usar fuentes de *flatpak* para los software GUI, con muchas dependencias o que
  poseen fuentes inestables en el gestor tradicional. Así como usar PIP/UV, Pixi
  o Cargo para algunos paquetes cuyo uso principal sea en desarrollo en lugar de
  uso general. Esta forma de compensar ayuda a facilitar también el
  *distrohopping*, pues independiza la instalación de muchos paquetes del gestor
  de paquetes específico de la distribución.
- Evitar modelos de liberación inmutables o derivados de Ubuntu (excepto
  [Linux Mint](/es/blog/2020/instalar-paquetes-snap-en-linux-mint-20.rst)): Los
  casos inmutables recurren continuamente a usar opciones tipo aislamiento
  (*sandboxing*) como los *flatpak*, *snap* o *AppImage* para las aplicaciones
  de usuario. Esto no solo reduce la libertad de elección, sino el conjunto de
  aplicaciones disponibles. Ubuntu se descarta por su tendencia a usar *snap*
  por debajo de *apt*.
- Evitar distribuciones FOSS: Una distribución FOSS (como Fedora) no permite
  fácilmente ni soporta software privativo. Esto es un problema fuerte para el
  soporte de hardware como tarjeta gráfica NVIDIA o algunos controladores de
  WiFi, o incluso la ola de *machine learning* que hace uso de CUDA. Esto
  descarta una distribución como Fedora.
- Entorno de escritorio KDE: Algo que con el tiempo me ha pasado, es que he
  usado cada vez más software asociado a proyectos de KDE, también es común que
  muchos otros paquetes que uso se basan en Qt que es la base de KDE. Y en
  aplicaciones base, que normalmente uso poco, igual el conjunto base de KDE es
  más sofisticado (ejemplo, su herramienta de captura de pantalla y los gestores
  de configuración). El proyecto KDE posee una distribución basada Ubuntu
  llamada Neon, y acorde a múltiples sitios las mejores experiencias en KDE se
  han percibido en Kubuntu, lo cual pueden ser dos buenas opciones en caso de
  mantenerse en las familias de Ubuntu.
- Distribuciones bien documentadas y de comunidad activa: En mi apreciación,
  esto es un punto fuerte de las distribuciones Arch y Ubuntu, y por extensión a
  sus derivadas.
- Distribuciones con repositorios extensos: Si quiero que algunas de mis
  actividades diarias estén cubiertas en paquetes preinstalados o que en su
  defecto, se instalen fácilmente, lo mejor es depender de distribuciones con
  repositorios extensos. En este punto, pero solo como deseo y no un criterio
  firme, favorecemos nuevamente a Arch, Ubuntu y sus deivados. Ejemplo de
  elementos mínimos, debería tener LibreOffice y Firefox en lo preinstalado, y
  no otros procesadores de texto y navegadores. Una sorpresa es que Manjaro
  incluye git, y esto me sirve hasta para sincronizar mis *scripts* para
  instalación.

### Ten presente los problemas comunes

Hay cuatro grandes padecimientos en Linux para los cuales debes prepararte y
validar antes del cambio.

- WiFi: Fácilmente, es lo que más vas a romper con los cambios de distribución o
  posterior a una actualización de núcleo o de versión de controladores. He
  tenido equipos en los cuales el WiFi funciona perfectamente en las versiones
  *live*, pero al instalar ya la distribución, el controlador no es soportado
  directamente, o al actualizar el núcleo la versión del controlador no está
  compilada para dicho núcleo y es necesario ajustar manualmente el *header* del
  código fuente y compilarlo. En otros casos como me ocurrió en el reciente
  cambio a Manjaro, el WiFi empezó a perder las redes disponibles aleatoriamente
  después de actualizar el núcleo y fue necesario ajustes en BIOS y en archivo
  de configuración del controlador. Ten disponible una conexión cableada de red.
- Tarjeta gráfica NVIDIA: Definitivamente, un gran dolor si requieres el máximo
  aprovechamiento. En Wayland esto es una limitante en múltiples distribuciones,
  pero si es realmente importante para ti, probablemente un derivado de Ubuntu
  sea lo mejor. Algunos software que usan aceleración de video por GPU también
  se pueden ver afectados y sea conveniente omitir la aceleración, usar una
  versión *sandbox* o esperar unos meses que el soporte se logre (en mi caso,
  espero que la rama de NVIDIA 560 llegue pronto a *Manjaro Stable*). Esto me
  afecta parcialmente la experiencia en Wayland y de aplicaciones que usan para
  el renderizado Vulkan (como Zed), pero mientras uso la versión KDE X11 en este
  equipo y el equipo con tarjeta integrada funciona sin problema Wayland. En
  algunos casos, el problema puede ser tener una pantalla completamente negra o
  errores de visualización continuamente si el controlador no se soporta
  adecuadamente (nada funcional). Valida el soporte de tu tarjeta NVIDIA con las
  versiones de los controladores disponibles y de la integración de Wayland.
- Procesadores (o hardware en general) nuevos: Si la distribución no es de
  liberación continua, la versión del núcleo no será la necesaria para soportar
  un equipo de última generación, contrario a lo que sucede con tu Windows
  preinstalado. Valida si tu procesador es soportado en la versión del núcleo de
  la distribución a probar.
- Software privativo: A veces no podemos simplemente buscar una alternativa,
  porque esto no compensa que debemos interactuar con otras personas. Si esto es
  algo importante, ejemplo, para fines laborales o de estudio, seguramente tu
  transición debe implicar seguir con el uso de Windows o alternativas para las
  cuales haya versión oficial. Valida si el software existe para la
  distribución.

### Crea un entorno de pruebas o un plan de respaldo

Sin duda, las cosas pueden fallar si haces un cambio radical de distribución,
como cuando se cambia de familia de distribución. Por este motivo, es bueno ir
con pequeños pasos seguros como:

- Empieza pruebas con una máquina virtual: Puedes usar QEMU-KVM o VirtualBox.
  Esto te ayudará al primer acercamiento de instalación del sistema operativo,
  explorar rápidamente el entorno de escritorio y el flujo de adecuación inicial
  como instalar el software que sea más importante para ti y verificar que
  funciona adecuadamente. Prueba así unos días para ver la estabilidad, pero
  esto no es una victoria, debido a que en la emulación no tienes el mismo
  hardware.
- Al pasar al hardware real, sería preferible mantener una partición para el
  nuevo sistema mientras que conservas otra para la anterior. En caso de fallo,
  puedes retomar tu trabajo y actividades en la distro anterior.
- Documenta o crea *scripts* de los pasos realizados. Esto será importante
  cuando requieras de una instalación desde cero nuevamente o replicar en otra
  máquina.
- En la medida que ya sea tu distribución diaria, crea respaldo de tus datos
  (documentos y otros archivos personales), así como de archivos de
  configuración. Aprovecha servicios de sincronización como Drive, Dropbox o
  GitHub. También puede ser mantener copias en un disco externo o tener una
  partición para el directorio `/home`.
- Considera tener un núcleo estable instalado en las distribuciones de
  liberación continúa. De esta forma, puedes pasar a este núcleo en caso de
  fallo.

### Crea una transición uniforme

**Instalación de paquetes**

Una opción rápida para enfocarte en los verdaderos problemas que pueden existir
en la distribución que has escogido, es depender menos del gestor de paquetes de
la distribución. Esto te permite documentar o tener *scripts* que serán
replicables en un eventual nuevo cambio y a reducir el impacto de buscar como
adecuar tu sistema.

**Entorno de escritorio**

Explora los entornos de escritorio en la distribución Linux que ya usas. Esto te
facilitará explorar el comportamiento visual y de las herramientas de gestión
generales y aplicaciones básicas con bajo esfuerzo y bajo riesgo. Una vez tengas
claro el entorno de escritorio, busca la nueva distribución con este entorno de
escritorio. En mi caso, pude explorar KDE a través de Kubuntu (variante de
Ubuntu) y así notar que se ajustaba a mi interés por sobre otros entornos.
Luego, esto me lleva a solo evaluar respecto a las distribuciones que tengan
soporte adecuado de KDE.

**Internet cableado y WiFi**

Recuerda que ante posibles problemas del controlador de WiFi, siempre es bueno
poder contar con una conexión cableada.

## Despedida

Espero que esto te ayude a lanzarte a tu nueva aventura en Linux con confianza.

Actualmente estoy usando Manjaro KDE y estoy encantado con las configuraciones y
aplicaciones predefinidas de KDE. ¡Es como tener un escritorio personalizado
listo para usar desde el primer momento! Además, tener git y flatpak
preinstalados es una gran ventaja.

¡Disfruta tu viaje por las distros!
