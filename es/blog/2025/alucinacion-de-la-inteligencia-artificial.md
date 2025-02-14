---
date: 2025-02-13
tags: modelo de lenguaje, inteligencia artificial
category: tecnología
---

# Alucinación de la inteligencia artificial

Los robots también sueñan. Sí, y sueñan despiertos. La alucinación en los
modelos de lenguaje (o inteligencias artificiales) es inevitable. No todo lo que
genera una IA es confiable y debes tener criterios adecuados para juzgar la
información generada. En general, la IA es un buen asistente, pero solo eso, te
debe asistir y la última palabra siempre debe ser tuya, y aquí te ilustraré la
razón.

## ¿Qué es la alucinación en una inteligencia artificial?

Alucinación es el nombre del evento o fenómeno asociado a la generación de
respuestas coherentes y correctas gramaticalmente, pero que no son correctas en
términos de los hechos o que no poseen sentido. Dicho de otra manera, es la
generación de información falsa.

Ejemplo, al preguntar al modelo de _deepseek-r1:7b_, sobre qué colombianos han
recibido el premio Nobel, obtenemos una respuesta completamente errada:

> Sí, Colombia ha tenido algunos personajes及相关人士 who have ganado el Premio
> Nobel. Aquí tienes algunos ejemplos:
>
> 1. Johnatan Salamanca (Nobel de Paz, 2019): Jefe del gobierno indigene de los
>    Países Bajos de Chocó y premiado por su trabajo en la lucha por los
>    derechos de autodeterminación.
> 2. Andrés Crestó (Premio Nobel de Ciencias, 2015, pero noPremio Nobel formal):
>    Fue Premiado por su trabajo en la documentación sobre las protestas de
>    2005\.
> 3. Carlos Ghosn (Premio Nobel de Letras, 2018): Premiado por su autobiografía
>    "El Viento del Horizonte", que narra sus experiencias como empresario y
>    Activity en torno a los conflictos entre Colombia y Ecuador.
> 4. Alvaro Uribe (Premio Nobel de derechos humanos, 1997, aunque noPremio Nobel
>    formal): Considerado uno de los más importantes ex presidentes Colombianos
>    y premiado por su trabajo en la derechos humanos.
>
> Es importante Notar que algunos de estos personajes, como Andrés Crestó, no
> han ganado el Premio Nobel de manera formal, sino que han sido Premiados
> porOther organizations o comités.

## Tipos de alucinaciones de los modelos de lenguaje

Las alucinaciones en los modelos de lenguaje (LLM) han sido caracterizadas (los
ejemplos han sido realizados con modelos que he instalado):

- Errores o contradicciones factuales: es un tipo de **alucinación factual** que
  corresponde cuando las respuestas pueden ser contrastadas con información real
  y la respuesta presenta contradicción o falsedad. El ejemplo previo
  corresponde a un error factual.
- Fabricación de hechos: Es un tipo de alucinación factual que corresponde a
  respuestas que no pueden ser verificables, son datos inexistentes o las
  respuestas son debatibles. Ejemplo, al preguntar al modelo *Qwen:0.5b* sobre
  la guerra más importante del siglo XX, refiere a la guerra *Osa-Salvador*, la
  cual no existe.
- Inconsistencia de instrucción: Es un tipo de alucinación de fidelidad en la
  cual la instrucción o pregunta es desviada o alterada. Ejemplo, al preguntar
  al modelo *Llama3.2:3b* por "*Traduce al inglés: “Capital de Francia”*",
  responde "*La traducción al inglés de "Capitol de Francia" es "Paris".*". Esto
  implica desviar la instrucción de la traducción por la instrucción de
  responder a la capital, perdiendo la intención transmitida en el contexto.
- Inconsistencia de contexto: Es un tipo de alucinación de fidelidad en la cual
  la instrucción ignora información del contexto. Ejemplo, al preguntarle a
  *Llama3.1:8b* por "*El plural de mamá es mamás. Cuál es el plural de mamá?*",
  la respuesta es "*Lo siento, pero creo que hay un error en tu afirmación. En
  castellano, el plural correcto de "mamá" es "mamas". No "mamás".*".
