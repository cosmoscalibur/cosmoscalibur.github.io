:redirect: blog/reformas-del-blog-parte-1
:date: 2020-05-26
:tags: blog, nikola, amazon, disqus, facebook, comentarios, publicidad, adsense
:category: tecnología
:author: Edward Villegas-Pulgarin

Reformas del blog: Parte 1
==========================

Bueno, he estado en múltiples ocasiones por escribir sobre mantener un blog, y
hoy fue el caso, pero centrado en unas actualizaciones que he hecho para
mejorar la experiencia de los lectores que usan su celular y deben soportar
altos tiempos de carga y una alta descarga en imágenes cuando las contiene.

Esto puede no ser válido para todos, pero resulta de mi experiencia particular
y, bajo la condición de tener un sitio generado de forma estática con Nikola
y alojado en GitHub. He planteado parte 1 porque pretendo hacer unas reformas
adicionales más adelante.

PageSpeed
---------

Antes que nada esto surge porque estuve haciendo seguimiento a las métricas de
la herramienta PageSpeed [ps_] que ofrece Google integrada a su plataforma de
Analytics (puedes usar de forma local con Lighthouse [lh_]). El análisis
entrega no solo métricas sino también algunas recomendaciones y por ello
procedí a ponerme en ello (dado que la mayor parte de mis lectores usan su
celular).

Sistema de comentarios
----------------------

Si bien pensar en una forma de interacción directa con los lectores del blog
es importante, se debe evaluar en el tiempo su impacto. En el caso de mi blog,
la cantidad de comentarios durante su historia lo hace despreciable cuando
contrasto con la penalización en el tiempo de carga que ha introducido el
sistema de comentarios.

Disqus [dqs_] es un sistema de comentarios importante, permite socializar y asocia un
perfil de los lectores y los generadores de contenido, lo cual permite también
generar tráfico, pero en mi caso tampoco representa una fuente de tráfico
importante ni de una contribución que quiera considerar.

Esto me llevó inicialmente a pensar en eliminar el sistema de comentarios,
pero también cuando veo como las publicaciones pueden tener mayor impacto en
redes sociales y que Facebook ofrece su sistema de comentarios [fb-comments_],
no veo descabellado cambiar. La mayor parte de mis lectores poseen Facebook y
el tráfico a razón de Facebook hoy es el mayor entre las fuentes de tráfico
sociales. Reduce el bloqueo de 800 ms a 400 ms.

.. update:: 2020-06-29 12:00:00

   Por alguna razón el *plugin* de comentarios de Facebook dejó de funcionar y además observo una caída abrupta en
   la analítica de visitas de Facebook que no se verifica con Google. Me da mala espina Facebook y retorno a Disqus.

Es necesario revisar como permitir el modo de carga asíncrono de Disqus que sea
compatible con Nikola.

Publicidad
----------

El blog no ha tenido publicidad, pero hace un tiempo he venido revisando el
tema de monetizar el blog. La idea es hacerlo de una forma no invasiva pero
sin muchas complicaciones para mi también.

Es así como Google AdSense [gads_] por sus procesos de validación y la
penalización que he sufrido en tiempo de carga por la adición en el código no
me parece prudente. Adicional, no puedo asegurar que la publicidad mostrada
sea realmente acorde al blog (así pueda serlo para el lector).

Por ello, he decido probar las opciones estáticas del programa de asociados de
Amazon [amz_]. No hay generación dinámica, ni selección de la posición óptima
de la publicidad, pero puedo decidir que promocionar en mis publicaciones,
ubicarla donde considere que no afecta la lectura o que genere confusión y que
además aporte realmente al lector que llega a mi publicación (por ejemplo,
recomendando un libro sobre el tema de la publicación).

Es posible que no sea permanente, pero quiero probarlo. El programa de
asociados también tiene unos tiempos máximos permitiendo publicidad sin
generar conversiones. Con este cambio, el bloqueo por la presentación de
publicidad pasó de 350 ms a menos de 40 ms.

.. update:: 2020-06-29 12:00:00

   Al no ser de generación dinámica resulta de difícil mantenimiento generar recomendaciones
   de publicidad acorde al lector que llega a una publicación. El trabajo manual de usar producto
   por artículo para hacerlo más acorde ha sido incómodo y un único producto genérico insertado
   en la plantilla posee bajo impacto. He decidido esperar que llegue mi código de Google AdSense.
   Tal vez la opción de Amazon sea muy buena para quienes directamente recomiendan productos.

Imágenes
--------

Con el fin de reducir la descarga y tiempo asociado a las imágenes, decidí
respaldar imágenes en el repositorio y usar la opción de thumbnail de Nikola
[thumb_]. Esto permite usar una versión de tamaño reducido para los artículos
pero que vincula a la imagen original (la cual puedo optimizar también).

Esto tiene una ventaja adicional, y es asegurar la existencia de las imágenes
para el futuro sin depender de la fuente original (la cual, en la medida de lo
posible mantendré referencia) y en un futuro puede permitir opciones de
servido por CDN (una opción tentadora es Statically [cdn_]), imágenes
optimizadas [opt_, tools_] como el uso del formato webp
[webp_, caniuse_, fallback_], tamaños diferentes por dispositivo
[picture-media_] y carga diferida [defer_, lazy_]. Este cambio permitió ver
en el artículo más crítico (:doc:`/es/blog/2013/cosmogonia-griega`) notar una reducción del
tamaño de archivos descargados (se compara el tamaño potencial de reducción de
las imágenes respecto a su peso en webp).

Debo decir que respecto a la conservación de las imágenes, una de las imágenes
la fuente no se encontraba disponible y fue necesario buscar su reemplazo
(sucedió con :doc:`/es/blog/2011/cerebro-prehistorico`).

Referencias
-----------

.. [ps] PageSpeed Insights https://developers.google.com/speed/pagespeed/insights/
.. [lh] Auditar apps web con Lighthouse https://developers.google.com/web/tools/lighthouse/
.. [dqs] Disqus https://disqus.com/
.. [fb-comments] Comments Plugin (Facebook) https://developers.facebook.com/docs/plugins/comments/
.. [gads] Google AdSense https://www.google.com/adsense/start
.. [amz] Amazon Associates https://affiliate-program.amazon.com/
.. [thumb] Thumbnails, The Nikola Handbook https://getnikola.com/handbook.html#thumbnails
.. [cdn] Statically https://statically.io/
.. [opt] Efficiently encode images https://web.dev/uses-optimized-images/
.. [webp] Serve images in next-gen formats https://web.dev/uses-webp-images/
.. [caniuse] Can I use webp? https://caniuse.com/#search=webp
.. [defer] Defer offscreen images https://web.dev/offscreen-images/
.. [lazy] Lazy load offscreen images with lazysizes https://web.dev/codelab-use-lazysizes-to-lazyload-images/
.. [fallback] Using WebP Images with Fallback https://usefulangle.com/post/114/webp-image-in-html-with-fallback
.. [tools] ImageOptim for various platforms https://imageoptim.com/versions
.. [picture-media] <picture>: The Picture element, MDN https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture