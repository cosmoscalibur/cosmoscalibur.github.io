---
date: 2026-02-23
tags: inteligencia artificial, modelo de lenguaje, ingeniería de prompt, ingeniería de contexto
category: opinión, tecnología
---

# Ingeniería de *prompt*: ¿Habilidad técnica o estafa?

La ingeniería de *prompt* se vendió como la habilidad del futuro. Cursos,
certificaciones, títulos de cargo, libros y hasta programas de posgrado
surgieron alrededor de la idea de que saber *cómo* hablarle a una inteligencia
artificial era una competencia técnica diferenciadora. Pero, ¿lo era realmente,
o era solo un parche temporal a las limitaciones de los modelos de lenguaje?

## El origen: un parche a modelos deficientes

Para entender por qué la ingeniería de *prompt* existió, hay que recordar cómo
eran los modelos de lenguaje hace apenas un par de años. GPT-3 y los primeros
modelos abiertos tenían una comprensión limitada del lenguaje natural. No
entendían instrucciones ambiguas, perdían el contexto fácilmente y necesitaban
que el usuario estructurara las solicitudes de maneras muy específicas para
obtener resultados útiles.

Ahí nació la ingeniería de *prompt*: un conjunto de técnicas —*few-shot
prompting*, *chain-of-thought*, *role prompting*, delimitadores, formatos de
salida explícitos— diseñadas para compensar las deficiencias de comprensión de
los modelos. No era una habilidad sobre *qué* necesitabas, sino sobre *cómo*
pedírselo a un modelo que no te entendía bien.

En otras palabras, la ingeniería de *prompt* era la interfaz de usuario que los
modelos no tenían. Era el equivalente a memorizar comandos de terminal antes de
que existieran las interfaces gráficas: necesario en su momento, pero destinado
a ser absorbido por la evolución de la tecnología.

## La forma de preguntar dejó de ser el problema

Los modelos de lenguaje actuales —Gemini 3, Claude Sonnet 4.5, GPT-5, Llama 4—
son radicalmente diferentes. Entienden instrucciones en lenguaje natural sin
necesidad de formatos rígidos. Pueden manejar contextos extensos, mantener
coherencia en conversaciones largas y, lo más importante, interpretar la
intención detrás de una solicitud imprecisa.

¿Necesitas decirle a Claude Sonnet que "actúe como un experto en X" para que te
dé una buena respuesta? No. ¿Necesitas estructurar tu pregunta con delimitadores
`###` y ejemplos *few-shot* para que Gemini 3 Pro entienda lo que quieres?
Tampoco. Los modelos ya son lo suficientemente capaces de entenderte si les
dices lo que necesitas de manera clara, como se lo dirías a un colega
competente.

Esto no significa que la forma de comunicarse con la IA sea irrelevante. Pero la
barrera dejó de ser técnica. Si sabes expresar lo que necesitas con claridad, el
modelo te va a entender. El problema ya no es el *cómo*, sino el *qué*.

### La excepción: desarrollo de IA

Hay un matiz importante. Para los desarrolladores de IA —quienes construyen
*pipelines* de procesamiento, agentes autónomos o sistemas RAG— la ingeniería de
*prompt* sigue siendo relevante como técnica de optimización. En ese contexto,
estructurar *prompts* del sistema, controlar la temperatura, usar *few-shot*
para tareas de clasificación o definir formatos de salida JSON son decisiones
técnicas válidas que impactan directamente en el rendimiento del sistema.

Pero esto es desarrollo de software, no una "habilidad del futuro" para el
usuario común. Es como decir que saber configurar un servidor web es una
habilidad universal porque todos usamos internet.

## De la ingeniería de *prompt* a la ingeniería de contexto

Si la ingeniería de *prompt* era sobre *cómo* pedirle algo a la IA, la
ingeniería de contexto es sobre *qué* necesitas y *con qué información* la IA
debe trabajar. Este cambio es fundamental.

La ingeniería de contexto se basa en dos pilares:

### 1. Contexto inyectado

Los agentes de IA modernos no trabajan solo con tu mensaje. Trabajan con capas
de contexto que tú configuras previamente:

- **Archivos de contexto**: Definen el comportamiento general, el estilo de
  respuesta, las restricciones y las convenciones que el agente debe seguir. Se
  configuran a nivel global o de proyecto mediante archivos como `AGENTS.md`,
  `CLAUDE.md`, `.cursorrules` o `.agent/rules` (Antigravity), que el agente lee
  automáticamente para entender las convenciones, la arquitectura y las
  decisiones técnicas de tu código.
- **Habilidades del agente** (*agent skills*): Instrucciones especializadas para
  tareas específicas que el agente carga cuando las necesita. Por ejemplo, una
  habilidad para escribir documentación, otra para hacer revisión de código,
  otra para generar pruebas. No es un *prompt* mágico: es una especificación de
  flujo de trabajo.

Nada de esto requiere conocer técnicas de *prompting*. Requiere saber definir
reglas claras, documentar convenciones y estructurar el conocimiento de tu
proyecto.

### 2. Especificaciones claras en el *prompt*

El segundo pilar es lo que realmente escribes en cada interacción. Y aquí está
la clave: no se trata de *cómo* escribirlo (eso es ingeniería de *prompt*), sino
de *qué* escribir. Las habilidades que necesitas son:

- **Diseño de especificaciones**: Saber describir con precisión qué quieres que
  se construya. Requisitos funcionales, restricciones, casos borde, criterios de
  aceptación. Es lo mismo que harías al escribir un *ticket* o una historia de
  usuario bien hecha.
- **Diseño de solución**: Tener una visión clara de cómo debería funcionar la
  solución. No necesitas implementarla, pero sí saber qué componentes
  intervienen, qué datos fluyen y qué resultado esperas.
- **Arquitectura de solución**: Para tareas complejas, saber descomponer el
  problema en partes manejables, definir interfaces entre componentes y
  establecer un orden de ejecución. Esto es pensamiento de ingeniería, no trucos
  de *prompting*.

En resumen: las habilidades que hacen que obtengas buenos resultados de la IA
son las mismas que te hacen un buen profesional. Claridad, precisión,
pensamiento estructurado y capacidad de descomponer problemas.

## Entonces, ¿fue una estafa?

No diría que fue una estafa deliberada, pero sí una habilidad con fecha de
caducidad sobre la que se construyó toda una industria. Los cursos de
"ingeniería de *prompt*" que prometen transformar tu carrera en 2026 están
vendiendo conocimiento obsoleto. Las certificaciones en *prompting* son el
equivalente actual a una certificación en uso de buscadores web en 2005.

Lo que realmente necesitas aprender no tiene nada que ver con trucos de formato.
Necesitas aprender a pensar con claridad, a diseñar soluciones, a escribir
especificaciones que no dejen ambigüedades. Y si trabajas con agentes de IA,
necesitas aprender a configurar su contexto: reglas, habilidades y documentación
de proyecto.

La ingeniería de *prompt* murió. La ingeniería de contexto la reemplazó. Y la
buena noticia es que las habilidades que necesitas para dominarla son las que
siempre han definido a un buen profesional.

## Referencias

- [Context engineering](https://simonwillison.net/2025/Jun/27/context-engineering/).
  Simon Willison.
- [The New Skill in AI is Not Prompting, It's Context Engineering](https://www.philschmid.de/context-engineering).
  Philipp Schmid.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
  Anthropic.
