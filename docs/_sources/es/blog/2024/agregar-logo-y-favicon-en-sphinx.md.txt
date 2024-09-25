---
date: 2024-09-24
tags: blog, sphinx, pydata
category: tecnología, blog con sphinx
author: Edward Villegas-Pulgarin
language: es
---

# Agregar logo y favicon en Sphinx

Un nuevo paso en mi blog, es que decidí dejar una huella de personalización a
través de un logo, algo sencillo, pero propio, distinto a una imagen descargada
como lo era antes y que por lo mismo no lo había configurado. Les cuento como
configurar el logo y el _favicon_ en Sphinx.


## Directorio de _assets_

Para iniciar, requerimos configurar el directorio que usaremos para los archivos
estáticos de logo y _favicon_. En nuestro archivo de configuración, `conf.py`,
vamos a ajustar el valor de la variable `html_static_path` como fue explicado en
una [publicación anterior](#sphinx-dir-setup).

Este paso es importante sobre todo si alojamos nuestro blog en GitHub, porque el
valor por defecto al tener como prefijo `_`, no permite que se carguen los archivos
en el despliegue.

## Logo

Bueno, la verdad este punto no tiene nada de extraño, pero dejaré una recomendación.
Es mejor tener un archivo fuente editable para nuestro logo, de tal forma que podamos
proceder con ajustes fácilmente. Ejemplo, tenemos la versión para temas oscuros, y luego
decidimos tener la versión para temas claros (en Sphinx con el tema de PyData es posible),
podamos hacer estos cambios sin rehacer el logo desde cero.

En mi caso, este logo lo hice con [Inkscape](https://inkscape.org/es/) en formato
vectorial (`.svg`), y lo sincronizo en el
[repositorio también](https://github.com/cosmoscalibur/cosmoscalibur.github.io/blob/master/static/logo/cosmoscalibur.svg)
y hace parte de los estáticos. Otra recomendación, es tener presente que en
dimensiones, es preferible que sea más horizontal que vertical, pero su ancho
no debe ser superior a los 200 pixeles.

Ahora, vamos a nuestro archivo `conf.py` nuevamente, y allí encontraremos la variable
`html_logo` la cual asignaremos la ruta relativa al archivo de configuración, apuntando
a nuestro logo. Ejemplo:

:::{code} python
html_logo = 'static/cosmoscalibur_logo.png'
:::

A mi parecer, con la única versión de logo está _ok_, pero si requieres usar una
versión por tema, esto es una condición que depende del tema seleccionado y en PyData
se puede usando las opciones de
[`html_theme_options`](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/branding.html#different-logos-for-light-and-dark-mode).

:::{figure} /images/agregar-logo-y-favicon-en-sphinx/logo-en-sphinx.png
   :alt: Visual del logo agregado en Sphinx en el blog.
   :align: center
   :width: 800px
   :height: 250px

   Así vemos ubicado el logo configurado en el blog.
:::


## Favicon

Para el _favicon_ también podemos usar las opciones propias de _Sphinx_ con la
variable `html_favicon`. Nuestro _favicon_ debe ser de 16 por 16 pixeles, y puede
ser de formato ICO, PNG, SVG o GIF.

Debido al tamaño cuadrado del _favicon_, el cual irá en las pestañas del navegador
o en los marcadores, es conveniente tener un segundo diseño basado en nuestro logo
que se adapte a estas dimensiones.

En nuestro `conf.py` entonces hacemos el ajuste:

:::{code} python
html_logo = 'static/cosmoscalibur_favicon.png'
:::

Finalmente, así se ve nuestro _favicon_.

:::{figure} /images/agregar-logo-y-favicon-en-sphinx/favicon-en-sphinx.png
   :alt: Ícono cuadrado favicon en la pestaña del navegador.
   :align: center
   :width: 289px
   :height: 125px

   Así vemos el _favicon_ en la pestaña del navegador.
:::


## Referencias

- [Sphinx - Configuration - HTML logo](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo).
- [Sphinx - Configuration - HTML favicon](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon).
- [PyData Theme - Branding and logo](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/branding.html).

