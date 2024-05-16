---
date: 2024-05-16
tags: blog, sphinx, python, ablog, pydata, sitio estático
category: tecnología
author: Edward Villegas-Pulgarin
---

# Crear un blog con Sphinx

Por fin he dado el paso de retomar el blog, y con ello un proceso de migración
que deseaba, generar el blog con Sphinx. Sobre este proceso les estaré contando
en varias entradas, ya que la migración no la he concluido, y esta es la primera
entrada al respecto, con lo más básico para iniciar y no fracasar en el intento.

## ¿Por qué Sphinx?

Sphinx es un generador estático de documentación, casi el estándar para los
proyectos desarrollados en Python, y para el cual se dispone de una buena cantidad
de extensiones que nutren a este generador, entre las cuales, encontramos incluso
una para convertir nuestro proyecto en un blog, y es Ablog.

Dado que mi lenguaje de programación principal es Python, es claro que por ello
quiero una opción basada en Python. Pero antes yo usaba Nikola, que también está
desarrollado en Python, pero Sphinx da el beneficio de una comunidad mayor y más
activa (como usuarios y desarrolladores). Adicional a esto, el desarrollo de Sphinx
y sus extensiones va más a la par de cambios en el ecosistema, y más alineado con
las directivas de docutils. En los cambios del ecosistema, me parece interesante como
el soporte de Jupyter Notebooks y Myst resulta muy natural, por lo cual entradas sobre
código pueden tener un beneficio, y Myst expande las opciones de Markdown (y no es
soportado adecuadamente en Nikola, ni en otros generadores que revisé).

También resulta que ya era más familiar con [Sphinx](project:/es/blog/2020/crear-documentacion-de-un-proyecto-python-con-sphinx.rst),
pero en el momento que pasé a un generador estático, no existía Ablog para ayudar
en el proceso de usarlo para un blog.

## Creando el blog

Bueno, hora de poner manos a la obra. Para ello vamos a seguir el paso a paso.

### Dependencias

Usaremos Sphinx para la generación del contenido estático y Ablog nos permitirá
incluir etiquetas para fechas, que son la diferencia esencial para distinguir una
página de una publicación (y con ello, opciones de filtros para índices).

Respecto a la apariencia, podemos encontrar distintos temas, pero yo me he
inclinado por PyData (que además usan varios blogs que sigo, así que he visto su
resultado y tengo como indagar como usan algunas cosas). Adicional, conviene
agregar Sphinx Design para añadir componentes adicionales como cuadrículas, pestañas,
tarjetas y otros.

Sin duda (y ya lo usaba en Nikola), es necesario disponer de videos de Youtube,
así que necesitamos Sphinx Contrib Youtube.

Aunque para compartir en las redes no necesitamos nada especial, poder contar
con la generación de metadatos adecuada nos ayudará a una mejor indexación y
una mejor previsualización. Para este fin usamos Sphinx Ext OpenGraph (que no
solo incluye el protocolo OpenGraph, sino una etiqueta extra para _Twitter Card_).
En este caso, tenemos un detalle extra, y es que para generar las imágenes que se
comparten (ya que por defecto no usa la primera imagen de la publicación y no
siempre hay una), es necesario instalar Matplotlib.

Y finalmente, para dar soporte de Markdown, usaremos Myst Parser. Algo
interesante es que en extensión con Myst NB, tendremos el soporte para generar
publicaciones en Notebook usando MystMd (así que instalamos también Jupyterlab).
Esto me encanta, porque será natural publicar notas sobre código con sus resultados.

Sitemap genera el sitemap del sitio, aunque para usarlo con el esquema de
internacionalización que deseo, tendré que cambiarlo en el futuro.

Copy button nos ayudará a crear la opción de copiar al portapapeles los blqoues
de código.

Con estos detalles, nuestro archivo `requirements.txt` lucirá de la siguiente forma:

```
# Generación estática blog
sphinx
ablog

# Tema y componentes
pydata-sphinx-theme
sphinx-design
sphinx-copybutton

# Mostrar Youtube
sphinxcontrib-youtube

# Metadatos para compartir en redes
sphinxext-opengraph
matplotlib
sphinx-sitemap

# Soporte de Markdown y Notebook
myst-parser
jupyterlab
myst-nb
```

:::{dropdown} Opcionales
No todo se trata sobre la generación del contenido a nivel automático, también
necesitamos apoyo mientras escribimos. Así que podemos instalar doc8, rstcheck
y esbonio, para las validaciones de nuestros archivos `.rst` y Jupyterlab Myst,
para ayudar en el renderizado en el Notebook mientras redactamos.

