# Cosmoscalibur

Este es el repositorio público de mi sitio web
[cosmoscalibur.com](https://www.cosmoscalibur.com).  

## Lenguaje

Soy colombiano, así que por supuesto mantendré el idioma de publicación principalmente en español. Se necesitan medios de divulgación de ciencia y tecnología en español que no sean solo copias de otros o traducciones sin contexto de los medios extranjeros y que sean activos (he visto morir muchos proyectos de este estilo, física pasión es ejemplo). Respecto a las otras temáticas no se discute el motivo, parto de que es claro.  

_¿Significa que no habrán publicaciones en inglés?_ No, pero no serán mi prioridad.  

## Desarrollado con

El sitio es generado con [Nikola](https://getnikola.com/) y alojado en GitHub. El código fuente de las
publicaciones es ReStructuredText y MarkDown, el cual puede consultar libremente. Los archivos de generación
del entorno son para entornos conda y el archivo apt.txt contiene paquetes adicionales de sistema para la
aplicación de filtros (instalación en ubuntu y derivados).  

    git clone https://github.com/cosmoscalibur/cosmoscalibur.github.io.git
    cd cosmoscalibur.github.io
    conda env create -f environment.yml
    cat apt.txt | xargs sudo apt install -y

## Redes

Por lo pronto los veo en las redes sociales:  

+   Twitter [@cosmoscalibur](http://www.twitter.com/cosmoscalibur).  
+   Facebook [cosmoscalibur](http://www.facebook.com/cosmoscalibur).  
+   Youtube [cosmoscalibur](https://www.youtube.com/channel/UC3am73vAC7qHgykOF-q06rQ).  
+   Instagram [blogcosmoscalibur](https://www.instagram.com/blogcosmoscalibur/).  
+   LinkedIn [cosmoscalibur](https://co.linkedin.com/in/cosmoscalibur).  
+   SlideShare [cosmoscalibur](www.slideshare.net/cosmoscalibur).  

## Licencia

El contenido de este blog se distribuye bajo licencia [CCBY40](https://creativecommons.org/licenses/by/4.0/deed.es) y el código asociado bajo [licencia MIT](LICENSE).  
