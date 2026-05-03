---
date: 2026-05-02
tags: agentes de código, inteligencia artificial, ingeniería de contexto, antigravity
category: programación
---

# Guía de comportamiento para agentes de código

En mi artículo sobre el
[marco de preparación para agentes](/es/blog/2026/marco-de-preparacion-para-agentes-de-codigo.md)
expliqué cómo evaluar y mejorar un repositorio para que los agentes de
inteligencia artificial trabajen de forma efectiva. Pero preparar el
entorno es solo la mitad del problema. La otra mitad es **decirle al
agente *cómo* comportarse** dentro de ese entorno.

Después de meses usando agentes de código —Antigravity, AmpCode,
Opencode— he notado patrones recurrentes de error que ningún *linter*
atrapa: sobreingeniería silenciosa, cambios cosméticos no solicitados,
suposiciones ocultas que explotan tres *commits* después. Resulta que
no soy el único. Andrej Karpathy
[documentó exactamente estos problemas](https://x.com/karpathy/status/2015883857489522876)
y la comunidad los convirtió en un conjunto de directrices con más de
100.000 estrellas en GitHub.

He integrado esas directrices en mi
[repositorio de plantilla](https://github.com/cosmoscalibur/template)
como parte del archivo `AGENTS.md`, adaptándolas a un formato genérico
que funciona con cualquier agente. Este artículo explica el porqué de
cada principio y cómo aplicarlo en la práctica.

## ¿Por qué los agentes necesitan guías de comportamiento?

Los modelos de lenguaje son herramientas poderosas para generar código,
pero tienen sesgos sistemáticos que afectan la calidad del resultado:

- **Asumen en silencio.** Cuando una instrucción es ambigua, el modelo
  elige una interpretación y avanza sin preguntar. No gestiona su propia
  confusión ni presenta las alternativas.
- **Sobreingenieran.** Prefieren abstracciones, capas de configuración
  y manejo de errores para escenarios imposibles. Donde 50 líneas
  bastarían, escriben 200.
- **Tocan código adyacente.** Mientras implementan lo que pediste,
  "mejoran" comentarios, reformatean funciones cercanas o eliminan
  código que no entienden del todo.

Estos comportamientos no son errores del modelo —son su naturaleza. Los
LLM están entrenados para ser útiles y exhaustivos, lo que en código se
traduce en hacer *más de lo necesario*. Una guía de comportamiento es
el contrapeso: un conjunto de reglas que fuerzan precisión sobre
entusiasmo.

## Los cuatro principios de Karpathy

Las directrices que integré en la plantilla se basan en las
observaciones de Karpathy, sistematizadas por el proyecto
[andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills).
Se resumen en cuatro principios.

### 1. Pensar antes de codificar

> Declara tus suposiciones explícitamente. Si existen múltiples
> interpretaciones, preséntalas —no elijas en silencio. Si algo no está
> claro, detente y pregunta.

Este principio ataca el problema más costoso: el agente que arranca a
implementar sobre una suposición incorrecta. Cuando el agente verbaliza
lo que asume, tú puedes corregirlo antes de que escriba una sola línea
de código.

En la práctica, esto significa que tu `AGENTS.md` debe instruir al
agente a explicitar sus interpretaciones al inicio de cada tarea, no
después de que ya implementó algo.

### 2. Simplicidad primero

> Nada de funcionalidades más allá de lo pedido. Nada de abstracciones
> para código de uso único. Nada de manejo de errores para escenarios
> imposibles. Si escribes 200 líneas y podrían ser 50, reescribe.
> Pregúntate: "¿Un ingeniero *senior* diría que esto está
> sobrecomplicado?" Si la respuesta es sí, simplifica.

La sobreingeniería es el pecado favorito de los LLM. Este principio
establece un test concreto: ¿un *senior* lo consideraría excesivo?
Es un filtro sorprendentemente efectivo porque obliga al modelo a
evaluar su propia salida contra el estándar de un profesional
experimentado.

### 3. Cambios quirúrgicos

> No "mejores" código adyacente, comentarios o formato. No refactorices
> lo que no está roto. Sigue el estilo existente. Elimina solo
> importaciones, variables o funciones que TUS cambios dejaron sin uso.
> Cada línea cambiada debe rastrearse directamente a la solicitud del
> usuario.

Este principio protege la base de código de la entropía. Sin él, cada
tarea del agente deja un rastro de cambios no solicitados que
contaminan los *diffs*, dificultan la revisión de código y
potencialmente introducen regresiones.

La regla de rastreo directo ("cada línea cambiada debe rastrearse a la
solicitud") es particularmente valiosa en equipos: si un *pull request*
contiene cambios que nadie pidió, algo falló.

### 4. Ejecución orientada a metas

> Transforma las tareas en metas verificables:
>
> - "Añade validación" → "Escribe pruebas para entradas inválidas,
>   luego haz que pasen"
> - "Corrige el *bug*" → "Escribe una prueba que lo reproduzca, luego
>   haz que pase"
> - "Refactoriza X" → "Asegura que las pruebas pasen antes y después"

Como señaló Karpathy: "Los LLM son excepcionalmente buenos iterando
hasta alcanzar metas específicas. No les digas qué hacer, dales
criterios de éxito y observa cómo los cumplen." Este principio
aprovecha esa fortaleza: en lugar de instrucciones imperativas, le das
criterios de verificación que el agente puede evaluar por sí mismo.

## Cómo integrar las guías en tu proyecto

Las directrices están integradas directamente en el `AGENTS.md` del
[repositorio de plantilla](https://github.com/cosmoscalibur/template).
Si usas la plantilla como base para nuevos proyectos, las obtienes
automáticamente.

Si ya tienes un proyecto existente, la integración es sencilla.
Añade una sección `## Behavioral Guidelines` a tu `AGENTS.md` (o
al archivo de instrucciones equivalente de tu agente) con las cuatro
reglas:

```{code} markdown
## Behavioral Guidelines

- **Think before coding.** State assumptions explicitly. If multiple
  interpretations exist, present them — don't pick silently.
- **Simplicity first.** No features beyond what was asked. No
  abstractions for single-use code.
- **Surgical changes.** Don't "improve" adjacent code. Match existing
  style. Every changed line should trace to the user's request.
- **Goal-driven execution.** Transform tasks into verifiable goals
  with tests as success criteria.
```

Dado que todos los agentes principales —incluyendo Antigravity desde
marzo de 2026— soportan `AGENTS.md` de forma nativa, estas directrices
funcionan de manera uniforme independientemente de la herramienta que
uses.

## La nota sobre el equilibrio

Un punto importante del proyecto original que conservé en la plantilla:
estas directrices sesgan hacia la cautela sobre la velocidad. Para
tareas triviales —correcciones de *typos*, cambios obvios de una
línea— el agente debería usar su juicio y no aplicar toda la
rigurosidad.

La meta es reducir errores costosos en trabajo no trivial, no
ralentizar las tareas simples.

## Conclusión

Preparar un repositorio para agentes de código requiere dos capas
complementarias: la **infraestructura** (documentación, pruebas,
*linting*, CI —cubierta por el
[marco de preparación](/es/blog/2026/marco-de-preparacion-para-agentes-de-codigo.md))
y el **comportamiento** (cómo el agente decide qué hacer y qué no
hacer). Las directrices de Karpathy cubren esta segunda capa con
cuatro principios simples que atacan los problemas más frecuentes de
los LLM en generación de código.

Si ya evaluaste tu repositorio con la
[habilidad de *agent readiness*](https://github.com/cosmoscalibur/template/tree/main/.agents/skills/agent-readiness)
y llegaste al nivel 2 o superior, añadir estas directrices de
comportamiento es el siguiente paso natural. El repositorio
[cosmoscalibur/template](https://github.com/cosmoscalibur/template)
las incluye listas para usar.

## Referencias

- [Andrej Karpathy sobre errores de LLM en código](https://x.com/karpathy/status/2015883857489522876).
  Andrej Karpathy, X.
- [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills).
  Forrest Chang. GitHub.
- [Agent-Ready Repository Template](https://github.com/cosmoscalibur/template).
  Cosmoscalibur. GitHub.
- [Marco de preparación para agentes de código](/es/blog/2026/marco-de-preparacion-para-agentes-de-codigo.md).
  Cosmoscalibur.