Siendo así, podemos tener nuestro archivo `requirements-dev.txt` así:

```
jupyterlab_myst
rstcheck
doc8
esbonio
```

Si usamos además VSCode, vale la pena las siguientes extensiones:

- MyST-Markdown: Para editar MystMD
- Esbonio: Para editar RST
- reStructuredText (lexstudio): Para editar RST
- Jupyter: Para manipular notebooks
- Emoji: Para insertar emoji con la paleta de comandos 😀
- Spell Right: Para corrección de ortografía.
:::

:::{dropdown} Otros
Bueno, aquí hay algunas extensiones que, posiblemente puedan ser útiles, pero
para mí no lo fueron:

- sphinxext-rediraffe: Con seguridad hay que tenerla a la mano. Es la extensión
  que más recomiendan para hacer redireccionamiento. En mi caso, no necesito
  todavía opciones avanzadas, así que me basta con la opción de las publicaciones
  de `:redirect:`.
- sphinx-intl: Ayuda a la internacionalización. Sin embargo, no lo considero
  adecuado en proyectos como un blog, en el cual no necesariamente todas las
  entradas poseen traducción o podrían tener contextos que hagan que su
  traducción no sea completa. Me parece adecuado para documentación, no para un
  blog.
:::

### Configuración

Puedes usar `ablog start` y responder las preguntas básicas de inicialización

```
> Root path for your project (path has to exist) [.]:
> Project name: Blog Cosmoscalibur
> Author name(s): Edward Villegas-Pulgarin
> Base URL for your project: https://www.cosmoscalibur.com/
```

Dado que GitHub Pages solo puede usar el directorio `docs/` para los sitios
estáticos, conviene dejar como raíz del proyecto el directorio raíz del
repositorio (si estás usando un repositorio git), para que el directorio de
salida este en dicho nivel.

Respecto al nombre del proyecto, por defecto este incluirá la palabra _blog_ al
final del nombre que disponemos (en inglés estaría perfecto). Pero también
encontraremos que el nombre HTML contiene la mención a _documentation_, que no
es apropiado para nuestro blog. Ajustaremos esto en las siguientes variables:

```python
project = 'Blog Cosmoscalibur'
blog_title = 'Blog Cosmoscalibur'
html_title = 'Blog Cosmoscalibur'
html_short_title = 'Cosmoscalibur'
```

Respecto al tema, por defecto Ablog configura Alabaster, pero como les indiqué,
usaremos el tema de PyData y podemos retirar alabaster del _import_.

```python
html_theme = 'pydata_sphinx_theme'
```

Para incluir los metadatos de OpenGraph, añadiremos la dirección base.

```python
ogp_site_url = 'https://www.cosmoscalibur.com'
```

Para configurar el idioma por defecto, usamos la variable respectiva con el
código ISO del lenguaje

```python
language = 'es'
```

En mi caso, aunque es mi lengua nativa, espero publicar algunas veces en inglés.
Por este motivo, pensando en la internacionalización del blog, dispondré de un
patrón de rutas de la forma `<lang>/blog/<year>/<post>`, de tal forma que con
cambiar directamente el segmento de `<lang>` se acceda a la versión del otro idioma.

Esto tiene impacto en la variable `blog_path_pattern` que permite definir el
patrón de ruta para que se reconozcan automáticamente las publicaciones (no es
necesario añadir la etiqueta).
Adicional, es necesario definir la ruta para el archivo de publicaciones.

```python
blog_path = 'blog'
blog_post_pattern = '*/blog/*/*'
```

Es necesario configurar también otros directorios y archivos. Para fines de
facilidad en GitHub Pages, vamos a remover el guion bajo de los directorios
destinados para los estáticos y las plantillas (por defecto son ignorados si
comienzan de esta forma). Y añadiremos un directorio especial que nos permita
agregar archivos directamente al raíz del despliegue (por ejemplo, para añadir
el archivo CNAME).

Importante para la generación con GitHub Pages, el directorio de salida debe
ser `docs`.

```python
templates_path = ['templates']
html_static_path = ['static']
html_extra_path = ['files']
ablog_website = 'docs'
```

Ahora vamos a definir los archivos que no deben ser procesados. Esto es
importante porque al estar el directorio de Sphinx al mismo nivel del
directorio del repositorio, se ven todos los archivos. Adicional a esto, hay
archivos generados por Sphinx que si no los borramos, en un despliegue posterior
se intentarán procesar.

