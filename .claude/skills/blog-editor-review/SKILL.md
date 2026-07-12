---
name: blog-editor-review
description: >-
  Review a drafted post for factual accuracy, citation quality, per-category
  style adherence, accessibility, and generic-LLM tells, then verify it
  renders correctly with `just build`. Use after `blog-writing` completes,
  before presenting the draft to the author for approval.
---

# Blog Editor Review

Read-only pass over a drafted post (and its English version, if
bilingual). Reports findings; doesn't rewrite prose itself unless the
author asks for the fixes to be applied after reviewing the findings.

## Fact-check and citations

- Every specific, checkable claim (a number, a date, a version, a quoted
  behavior) has an inline link at the point it's made, *and* a
  corresponding entry in the closing `## Referencias`/`## Fuentes` list.
  Flag any claim with only one or neither.
- Every source resolves to something real — no approximated or
  hallucinated URL. Spot-check at least the non-obvious ones.
- Flag claims that go beyond what the cited source actually supports.

## Fabricated personal experience

- Flag every first-person experiential claim in the draft — "probé X",
  "en mi caso...", "me pasó que...", "lo instalé y...", any anecdote,
  opinion, or observed result attributed to the author — that isn't
  traceable to something the author actually supplied (via the plan, the
  research dossier, or explicit statement in conversation). `blog-writing`
  is instructed never to invent these, but this pass exists precisely
  because that instruction can still be missed or drift in during drafting
  — verify it wasn't, don't just assume it.
- A generic "I tried this and it worked" with no specific, author-sourced
  detail behind it is exactly the kind of plausible-sounding fabrication
  to flag — it reads as authentic but isn't.

## Generic-LLM-tell checklist

- **Titles**: descriptive noun/gerund phrase about the actual topic — flag
  clickbait, curiosity-gap phrasing, "the complete guide to...", or a
  first-person narrative sentence standing in for a title. A colon
  subtitle must be an appositive or rhetorical question, never a
  "trigger: result" formula.
- **Headers**: match the post type set in the plan — question-format for
  Science/Opinion, plain topical (often code-ticked) for
  Programming/Technology, none at all for Poetry. A post with the wrong
  header register for its type reads off-voice even if each header is
  individually fine.
- **Body focus**: flag hedge-everything phrasing, false-balance padding
  ("on one hand... on the other hand..." where there's a clear practical
  answer), and "there are many ways to do X" throat-clearing that delays
  the actual solution. This blog explains *why* something works and
  commits to the approach used, not an exhaustive option survey.
- **Closings**: Science/Programming/Technology posts end on
  `## Referencias` with no summary paragraph or CTA — flag any synthetic
  wrap-up added onto one of these types. Opinion posts are the one type
  that earns a real closing stance; Poetry ends on the poem (optionally a
  companion video), never a summary.
- **Filler phrases**: flag "es importante destacar que", "cabe resaltar",
  "en resumen", "sin duda alguna", "en esta guía completa aprenderás", and
  English equivalents ("it's worth noting", "in conclusion", "without a
  doubt", "in this comprehensive guide") wherever they appear.
- **Sentence rhythm**: genuinely uniform sentence length across a whole
  section is itself a tell — flag sections that read metronomic, not as a
  hard rule but as a prompt to vary rhythm.
- **Hedged AI-disclaimer language**: flag phrases like "cabe mencionar que
  esto es solo mi opinión" or "por supuesto, esto puede variar" unless the
  hedge is genuinely load-bearing to the point being made.
- **Emoji**: sparing, mid-sentence attention markers only (matches the
  Opinion-post convention in the corpus) — flag decorative bullet-prefix
  or paragraph-opening emoji use.
- **MyST/UI chrome**: flag `{tab-set}`, `{dropdown}`, `{card}`, or
  `{grid}` used without a real structural justification (e.g. showing
  equivalent RST/MD syntax) — decorative use of these is itself a tell,
  and each one taxes page CSS weight regardless.

## Accessibility (nothing else in the build catches this)

- Every `{figure}`/image has a non-empty, descriptive `alt:` — not a
  filename, not "imagen"/"screenshot"/"image". This is the single biggest
  unprotected risk in the pipeline: a missing alt silently becomes `""`
  and nothing in the build warns about it.
- Heading hierarchy has no skipped levels (H1 → H2 → H3, never a jump to
  H4 without an H3 in between).
- Link text is descriptive — flag bare "aquí"/"here" link text.
- If a figure caption describes meaning by color or shape alone, flag it.

## Build verification

- Run `just build` and confirm zero new Sphinx errors/warnings tied to the
  new or changed files (broken cross-references, unresolved images, MyST
  syntax errors).
- Spot-check the rendered output at `docs/{lang}/blog/{year}/{slug}/`:
  headings present in the right order, figures resolved, admonitions
  render with the correct title (Spanish posts must show `class:`-based
  admonitions correctly, not a raw directive), no unrendered MyST syntax
  leaking into the page text.
- Optional: spell-check via `codebook` (Spanish dictionary configured in
  `codebook.toml`) invoked directly as an external CLI — it's an
  editor/LSP-integrated tool, not a `uv`-managed dependency, so don't
  route it through `uv run`.

## Handoff

Report findings to the author for **checkpoint 2** approval. Only after
explicit approval does the post proceed to `blog-publish`. If findings
reveal the outline itself doesn't hold up (not just a wording fix), send
it back to `blog-planning` for re-approval rather than patching around it
here.
