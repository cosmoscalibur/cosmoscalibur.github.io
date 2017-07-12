<!--
.. title: Topónimos colombianos en RLA-ES
.. slug: toponimos-colombianos-en-rla-es
.. date: 2017-07-11 18:19:13 UTC-05:00
.. tags: Español,Topónimos,RLA-ES,Diccionario,Corrector de ortografía,Libre,Colombia
.. category: Contribuciones
.. link:
.. description: Aporte al proyecto RLA-ES con los topónimos colombianos para la localización del diccionario es_CO.
.. type: text
.. author: Edward Villegas Pulgarin
-->

Primero, saludo después de un tiempo largo de ausencia. Por diversos motivos el blog tuve que dejarlo en el olvido pero hoy lo reanudo. El como volví merece una publicación posterior.  

En esta ocasión quiero contarles de una contribución que me aprobaron el día de ayer en el proyecto "Recursos Lingüísticos Abiertos del Español" y de paso, sobre el proyecto en si mismo que me parece bastante interesante.  

# El proyecto

Resulta que finalizando mayo buscaba sobre proyectos que implicarán procesamiento de texto y lenguaje natural, por diversos motivos (aprender, prácticar y hacer una propuesta a una estudiante). En esa búsqueda me tope por casualidad con el proyecto [__Recursos Lingüisticos Abiertos del Español__](https://github.com/sbosio/rla-es) que es liderado por Santiago Bosio ([@sbosio](https://github.com/sbosio) en github).  

Este proyecto ha aportado diversas localizaciones del español en proyectos como LibreOffice, OpenOffice y Mozilla (proyectos que usan Hunspell para la corrección de ortografía). Y de paso, indirectamente había sido la fuente del diccionario para mis editores de texto plano (TeXMaker, Atom y ReText), pues no uso los que vienen por defecto en la distribución de Ubuntu sino que descomprimo la extensión de LibreOffice y tomo los archivos `dic` y `aff` (con el fin de tener versiones más recientes).  

Aunque por si mismo el proyecto no era lo que buscaba, vi la oportunidad no solo de usar una versión actualizada del diccionario sin esperar las liberaciones de versión (y sus respectivas subidas a los proyectos), sino una oportunidad de contribuir en la localización de Colombia.  

# La contribución

En el reporte [\#81](https://github.com/sbosio/rla-es/issues/81) del repositorio de github, se propuso como mejora agregar los topónimos de las localizaciones que aún no tuvieran dicha información. La localización de Colombia era uno de esos casos, y efectivamente una necesidad como colombiano para hacer algunos documentos en los que requiera mención a entes territoriales (y cuantos estudiantes en sus clases de geografía colombiana).  

Con esta necesidad y el ánimo de aportar por primera vez a un proyecto existente (a través del [semillero de física teórica y computacional](https://github.com/fisicatyc) ya lo había hecho, pero finalmente es algo que cofundé), inicie la búsqueda de la fuente de insumos para esta tarea.  

Así encontré [DIVIPOLA](https://geoportal.dane.gov.co/v2/?page=elementoHistoricoDivipola), que es la Codificación de la División Político-administrativa de Colombia. En ella, se pueden consultar los reportes históricos de la división nacional en entes territoriales para descargar y afortunadamente en un formato "amigable" (excel). Y aquí comenzo el trabajo, usando herramientas libres claro esta, que fueron `soffice` (la interface de comandos de LibreOffice) para la conversión del archivo de excel a texto plano (en específico a un archivo de valores separados por coma -CSV-) y las utilidades `tail`, `cut`, `tr` y `sed` para la manipulación del texto como la extracción de las columnas de datos necesarias, eliminación de números (cardinales y romanos), eliminación de palabras comunes (ya que no aportan al diccionario), eliminación de signos y conversión a minúsculas con mayúscula inicial. Y por supuesto, `git` para el control de versiones.  

No haré detalle técnico más allá de la mención anterior, pero si quieres ver como se hace (es un buen ejercicio), dejé constancia en el repositorio de como se hace el proceso como referencia para un futuro mantenimiento ([ver explicación](https://github.com/sbosio/rla-es/tree/master/ortograf/palabras/toponimos/l10n/es_CO)).  

Finalmente en el reporte [\#120](https://github.com/sbosio/rla-es/pull/120) realice la solicitud de inclusión (_pull request (PR)_) y unida (_merged_) al ramal principal el 10 de julio de 2017, y espera ver la luz oficialmente en la versión 2.3 de RLA-ES (sin fecha programada aún).  

¡Corrección de topónimos colombianos a la mano! Claro, faltan accidentes geográficos, pero es el primer paso. Espero poder aportar a la localización mucho más y al proyecto en general.  

# Uso

Una vez sea liberada la versión 2.3, estará disponible a traves de las extensiones de los proyectos y de la página de [_releases_ de RLA-ES](https://github.com/sbosio/rla-es/releases). Por ahora, es necesario generar el archivo descargando (o clonando) el proyecto y siguiendo las instrucciones dadas en la [wiki del proyecto](https://github.com/sbosio/rla-es/wiki/Generar-diccionario-corrector) (para la localización de Colombia, debemos usar `es_CO`).  

Finalmente, para poderlo usar en nuestros editores de texto plano (si, diccionario para nuestros documentos de LaTeX y MarkDown), debes seguir las indicaciones finales de la sección de la wiki (que se resúmen en descomprimir el archivo generado).  

__Fuentes__:  

+   [sbosio/rla-es](https://github.com/sbosio/rla-es): Proyecto original.  
+   [cosmoscalibur/rla-es](https://github.com/cosmoscalibur/rla-es): Mi derivación (_fork_) del proyecto para hacer las contribuciones.  