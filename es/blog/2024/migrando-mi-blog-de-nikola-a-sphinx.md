---
date: 2024-05-24
tags: sphinx, python, ablog, pydata, página web estática, blog con sphinx
category: tecnología
---

# Migrando mi blog de Nikola a Sphinx

Migrar de un generador estático a otro no es un proceso del todo transparente,
así que aquí te explico algunos por menores para hacer una migración de Nikola a
Sphinx.

Pero antes, es necesario tener presente, que lo básico del proceso de migración,
inicia por tener lo mínimo desde cero, con Sphinx. Para este fin, debes seguir
las indicaciones dadas en <project:/es/blog/2024/crear-un-blog-con-sphinx.md>.

## Migrando

Bueno, una vez tenemos la base de nuestro blog, sigue hacer los ajustes para que
nuestras entradas previas sigan funcionando.

### Publicación

#### Front matter

Dado que en la configuración inicial añadimos un [patrón de ruta](#blog-conf)
para las publicaciones, no es necesario agregar la directiva de `..post:` o el
atributo de `:blogpost: true`. Solo ubica los archivos en la ruta que cumpla el
patrón 👀.

Importante, en Nikola definíamos la ruta de navegación mediante el `..slug:`,
pero esto en Sphinx depende del nombre del archivo y su ruta en el directorio.
Asegurate de usar la misma ruta de directorios al definido en el _slug_ y el
nombre del archivo igual a la parte final de este 👀. Otra opción, es que sin
importar el nombre y ruta de directorios, uses el valor del _slug_ como valor de
`:redirect:` (en este caso, añade al archivo de configuración
`post_redirect_refresh=0`).

Para indicar el título en _Nikola_, se usaba el atributo de `.. title:`, pero
ahora este debe ser explícito en la marcación de la publicación. Ejemplo:

`````{tab-set}

````{tab-item} RST
```{code} rst

Migrando mi blog de Nikola a Sphinx
===================================
```
````

````{tab-item} MD
```{code} md

# Migrando mi blog de Nikola a Sphinx
```
````

`````

Esto hace que los títulos ya existentes, deban aumentar de nivel 👀.

En _ablog_ no tenemos el equivalente del `..status:` de Nikola, pero se puede
controlar que una fecha actual o pasada sea equivalente a `published` y si es
una fecha futura o sin fecha es el equivalente de `draft`. El caso del `private`
podríamos hacerlo [excluyendo el archivo](#exclude-files). El caso `featured` es
más personalizado, pero se podría explorar con el objeto de las _cards_ en el
índice.

Si queremos indicar la imagen de previsualización, en Nikola se usaba
`.. previewimage:`, pero en _ablog_ lo hacemos con `:image:` y el valor no es la
ruta de la imagen, sino el número asociado en orden de aparición en la
publicación. Esto se puede dejar con un valor por defecto acorde a la variable
en el archivo de configuración de `post_auto_image`.

El atributo de `.. description:` es tomado por defecto por truncamiento del
primer párrafo de la publicación (esto se usa en los metadatos de la
publicación), pero también podemos dejarlo si lo queremos personalizado (esto se
hace con la extensión de open-graph).

El caso de `.. link:` se debe convertir en `:external_link:`.

Para la las actualizaciones, esto en lugar de ser un atributo, pasa a ser una
anotación con marca de tiempo, pero con información de contexto.

`````{tab-set}

````{tab-item} RST
```{code} rst

.. update:: 2011-12-15

   Se añade info extra
```
````

````{tab-item} MD
```{code} md

```{update} 2011-12-15

Se añade info extra
```
```
````

`````

Con los atributos de `.. nocomments:`, `.. tags:`, `.. date:`, `.. author:` y
`.. category:`, basta con cambiar `.. ` inicial por `:`.

Respecto a la fecha es importante tener claro, que a diferencia de Nikola no
podemos mezclar tipos de formato de fecha. Estos deben añadirse según la
definición que se tenga en el archivo de configuración, en la variable
`post_date_format`.

No es necesario un atributo para habilitar las ecuaciones, ya que Sphinx las
habilita por defecto. En Nikola era necesario con `.. has_math: true`.

El caso de `.. type:` no posee equivalente.

⚠️ Si estamos usando _markdown_, la diferencia es quitar el `:` inicial, tal
como se evidencia en la sección de
[primera publicación](./crear-un-blog-con-sphinx.md#primera-publicaci%C3%B3n), y
el separador `<!-- --> ` pasa a `---`.

#### Contenido

En algunos casos, podíamos recurrir a listados de publicaciones mediante algún
filtro con `.. post-list::` y el atributo de `:categories`. Esto ahora pasa a
`.. postlist::` con el atributo `:category:` (puedes usar otros filtros
también).

Respecto a `.. thumbnail::` esta directiva no existe, y se reemplaza por
`.. figure::`.

La definición del _teaser_ en Nikola dependía de una marcación específica como
directiva para el texto, pero en _ablog_ esto es controlado por el atributo
`:excerpt:`, para denotar el número de párrafos a incluir. Pero podemos dejarlo
con un valor por defecto acorde a `post_auto_excerpt` en el archivo de
configuración.

Para las referencias a documentos, en Markdown pasamos de
`{{% doc %}} path {{% /doc %}}` a `<project:path>` o `[](path)`, mientras que en
RST podemos mantener `:doc:` siempre y cuando no apunte a una etiqueta, en cuyo
caso sería `:ref:`.

### Configuración

#### Archivos en el raíz

Los archvos en el raíz, se definen en un directorio que disponemos con la
variable `html_extra_path`, la cual podemos definir con el mismo nombre que
viene en Nikola (`files`).

#### Sistema de comentarios

Si usamos Disqus (en Nikola, `COMMENT_SYSTEM='disqus'`), el `disqus_shortname`
en el archivo de configuración toma el valor del antiguo `COMMENT_SYSTEM_ID`.

```{note}

La verdad, he decidido retirar el sistema de comentarios de Disqus. Aporta poco valor
respecto a lo que introduce en tiempo de carga. Posiblemente explore disponer el enlace
de la publicación en Mastodon para que se desarrolle la eventual discusión.
```

#### Youtube

Necesitamos instalar `sphinxcontrib-youtube` y habilitar `sphinxcontrib.youtube`
en las extensiones. De esta forma, la directiva de `.. youtube::` sigue tal
cual.

## Referencias

- [Migrating the website to Sphinx + ABlog](https://adriaanrol.com/posts/2023/sphinx_migration/)
- [Migration to Cloudflare Pages](https://dailystuff.nl/blog/2021/migration-to-cloudflare-pages)
- [Ablog](https://ablog.readthedocs.io/en/stable/manual/ablog-quick-start.html)
- [Myst Parser](https://myst-parser.readthedocs.io/en/latest/)
