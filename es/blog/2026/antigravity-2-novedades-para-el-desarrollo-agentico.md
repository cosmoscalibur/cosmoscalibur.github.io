---
date: 2026-05-28
tags: antigravity, agentes de código, inteligencia artificial, ide
category: tecnología
---

# Antigravity 2: novedades para el desarrollo agéntico

Ya había compartido mi experiencia con
[Antigravity como entorno de desarrollo con inteligencia artificial](/es/blog/2026/herramientas-de-ia-gratuita-para-desarrolladores-en-2026.md),
cubriendo modelos, cuotas y flujos básicos. Pero desde el lanzamiento de
Antigravity 2.0 en mayo de 2026, la herramienta dio un salto que
cambió mi forma de trabajar con agentes de código. Ya no se trata solo
de un IDE con un agente integrado: ahora es una plataforma de
orquestación de agentes autónomos.

En este artículo comparto las novedades que más impacto han tenido en
mi flujo de trabajo diario, una comparativa honesta con Claude Code,
y cómo instalar todo en Arch y Manjaro.

## Antigravity como producto modular

Lo primero que hay que entender de Antigravity 2 es que ya no es un
producto monolítico. Ahora se compone de tres piezas complementarias
que comparten el mismo motor de agentes:

- **Antigravity 2.0** (aplicación de escritorio): el centro de mando
  para orquestación de agentes. Una GUI potente, versátil, ideal para
  quienes prefieren interfaces visuales o no tienen familiaridad con
  editores en modo CLI.
- **Antigravity CLI**: una TUI construida en Go, ligera y rápida.
  Integración nativa con terminales y editores existentes como Neovim
  o tmux, y funciona perfectamente vía SSH. Las sesiones son
  intercambiables con la aplicación de escritorio.
- **Antigravity IDE**: un *fork* de VS Code con integración profunda
  de agentes para quienes prefieren ese ecosistema.

Los tres comparten *backend*, reglas, *skills*, *hooks* y concepto de
proyecto. Esta modularidad es clave porque significa que Antigravity
cubre tanto al desarrollador visual como al purista de terminal, sin
obligar a elegir un solo flujo de trabajo.

## Novedades clave en Antigravity 2

### *Worktrees* nativos para desarrollo en paralelo

Antes de la versión 2, desarrollar características simultáneas en un
mismo repositorio era un ejercicio de paciencia. El flujo típico
implicaba `git checkout` constante para saltar entre ramas, o gestionar
manualmente *worktrees* con `git worktree add`. Ambas opciones
interrumpían el contexto del agente y del desarrollador.

Antigravity 2 integra *worktrees* de forma nativa. Al iniciar una
conversación, se puede seleccionar el modo *worktree* y el IDE
provisiona automáticamente un directorio aislado en segundo plano. Esto
permite que varios agentes trabajen en ramas separadas de forma
simultánea sin interferencias.

En la práctica, esto significa que puedo tener un agente corrigiendo un
*bug* en `fix/auth-error` mientras otro desarrolla una característica
nueva en `feature/dashboard`, cada uno en su propio *worktree*, sin que
uno pise los cambios del otro. Al terminar, el *worktree* se limpia
automáticamente.

### Concepto de proyecto multi-repositorio

Muchos proyectos reales no viven en un solo repositorio. Un *backend*
en un lado, un *frontend* en otro, quizás una biblioteca compartida en
un tercero. Antes de Antigravity 2, cada repositorio era un contexto
aislado y coordinar intervenciones entre ellos requería esfuerzo
manual.

El concepto de proyecto en Antigravity 2 permite agrupar múltiples
carpetas en una unidad lógica con configuración compartida de agentes,
reglas y permisos. Esto es especialmente útil para proyectos *full
stack* donde un cambio en la API del *backend* requiere actualizar el
*frontend* de forma coordinada.

Además, el proyecto funciona como una capa de memoria persistente
entre sesiones. El contexto del proyecto — preferencias, decisiones
previas, hechos relevantes del *codebase* — se mantiene y se inyecta
en sesiones nuevas. Esto evita tener que re-explicar el contexto cada
vez que inicio una conversación, algo que en herramientas sin este
concepto genera fricción constante.

### Gestión de *hooks* y tareas asíncronas

En la versión anterior, lanzar un *build*, ejecutar *tests* o
cualquier proceso de larga duración bloqueaba la conversación. El
agente quedaba esperando la salida del comando y no podía avanzar en
otras tareas. Era un cuello de botella silencioso pero real.

Antigravity 2 introduce *hooks* en formato JSON que permiten
interceptar y controlar el comportamiento del agente ante ciertos
eventos. Combinado con la gestión asíncrona de tareas, el agente
principal puede continuar trabajando mientras un *build* o un conjunto
de *tests* se ejecuta en segundo plano. Al terminar, se recibe una
notificación con el resultado.

Esto reduce drásticamente los tiempos muertos. En lugar de sentarme a
esperar que termine un *pipeline* de CI para recién entonces pedir al
agente que corrija los errores, el flujo es continuo: el agente
monitorea, se notifica y actúa.

### Subagentes dinámicos para contexto limpio

Este es probablemente el cambio más transformador. En conversaciones
largas y complejas, el contexto se contamina inevitablemente. El
agente acumula información de subtareas completadas, intentos fallidos
y decisiones intermedias que ya no son relevantes, pero que ocupan
espacio en la ventana de contexto y pueden confundir respuestas
futuras.

Los subagentes dinámicos resuelven esto delegando subtareas a agentes
especializados con su propio contexto aislado. El agente principal
define un subagente, le asigna una tarea concreta y recibe el
resultado sin heredar todo el contexto intermedio.

La ventaja es doble:

