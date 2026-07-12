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

Never invent experiential specifics — personal anecdotes, what-was-tried,
observed results, opinions. If the plan or dossier didn't supply one and
the post type needs it, ask the author rather than fabricate it.

- **Science/divulgación**: question-format H2 headers (`## ¿Qué es...?`).
  Explains the phenomenon, uses `{figure}`/`{important}`/`{hint}` for
  concrete detail. Ends on `## Referencias` — no summary paragraph, no
  CTA. The post just stops once the sources are listed.
- **Programming/notes**: plain topical headers, often with inline code
  (`` `cargo` ``) — not questions. Opens with a direct, undisclaimed
  framing of what's covered; write with the confidence appropriate to what
  was actually verified, not more. Ends on `## Referencias`, sources may
  carry a one-line progress/relevance note.
- **Technology/practical**: commits to the solution that was actually
  used — explains *why* it works, not an exhaustive survey of every
  alternative. Minimal hedging. Ends on `## Referencias`.
- **Opinion**: colon+rhetorical-question headers, named concrete anecdotes,
  earns a real closing stance (this is the one type where a closing
  paragraph belongs) before `## Referencias`.
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
