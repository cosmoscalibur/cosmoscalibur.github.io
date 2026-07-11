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
- **Never invent experiential specifics.** Personal narrative details — how
  or when the author learned something, what tool/channel surfaced it, their
  circumstances or reactions — must come from the author's brief, not be
  fabricated for color. If the post's opening or a transition calls for a
  personal-context detail the user hasn't provided, ask the user for it
  instead of writing a plausible-sounding invented one (e.g., don't assume
  "no advance notice" when the author never said that — ask how they
  actually found out). This is a personal, authentic blog; an invented lived
  experience breaks that authenticity even if the surrounding facts are
  correct.
- **Direct, no expectation-building teasers in body text.** The
  "avoid clickbait, expectative, viral" rule for titles (see
  [Title principles](#title-principles)) applies to prose too. Don't write
  curiosity-gap phrases like "and what I found while digging into it..." or
  "you won't believe what happened next" that promise a payoff instead of
  stating it. If a sentence sets up a reveal, deliver the reveal in the same
  sentence or the next one — the author's style is direct, not teased.
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
- **Titles are descriptive noun/gerund phrases about the topic or change, not
  first-person narrative sentences.** The existing corpus never titles a post
  as a story beat ("Cuando X pasó, hice Y"); it names the topic directly:
  "Migrando mi blog de Nikola a Sphinx", "Buscando el mejor cliente de
  Mastodon para Android", "Alucinación de la inteligencia artificial". Prefer
  "Migrando a Claude Code como alternativa al modo consumo en Antigravity
  GCP" over "Cuando Antigravity corporativo pasó a consumo, migré a Claude
  Code" — same content, but the first reads like the rest of the blog and the
  second reads like a diary entry.
- **A colon introduces a subtitle or a question, never a cause → consequence
  formula.** Existing titles use the colon as "topic: descriptive appositive"
  (e.g., "Proton: Modo de compatibilidad de Steam") or "topic: rhetorical
  question" (e.g., "Factura electrónica: ¿Qué hacer si te la niegan?"). Don't
  use it to mechanically join a trigger and a decision/result (e.g.,
  "Antigravity pasa a consumo: por qué migro a Claude Code") — that reads as
  a formula, not a title.

#### Good vs. bad title examples

| ✅ Good | ❌ Bad | Why |
|---------|-------|-----|
| Montar disco en Linux y error de volumen sucio | ¡No vas a creer lo que pasó con mi disco! | Clickbait, no topic info |
| Herramientas de IA gratuita para desarrolladores en 2026 | Las mejores herramientas que todo dev necesita | Vague, no keywords |
| Alineación planetaria 2025 | Algo increíble está pasando en el cielo | Expectative, unspecific |
| Configurar Starship en Manjaro y Zsh | Mi nuevo prompt favorito | Missing topic/tags |
| Migrando a Claude Code como alternativa al modo consumo en Antigravity GCP | Cuando Antigravity corporativo pasó a consumo, migré a Claude Code | Narrative sentence instead of a descriptive noun phrase matching the blog's title pattern |

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
- **Headings must be concise (aim 4-8 words) and name the section's lead
  idea — not an enumeration of every sub-point it covers.** If a section
  merges several related sub-points (see
  [Section granularity](#section-granularity)), title it after the
  overarching argument, not a comma-joined list of its parts: prefer "El
  modo consumo: más factura y sin Claude" over "Facturación, ausencia de
  Claude en modo consumo y la aclaración de fondo" for a section covering
  all three of those points.

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

### Cite specific claims inline, not only in References

When the post states a specific, checkable external fact — a product change,
a policy update, a dated announcement — link to the source **inline, at the
point the claim is made**, in addition to listing it in References. Don't
make the reader guess which entry in References backs which sentence. A
generic product page ("what's new") doesn't substitute for the actual
announcement being described; find and link the specific source.

## Planning & Approval Workflow

**Before writing any content**, the agent must present a structured plan to the
user and obtain explicit approval. No blog post, social media draft, or file
should be created until the plan is approved. This ensures editorial alignment on
focus, strategy, and scope.

### Plan structure

Present the following plan as an artifact for user review:

1. **Topic & Angle** — One-paragraph summary of what the post will cover and the
   specific angle or thesis. Explain *why* this angle was chosen over
   alternatives. If the angle relies on a personal-experience detail the user
   hasn't stated (how they found out, their specific circumstances), ask
   before including it — don't invent one (see
   [Writing Style](#writing-style)).
2. **Target Audience** — Who is this post for? What level of expertise is
   assumed?
3. **Post Type** — One of: Technology/Troubleshooting, Science, Opinion,
   Culture/Entertainment (see [Writing Style](#writing-style)).
4. **Proposed Title** (Spanish & English) — Following the
   [Title & Slug Strategy](#title--slug-strategy). Include the derived slug.
5. **Tags & Categories** — Proposed tags (Spanish & English) and categories.
   Justify tag choices: why these tags serve discoverability and ad relevance.
   **Every tag must correspond to a topic the post actually covers in its
   own sections** — not a topic merely adjacent to it or implied by the
   broader subject area. Before finalizing tags (both at planning time and
   again after the draft is written), check each one against the section
   outline: if no section substantively discusses it, drop the tag. Example:
   a post about a product's billing and model-availability change doesn't
   automatically earn a `modelo de lenguaje`/`language model` tag just
   because it mentions specific model names in passing — that tag belongs
   on posts that actually discuss language models as a subject.
6. **Section Outline** — Numbered list of H2/H3 sections with a one-sentence
   description of each section's content. This defines the post's structure and
   flow.

   #### Section granularity

   Group sub-points that build toward the same argument under one H2 instead
   of giving each its own section — but keep genuinely distinct arguments or
   phases (e.g., "the problem" vs. "the decision") as separate sections. As a
   rule of thumb, target **4-7 H2 sections** for a standard post: enough to
   keep each section atomic (one clear idea), without fragmenting into a
   section per sentence. Resolve grouping at outline review, not after the
   draft is written — merging sections after the fact tends to produce
   comma-joined heading titles (see
   [Headings must include tags](#headings-must-include-tags)).
7. **Focus & Strategy Review** — Editorial assessment covering:
   - **SEO focus**: Primary keyword phrase and 2–3 secondary keywords targeted.
   - **Ad alignment**: Which high-value keyword areas does this post tap into?
   - **Content gap**: What makes this post distinct from existing content on the
     blog or competing sources?
   - **Bilingual decision**: Should this post be bilingual? Justify using the
     criteria in [When to create both versions](#when-to-create-both-versions).
8. **Social Media Drafts** — Draft posts for both X and Mastodon (Spanish &
   English). These are reviewed as part of the plan, not after the post is
   written. See [Social Media Posts](#social-media-posts) for format and
   character limits.

### Approval rules

- The user must **explicitly approve** the plan before writing begins.
- The user may request changes to any section of the plan. Iterate until
  approved.
- If the user provides a very specific brief (e.g., "write about X with these
  tags"), still present the plan for confirmation — do not skip the approval
  step.
- After approval, follow the plan faithfully. Deviations discovered during
  writing should be flagged to the user for re-approval.

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

After creating blog posts, create proposed social media posts to
`social-posts.md` at the project root. Create **separate posts** for each
platform:

- **X (Twitter)**: **280 characters maximum** (including URL and hashtags).
- **Mastodon**: **500 characters maximum** (including URL and hashtags). Use the
  extra space for a more detailed or nuanced message — not just a padded version
  of the X post.

Character counts must be verified before finalizing. The URL
(`https://www.cosmoscalibur.com/...`) and hashtags count toward the limit.

### Format

```markdown
## {slug}

### X

#### Español

{emoji} {Concise engaging summary — fits within 280 chars total with URL and hashtags.}

https://www.cosmoscalibur.com/es/blog/{year}/{slug}

#{Tag1} #{Tag2} #{Tag3}

#### English

{emoji} {Concise engaging summary — fits within 280 chars total with URL and hashtags.}

https://www.cosmoscalibur.com/en/blog/{year}/{slug}

#{Tag1} #{Tag2} #{Tag3}

### Mastodon

#### Español

{emoji} {More detailed summary — up to 500 chars total. Add context, a key insight, or a question to spark discussion.}

https://www.cosmoscalibur.com/es/blog/{year}/{slug}

#{Tag1} #{Tag2} #{Tag3} #{Tag4}

#### English

{emoji} {More detailed summary — up to 500 chars total. Add context, a key insight, or a question to spark discussion.}

https://www.cosmoscalibur.com/en/blog/{year}/{slug}

#{Tag1} #{Tag2} #{Tag3} #{Tag4}
```

### Social media guidelines

- **X posts**: Keep within 280 characters. Be punchy and direct.
- **Mastodon posts**: Up to 500 characters. Use the space to add nuance, a
  thought-provoking question, or additional context that wouldn't fit on X.
- Use a relevant emoji at the start.
- Include 3–4 hashtags derived from post tags.
- Link to the corresponding language version.
- Mastodon posts should feel like a distinct, richer version — not just the X
  post with filler added.
