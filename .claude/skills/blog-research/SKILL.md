---
name: blog-research
description: >-
  Validate a blog post topic before any outline exists — check it isn't
  redundant with the existing corpus, find real citable sources, and name
  the differentiating angle. Use when the author gives a topic brief or
  idea for a new post, before invoking `blog-planning`. Also handles
  narrow, single-fact or single-source research requests against an
  already-started dossier, not only full new-topic briefs.
---

# Blog Research

Turns a topic brief into a dossier `blog-planning` can build an outline
from. Never writes post content or drafts an outline — that's
`blog-planning`'s job.

## Rules

- Search the existing corpus first: grep `es/blog/` and `en/blog/`
  frontmatter (`tags:`, `category:`) and titles for prior posts on the same
  or an adjacent topic. If one exists, decide explicitly: genuine
  follow-up (candidate for a `{update}` directive on the existing post) or
  a distinct enough angle to justify a new post. State the verdict — never
  proceed silently past a possible duplicate.
- Use `WebSearch`/`WebFetch` to find current, real, citable sources.
  Prefer primary/dated sources (official docs, changelogs, announcements,
  papers) over aggregator/SEO-farm blog posts paraphrasing the same
  primary source. A source that can't be traced to something real doesn't
  go in the dossier — never invent or approximate a URL.
- Name the differentiating angle explicitly: one line stating what this
  post says that isn't already on the blog or dominating the top web
  results for the topic. If nothing differentiates it, say so — that's a
  valid finding to hand back to the author, not something to paper over.
- Surface internal cross-link candidates: specific prior posts (with
  section anchors where relevant) that a natural sentence in the new post
  could quietly link to. Don't propose an "as I mentioned before" callout —
  just the link target and where it would fit.
- Flag where the brief depends on a personal-experience detail (what the
  author actually did, saw, or decided) that no source can supply — list
  it as an open question for the author rather than letting `blog-writing`
  discover it later and improvise. Capture it verbatim (exact platform,
  date, what happened) — this is narrative content to carry forward
  unchanged, not a fact to generalize or neutralize.
- If the differentiating angle depends on applying a source's method or
  formula to the brief's specific real-world subject or event (not just
  citing the source's own generic examples), actively search for data
  about that specific subject — don't stop at the source's own table or
  examples. If nothing verifiable exists, say so explicitly in the
  dossier as its own finding, the same way an absent differentiating angle
  gets flagged — don't let the gap surface for the first time downstream.
- If the brief centers on a specific image (a viral photo, a screenshot,
  a chart from a source), identify its real origin URL and note its
  licensing/attribution situation (who owns it, whether hotlinking or an
  official embed is realistic) as its own dossier line — this is sourcing
  work, not something `blog-writing` should be discovering or working
  around at draft time.
- Output a short dossier: topic redundancy verdict, differentiating angle,
  3-8 sources with URL + one-line relevance note, internal link
  candidates, open questions for the author. Conversational handoff is
  fine — no persisted file required.

## Handoff

Once the dossier is ready, proceed to `blog-planning`. If the redundancy
verdict is "this duplicates an existing post," say so and let the author
decide between an `{update}` to the old post or proceeding anyway, before
`blog-planning` starts.

`blog-research` isn't only a pipeline entry point. A request can also be
narrow and specific — a single missing fact, data point, or image source
against a dossier that already exists — instead of a full new-topic
brief. Scope comes from what's asked, not from who's asking: a narrow
request gets a scoped pass (find the specific missing thing, report back)
without redoing the whole dossier.
