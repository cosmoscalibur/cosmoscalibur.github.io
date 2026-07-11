---
date: 2026-07-11
tags: antigravity, claude code, google workspace, opinión
category: tecnología
---

# Migrando a Claude Code como alternativa al modo consumo en Antigravity GCP

Me enteré por un *pop-up* en la propia interfaz de Antigravity de que
la herramienta dejaría de estar incluida en la licencia de Google
Workspace corporativa. El cambio se hizo efectivo el 7 de julio de
2026, y mi cuenta de trabajo quedó con el mismo límite de cuota que
cualquier usuario gratuito. Ya había escrito sobre las
[novedades de Antigravity 2](/es/blog/2026/antigravity-2-novedades-para-el-desarrollo-agentico.md)
con bastante entusiasmo, pero este cambio de facturación me llevó a
replantear por completo mi *stack* de desarrollo agéntico, tanto en
lo corporativo como en lo personal.

El recorte no fue un simple ajuste de cuotas. Según se documentó en un
[hilo de la comunidad de Google AI](https://discuss.ai.google.dev/t/antigravity-seems-to-be-soft-deprecated/143615/3),
Google notificó a los administradores de Workspace, alrededor del 5 de
mayo de 2026, que discontinuaría el add-on AI Ultra Access — el plan
de Workspace (~250 USD/mes) que incluía las herramientas de
desarrollo Antigravity, Gemini CLI y los *plugins* de Gemini Code
Assist. Sin intervención del administrador, la organización migra
automáticamente al add-on AI Expanded Access, mucho más económico
(24 USD/mes), que no incluye esas herramientas de desarrollo. El
cambio aplica desde el 7 de julio de 2026 para planes flexibles, y
desde la siguiente renovación posterior a esa fecha para planes
anuales. Al perder ese add-on, no hay una opción intermedia: no
existe un plan de suscripción corporativo de pago para Antigravity
como tal.

## El modo consumo: más factura y sin Claude

El cambio obliga a elegir entre dos caminos, y ninguno es gratuito ni
cómodo. El primero es habilitar el modo de consumo: activar la Agent
Platform API en un proyecto de Google Cloud (GCP) propio o de la
organización, vincular una cuenta de facturación, e iniciar sesión en
Antigravity usando ese proyecto como respaldo. El uso pasa a
facturarse por token y por tiempo de cómputo del *sandbox* del
agente, en lugar de estar incluido en la licencia de Workspace — la
factura sube, sin excepción.

Pero el problema real de este camino no es solo el aumento de costo:
según la
[documentación de modelos de Antigravity](https://antigravity.google/docs/models),
los planes Enterprise —a los que corresponde el modo consumo— solo
ofrecen modelos Gemini. Los modelos de Anthropic están disponibles
únicamente en los planes personales. Para cualquier equipo corporativo
que dependa de Claude para su flujo de trabajo agéntico, este es el
punto crítico: la vía "oficial" para seguir usando Antigravity como
empresa te deja, en la práctica, sin acceso a Anthropic.

Es un problema real de SLA: Google actúa como enrutador hacia una
infraestructura de un tercero que no aloja ni opera directamente, y
por eso no puede extender a sus clientes Enterprise la misma garantía
de servicio que ofrecería sobre su propia infraestructura.

## Cuenta personal: Claude 4.6 sin actualización a la vista

El segundo camino es no habilitar el modo consumo y quedarse con una
cuenta personal de pago. Ahí sí aparece Claude en el selector — pero
el modelo de Anthropic más reciente disponible sigue siendo Claude
4.6, sin ninguna mención de una actualización cercana, mientras
Anthropic ya lleva tres versiones adelante: 4.7, 4.8 y 5.

Esto es lo más frustrante del asunto, porque la experiencia de
desarrollador en Antigravity me sigue pareciendo, en varios aspectos,
mejor que la de Claude Code: soporte nativo de proyectos *multirepo*,
gestión de *worktree* por conversación sin intervención manual, la
posibilidad de dejar comentarios in situ sobre los artefactos que
produce el agente, y estándares ya compartidos con Claude Code como
AGENTS.md. Pero todas esas ventajas se vuelven
irrelevantes —incluso en contra— si el modelo detrás no está a la
altura de la tarea. Un IDE brillante orquestando un modelo
desactualizado sigue produciendo peor código que un CLI más austero
orquestando el mejor modelo disponible.

Ante la falta de modelos actualizados de Anthropic —ya sea porque el
modo consumo simplemente no ofrece Claude, o porque la cuenta personal
lo deja atascado en 4.6—, probé en serio usar Gemini Flash y Gemini
Pro como motor principal dentro de Antigravity para tareas reales de
desarrollo. La experiencia no fue agradable: en tareas de
refactorización con contexto amplio, en seguir instrucciones de estilo
de código específicas del proyecto, y en la calidad general de los
*diffs* propuestos, ambos modelos quedaron consistentemente por
debajo de lo que ya obtenía con Claude en el mismo IDE. No es un
rechazo genérico a los modelos de Google — para otras tareas
seguramente rinden bien — pero para el tipo de trabajo agéntico de
codificación que hago a diario, la diferencia fue lo bastante notoria
como para descartarlos como opción principal.

## Mi decisión: migrar a Claude Code

Con las dos rutas agotadas —modo consumo sin Claude, o cuenta personal
con Claude estancado— la decisión fue sencilla, aunque incómoda: migro
mi flujo de trabajo, personal y corporativo, a Claude Code.

Prefiero la curva de aprendizaje y la fricción de un control paso a
paso más estricto, con un modelo actualizado detrás, que la comodidad
de un IDE superior atado a un catálogo de modelos que o no incluye
Claude, o lo deja obsoleto. Esto no cierra la puerta a Antigravity —
si Google conecta Claude en el modo consumo y actualiza el tope de la
cuenta personal, la ecuación puede cambiar de nuevo. Pero por ahora,
la relación entre la herramienta y el modelo es la que decide cuál
uso, no al revés.

## Conclusión

El recorte de Antigravity para cuentas de Workspace el 7 de julio fue
solo la puerta de entrada a un problema más profundo: ni el modo
consumo ni la cuenta personal dan acceso a un Claude actualizado
dentro de Antigravity. Esa limitación es un problema de SLA
—consecuencia de depender de un tercero que Google no opera
directamente— y de la hoja de ruta de producto de Google. Mientras
esa brecha exista, ninguna ventaja —por buena que sea— compensa
trabajar sin el mejor modelo disponible.

## Referencias

- [Antigravity — Modelos disponibles por plan](https://antigravity.google/docs/models).
  Google.
- [Antigravity seems to be soft-deprecated](https://discuss.ai.google.dev/t/antigravity-seems-to-be-soft-deprecated/143615/3).
  Google AI Developers Forum.
- [Antigravity 2: novedades para el desarrollo agéntico](/es/blog/2026/antigravity-2-novedades-para-el-desarrollo-agentico.md).
  Cosmoscalibur.
