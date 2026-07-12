---
name: blog-planning
description: >-
  Produce a post plan (title, slug, category, tags, section outline) from
  `blog-research`'s dossier, for the author's explicit approval before any
  writing starts. Use after `blog-research` completes, or directly for a
  brief specific enough to skip research.
---

# Blog Planning

Turns a research dossier into a concrete, approvable plan. Never writes
post prose — that's `blog-writing`'s job, and it doesn't start until the
author approves this plan.

## Reference

Categories, frontmatter schema, and the slug-derivation algorithm are
defined in `CONTRIBUTING.md` — follow them exactly, don't reconstruct or
restate them here.

## Rules

- Build on `blog-research`'s dossier: cite its differentiating angle and
  sources directly in the plan. Don't re-derive an editorial angle from
  nothing if research already produced one.
- Post type drives voice from the start — flag one of: Science/divulgación,
  Programming/notes, Technology/practical, Opinion, Poetry (`La flecha
  temporal`, ES only). This determines `blog-writing`'s and
  `blog-editor-review`'s conventions downstream (question-format headers
  vs. plain topical headers, abrupt References-ending vs. an earned closing
  stance, etc.) — get it right here, not later.
- **Title**: a descriptive noun/gerund phrase naming the actual topic —
  never a first-person narrative sentence, never clickbait or a
  curiosity-gap tease ("you won't believe...", "what I learned when..."),
  never generic filler ("the complete guide to..."). A colon subtitle is
  allowed only as an appositive (`Tema: aclaración concreta`) or a
  rhetorical question (`Tema: ¿pregunta específica?`) — never a
  "trigger: result" formula (e.g. "X pasa a Y: por qué migro a Z" reads as
  a formula, not a title). Match the length and register of real titles in
  the target category rather than inventing a house style.
- **Tags**: 3-7, each justified against a section that will actually exist
  in the outline — a tag with no corresponding content is padding. There
  is no `<meta name="keywords">` tag anywhere in this stack; tags only
  power on-site tag pages, breadcrumbs, and JSON-LD. "Keyword strategy"
  here means real terms readers search for, worked naturally into headings
  and the opening paragraph — not a metadata field, and not stuffed
  repetition.
- **Opening paragraph focus**: sketch its SEO-bearing sentence at plan
  time, not just its narrative hook. This paragraph is auto-extracted
  (first ~200 characters after the H1, admonitions skipped) as the page's
  `<meta name="description">` and `og:description` — there is no override
  field in use anywhere in the corpus. It has to work as both the post's
  actual opening and a standalone search-result snippet.
- **Section outline**: 4-7 H2s, each with a one-line focus statement. Every
  section must trace to something in the dossier (a source, the
  differentiating angle, or an explicit author-supplied experiential
  detail) — no filler section added just to hit a section count.
- Bilingual decision: Spanish is written first and is primary. Only plan
  an English version if the topic has standalone value to an
  English-reading audience (not just "everything gets translated by
  default").
- Present the full plan — post type, title+slug (both languages if
  bilingual), category, tags with justification, section outline with
  per-section focus, opening-paragraph sketch — and stop. Do not create
  any file or draft any prose until the author explicitly approves it.

## Handoff

Once the author approves the plan, proceed to `blog-writing` with the
approved plan as its brief. If `blog-writing` or `blog-editor-review`
later finds the outline doesn't hold up, that goes back to the author for
re-approval — never adjusted silently past this checkpoint.
