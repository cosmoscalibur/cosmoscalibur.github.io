---
date: 2024-09-25
tags: sphinx, google ads
category: tecnología, blog con sphinx
author: Edward Villegas-Pulgarin
language: es
---

# Agregar Google Ads en Sphinx

Siguiendo con ajustes en mi blog, algo que quería darle una nueva oportunidad,
así algunos lo odien, es a _Google Ads_ y ver esto como permite generar algún
ingreso ahora que muchos usamos bloqueadores (sí, yo también). Les cuento como
configurarlo a través de la modificación de las plantillas por defecto.

## Directorio de _assets_

Necesitamos configurar [directorios](#sphinx-dir-setup) de archivos generales
que van a nivel de raíz del despliegue y el directorio de plantillas, esto con
el fin de asegurarnos del directorio sin el prefijo `_` problemático en _GitHub
Pages_ y ser consciente del valor en lugar de tomar el valor por defecto.

```{code} python
html_extra_path = ['files']
templates_path = ['templates']
```

Creamos los directorios `files` y `templates` si no los hemos creado.

## Archivo Ads

Un primer paso para incluir _Google Ads_ es incluir nuestra validación como
publicador y esto puede hacerse incluyendo _scripts_ o un archivo `ads.txt`. Es
recomendable esta última opción para reducir la carga de _scripts_, y acorde a
Google es más recomendable para las validaciones por proveedores de anuncios y
cuando son múltiples.

Este archivo debe estar en la raíz de nuestro sitio, por lo que vamos a disponer
de este archivo en el directorio `files` que es el destinado para este tipo de
archivos.

Una vez tenemos la aprobación, seguiremos con el _script_.

## _Script_ en _head_

En el interior de `templates`, necesitamos crear un nuevo archivo que usaremos
para modificar el comportamiento por defecto de la plantilla de `layout.html`,
que es la plantilla usada por _Sphinx_ que contiene lo que se agrega entre las
etiquetas de apertura y cierre de `head`.

Creamos el archivo con el mismo nombre de la plantilla que deseamos reemplazar,
y en su interior se indica que extiende dicha plantilla en la primera línea.
Usamos ahora el bloque asociado a `extrahead` para añadir el _script_ de _Google
Ads_ que requerimos esté en el _head_.

Para mi caso, luciría de la siguiente forma (debes cambiar acorde al generado en
tu sección de Google Adsense).

```{code} html
{% extends "!layout.html" %}

{{ super() }}

{% block extrahead %}
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-0356238418278924"
    crossorigin="anonymous"></script>
{% endblock %}
```

Unos minutos (u horas) después, tendremos la visualización de anuncios en
nuestro sitio generado con Sphinx.

```{figure} /images/agregar-google-ads-en-sphinx/ads-en-sphinx.png
---
alt: Visualización de anuncios en sitio generado con Sphinx.
align: center
width: 500px
height: 250px
---
   Visualización de anuncios en sitio generado con Sphinx.
```

## Referencias

- [Sphinx - Configuration - `html_extra_path`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path).
- [Sphinx - Configuration - `templates_path`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-templates_path).
- [Sphinx - HTML theme development - Templating](https://www.sphinx-doc.org/en/master/development/html_themes/templating.html).
