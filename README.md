# Cosmoscalibur

Este es el repositorio público de mi sitio web,
[cosmoscalibur.com](https://www.cosmoscalibur.com) `> ⚛️ _|`.

## Lenguaje

Soy colombiano, así que por supuesto mantendré el idioma de publicación
principalmente en español. Se necesitan medios de divulgación de ciencia y
tecnología en español que no sean solo copias de otros o traducciones sin
contexto de los medios extranjeros y que sean activos (he visto morir muchos
proyectos de este estilo, física pasión es ejemplo). Respecto a las otras
temáticas no se discute el motivo, parto de que es claro.

_¿Significa que no habrán publicaciones en inglés?_ No, pero no serán mi
prioridad.

## Desarrollado con

El sitio es generado con [Sphinx](https://www.sphinx-doc.org/),
[Ablog](https://ablog.readthedocs.io/en/stable/) y el tema de
[PyData Sphinx](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html).
El sitio está alojado en GitHub, servido a través de GitHub Pages, y el código
fuente de las publicaciones es ReStructuredText y MarkDown/Myst (incluyendo
Notebook), el cual puede consultar libremente.

Requisitos:

- UV
- Git
- Just

```
git clone https://github.com/cosmoscalibur/cosmoscalibur.github.io.git
cd cosmoscalibur.github.io
uv venv --python 3.12.7
uv sync
just serve
```

Para ejecutar tras la instalación

```
just serve
```

Si deseamos generar la versión final para publicarla en GitHub Pages

```
just deploy
```

## Redes

Por lo pronto los veo en las redes sociales:

- GitHub [cosmoscalibur](https://github.com/cosmoscalibur).
- Mastodon [@cosmoscalibur@col.social](https://col.social/@cosmoscalibur).
- Youtube [cosmoscalibur](https://www.youtube.com/c/CosmoscaliburCo).
- X (Twitter) [@cosmoscalibur](http://www.twitter.com/cosmoscalibur).
- Facebook [cosmoscalibur](http://www.facebook.com/cosmoscalibur).
- Instagram [blogcosmoscalibur](https://www.instagram.com/cosmoscalibur/).
- LinkedIn [cosmoscalibur](https://co.linkedin.com/in/cosmoscalibur).
- SlideShare [cosmoscalibur](www.slideshare.net/cosmoscalibur).

## Licencia

El contenido de este blog se distribuye bajo licencia
[CCBY40](https://creativecommons.org/licenses/by/4.0/deed.es) y el código
asociado bajo [licencia MIT](LICENSE).
