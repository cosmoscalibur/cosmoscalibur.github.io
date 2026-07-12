# Editorial pipeline orchestration

Content and technical conventions (categories, frontmatter, slugs, MyST,
the `just` workflow) live in `CONTRIBUTING.md` — followed identically by a
human author or an agent, never restated here. What each stage does
procedurally, and the voice/bias-correction rules specific to
AI-assisted drafting, live in the five `blog-*` skills under
`.claude/skills/`. This file only holds sequencing and the rules that
apply regardless of which skill is active.

## 1. Stage sequencing

```
blog-research → blog-planning → [checkpoint 1] → blog-writing →
blog-editor-review → [checkpoint 2] → blog-publish
```

- A new post request always starts at `blog-research`, even for a brief
  specific enough that it feels like planning could start directly — the
  redundancy check and source-gathering still need to happen first.
- `blog-research` → `blog-planning`: no checkpoint between these two; the
  dossier's quality is validated implicitly by whether the resulting plan
  holds up.
- **Checkpoint 1**: the author must explicitly approve `blog-planning`'s
  plan before `blog-writing` starts. No post file is created before this
  approval.
- `blog-writing` → `blog-editor-review`: no checkpoint between these two —
  editor review is a read-only pass, same as the code `review` skill.
- **Checkpoint 2**: `blog-editor-review` must clear (its checklist and a
  clean `just build`) *and* the author must explicitly approve the
  reviewed draft before `blog-publish` starts.
- If a later stage finds the prior stage's output doesn't hold up (e.g.
  editor-review finds the outline doesn't work), that goes back to the
  relevant checkpoint for re-approval — never patched around silently.

## 2. Git safety (non-negotiable)

- Only `blog-publish` touches git, and only after the author's explicit
  approval of the exact commit message in that turn. Checkpoint 1 and
  checkpoint 2 approvals do not carry over to this one.
- This file, and no skill under `.claude/skills/`, grants blanket
  authorization for `git add`, `git commit`, `git push`, or `just
  publish`. This mirrors the standing global git-safety rules and cannot
  relax them.
- `just build` / `just deploy` (local rendering) are not git operations
  and don't require this approval gate — only the actual git actions do.

## 3. Scope

- Social copy (`blog-publish`) is draft-only, written to `social-posts.md`.
  Nothing in this pipeline posts to any platform via API.
