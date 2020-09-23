.. title: Datos y responsabilidad: Covid19
.. slug: datos-y-responsabilidad-covid19
.. date: 2020-04-05 19:11:52-05:00
.. tags: datos, responsabilidad, covid19, coronavirus, pandemia, colombia
.. category: opinión
.. link: 
.. description: 
.. type: text
.. author: Edward Villegas-Pulgarin
.. has_math: true

Había tratado de estar al margen de hacer muy público lo que pienso y analizo
de los datos de la pandemia por covid19 en Colombia, y de las medidas tomadas.
Sin embargo, finalmente me motivé a hacer una segunda afirmación del todo
pública (si, ya les contaré que fue lo anterior) porque veo algo recurrente en
colegas "científicos de datos" (*data scientists* que se gustan decir en
inglés), donde creen prudente hacer ajustes de curvas básicas y hacer
interpretaciones del futuro y observaciones sin contexto del fenómeno.

.. note::
   No soy epidemiólogo, médico, biólogo o similar. Trabajo en analítica de
   datos y modelización matemática, graduado de ingeniería física y maestría en
   física aplicada. Y esto es un llamado a la prudencia y responsabilidad de
   mis colegas.

.. TEASER_END

Ruido y desinformación
======================

Esta es la razón de hacer esta publicación, así que empezaré con mencionar
algunas señales de ruido en medio de esta pandemia y, luego brevemente
comentaré porque no debe considerarse esa situación y que si podríamos decir
sanamente.

Ha sido días con mucha agitación en redes con menciones basadas en los datos
pero no revisadas por epidemiólogos, los expertos a los cuales debemos escuchar
en medio de esta crisis, sino por "expertos" en analítica de datos y como les
gusta en inglés, "*data scientists*". El porque de las comillas es parte de mi
crítica, y es que no estamos en una situación que permita salir públicamente a
llenarse el ego de sé predecir con modelos de juguetes e impresionar a público
que no tiene formación ni en datos ni en epidemiología. ¿Usan esos modelos en
sus trabajos?

Pero al grano, ¿qué han afirmado?, e incluso, ¿qué han ayudado a soportar
erradamente a nuestros gobernantes o a los conspiranoicos?

+ Los datos son sospechosos y no son de creer, en otros países crece muy
  rápido.
+ El gobierno nos esconde información, hay muertos que no reportan.
+ La curva se está aplanando y el comercio se puede reactivar.
+ La cuarentena si ha servido.

Pues todas estas cosas, son afirmaciones que no son posibles y debemos entender
el fenómeno y la captura de datos (ambos importantes en cualquier análisis de
datos). Mi idea no es difamar a los colegas, por lo cual no enlazo a las
publicaciones (ya en los casos respectivos he comentado porque no debería
hacerse).

Subestimación de los datos
==========================

Una de las cosas más importantes al iniciar a revisar la información de los
casos de covid19 en todo el mundo, es la mención a "Casos positivos
confirmados". Y aquí, **confirmados** es la clave.

.. figure:: /images/datos-y-responsabilidad-covid19/comunicado-covid-colombia-4-abril-2020.png
   :alt: Comunicado gráfico de los casos de Covid19 en Colombia del 4 de abril de 2020.
   :align: center
   :height: 300px
   :width: 150px

   Se resalta la mención de **confirmados** en los comunicados oficiales. En el
   ejemplo, comunicado del 5 de abril de 2020.

Esto es importante porque es claro con esta mención, que la cifra dada en todos
los casos (infectados, muertos e incluso recuperados) siempre será una
subestimación. Pero, ¿por qué es así? Resulta que la sola política o criterio
de toma de muestras afecta. Dado que las muestras poseen un costo asociado y no
hay presupuesto infinito (si, todo es plata), la cantidad de pruebas es
limitada y priorizadas según los casos que puedan preveerse de mayor
complejidad, o que tengan motivos para considerar una alta probabilidad de
contagio. Ejemplo de esta subestimación en rechazos a pruebas es que al inicio
del fenómeno si no procedías del extranjero, no eras consciente del contacto
con personas provenientes del extranjero o con personas positivas a covid19,
simplemente no te hacían el examen y el diagnóstico era una enfermedad
respiratoria adicional. Igual, si no tenías fiebre tampoco te hacían la
prueba. ¿Y si eres asintomático? Pues ni siquiera vas a solicitar la prueba.

