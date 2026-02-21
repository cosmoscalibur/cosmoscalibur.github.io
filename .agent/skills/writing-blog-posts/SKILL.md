---
name: writing-blog-posts
description: "Creates bilingual blog posts (Spanish/English) for Cosmoscalibur. Use when asked to write, create, or draft a blog post, article, or entry."
---

# Writing Blog Posts

Creates blog posts for the Cosmoscalibur blog, a bilingual (Spanish/English) personal blog built with Sphinx and ABlog using MyST Markdown.

## File Structure

Posts are organized by language and year:

```
es/blog/{year}/{slug}.md      # Spanish version (primary)
en/blog/{year}/{slug}.md      # English version
images/{slug}/                 # Images directory (if needed)
```

- The **slug** is always in Spanish, lowercase, with hyphens. Used for both `es/` and `en/` paths.
- The **year** is the publication year (use today's date).
- For code-heavy posts with executable examples, use Jupyter Notebooks (`.ipynb`) instead of `.md`.

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

Note: English posts include `language: en`. Spanish posts do not include a `language` field.

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

English notebooks include `"language": "en"` in metadata. Tags and categories are translated.

### Categories Reference

Spanish categories and their English equivalents:

| Spanish | English |
|---|---|
| tecnología | technology |
| programación | programming |
| ciencia | science |
| astronomía | astronomy |
| física computacional | computational physics |
| linux | linux |
| opinión | opinion |
| entretenimiento | entertainment |
| videojuegos | videogames |
| películas y series | movies and series |
| software | software |
| blog con sphinx | blog with sphinx |

Tags are also translated between languages.

## Writing Style

### General

- First person, personal narrative tone. The author shares experiences and opinions.
- Accessible but technically accurate.
- Short paragraphs, with line wraps at ~80 characters in the source.
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

## MyST Markdown Conventions

### Code blocks

```markdown
```{code} bash
command here
`` `
```

### Figures

```markdown
```{figure} /images/{slug}/{image-name}.png
---
alt: Description of the image
align: center
width: 800px
height: 400px
---
   Caption text.
`` `
```

Images are stored in `/images/{slug}/` directory. Create the directory when the post uses images.

### Admonitions

```markdown
```{attention}
Warning text here.
`` `
```

Available: `attention`, `note`, `tip`, `warning`, `important`.

### Keyboard shortcuts

Use `{kbd}` role: `{kbd}\`Win+I\``

### Program references

Use `{program}` role: `{program}\`ollama\``

### File path references

Use `{file}` role: `{file}\`/dev/sda1\``

### Cross-references to other posts

Use relative or absolute paths:

```markdown
[Link text](/es/blog/2025/post-slug.md)
[Link text](../2025/post-slug.md)
```

### References Section

End posts with a `## Referencias` (Spanish) or `## References` (English) section listing sources:

```markdown
## Referencias

- [Title](URL). Source.
- [Title](URL). Source.
```

## Bilingual Workflow

1. Write the **Spanish version first** (primary language of the blog).
2. Create the **English version** as a translation, not a literal word-for-word copy. Adapt idioms and cultural references naturally.
3. Both versions use the **same slug** (Spanish slug).
4. Both versions share the **same images directory**.
5. Translate tags and categories to their English equivalents.
6. English frontmatter includes `language: en`.

### When to create both versions

- **Technology/Programming posts**: Always bilingual (relevant to international audience).
- **Science posts**: Always bilingual.
- **Opinion posts**: Bilingual only if the topic is relevant beyond Spanish-speaking audiences.
- **Culture posts**: Bilingual only if universally relevant. Local topics (Colombian law, local events) may stay Spanish-only.

## Social Media Posts

After creating blog posts, append X (Twitter) proposed posts to `social-posts.md` at the project root.

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
