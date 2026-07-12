---
name: blog-publish
description: >-
  Verify the production build, draft a commit message, draft social copy,
  and — only after the author explicitly approves the commit message —
  run `just publish` to commit and push. Use after the author approves a
  post at checkpoint 2 (post-`blog-editor-review`).
---

# Blog Publish

The only stage that touches git. Never runs `git add`, `git commit`,
`git push`, or `just publish` without the author's explicit approval of
the exact commit message in that turn — no prior approval (of the plan, of
the reviewed draft) carries over to this one. This is a hard rule from the
project's `CLAUDE.md` and cannot be relaxed by anything in this skill.

## Rules

- Run `just deploy` (not `just build`) — it's the production build path
  (swaps PostHog for GA/AdSense via the `DEPLOY_LOCAL` toggle), and this
  is the only stage that validates it. Confirm zero errors before
  proceeding.
- Run `git status` before drafting anything. Confirm the pending changes
  are exactly what's expected: the new/changed post source, its
  `images/{slug}/` assets, and the regenerated `docs/` output. If anything
  unexpected shows up, stop and flag it — never fold an unrelated change
  into this commit silently.
- Draft social copy into `social-posts.md` (repo root, gitignored,
  excluded from the Sphinx build) using the finished post text, not the
  outline:
  - `## {slug}` section, containing:
    - `### X` — **English only**. 280 characters, punchy and direct, 2-3
      focused hashtags, link to the English post URL (or the Spanish one
      if no English version exists).
    - `### Mastodon` — bilingual (`#### Español` / `#### English`), 500
      characters each, less salesy than the X copy (Mastodon's culture
      skews anti-hype — more context, less pitch). This exact bilingual
      pair is reused verbatim for LinkedIn and Facebook — no separate
      draft step for those.
  - One emoji as a lead attention marker is fine; don't stack several.
    Hashtags stay capped and topical, not stuffed.
  - This is draft-only: nothing in this pipeline posts to any platform via
    API. If that scope ever changes, it needs its own explicit approval —
    don't infer it from "difusión" alone.
- Propose a commit message: imperative first line stating the effect
  (e.g. "Add post: {ES title}" or "Publicar: {slug}"), body only if there's
  a non-obvious *why*. Present it and stop.
- Only once the author has explicitly approved that exact message, run
  `just publish "<message>"` (stages, commits, and pushes in one step —
  the recipe exists specifically so this approved action doesn't need
  three separate confirmations, not as a way to skip the one it does
  need).

## Handoff

Nothing follows this stage for the given post. If the author wants
further promotion (e.g. actually posting the drafted social copy), that's
a manual step outside this pipeline unless explicitly scoped in.