```python
exclude_patterns = [
    "_build",
    "***/.ipynb_checkpoints/*",
    'Pipfile',
    'LICENSE',
    'README.md',
    'requirements*.txt',
    '.vscode',
    '.venv',
    'docs',
    '.doctrees',
    '.gitignore',
]
```

Para habilitar las extensiones que vamos a usar, es necesario listarlas en
`extensions`. Un detalle es que, aunque tenemos instalado Myst Parser, no lo
añadimos explícitamente porque genera conflicto por ya estar definido dentro
de Myst NB.

Algunos errores que se producen por esto son:

```
WARNING: mientras configura la extensión myst_nb: el rol 'sub-ref' ya está registrado, ese se reemplazará
WARNING: mientras configura la extensión myst_nb: la directiva 'figure-md' ya está registrada, esa se reemplazará
Extension error:
Valor de configuración 'myst_commonmark_only' ya presente
---
source_suffix '.md' is already registered
```

Así, entonces definimos

```python
extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    "myst_nb",
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinxcontrib.youtube",
    'ablog',
    'sphinx_sitemap',
    'sphinx_copybutton'
]
```

Los dos primeros casos que habilitamos, son extensiones que vienen por defecto,
y nos servirán para acortar la notación de URL y para enlazar cómodamente con
otros proyectos de Sphinx (en futuras entradas lo revisaremos).

Ahora que tenemos habilitado Myst NB, podemos remover la línea de `source_suffix`
porque esta es configurada por la extensión, y el valor por defecto evita que se
compilen los archivos Markdown.

Respecto a las opciones de Myst, vamos a habilitar de momento tres extensiones,
que nos permitan usar más fácilmente las directivas (no usar el _backtick_),
hacer sustituciones y habilitar el símbolo de dólar para las ecuaciones. adicional,
vamos a crear referencias (_targets_) para los títulos hasta de tercer nivel
(h1, h2 y h3).

:::{code} python
myst_enable_extensions = ['colon_fence', 'substitution', 'dollarmath']
myst_heading_anchors = 3
:::

De la misma manera, espero que en la tabla de contenidos de la derecha, se
muestren los títulos de tercer nivel. Para esto debemos ajustar las
configuraciones del tema.

Nuestro identificador de Google Analytics también se dispone en esta misma
parte (PyData soporta también Plausible).

También podemos agregar nuestros enlaces de Twitter y GitHub en la
configuración del tema.

:::{code} python
html_theme_options = {
    'show_toc_level': 2,
    'analytics': {
        'google_analytics_id': 'G-XXXXXXXXXX'
    },
    'twitter_url': 'https://twitter.com/cosmoscalibur',
    'github_url': 'https://github.com/cosmoscalibur/',
}
:::

Respecto a los paneles laterales, haremos la siguiente configuración de momento