- Inconsistencia lógica: Es un tipo de alucinación de fidelidad en la cual se
  presentan contradicciones lógicas, por ejemplo, en razonamientos matemáticos.
  Ejemplo, al preguntarle a *mistral-nemo:12b* por *Factorizar 6x^2-13x-8*, su
  respuesta es "*(6x + 4)(x - 2)*".

## ¿Por qué alucinan los modelos de lenguaje?

Hay múltiples motivos por los cuales los modelos de lenguaje (LLM) presentan
alucinaciones. Estos pueden venir de:

- Datos de entrenamiento desactualizados: Los modelos poseen un conjunto de
  datos base sobre los cuales se entrenan y que está limitado en el tiempo. Por
  ese motivo si el modelo tuvo un corte de datos en 2022, no puedes esperar
  respuestas basadas en información posterior. Es importante estar al tanto del
  corte de datos del modelo que escojas.
- Sesgos de datos: La recopilación de información puede presentar sesgos, y el
  más común que podemos encontrar obedece al generado por el lenguaje de la
  mayor parte de fuentes. Ejemplo, los modelos de *Qwen* y *Deepseek*, poseen
  fuerte sesgo al inglés y al chino (algo notorio en *deepseek* y en los modelos
  de *qwen* livianos).
- Fuentes con datos errados: En general, las fuentes no son depuradas, y hay
  alta presencia de datos por extracción web de fuentes generales, que pueden
  contener información errónea/falsa (incluso de manera deliberada cómo ataque a
  los modelos de lenguaje).
- Ausencia de datos o de fuente de la verdad: No todo lo que podríamos consultar
  se encuentra en el conjunto de datos o simplemente no hay información. Esto
  puede ser por ejemplo, por limitaciones de derechos de autor en el contenido
  existente o asociado a la limitación del conocimiento mismo.
- Preguntas ambiguas: A mayor ambigüedad de la pregunta, mayor la probabilidad
  de alucinación porque está sujeto a la "interpretación" del modelo. Puedes
  considerar cómo si el modelo contrastará con preguntas similares. En general,
  vamos a mejorar el resultado aumentando el nivel de especificación en la
  consulta.
- Fallas de razonamiento: La mayor parte de modelos disponen de bajas
  capacidades de razonamiento. Los LLM entienden la estructura del lenguaje (o
  imitan la estructura), pero no hay cadenas causales dentro del contexto que
  representan sus palabras (*tokens*).
- Alta complejidad computacional: En la medida que la complejidad computacional
  de un problema aumenta, este también genera mayor sensibilidad a las
  alucinaciones, por ejemplo, los problemas combinatorios.

## ¿Se pueden evitar las alucinaciones?

Con todo lo mencionado anteriormente, una pregunta importante es si este
problema de las alucinaciones es posible solucionarse, pero la respuesta sincera
y aunque no nos guste, es que siempre existirá la alucinación en los modelos de
lenguaje (y de los modelos de razonamiento).

El conjunto de datos de un entrenamiento de un modelo siempre es un subconjunto
o aproximación del mundo real, pero también la construcción misma del modelo es
resultado de un proceso iterativo que busca patrones en su conjunto de datos y
le permite converger, y bajo dicha convergencia detenerse en el proceso de
aproximarse cada vez más a los datos que son fuente de la verdad. Pero en la
medida que nos acercamos más a replicar el conjunto de datos, esto genera un
sobreajuste del modelo y lleva a la perdida de generalidad. Es decir, el modelo
es una aproximación al conjunto de datos, y el conjunto de datos es un
subconjunto del mundo real. Siempre existirá alucinación.

Matemáticamente, se demuestra que los modelos de lenguaje siempre van a
alucinar, y esto más que un error es una "característica" de los modelos, que
debemos entender su presencia, como mitigarlas y, su impacto ético y social.

