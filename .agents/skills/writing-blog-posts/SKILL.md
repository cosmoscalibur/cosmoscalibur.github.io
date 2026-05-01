---
name: writing-blog-posts
description: Creates bilingual blog posts (Spanish/English) for Cosmoscalibur. Use when asked to write, create, or draft a blog post, article, or entry.
---

# Writing Blog Posts

Creates blog posts for the Cosmoscalibur blog, a bilingual (Spanish/English)
personal blog built with Sphinx and ABlog using MyST Markdown.

## File Structure

Posts are organized by language and year:

```
es/blog/{year}/{slug}.md      # Spanish version (primary)
en/blog/{year}/{slug}.md      # English version
images/{slug}/                 # Images directory (if needed)
```

- The **slug** is always in Spanish (see
  [Title & Slug Strategy](#title--slug-strategy) for derivation rules). Used
  for both `es/` and `en/` paths.
- The **year** is the publication year (use today's date).
- For code-heavy posts with executable examples, use Jupyter Notebooks
  (`.ipynb`) instead of `.md`.

## Frontmatter

### Markdown posts (`.md`)

**Spanish (primary):**

```yaml
---
date: YYYY-MM-DD
tags: tag1, tag2, tag3
category: categoría1, categoría2
---
```

**English:**

```yaml
---
date: YYYY-MM-DD
tags: tag1, tag2, tag3
category: category1, category2
language: en
---
```

Note: English posts include `language: en`. Spanish posts do not include a
`language` field.

### Jupyter Notebook posts (`.ipynb`)

Metadata goes in the notebook's top-level `metadata` object (not in a cell):

```json
{
  "metadata": {
    "date": "YYYY-MM-DD",
    "tags": "tag1, tag2, tag3",
    "category": "categoría1, categoría2",
    "kernelspec": { ... },
    "language_info": { ... }
  }
}
```

English notebooks include `"language": "en"` in metadata. Tags and categories
are translated.

### Categories Reference

Spanish categories and their English equivalents (source of truth: manual pages
in `{lang}/blog/category/`). Adding a new manual category page automatically
adds it to the navbar menu.

| Spanish              | English               |
| -------------------- | --------------------- |
| ciencia              | science               |
| La flecha temporal   | *(no English page)*   |
| linux                | linux                 |
| programación         | programming           |
| tecnología           | technology            |

Tags are also translated between languages.

## Writing Style

### General

- First person, personal narrative tone. The author shares experiences and
  opinions.
- Accessible but technically accurate.
- Short paragraphs, with line wraps at ~80 characters in the source.
- Foreign words relative to the post's language must be italicized (e.g.,
  *prompt*, *software*, *hype* in Spanish posts; loanwords from Spanish in
  English posts).
- No trailing comments like `<!-- ... -->` or unnecessary whitespace.

### By Post Type

**Technology/Troubleshooting:**

- Opens with personal context of encountering the problem.
- Explains the technical background or what the tool/concept is.
- Shows what was tried and what worked (with commands and code).
- Ends with a concise conclusion and references section.
- Example: `es/blog/2025/montar-disco-en-linux-y-error-de-volumen-sucio.md`

**Science:**

- Opens with a hook about the topic or an event.
- Explains concepts in an educational but engaging way.
- Uses analogies and accessible language for complex topics.
- May include mathematical notation (LaTeX via `$...$` or `$$...$$`).
- Example: `es/blog/2025/alineacion-planetaria-2025.md`

**Opinion:**

- Opens with a direct statement or question.
- Personal perspective backed by facts or experience.
- Conversational tone, may address the reader directly ("tú" form in Spanish).
- Example: `es/blog/2024/factura-electronica-que-hacer-si-te-la-niegan.md`

**Culture/Entertainment:**

- Accessible, informal tone.
- Comparisons and personal recommendations.
- Example: `es/blog/2024/la-mejor-alternativa-gratis-a-netflix.md`

## Title & Slug Strategy

### Title principles

- **Concise and topic-specific.** The title must tell the reader exactly what the
  post is about. Avoid clickbait, expectative, viral, or vague titles.
- **Include the main topic and at least one primary tag** in the title itself.
  This serves both the reader and search engines.
- **Avoid filler words** in the title when possible (e.g., prefer
  "Configurar Starship en Manjaro y Zsh" over "Cómo puedes configurar el
  prompt Starship en tu terminal Manjaro con Zsh").
- **Use the post's language** for the title — Spanish for `es/`, English for
  `en/`.

#### Good vs. bad title examples

| ✅ Good | ❌ Bad | Why |
|---------|-------|-----|
| Montar disco en Linux y error de volumen sucio | ¡No vas a creer lo que pasó con mi disco! | Clickbait, no topic info |
| Herramientas de IA gratuita para desarrolladores en 2026 | Las mejores herramientas que todo dev necesita | Vague, no keywords |
| Alineación planetaria 2025 | Algo increíble está pasando en el cielo | Expectative, unspecific |
| Configurar Starship en Manjaro y Zsh | Mi nuevo prompt favorito | Missing topic/tags |

### Slug derivation rules

The slug is derived from the **Spanish title** following these transformations,
in order:

1. Convert to lowercase.
2. Normalize accented/special characters to their ASCII equivalents
   (`á` → `a`, `ñ` → `n`, `ü` → `u`, etc.).
3. Replace spaces and non-alphanumeric characters with hyphens (`-`).
4. Collapse consecutive hyphens into one.
5. Remove leading/trailing hyphens.
6. Aim for **8 words max**, but this is not rigid — clarity takes priority over
   strict length. Drop articles and prepositions only if the result remains
   clear.

#### Slug derivation examples

| Spanish title | Slug |
|---------------|------|
| Montar disco en Linux y error de volumen sucio | `montar-disco-en-linux-y-error-de-volumen-sucio` |
| Alineación planetaria 2025 | `alineacion-planetaria-2025` |
| Ingeniería de *prompt*: ¿Habilidad técnica o estafa? | `ingenieria-de-prompt-habilidad-o-estafa` |
| Configurar *Starship* en Manjaro y Zsh | `configurar-starship-en-manjaro-y-zsh` |

The slug is used identically for both `es/` and `en/` paths and for the images
directory.

## SEO & Ads Optimization

These guidelines ensure posts are discoverable by search engines and aligned with
ad-monetization keywords, **without sacrificing the blog's personal, authentic
writing style**.

### Headings must include tags

- The **H1 title** must contain at least the primary tag or its synonym.
- **H2 and H3 section headings** should incorporate relevant tags naturally.
  Treat them as sub-queries a reader might search for.
- Prefer question-format headings for H2/H3 when it fits naturally (e.g.,
  "¿Qué es Seekee?" rather than "Descripción"), as they match search intent.

#### Heading examples from existing posts

| Tag(s) in frontmatter | Heading | Tags reflected? |
|------------------------|---------|:---------------:|
| `planetas, sistema solar` | `## ¿Qué planetas se pueden ver en la alineación?` | ✅ `planetas` |
| `starship, manjaro, zsh` | `# Configurar Starship en Manjaro y Zsh` | ✅ all three |
| `streaming` | `## ¿Qué es Seekee?` | ⚠️ could add "streaming" context |

### Opening paragraph strategy

The **first paragraph** (immediately after H1) is critical for both SEO and ad
targeting. It must:

1. **State the main topic explicitly** — name the technology, concept, or problem
   directly. Don't rely on context or pronouns.
2. **Include at least 2–3 primary tags** as natural mentions within the first
   2–3 sentences.
3. **Include one high-value keyword phrase** relevant to the topic's ad niche
   when possible. Explore potential high-impact keywords at writing time based
   on the specific topic.
4. **Maintain the personal narrative hook** — the keyword integration must feel
   natural within the author's storytelling style, not like SEO filler.

#### Opening paragraph template (mental model, not rigid)

> [Personal context sentence connecting to the topic].
> [Direct statement naming the main topic/tool/concept and why it matters].
> [Sentence that naturally includes 1–2 additional tags and a high-value keyword
> phrase].

#### Example analysis — existing post

**Post:** *Herramientas de IA gratuita para desarrolladores en 2026*
**Tags:** `inteligencia artificial, agentes de código, zed, antigravity, ollama, ide`

> Estamos en 2026 y la **inteligencia artificial** ya no es una novedad, es el
> estándar. Sin embargo, el cuello de botella sigue siendo el mismo para muchos
> **desarrolladores** independientes y estudiantes: el costo de las suscripciones.

✅ Mentions "inteligencia artificial" (tag) + "desarrolladores" (audience keyword)
in the first two sentences.

### Keyword integration rules

- **DO** weave tags into headings and the first paragraph naturally.
- **DO** use long-tail keyword phrases that match real search queries.
- **DO** keep the personal, first-person narrative voice intact.
- **DON'T** stuff keywords unnaturally or repeat them excessively.
- **DON'T** add generic SEO phrases that feel out of place ("en esta guía
  completa aprenderás...").
- **DON'T** sacrifice readability for keyword density.

### High-value keyword awareness

When writing about a topic, explore which related terms carry higher advertising
value and incorporate them naturally. Use this as minimal guidance — research
specific high-impact keywords at writing time based on the post's topic:

| Topic area | Example high-value terms |
|------------|------------------------|
| Linux/DevOps | configuración, solución de errores, herramientas de desarrollo |
| AI/ML | inteligencia artificial, modelo de lenguaje, automatización |
| Programming | framework, desarrollo de software, API, arquitectura |
| Streaming/Apps | alternativa gratuita, mejor aplicación, comparativa |
| Science | observación astronómica, divulgación científica |

These are **starting points, not exhaustive lists**. Always explore topic-specific
keywords when drafting a new post.

## MyST Markdown Conventions

### Code blocks

````markdown
```{code} bash
command here
`` `
````

### Figures

````markdown
```{figure} /images/{slug}/{image-name}.png
---
alt: Description of the image
align: center
width: 800px
height: 400px
---
   Caption text.
`` `
````

Images are stored in `/images/{slug}/` directory. Create the directory when the
post uses images.

### Admonitions

**English posts** can use built-in directive names directly:

````markdown
```{attention}
Warning text here.
`` `
````

Available: `attention`, `note`, `tip`, `warning`, `important`.

**Spanish posts** must use the generic `{admonition}` directive with a `class`
option, because ABlog/Sphinx built-in directive titles render in English (the
Spanish locale translations are incomplete). Provide the translated title
manually:

````markdown
```{admonition} Título en español
---
class: tip
---
Contenido de la amonestación.
`` `
````

**Update admonitions** follow the rule:

- Use `{update}` directly (renders "Updated on YYYY-MM-DD").

````markdown
```{update} YYYY-MM-DD
Descripción de la actualización.
```
````

### Keyboard shortcuts

Use `{kbd}` role: `{kbd}\`Win+I\`\`

### Program references

Use `{program}` role: `{program}\`ollama\`\`

### File path references

Use `{file}` role: `{file}\`/dev/sda1\`\`

### Cross-references to other posts

Use standard Markdown link syntax with absolute or relative paths. **Do NOT use
`{ref}` for cross-references to other posts.**

```markdown
[Link text](/es/blog/2025/post-slug.md)
[Link text](../2025/post-slug.md)
[](/es/blog/2025/post-slug.md)           # Empty brackets: MyST auto-resolves the title
```

For section anchors within another post:

```markdown
[Link text](/es/blog/2025/post-slug.md#section-anchor)
```

### References Section

End posts with a `## Referencias` (Spanish) or `## References` (English) section
listing sources:

```markdown
## Referencias

- [Title](URL). Source.
- [Title](URL). Source.
```

## Bilingual Workflow

1. Write the **Spanish version first** (primary language of the blog).
2. Create the **English version** as a translation, not a literal word-for-word
   copy. Adapt idioms and cultural references naturally.
3. Both versions use the **same slug** (Spanish slug).
4. Both versions share the **same images directory**.
5. Translate tags and categories to their English equivalents.
6. English frontmatter includes `language: en`.

### When to create both versions

- **Technology/Programming posts**: Always bilingual (relevant to international
  audience).
- **Science posts**: Always bilingual.
- **Opinion posts**: Bilingual only if the topic is relevant beyond
  Spanish-speaking audiences.
- **Culture posts**: Bilingual only if universally relevant. Local topics
  (Colombian law, local events) may stay Spanish-only.

## Social Media Posts

After creating blog posts, create X (Twitter) proposed posts to
`social-posts.md` at the project root.

### Format

```markdown
## {slug}

### Español

{emoji} {Engaging summary of the post in 1-2 sentences. Include the key takeaway.}

https://www.cosmoscalibur.com/es/blog/{year}/{slug}

#{Tag1} #{Tag2} #{Tag3}

### English

{emoji} {Engaging summary of the post in 1-2 sentences. Include the key takeaway.}

https://www.cosmoscalibur.com/en/blog/{year}/{slug}

#{Tag1} #{Tag2} #{Tag3}
```

- Keep within X character limits (~280 chars per post).
- Use a relevant emoji at the start.
- Include 3-4 hashtags derived from post tags.
- Link to the corresponding language version.
