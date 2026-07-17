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

- Specify content requirements only — what must appear, and in which
  section — never a MyST construct or directive name. An image need is
  "this section uses the sourced photo, with this licensing constraint,"
  not `{figure}`; tabular data is "present these values as a table," not
  a markup choice. Which MyST syntax realizes that requirement is
  `blog-writing`'s craft, per `CONTRIBUTING.md`'s MyST conventions —
  without exception, including for images and tables.
- Build on `blog-research`'s dossier: cite its differentiating angle and
  sources directly in the plan. Don't re-derive an editorial angle from
  nothing if research already produced one.
- Before drafting the outline, check the dossier actually supports it: if
  the differentiating angle depends on subject-specific data (an
  "apply this method to the real case" angle) or a specific image, and the
  dossier doesn't have it, don't paper over the gap or push it downstream
  to `blog-writing` to improvise. Send a narrow, specific request back to
  `blog-research` for exactly that missing piece, then resume planning —
  this happens before the plan is presented, and needs no approval of its
  own. If `blog-research` reports nothing verifiable exists, that becomes
  an explicit open question or a scoped-down angle in the plan presented
  to the author — never a silent substitution.
- Post type drives voice from the start — flag one of: Science/divulgación,
  Programming/notes, Technology/practical, Opinion, Poetry (`La flecha
  temporal`, ES only). This determines `blog-writing`'s and
  `blog-editor-review`'s conventions downstream (abrupt References-ending
  vs. an earned closing stance, etc.) — get it right here, not later.
- **Slug**: compute it by running
  `uv run .claude/skills/blog-planning/scripts/slugify.py "<título ES>"` —
  never derive it by hand or by interpreting `CONTRIBUTING.md`'s prose
  rule yourself. The script is the deterministic implementation of that
  rule; if its output looks wrong, the fix is to the script or to
  `CONTRIBUTING.md`, not a manual override in this plan.
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
- **Opening paragraph focus**: this skill owns the opening paragraph's
  content requirements — `blog-writing` drafts the final prose, but from
  what's decided here, not from its own judgment. Sketch its SEO-bearing
  sentence at plan time, not just its narrative hook. This paragraph is
  auto-extracted (first ~200 characters after the H1, admonitions skipped)
  as the page's `<meta name="description">` and `og:description` — there
  is no override field in use anywhere in the corpus. It has to work as
  both the post's actual opening and a standalone search-result snippet.
  If the dossier records why the author personally cares about the topic
  or about connecting two specific facts, name that motivation explicitly
  as part of the sketch — don't let it get laundered into a neutral,
  impersonal disclaimer downstream that drops the author's actual reason
  for writing.
- **Section outline**: 4-7 H2s, each presented with its literal header
  text — verbatim, including any sub-heading level and wording, not a
  paraphrased label — plus a one-line focus statement. The author is
  approving the actual words that will appear on the page; `blog-writing`
  uses them exactly as given and makes no header-format decisions of its
  own. Every section must trace to something in the dossier (a source,
  the differentiating angle, or an explicit author-supplied experiential
  detail) — no filler section added just to hit a section count. If a
  section's angle centers on a specific image, state here whether and
  where that image is used, with the source/licensing the dossier
  recorded — this is not a call `blog-writing` makes on its own. How that
  image is realized in MyST is `blog-writing`'s craft, not this skill's.
- Bilingual decision: Spanish is written first and is primary. Only plan
  an English version if the topic has standalone value to an
  English-reading audience (not just "everything gets translated by
  default").
- Present the full plan — post type, title+slug (both languages if
  bilingual), category, tags with justification, section outline with
  per-section focus, opening-paragraph sketch — and stop.

## Handoff

Once the author approves the plan, proceed to `blog-writing` with the
approved plan as its brief.
