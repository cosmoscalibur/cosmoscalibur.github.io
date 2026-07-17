# Convenciones del contenido

Este documento define las convenciones técnicas y editoriales que sigue
toda entrada del blog — sin importar si la escribe un humano o un agente
de código. Es la fuente única: ni `CLAUDE.md` ni las skills bajo
`.claude/skills/blog-*` repiten estas reglas, las referencian. El flujo
agéntico en etapas (investigación, planeación, escritura, revisión,
publicación) y sus puntos de control están orquestados en `CLAUDE.md`, no
aquí.

Para instalar y ejecutar el sitio, ver `README.md`.

## Categorías

`category:` en el frontmatter, separadas por coma si aplica más de una:

| Categoría | ES | EN |
|---|---|---|
| Ciencia | `ciencia` | `science` |
| Linux | `linux` | `linux` |
| Programación | `programación` | `programming` |
| Tecnología | `tecnología` | `technology` |
| Literario/poesía | `La flecha temporal` | *(sin página en inglés)* |

## Frontmatter

YAML para entradas `.md`/`.ipynb`:

- `date` (obligatorio, `YYYY-MM-DD`) — una fecha futura excluye la entrada
  de listados/feeds hasta esa fecha, útil para programar publicaciones.
- `tags` — lista separada por comas.
- `category` — lista separada por comas, según la tabla anterior.
- `language` no es necesario — se infiere de la ruta `{lang}/blog/...`.
- No existe un campo `description` — el meta-description se autogenera a
  partir de los primeros ~200 caracteres del cuerpo tras el H1 (los
  admonitions se omiten). El párrafo inicial de toda entrada cumple ese
  doble propósito: gancho narrativo y descripción para buscadores.

## Slug en relación al título

El slug se deriva de forma determinista a partir del título en español,
por normalización de caracteres — nunca se eliminan palabras:

1. Minúsculas.
2. Quitar tildes/diacríticos.
3. Quitar puntuación.
4. Espacios a guiones.
5. Máximo ~60 caracteres.
6. La versión en inglés (si existe) reutiliza el mismo slug y el mismo
   directorio `images/{slug}/` — no se traduce el slug.

Ruta de archivo: `{lang}/blog/{año}/{slug}.md` (o `.rst`/`.ipynb`).
Imágenes: `/images/{slug}/`.

## Convenciones de MystMD

- **Markdown vs. notebook**: usar `.ipynb` (vía jupytext) solo cuando la
  entrada necesita salida ejecutada de verdad (gráficas calculadas,
  resultado de comandos capturado en vivo). Markdown plano en cualquier
  otro caso — un notebook añade complejidad de build que no se justifica
  para una entrada de solo texto.
- **Admonitions**: en inglés, los directivos nativos (`{note}`,
  `{important}`, `{hint}`, `{warning}`) funcionan directamente. En
  **español**, el locale de Sphinx no localiza sus títulos, así que se usa
  `{admonition}` con `class:` explícito:
  ```
  ```{admonition} Nota
  ---
  class: tip
  ---
  Contenido de la nota.
  ```
  ```
- **`{update}`**: para un addendum fechado a una entrada existente (alimenta
  `dateModified` en JSON-LD y el feed Atom):
  ```
  ```{update} YYYY-MM-DD
  Qué cambió y por qué.
  ```
  ```
- **`{figure}`**: toda imagen lleva un `alt:` real y descriptivo — nunca un
  nombre de archivo, nunca "imagen"/"screenshot". Nada en el pipeline de
  build detecta un alt vacío o ausente.
  ```
  ```{figure} /images/{slug}/nombre.webp
  ---
  alt: Descripción concreta de lo que muestra la imagen
  align: center
  width: 800px
  ---
  Texto de la leyenda.
  ```
  ```
  El orden importa: la primera imagen de la entrada se trata como
  candidata a LCP y se carga eager; el resto se carga lazy
  automáticamente. Coloca la imagen más relevante primero — es la única
  palanca disponible, ya que ancho/alto/`loading` se inyectan solos.
- **Referencias cruzadas internas**: enlace Markdown plano dentro de una
  frase, nunca el rol `{ref}`.
- **`sphinx-design`** (`{tab-set}`, `{dropdown}`, `{card}`, `{grid}`):
  usar solo ante una necesidad estructural real (p. ej. mostrar sintaxis
  RST vs. MD en paralelo) — cualquier directivo de sphinx-design usado en
  una página mantiene su CSS cargado en esa página. Preferir por defecto
  los elementos nativos de MyST (admonitions, listas de definición,
  `{figure}`).
- ~80 caracteres de ancho de línea en el fuente. Sin comentarios HTML al
  final del archivo.

## Flujo de `just`

- `just serve` — servidor local con recarga para iterar mientras se
  escribe.
- `just build` — build local (analítica de desarrollo) para verificar que
  una entrada renderiza sin errores/warnings de Sphinx antes de darla por
  revisada.
- `just deploy` — build de producción (analítica real) — la validación
  final antes de publicar.
- `just publish "<mensaje>"` — `git add` + `git commit` + `git push` en un
  solo paso. Es una conveniencia posterior a la aprobación del mensaje de
  commit, nunca una forma de saltarla — ver la sección de seguridad de git
  en `CLAUDE.md`.