- **Contexto limpio**: el agente principal mantiene su ventana de
  contexto enfocada en la tarea de alto nivel.
- **Ejecución en paralelo**: múltiples subagentes pueden trabajar
  simultáneamente en tareas independientes.

En mi flujo habitual, uso subagentes para investigación de *codebase*
mientras el agente principal implementa código. El subagente de
investigación lee archivos, busca en la web y reporta hallazgos, todo
sin contaminar el contexto de implementación.

### Tareas programadas con *cron* y temporizadores

Esta *feature* me resolvió un problema muy específico que ilustra
perfectamente su utilidad. Estaba iterando en el desarrollo de una
integración con una API cuya cuota gratuita era muy reducida. Al
agotar la cuota, normalmente habría tenido que abandonar la sesión y
volver a retomar el trabajo horas después, reconstruyendo todo el
contexto.

Con las tareas programadas de Antigravity 2, en lugar de eso, programé
un temporizador para la hora exacta de renovación de la cuota. El
agente no simplemente lanzó un comando diferido — quedó pendiente de
la señal, retomó la iteración automáticamente y continuó el ciclo de
desarrollo sin intervención humana.

La diferencia con un simple `sleep` o un *cron* del sistema es
fundamental: aquí el agente mantiene el contexto completo de la tarea,
entiende qué estaba haciendo antes de la pausa y sabe cómo continuar.
Es la diferencia entre delegar a un colega que recuerda todo el
proyecto y poner una alarma para recordarte a ti mismo.

## Antigravity 2 frente a Claude Code

Ambas herramientas lideran el espacio de codificación agéntica, pero
con filosofías muy distintas. Después de usar ambas extensamente, esta
es mi valoración.

### Ventajas de Antigravity

- **Cobertura de perfiles**: GUI (aplicación de escritorio), CLI
  (terminal) e IDE (VS Code) — un mismo motor para todo tipo de
  desarrollador. Claude Code solo ofrece CLI.
- **Soporte multi-modelo**: Gemini, Claude y GPT en un solo entorno,
  sin necesidad de cambiar de herramienta para aprovechar las
  fortalezas de cada modelo.
- **Estándares compartidos**: adopción de AGENTS.md y MCP como
  protocolos de interoperabilidad.
- **Orquestación avanzada**: subagentes dinámicos, *worktrees*
  nativos, proyectos multi-repositorio con memoria persistente y
  tareas programadas — todo integrado nativamente.
- **Paridad en terminal**: {program}`antigravity-cli` iguala a Claude
  Code en integración con terminales, editores y huella ligera de
  recursos. El argumento de que Claude Code es "más ligero" no aplica
  cuando se compara con el CLI.

### Ventajas de Claude Code

- **Control secuencial estricto**: su modelo de aprobación explícita
  paso a paso es muy predecible, ideal para entornos de producción
  donde la supervisión debe ser rigurosa.
- **Ecosistema MCP maduro**: por su mayor antigüedad, cuenta con más
  integraciones de terceros y servidores MCP disponibles.
- **Madurez en *auto-memory***: aunque el concepto de proyecto de
  Antigravity ofrece funcionalidad equivalente, la memoria automática
  de Claude Code tiene más iteraciones de refinamiento.

### ¿Cuándo elegir cada uno?

Mi punto personal: Antigravity cubre tanto al desarrollador visual
como al de terminal, mientras Claude Code solo atiende al segundo.
Para quien ya vive en el ecosistema de Google o necesita orquestación
de múltiples agentes, Antigravity es la elección natural. Claude Code
brilla cuando necesitas control granular paso a paso y trabajas
exclusivamente en terminal.

## Instalación de Antigravity en Arch y Manjaro desde el AUR

La filosofía modular de Antigravity se refleja en su distribución.
Cada componente tiene su propio paquete en el AUR, lo que permite
instalar exactamente lo que necesitas:

- {program}`antigravity` — aplicación de escritorio, centro de mando.
- {program}`antigravity-cli` — agente en terminal.
- {program}`antigravity-ide` — *fork* de VS Code con agentes
  integrados.

La instalación desde el AUR se realiza con {program}`pamac`:

```{code} bash
pamac build antigravity antigravity-cli antigravity-ide
```

```{admonition} Nota sobre Wayland
---
class: tip
---
Si la aplicación se abre con una ventana en blanco en Wayland, lánzala
con el *flag* `--ozone-platform-hint=auto`. Para hacerlo permanente,
edita el archivo {file}`.desktop` correspondiente y agrega el *flag*
al campo `Exec=`.
```

Para otras distribuciones de Linux, la instalación general se realiza
descargando el archivo tar desde la
[página oficial de descarga](https://antigravity.google/download).

## Conclusión

Antigravity 2 no es una actualización incremental. Los *worktrees*
nativos, el concepto de proyecto, los subagentes dinámicos y las
tareas programadas transforman fundamentalmente la relación entre
desarrollador y agente. Ya no se trata de pedir ayuda línea por línea:
se trata de orquestar un equipo de agentes autónomos que trabajan en
paralelo mientras mantienes la visión de alto nivel.

El futuro de los IDE no es solo asistir, sino orquestar.

## Referencias

- [Antigravity — Documentación oficial](https://antigravity.google/).
  Google.
- [Antigravity 2.0 — What's new](https://antigravity.google/whats-new).
  Google.
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code).
  Anthropic.
- [Antigravity AUR packages](https://aur.archlinux.org/packages?K=antigravity).
  Arch Linux.
- [Herramientas de IA gratuita para desarrolladores en 2026](/es/blog/2026/herramientas-de-ia-gratuita-para-desarrolladores-en-2026.md).
  Cosmoscalibur.