:::{code} python
html_sidebars = {
    'index': [],
    "blog": ["ablog/categories.html", "ablog/archives.html"],
    "*/blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}
:::

No te preocupes, en otra entrada lo explicaré. De momento tomaré un por defecto,
ya que estos paneles en caso de requerir personalización, necesitamos hacer HTML
y quiero pensar bien que poner cuando no sean entradas de blog (en los cuales
los casos dispuestos me parecen perfectos).


También podemos incluir los íconos de Font Awesome {fa}`rocket` con 
:::{code} python
fontawesome_included = True
:::

Debo decir que no me gusta la idea de habilitar que se muestre el código fuente
de la publicación desde el sitio mismo, pues eso genera copia de los archivos en
el directorio de salida duplicando estos. Si alguien lo desea ver, considero que
para eso es el repositorio. Así que lo deshabilitamos.

:::{code} python
html_show_sourcelink = False
:::

Ahora, la configuración para las publicaciones.
Necesitamos ahora definir el formato de la marca de tiempo, y podemos definir
a nuestro gusto (pero debe ser consistente para esta opción en todas las
publicaciones). También podemos indicar cuántos párrafos serán usados en la
descripción y cuál imagen considerar para la previsualización. Finalmente, en
caso de tener redireccionamiento, el tiempo en segundos para su ejecución.

:::{code} python
post_date_format = '%Y-%m-%d'
post_auto_excerpt = 1
post_auto_image = 1
post_redirect_refresh = 0
:::

Ahora vamos a habilitar que los _feeds_ tengan texto completo para que puedan
ser consumidos de forma completa por los lectores de este formato.

:::{code} python
blog_feed_fulltext = True
:::

Es importante configurar nuestra generación del _sitemap_ para ayudar a los
motores de búsqueda.

:::{code} python
sitemap_url_scheme = '{link}'
html_baseurl = 'https://www.cosmoscalibur.com/'
:::

Finalmente, y aunque no es lo último que pienso configurar (pero serán temas
de otras entradas), los comentarios por Disqus (aunque estoy considerando
cambiarlo, pero también será tema de otra entrada).

:::{code} python
disqus_shortname = 'XXXXXXX'
:::

### Archivos y directorios extras

Dentro de la configuración (`conf.py`), añadimos el directorio `files`. Este
directorio nos permite añadir archivos directamente al directorio raíz del
sitio generado. Esto es importante porque algunas validaciones requieren archivos
en esta posición, como lo son:

- `CNAME`: Para la validez de nuestro nombre de dominio.
- `.nokekyll`: Para que GitHub ignore que es compilado por Jekyll. Si no hacemos
   esto, los directorios y archivos que inician por guion bajo se ignoran.
- Archivo de Google Site verification: para demostrar propiedad de dominio ante
  Google.
- Otros archivos de verificación de propiedad.
- Archivo de `robots.txt`.

También si usamos un directorio a nivel de raíz del repositorio, este quedará disponible
a este nivel. Este es mi caso con el directorio de `images` para las imágenes que uso.

### Primera publicación

Ablog nos ayudó generando en la inicialización, unos archivos de demostración.
Puedes editarlos y disponerlos en la ubicación que consideres.

El caso de `index.rst`, es necesario disponerlo en la ubicación generada para la
compilación del proyecto.

También nos crea una publicación por defecto. Esta podemos moverla a nuestro
directorio `es/blog/2024` (dado el año de elaboración) y allí editar.

Es importante tener presente que el título de primer nivel es el título de la
publicación (en otros generadores, el título se añade como parte de una directiva).
Como ya configuramos el patrón de ruta de las publicaciones, y la estamos cumpliendo,
no es necesario seguir las directivas sino el _front matter_, ejemplo:

:::::{tab-set}

::::{tab-item} RST
:::{code} rst

:redirect: blog/configurar-retroarch-en-steam
:date: 2021-12-14
:tags: steam, retroarch, libretro, gaming, linux, controles, videojuegos, emuladores
:category: tecnología/videojuegos
:author: Edward Villegas-Pulgarin
:::
::::

::::{tab-item} MD
:::{code} md

---
date: 2024-05-14
tags: blog, sphinx, python, ablog, pydata
category: tecnología
author: Edward Villegas-Pulgarin
---
:::
::::

:::::

La sintaxis ya propia de MD y RST la puedes consultar. No es difícil.

### Generación

Estamos listos, así que generemos el sitio.

:::{code} bash
ablog clean && ablog build && ablog serve
:::

La parte de `ablog clean` es necesaria si queremos una compilación completa,
ya que esto borra los temporales generados para evitar recompilar todo. Con
`ablog serve` se abrirá el navegador y podremos explorar.

## ¿Y ahora qué?

Pues te cuento que ahora sigue empezar a escribir en el blog. Pero también nos
queda algo de exploración todavía.

De mi parte, algunos detalles que quiero próximamente

- Barra de búsqueda basada en Google.
- Soporte de internacionalización basado en directorio manual y no en `pot`.
- Soporte de _sitemap_ con internacionalización con el esquema anterior.
- Vincular con otros external links, no solo github y twitter (ejemplo, mastodon).

## Referencias

- [Sphinx blogging](https://chrisholdgraf.com/blog/2020/sphinx-blogging/)
- [Sphinx blog](https://www.errbufferoverfl.me/posts/2020/sphinx-blog/)
- [Sphinx blog part one](https://www.errbufferoverfl.me/posts/2020/sphinx-blog-part-one/)
- [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/)
- [Ablog](https://ablog.readthedocs.io/en/stable/manual/ablog-quick-start.html)
- [Sphinx Redirects Folder](https://chrisholdgraf.com/blog/2022/sphinx-redirects-folder/)
- [Sphinx Myst Markdown](https://jdsalaro.com/cheatsheet/sphinx-myst-markdown/)
- [Myst Parser](https://myst-parser.readthedocs.io/en/latest/)