¿Y esto a nivel de datos qué representa? En el reporte de la Organización
Mundial de la Salud, el 87.9% de los infectados confirmados presentó fiebre
[who-report_], así que usando los criterios de pruebas tenemos un potencial
12.1% de casos que tuvieron que esperar complicaciones o simplemente están
como si nada. Pero también, hay otro porcentaje, que en el mismo reporte se
considera bajo, pero que en una gran cantidad representa muchas personas, y
son los asintomáticos.

Siendo esto claro, vemos que también en la medida que se puedan realizar más
pruebas conoceremos mejor la realidad del país. Algo de estadística básica nos
dice que siempre tenemos incertidumbre en la medida que no se conozca
información de cada individuo de la población sino de una muestra. Pero
adicional, la muestra desde el punto de vista estadístico para la aplicación de
las pruebas presenta un sesgo (depende de tener ciertos síntomas y condición de
vulnerabilidad). Con la llegada de las pruebas rápidas al país podremos ver
eventualmente una realidad más clara de la condición real, pues los casos
confirmados son limitados por la capacidad de hacer pruebas.

Tomo en consideración lo afirmado en la sección sobre las pruebas en *Our World
in Data* [ourworldindata_]:

   8) What are the typical testing practices in the country?
   Having a sense of how often and when individuals are tested, can help the
   users of these statistics understand how estimates of tests performed and
   individuals tested might relate to each other.
   For instance, how many tests does a case investigation require? What are the
   eligibility criteria to be tested? Are health workers, or other specific
   groups, being routinely retested?

Finalmente, no todos los países tienen las mismas políticas y medidas
implementadas, así como sus dinámicas sociales e incluso ambiente son
diferentes. Esto lleva a que la comparación con otros países no sirve de
referente para un análisis más allá de un consuelo de tontos de ver que otros
lloran más muertos que nosotros.

Predicción y aplanamiento de la curva
=====================================

Si es posible hacer pronósticos matemáticos sobre la evolución de la pandemia,
eso es algo claro y es uno de los insumos importantes para tomar decisiones
sobre las medidas a implementar para controlar su propagación. Y entonces, ¿por
qué la crítica a mis colegas?

No están considerando múltiples variables, las cuales describiré:

+ Tipo de contagio: Es una descripción que aporta a la definición de la fase de
  la pandemia en la que nos encontramos. Puede ser:

  Importado
     Son los casos que ingresas al país ya infectados. La forma como evoluciona
     depende de las políticas externas, la condición de la pandemia en el
     extranjero, la frecuencia de viajes internacionales y la distribución de
     orígenes. Esto lleva a una medida de suspensión de vuelos internacionales
     y cierre de fronteras.
   
   Relacionados
      Son los casos que se establecen como infectados por interacción directa
      con los casos positivos. Su control en buena medida depende de la
      trazabilidad de las interacciones de los casos importados al inicio de la
      pandemia (son los únicos positivos al inicio) pero después se amplia al
      trabajo de seguimiento sobre los demás relacionados.
   
   Autóctonos
      Autóctonos o de transmisión comunitaria, no es más que la forma bonita de
      decir que le perdimos el rastro a los infectados. Es por eso que los
      datos oficiales mencionan "En estudio" y no algo como esto. Aquí, al
      perder el rastro y considerando los casos asintomáticos y subclínicos (el
      infectado si desarrollará síntomas pero aún no los tiene o no son
      detectables). Aquí es donde el distanciamiento social y el aislamiento
      poseen un papel importante (cualquiera puede ser potencial portador).

