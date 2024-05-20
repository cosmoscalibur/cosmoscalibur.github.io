
Migración

ERROR: Unknown directive type "youtube"
Para agregar videos de youtube, usaremos sphinxcontrib-youtube y se agrega como  "sphinxcontrib.youtube"

html_extra_path para definir el directorio de archivos del root (directorio files de Nikola)

ERROR: Unknown directive type "post-list"
La directiva rst de Nikola `post-list` debe reemplazarse por `postlist`, y `categories` por `category`.

ERROR: Unknown directive type "thumbnail"
La directiva thumbnail no existe, pero puede reemplazarse por figure.

La fórmula {{% thumbnail "/images/determinar-intersecciones-en-el-diagrama-de-venn-con-r/primes_even_fibo.png" %}}<p>Venn diagram generate here with VennDiagram.</p>{{% /thumbnail %}}
pasa a 
```{figure} /images/determinar-intersecciones-en-el-diagrama-de-venn-con-r/primes_even_fibo.png
:name: figure_1
:alt: Venn diagram generate here with VennDiagram.
:align: center

Venn diagram generate here with VennDiagram.
```

se debe incluir la directiva `.. post::`, seguida de la fecha o con `:blogpost: true`
También con el patrón de ruta se puede evitar usar esta opción.

.. slug: es la parte de la url, que en sphinx viene dada por el nombre del archivo.
.. status: no posee equivalente como opción en si. el estado _published_ corresponde a una fecha
pasada. Mientras que la ausencia de fecha o una fecha futura, es un borrador _draft_. _featured_
no posee equivalente directo pero puede construirse. Y _private_ no sale en el índice, así que es
suficiente con no mencionarlo como _post_.
.. previewimage: equivale a :image:, sin embargo, en lugar de la ruta es la numeración en aparición dentro
de la publicación.
.. nocomments: es :nocomments:
.. title: se convierte en título de primer nivel con ===
.. tags: -> :tags:
.. date: -> :date:
.. author, category
.. updated: no tiene conversión directa, ya que en Ablog la actualización es una anotación con su párrafo,
mientras que en Nikola es un metadato.
.. link: corresponde a :external_link:
.. type: y .. description: no poseen equivalente

Para redireccionar, con 0 segundos, ajustar post_redirect_refresh (descomentar)
y agregar :redirect: blog/con la ruta antigua (.. slug:)


disqus_shortname es el COMMENT_SYSTEM_ID si COMMENT_SYSTEM es disqus

Para las referencias cruzadas en markdown, es necesario cambiar los casos `{{% doc %}} path {{% /doc %}}` por
`<project:path>`
En el caso de rst, pasamos de :doc:`path` funciona, excepto si tenemos una etiqueta a un punto arbitrario. En ese caso
debemos usar ref y apuntar con un target al título. Si se usa un nombre personalizado, también usar ref.
Importa la ruta relativa o absoluta, no simplemente el nombre.

.. has_math: true se remuve, por defecto se soportan ecuaciones

respecto a la fecha, es necesario hacer compatible el formato. Nikola permite soportar múltiples,
pero ablog solo soporta el especificado en post_date_format. Así, removemos ` UTC-05:00` y `-05:00`

`.. TEASER_END` y `<!-- TEASER_END -->` (rst y md respectivamente), no son requeridas.
Por defecto, el primer párrafo se usará para este fin, pero si se desea usar más, se debe
ajustar con la opción de `:excerpt:` de la directiva `post`. indicando el número de párrafos.

TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}" es el patrón de nombre para las traducciones. Es recomendable
en este caso formar el patrón en el directorio
{lang}/blog/{path}.{ext}

para distinguir los metadatos de md, es la misma estructura de rst, pero de nikola a sphinx cambiamos la forma
de comentario html <!-- --> por ---
Cuando agreguemos el título, es necesario aumentar el nivel de los títulos ya existentes.

PRETTY_URLS es para que no salga html, y se convierte en por defceto en sphinx.


uv
pipenv