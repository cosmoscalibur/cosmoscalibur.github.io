Inicializar el blog

```
ablog start
```

Responder las preguntas

```
> Root path for your project (path has to exist) [.]:
> Project name: Blog Cosmoscalibur
> Author name(s): Edward Villegas
> Base URL for your project: https://www.cosmoscalibur.com/
```

Enter en el directorio, deja el directorio actual.
El nombre del proyecto, por defecto ya incluye _Blog_ al final del nombre
asignado. Si es en inglés, está bien, de otra forma lo modificaremos en `conf.py`.
Variables: `project`, `blog_title`.

.nojekyll
Además, cambiar _templates y _static por las versiones sin guion bajo

html_title y html_short_title

Por defecto el tema es _alabaster_. Esto se encuentra tanto en el bloque de importaciones
como en las líneas de configuración.
En `html_theme` vamos a configurar `pydata_sphinx_theme`. Las demás menciones de _alabaster_, vamos a retirar las líneas.

Creamos directorio es para internacinalizacion con español

Crearemos el directorio `blog/` para nuestras publicaciones. Buscamos en `conf.py` la variable `blog_path` (comentada) y debajo podemos ubicar

```
blog_post_pattern = "*/blog/*/*"
```
De esta forma, todo archivo con este patrón (cualquier archivo en cualquier directorio de _blog_) es reconocido como publicación, y no es necesaria la etiqueta en el archivo.
Adicional a esto, el patrón corresponde a una forma habitual para manejar el archivo de publicaciones, basado en año (los subdirectorios son los años).

Para redireccionar hay varias opciones
redirect https://github.com/sphinx-contrib/redirects - recomiendan rediraffe
reredirect https://documatt.com/sphinx-reredirects/
rediraffe https://github.com/wpilibsuite/sphinxext-rediraffe

Añadimos rediraffe en las extensiones como `"sphinxext.rediraffe"`
En la configuración es un diccionario que mapea ruta de archivo vieja a nueva (incluyendo sufijo/extensión).
rediraffe_redirects
Basado en https://chrisholdgraf.com/blog/2022/sphinx-redirects-folder/, se establece el redireccinamiento


Para algunos nuevos elementos estilizados, usamos la extensión "sphinx_design".

Con el fin de soportar Myst Markdown, usaremos la extensión de "myst_parser", y con el soporte de notebook usaremos "myst_nb"
(https://docs.readthedocs.io/en/stable/guides/jupyter.html#background). Podemos instalar jupyterlab_myst para ofrecer el uso de myst
directamente en notebook y facilitar la edición.

Añadimos configuración para myst (habilitar extensiones y anchor).


Errores
```
cargando traducciones [es]... hecho
WARNING: mientras configura la extensión myst_nb: el rol 'sub-ref' ya está registrado, ese se reemplazará
WARNING: mientras configura la extensión myst_nb: la directiva 'figure-md' ya está registrada, esa se reemplazará

Extension error:
Valor de configuración 'myst_commonmark_only' ya presente
```

Se resuelve añadiendo primero la extensión de myst_nb

Extension error:
source_suffix '.md' is already registered

se resuelve removiendo del listado myst_parser, ya que es activado por myst_nb

Incluiremos open graph metadata con sphinxext-opengraph y se añade a la extensiones como "sphinxext.opengraph".
Añadimos la configuración de opengraph
ogp_site_url = "https://www.cosmoscalibur.com"

Tendremos el directorio de plantillas
templates_path = ["_templates"]
y añadiremos las exclusiones (archivos que no se procesan)

exclude_patterns = ["_build", "**/.ipynb_checkpoints/*"]
_build es el directorio generado en la compilación

Cambiamos el lenguaje del proyecto language = "es"

ERROR: Unknown directive type "youtube"
Para agregar videos de youtube, usaremos sphinxcontrib-youtube y se agrega como  "sphinxcontrib.youtube"


html_theme_options debe ajustarse según el tema. En pydata no está el botón de github
WARNING: opción de tema no soportada 'github_button' fue dada
html_theme_options = {
    'github_button': False,
}

html_extra_path para definir el directorio de archivos del root (directorio files de Nikola)

ERROR: Unknown directive type "post-list"
La directiva rst de Nikola `post-list` debe reemplazarse por `postlist`, y `categories` por `category`.

ERROR: Unknown directive type "thumbnail"
La directiva thumbnail no existe, pero puede reemplazarse por figure.

Nuestro directorio de imágenes va al mismo nivel del raíz del proyecto, y con esto se puede ubicar sin problema.

Para las referencias cruzadas en markdown, es necesario cambiar los casos `{{% doc %}} path {{% /doc %}}` por
`<project:path>`
En el caso de rst, pasamos de :doc:`path` funciona, excepto si tenemos una etiqueta a un punto arbitrario. En ese caso
debemos usar ref y apuntar con un target al título. Si se usa un nombre personalizado, también usar ref.
Importa la ruta relativa o absoluta, no simplemente el nombre.

.. has_math: true se remuve, por defecto se soportan ecuaciones

La presentación inicial del blog, se construye en el archivo `index.rst`. Allí de paso, corregimos el texto
de bienvenida genérico.

La fórmula {{% thumbnail "/images/determinar-intersecciones-en-el-diagrama-de-venn-con-r/primes_even_fibo.png" %}}<p>Venn diagram generate here with VennDiagram.</p>{{% /thumbnail %}}
pasa a 
```{figure} /images/determinar-intersecciones-en-el-diagrama-de-venn-con-r/primes_even_fibo.png
:name: figure_1
:alt: Venn diagram generate here with VennDiagram.
:align: center

Venn diagram generate here with VennDiagram.
```

Añadimos el contexto html, que es información relacionada con GitHub
html_context = {
    "github_user": "cosmoscalibur",
    "github_repo": "cosmoscalibur.github.io",
    "github_version": "master",
    "doc_path": "docs",
}


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

Descomentar post_date_format y ajustar formato = '%%Y-%%m-%%d %%H-%%M-%%S' y
Para redireccionar, con 0 segundos, ajustar post_redirect_refresh (descomentar)
y agregar :redirect: blog/con la ruta antigua (.. slug:)
rediraffe
https://chrisholdgraf.com/blog/2022/sphinx-redirects-folder/

disqus_shortname es el COMMENT_SYSTEM_ID si COMMENT_SYSTEM es disqus

respecto a la fecha, es necesario hacer compatible el formato. Nikola permite soportar múltiples,
pero ablog solo soporta el especificado en post_date_format. Así, removemos ` UTC-05:00` y `-05:00`

probar
ablog clean && ablog build && ablog serve

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

Referencias
https://chrisholdgraf.com/blog/2020/sphinx-blogging/
https://www.errbufferoverfl.me/posts/2020/sphinx-blog/
https://www.errbufferoverfl.me/posts/2020/sphinx-blog-part-one/
https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/ablog.html
https://ablog.readthedocs.io/en/stable/manual/ablog-quick-start.html