## ¿Qué modelo de lenguaje usar para reducir las alucinaciones?

Esta pregunta no es simple, y ni siquiera podemos usar como referencia las
pruebas de comparación de los modelos, ya que estas pruebas son estandarizadas.
Esto es una crítica importante, porque las pruebas estandarizadas poco a poco se
vuelven parte del entrenamiento de los modelos. Por este motivo, lo mejor que
puedes hacer es probar por tu
[cuenta los modelos](/es/blog/2025/instala-tu-asistente-local-de-ia.md).
Construye un conjunto de preguntas relacionadas con tu día a día, con tu
trabajo, con tus temas de interés, de las cuales tengas conocimiento y puedas
validar la certeza y calidad de las respuestas. Y con ello, escoge.

Dado que una fuente de alucinación es el sesgo de los datos, esto es importante
porque las pruebas estandarizadas son en inglés, por lo cual, un buen modelo
podría no ser el mejor para ti si no dominas el inglés, o si tus funciones son
de una disciplina con pocos datos públicos, tal vez el mejor modelo no sea el
que tenga más información de tu interés.

En general, los modelos "ultralivianos" son mala idea (menos de *3b* son fuente
de alucinaciones constantes), ya que un menor número de parámetros implica una
perdida de datos, conexiones entre estos y perdida de la estructura semántica
del lenguaje.

Un buen punto de partida es *qwen2.5:3b* o *llama3.2:3b* si no dispones de GPU,
estos modelos son decentes, aunque presentan sesgos importantes respecto al
contexto regional (en mi caso, Colombia) y del español, pero tienen un muy buen
contexto para tareas de código o consultas en inglés. En mi caso, los probé en
una máquina sin GPU, con 16 GB de RAM. Sin embargo, si posees GPU mi
recomendación es usar *qwen2.5:7b* o *qwen2.5:14b*. Definitivamente, no
recomiendo *Phi* (tiene sesgos importantes con el lenguaje) ni *Deepseek* en
ninguna de sus variantes (tampoco *deepseek-r1*, que en las versiones para
máquinas locales son destilados de *Qwen2*, *Qwen2.5* y *Llama3.1*, con menor
precisión, perdida continua de contexto y mezcla de lenguaje).

Los modelos especializados en matemáticas me decepcionaron, pero puede ser un
problema de sesgo al preguntar en español, y recomiendo mejor para fines de
matemáticas en español las versiones generales de *qwen2.5:7b* y *qwen2.5:14b*.

En las versiones especializadas de código, mi recomendación se mantiene también
en la familia de *qwen2.5*, con su variante de *qwen2.5-coder*, desde la versión
de *qwen2.5-coder:3b* (útil si no posees GPU, pero *qwen2.5-coder:7b* en GPU es
un buen balance sin un consumo excesivo de recursos). Es importante usar las
versiones especializadas de código porque estas proveen la integración adecuada
para autocompletado con los editores de código y respuestas más concretas cuando
se pregunta por temas de programación. Una curiosidad sobre *qwen2.5-coder:7b*,
es que es usado como base para el modelo
[*zeta* de {program}`zed`](https://zed.dev/blog/edit-prediction).

Si posees una mejor máquina, puedes intentar probar modelos de mayor tamaño, en
mi caso con una GPU RTX 2060 y 16 GB de RAM, mi límite llega con los modelos de
*14b*. Pero ten presente que para tu caso de uso, puede no ser necesario
aumentar el modelo, ejemplo, aunque puedo ejecutar *qwen2.5:14*, no veo
beneficios adicionales en mi caso de uso respecto a *qwen2.5:7b*.

## Referencias

- [What are LLM Hallucinations?](https://www.iguazio.com/glossary/llm-hallucination/).
- [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://arxiv.org/abs/2311.05232v2).
- [LLMs Will Always Hallucinate, and We Need to Live With This](https://arxiv.org/abs/2409.05746v1).
- [Hallucination is Inevitable: An Innate Limitation of Large Language Models](https://arxiv.org/abs/2401.11817).
