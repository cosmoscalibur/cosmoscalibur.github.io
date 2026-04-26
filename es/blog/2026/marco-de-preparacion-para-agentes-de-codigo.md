---
date: 2026-03-07
tags: agentes de código, antigravity, ingeniería de contexto, inteligencia artificial
category: programación
---------------------

# Marco de preparación para agentes de código

Los agentes de código están aquí, y no van a irse. Pero después de meses
usándolos —Antigravity, AmpCode, Opencode, el agente de Zed— he llegado a
una conclusión incómoda: **el problema no suele ser el agente, sino el
proyecto**. Un repositorio mal preparado derrota a cualquier agente, sin
importar qué tan avanzado sea el modelo que tenga detrás.

En mi publicación sobre
[ingeniería de contexto](/es/blog/2026/ingenieria-de-prompt-habilidad-o-estafa.md),
hablé de cómo el paradigma cambió del *cómo* preguntarle a la IA al *qué*
darle como contexto. Este artículo es la continuación natural: un marco
metódico para preparar tu repositorio y convertirlo en un entorno donde los
agentes (y los humanos) puedan trabajar de forma efectiva.

El marco que presento se basa en el *Agent Readiness Model* de
[Factory AI](https://factory.ai/news/agent-readiness), que propone cinco
niveles de madurez y nueve pilares técnicos para evaluar qué tan preparado
está un repositorio para el desarrollo autónomo. Lo adapto aquí con mi
experiencia práctica y con una consideración especial para quienes usan
Antigravity, cuyo sistema de contexto difiere del estándar `AGENTS.md`.

## ¿Qué es el marco de preparación para agentes?

Es un modelo de madurez que mide qué tan listo está tu repositorio para que
agentes de IA trabajen en él de forma autónoma. No evalúa al agente, evalúa
al proyecto: su documentación, *tooling*, pruebas, seguridad y
convenciones.

La premisa fundamental es que **el agente no es mágico**. Es tan bueno
como el entorno que le proporcionas. Un repositorio con *hooks* de
*pre-commit*, pruebas rápidas y documentación clara permite que el agente
itere en segundos. Uno sin esas bases obliga al agente a adivinar, esperar
minutos por retroalimentación de CI, y repetir errores que una verificación
local habría atrapado al instante.

Lo mejor: cada mejora que hagas para los agentes beneficia igualmente a
los desarrolladores humanos del proyecto.

## Los cinco niveles de preparación

El modelo define cinco niveles progresivos. Para desbloquear el siguiente,
necesitas cumplir al menos el 80% de los criterios del nivel actual.

### Nivel 1: Funcional

El código compila y se ejecuta, pero requiere configuración manual y carece
de validación automatizada. Es el mínimo que cualquier repositorio debería
tener.

**Criterios clave:**

- {file}`README.md` con instrucciones de configuración y ejecución.
- *Linter* configurado (ejemplo: {program}`ruff` para Python,
  {program}`eslint` para JavaScript).
- Verificador de tipos (ejemplo: {program}`pyright`, TypeScript *strict*).
- Pruebas unitarias existentes y ejecutables localmente.
- Formateador de código configurado.

**Sin esto:** El agente no puede verificar su propio trabajo. Genera
código, espera al CI (si existe), falla, e itera a ciegas.

### Nivel 2: Documentado

La documentación básica y los procesos existen. Los flujos de trabajo están
escritos y hay algo de automatización.

**Criterios clave:**

- `AGENTS.md` o archivo equivalente de instrucciones para agentes con
  comandos, convenciones y límites.
- *Devcontainer* o entorno de desarrollo reproducible.
- *Hooks* de *pre-commit* configurados.
- Protección de ramas (*branch protection*) habilitada.
- Variables de entorno documentadas (ejemplo: {file}`.env.example`).

**Sin esto:** El agente tiene que descubrir cómo funciona tu proyecto por
su cuenta. Adivina convenciones, no sabe qué comandos ejecutar, y no tiene
guardarraíles de seguridad.

### Nivel 3: Estandarizado

Procesos claros definidos, documentados y aplicados mediante automatización.
**Este es el objetivo mínimo para trabajo productivo con agentes.**

**Criterios clave:**

- Pruebas de integración y/o *end-to-end*.
- Escaneo de secretos (*secret scanning*).
- Trazabilidad distribuida y métricas (*observability*).
- Documentación mantenida y actualizada.
- {file}`CODEOWNERS` configurado.

**Sin esto:** El agente puede manejar tareas simples pero introduce
errores sutiles en flujos complejos que solo pruebas de integración
atraparían.

### Nivel 4: Optimizado

Ciclos de retroalimentación rápidos y mejora basada en datos. Los sistemas
están diseñados para productividad y se miden continuamente.

**Criterios clave:**

- CI con retroalimentación rápida (minutos, no horas).
- Frecuencia de despliegue regular.
- Detección de pruebas inestables (*flaky tests*).
- Métricas de rendimiento del equipo.

**Sin esto:** El agente funciona, pero lento. Espera demasiado por
retroalimentación y no puede iterar a la velocidad que su capacidad
permite.

### Nivel 5: Autónomo

Sistemas auto-mejorables con orquestación sofisticada. Requerimientos
complejos se descomponen automáticamente en ejecución paralela.

Este nivel representa el objetivo a largo plazo: el agente no solo
implementa, sino que descubre trabajo, prioriza, ejecuta y verifica de
forma autónoma.

## Los nueve pilares técnicos

Cada nivel se evalúa a través de nueve pilares que cubren las dimensiones
fundamentales de un repositorio:

1. **Estilo y validación**: *Linters*, formateadores, verificadores de
   tipos, *pre-commit hooks*.
2. **Sistema de compilación**: Comandos deterministas, dependencias fijadas,
   compilación documentada.
3. **Pruebas**: Unitarias, integración, ejecutables localmente, cobertura.
4. **Documentación**: *README*, `AGENTS.md`, guías de arquitectura,
   convenciones de código.
5. **Entorno de desarrollo**: *Devcontainer*, plantillas de entorno,
   configuración de servicios locales.
6. **Depuración y observabilidad**: *Logging* estructurado, trazabilidad
   distribuida, métricas.
7. **Seguridad**: Protección de ramas, escaneo de secretos, *CODEOWNERS*.
8. **Descubrimiento de tareas**: Plantillas de *issues*, sistema de
   etiquetas, plantillas de PR.
9. **Producto y experimentación**: Analítica, *feature flags*,
   infraestructura de experimentos.

```{admonition} Nota
---
class: tip
---
No necesitas cumplir todos los pilares para empezar. Concéntrate en los
pilares de los niveles 1 y 2 primero: estilo, compilación, pruebas y
documentación. Son los que mayor impacto tienen en la calidad del trabajo
del agente.
```

## La documentación de agentes: `AGENTS.md` y sus alternativas

Un componente central del nivel 2 es el archivo de instrucciones para
agentes. `AGENTS.md` se ha convertido en el estándar emergente, adoptado
por más de 60.000 repositorios en GitHub y respaldado por la Agentic AI
Foundation bajo la Linux Foundation.

Un buen `AGENTS.md` incluye:

- Comandos de compilación, pruebas y verificación de estilo copiables.
- Convenciones de código y patrones preferidos.
- Estructura del proyecto y ubicación de archivos clave.
- Límites: qué no debe tocar el agente, qué decisiones de arquitectura
  son inamovibles.
- Instrucciones de pruebas y *workflow* de git.

`CLAUDE.md` fue el precursor creado por Anthropic para Claude Code, y
`AGENTS.md` es su evolución estandarizada que funciona con la mayoría de
agentes: GitHub Copilot, AmpCode, Cursor, Opencode, Zed, y otros.

### Particularidad de Antigravity

Si usas Antigravity como IDE principal (como es mi caso), hay un detalle
importante: **Antigravity no lee `AGENTS.md` ni `CLAUDE.md`
automáticamente**. Su sistema de contexto utiliza
{file}`.agent/rules/` para reglas del espacio de trabajo y
{file}`~/.gemini/GEMINI.md` para la configuración global.

Esto no invalida el marco —los cinco niveles y nueve pilares aplican
igual—, pero requiere una adaptación en cómo proporcionas el contexto al
agente:

1. **Mantener la documentación en {file}`README.md` y {file}`docs/`**, como
   fuente de verdad compartida entre humanos y agentes.
2. **Crear una regla de agente** en {file}`.agent/rules/` que instruya
   explícitamente al agente a leer esa documentación antes de actuar.
3. **Opcionalmente, mantener `AGENTS.md`** para las herramientas que lo
   soporten. La fuente de verdad sigue siendo tu documentación.

Un ejemplo de regla en {file}`.agent/rules/documentation-first.md`:

```{code} markdown
Before starting any task in this project, read the following files:
- README.md for project overview and setup
- docs/architecture.md for system architecture
- docs/conventions.md for coding conventions
Follow the guidelines in these documents for all code generation.
```

De esta forma, un solo conjunto de documentación sirve para todos los
agentes y para cualquier desarrollador humano.

## Evalúa tu repositorio

He creado una
[habilidad de agente](https://github.com/cosmoscalibur/template/tree/main/.agents/skills/agent-readiness)
que automatiza la evaluación de preparación para agentes. La habilidad
audita los nueve pilares, asigna una puntuación por criterio (✅ pasa /
⚠️ parcial / ❌ falla), determina el nivel actual del repositorio y
genera un plan de mejora por fases.

La habilidad está diseñada como un *agent skill* estándar, compatible con
Antigravity y otros agentes que soporten el formato de habilidades. Puedes
copiarla a tu proyecto y ejecutarla desde tu agente.

Incluye:

- Detección automática del ecosistema (Python, Rust, Node, Go, etc.).
- Evaluación detallada de los nueve pilares con evidencia por criterio.
- Evaluación de calidad del contenido de contexto del agente (no solo si
  existe el archivo, sino si el contenido es útil).
- Recomendaciones de modernización (ejemplo: migrar de {program}`pylint`
  a {program}`ruff`, de {program}`pip` a {program}`uv`).
- Plan de implementación por fases con marcadores de cambios
  `[NEW]` / `[MODIFY]` / `[DELETE]`.

## Conclusión

La preparación para agentes no es un concepto abstracto. Es un conjunto
concreto de prácticas que puedes medir, mejorar iterativamente y que
benefician a todos los que trabajan en el proyecto —humanos y agentes por
igual.

El *Agent Readiness Model* proporciona una hoja de ruta clara: empieza
por el nivel 1, llega al nivel 3 como mínimo viable para trabajo
productivo con agentes, y sigue avanzando. La inversión no se pierde cuando
cambies de agente o de herramienta, porque estás mejorando el proyecto, no
optimizando para un *prompt*.

Como dije en mi artículo sobre
[ingeniería de contexto](/es/blog/2026/ingenieria-de-prompt-habilidad-o-estafa.md):
las habilidades que hacen que obtengas buenos resultados de la IA son las
mismas que te hacen un buen profesional. Este marco es la expresión
práctica de esa idea.

## Referencias

- [Introducing Agent Readiness](https://factory.ai/news/agent-readiness).
  Factory AI.
- [Agent Readiness Overview](https://docs.factory.ai/web/agent-readiness/overview).
  Factory AI Documentation.
- [AGENTS.md](https://agents.md/). AGENTS.md.
- [How to write a great agents.md: Lessons from over 2,500 repositories](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/).
  GitHub Blog.
- [Is your repo ready for the AI Agents revolution? Checklist](https://domizajac.medium.com/is-your-repo-ready-for-the-ai-agents-revolution-926e548da528).
  Dominika Zając.
- [Rules / Workflows](https://antigravity.google/docs/rules-workflows).
  Google Antigravity Documentation.
- [Agent Readiness Skill](https://github.com/cosmoscalibur/template/tree/main/.agents/skills/agent-readiness).
  Cosmoscalibur.