+ Medidas implementadas o anomalías: Es importante a la hora de interpretar
  resultados, considerar las fechas de implementación de las distintas medidas
  implementadas y no solo de la última o que se considere importante. También,
  hay otras afectaciones en el tiempo como la disminución o aumento de la
  capacidad de pruebas.

   + 11 de marzo: Primer caso relacionado [covid-colombia_].
   + 14 de marzo: Cierre de frontera con Venezuela [tt-duque_].
   + 16 de marzo: Se niega ingreso a extranjeros provenientes de Europa o Asia.
     Colombianos tendrán aislamiento de 14 días [tt-duque_].
   + 17 de marzo: Cierre de fronteras terrestres, marítimas y fluviales
     [cnn-fronteras_].
   + 20 de marzo: Simulacro de cuarentena en Bogotá [tiempo-simulacro_]. Otras
     localidades del país hacen medidas similares el fin de semana.
   + 23 de marzo: Suspenden vuelos internacionales [tt-presidencia-int_]
   + 23 de marzo: Primer caso de transmisión comunitaria [covid-colombia_].
   + 25 de marzo: Inicia cuarentena [tiempo-cuarentena_].
   + 25 de marzo: Suspenden vuelos nacionales [tt-presidencia-nal_].
   + 27 de marzo: Daño en máquina del INS para procesar pruebas [tt-INS-daño_].
   + 4 de abril: Se anuncia por el gobierno nacional el uso obligatorio de
     tapabocas en transporte masivo y público [minsalud-tapabocas_]. En
     Medellín comenzará el 7 de abril [tt-quintero_].
   + (abril): INS anunció el 22 de marzo que se avalaran distintos laboratorios
     en el país para hacer pruebas de covid19 [presidencia-covid_].
   + Distintas regiones han aplicado pico y cédula pero el inicio ha sido en
     fechas diferentes.
   
¿Y entonces qué? Bueno, en buena medida muchas de estas fechas deberían llevar
a ingresar consideraciones en el modelo pero sino, mínimamente deben ser usadas
adecuadamente para interpretar los datos y tendencias. Esto, contrastando con
los 15 días típicos de tiempo de incubación.

.. figure:: /images/datos-y-responsabilidad-covid19/casos-covid-colombia-tipo-4-abril-2020.png
   :alt: Casos acumulados de Covid19 al 4 de abril de 2020 por tipo en Colombia.
   :align: center

   Acumulado de casos positivos confirmados de covid19 por tipología incluyendo
   el total. La curva azul presenta crecimiento exponencial.

Con lo anterior en mente, vemos que la interpretación de los datos debe hacerse
a la vista de los 3 tipos de contagio, donde notamos al separar la evolución
que el aplanamiento observado está en las curvas de importados y relacionados,
pero la curva de los casos de estudio (alias comunitarios) crece
exponencialmente e incluso ha alcanzado los valores de los relacionados. Esto
nos hace esperar que el aplanamiento observado sea temporal y probablemente en
el transcurso de la semana evidenciemos nuevamente un incremento exponencial
pero no tan pronunciado porque los casos importados deberán ser poco
apreciables sobre el fin de semana.

Vale recordar la afirmación de los expertos y compartida por el ministro de
salud en entrevista el día de ayer por el canal Caracol, "Las cifras de hoy son
de pacientes de hace 14 días" [tt-caracol_].

Conceptos
=========

Generalmente los comportamientos de crecimientos de población o de la
propagación en poblaciones se modelan con comportamientos de tipo exponencial,
gausianas y logísticas (si, igual las otras tienen exponenciales por dentro).

Normalmente nos encontramos que la manera como interactuamos con las personas
y manteniendo el trazado de la interacción de estas, lleva a consolidar el
número de personas con interacción directa e indirecta con el crecimiento
exponencial (:math:`A\exp(r t)`, donde :math:`r` es la tasa de crecimiento y
:math:`A` es la población inicial afectada).

Las curvas gausianas [wiki-gausiana_] pueden describir los casos activos, es
decir, los casos actuales que se encuentran afectados actualizando respecto a
los casos de recuperados y muertos que se descuentan de los infectados. Esta es
la famosa curva que nos comunican que debemos aplanar [bbc-aplanar_] mediante
medidas como el distanciamiento social, el aislamiento
[elcolombiano-distancia_] y el uso masivo de tapabocas [minsalud-tapabocas_].

