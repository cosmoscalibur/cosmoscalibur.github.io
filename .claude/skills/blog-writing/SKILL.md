---
name: blog-writing
description: >-
  Draft (and translate, if bilingual) a blog post from an approved
  `blog-planning` plan, using the site's MyST conventions. Use only after
  the author has approved a plan — never to draft from an unapproved brief.
---

# Blog Writing

Drafts post prose from an approved plan. Never starts without an approved
plan from `blog-planning` — an unapproved brief goes back there first.

## Reference

File paths, frontmatter, MyST directive syntax (admonitions, `{update}`,
`{figure}`, cross-references), image-ordering, notebook-vs-markdown
choice, and the sphinx-design-restraint rule are all defined in
`CONTRIBUTING.md` — follow them exactly, don't reconstruct or restate them
here.

## Voice, by post type (set in the approved plan)

Title and every header (H2/H3, any level) are `blog-planning`'s decision,
never `blog-writing`'s — in every post type, with no exception. The plan
gives verbatim title and heading text; use it exactly as approved. Never
reformat, reword, or "correct" a title or header to match a type's usual
pattern (e.g. converting a plain topical header into question-form
because the post is Science, or adding inline code to a Programming
header the plan wrote in plain text) — the per-type notes below describe
tone and structure only, not header form, precisely because that decision
doesn't belong here.

`blog-writing` operates strictly on what `blog-research` and
`blog-planning` already handed it. It does not go find new facts,
sources, or images, or compute an estimate on its own: if the plan's
outline calls for applying a source's method to the post's specific
subject and the brief doesn't include the subject-specific data or figure
that requires, stop and ask the author — that gap belongs to
`blog-research`/`blog-planning`, not to this stage.

MyST structural elements — `{figure}`, admonitions (`{note}`,
`{important}`, `{hint}`, `{warning}`, or `{admonition}` with `class:` in
Spanish), tables — are available in every post type, not just Science.
Use them wherever the plan's outline calls for concrete detail
(a warning in a Linux post, a hint in a Programming one), regardless of
category.

- **Science/divulgación**: explains the phenomenon. Ends on
  `## Referencias` — no summary paragraph, no CTA. The post just stops
  once the sources are listed.
- **Programming/notes**: opens with a direct, undisclaimed framing of
  what's covered; write with the confidence appropriate to what was
  actually verified, not more. Ends on `## Referencias`, sources may
  carry a one-line progress/relevance note.
- **Technology/practical**: commits to the solution that was actually
  used — explains *why* it works, not an exhaustive survey of every
  alternative. Minimal hedging. Ends on `## Referencias`.
- **Opinion**: named concrete anecdotes, earns a real closing stance
  (this is the one type where a closing paragraph belongs) before
  `## Referencias`.
- **Poetry (`La flecha temporal`, ES only)**: the poem itself, no headers,
  no References section. A companion `{youtube}` embed is a common,
  optional closing element — never a summary paragraph.

## Rules

- Ban generic filler regardless of type: "en esta guía completa
  aprenderás...", "es importante destacar que...", "cabe resaltar...",
  "en resumen...", "sin duda alguna...", and their English equivalents
  ("in this comprehensive guide...", "it's worth noting...", "in
  conclusion...", "without a doubt..."). These read as generated filler in
  every post type on this blog.
- No forced closing CTA ("let me know in the comments", "stay tuned") on
  any post type — the corpus doesn't use them, and Science/Programming/
  Technology posts end on `## Referencias` with no wrap-up at all.
- Citations are hybrid, both parts required for any checkable claim: an
  inline link at the point the claim is made, *and* an entry in the
  closing `## Referencias`/`## Fuentes` list. A claim with only one or
  neither is incomplete. Every source must be real — carried from
  `blog-research`'s dossier, never approximated.
- Cross-references to other posts on this site: worked quietly into a
  sentence (mechanics — plain Markdown link, not `{ref}` — are in
  `CONTRIBUTING.md`), never announced ("as I mentioned in my previous
  post...").
- Italicize loanwords relative to the post's language (*prompt*,
  *software*, *hype* in Spanish text; the reverse is rare but applies the
  same way in English posts).
- Bilingual posts: Spanish is written first and is the primary version.
  The English version is an adapted translation, not literal — register
  adjusted naturally for an English-reading audience (file/slug reuse
  mechanics are in `CONTRIBUTING.md`).

## Handoff

Once drafting (and translation, if applicable) is complete, proceed to
`blog-editor-review`. Don't self-review past the checklist above — that
pass is `blog-editor-review`'s job, done fresh.