Las curvas logísticas [wiki-logistica_] sirven para describir los casos
acumulados de registros nuevos (en el caso de infectados, así se recuperen o
mueran no se reduce el conteo).

Las menciones anteriores son solo resultados rápidos que se pueden usar de
modelos más elaborados [wiki-modelling_] que dependen de resolver sistemas de
ecuaciones diferenciales, pero aún así, estos modelos resultan ser muy simples
comparando con la dinámica real que se debe capturar. Es por este motivo que se
usan modelos estocásticos si hablamos de un modelo serio que permita reflejar
incluso el comportamiento de las interacciones humanas en un mayor detalle y
las medidas implementadas [wiki-stochastic_].

Recomendaciones para saber más
==============================

Siga fuentes oficiales de información y las recomendaciones de las autoridades
sanitarias. Y antes de consumir información sobre este tema, le recomiendo leer
las publicaciones que epidemiólogos y expertos afines han realizado en una
forma digerible y divulgativa. Respecto a esto último recomiendo los hilos en
twitter de `Zulma Cucunubá <https://twitter.com/ZulmaCucunuba>`_, epidemióloga,
doctora en dinámica de enfermedades infecciosas.

A nivel de gráficos, es posible que actualice el
`álbum en facebook <https://www.facebook.com/pg/cosmoscalibur/photos/?tab=album&album_id=2580908872196780>`_.



Referencias
===========

.. [wiki-gausiana] https://es.wikipedia.org/wiki/Funci%C3%B3n_gaussiana
.. [bbc-aplanar] https://www.bbc.com/mundo/noticias-51835806
.. [elcolombiano-distancia] https://www.elcolombiano.com/colombia/salud/coronavirus-que-es-el-distanciamiento-social-BG12632636
.. [minsalud-tapabocas] https://www.minsalud.gov.co/Paginas/El-uso-de-tapabocas-se-hace-obligatorio-en-el-sistema-de-transporte-publico.aspx
.. [wiki-modelling] https://en.wikipedia.org/wiki/Mathematical_modelling_of_infectious_disease
.. [wiki-stochastic] https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
.. [who-report] https://www.who.int/docs/default-source/coronaviruse/who-china-joint-mission-on-covid-19-final-report.pdf
.. [ourworldindata] https://ourworldindata.org/covid-testing
.. [cnn-fronteras] https://cnnespanol.cnn.com/2020/03/16/alerta-colombia-cerrara-sus-fronteras-desde-el-17-de-marzo-hasta-el-30-de-mayo-como-medida-contra-el-coronavirus/
.. [tt-duque] https://twitter.com/IvanDuque/status/1238666927779823618
.. [tt-presidencia-nal] https://twitter.com/infopresidencia/status/1241790747571077122
.. [tt-presidencia-int] https://twitter.com/infopresidencia/status/1240646520287961089
.. [tt-INS-daño] https://twitter.com/INSColombia/status/1243617211186544640
.. [presidencia-covid] https://id.presidencia.gov.co/Paginas/prensa/2020/Instituto-Nacional-Salud-anuncia-que-22-nuevos-laboratorios-preparan-para-iniciar-diagnosticos-COVID-19-en-el-pais-200322.aspx
.. [tiempo-cuarentena] https://www.eltiempo.com/salud/cuarentena-total-en-colombia-por-el-coronavirus-declara-el-presidente-ivan-duque-475512
.. [tiempo-simulacro] https://www.eltiempo.com/bogota/preguntas-y-respuestas-sobre-el-simulacro-de-cuarentena-en-bogota-474192
.. [covid-colombia] Revisar en el archivo de datos. https://coronaviruscolombia.gov.co/Covid19/index.html
.. [tt-caracol] https://twitter.com/NoticiasCaracol/status/1246957124858585088
.. [wiki-logistica] https://es.wikipedia.org/wiki/Funci%C3%B3n_log%C3%ADstica
.. [tt-quintero] https://twitter.com/QuinteroCalle/status/1246049721334018050