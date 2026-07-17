---
name: blog-skill-feedback
description: >-
  Diagnose and fix a defect in one of the editorial pipeline's skills or
  in `CLAUDE.md` — not a one-off content mistake in a single post, but a
  gap or contradiction in the rules that produced it. Use when the author
  flags that something is a process/skill problem rather than a draft
  problem, or when `blog-editor-review` recommends it after spotting a
  pattern-shaped finding. Invoked explicitly by the author; not part of
  the linear `blog-research` → ... → `blog-publish` pipeline.
---

# Blog Skill Feedback

Reviews and edits the editorial pipeline's own skills (and, when the
defect is genuinely about sequencing, `CLAUDE.md`) in response to a
concrete failure observed in a real post. Never edits speculatively —
every change traces to something that actually went wrong, not a
hypothetical improvement.

## Diagnostic checklist

Run every candidate fix through these questions before proposing it.
Getting the placement wrong (skill vs. orchestrator, or the wrong skill)
just relocates the same failure mode instead of fixing it.

- **Orchestrator vs. skill**: does the defect concern *sequencing or
  approval-waiting between two skills* (which skill runs next, who waits
  for the author before proceeding)? That's `CLAUDE.md`'s job — fix it
  there, not in either skill. Does it concern *what one stage does with
  its own inputs* (voice, fact-gathering, structure)? That's the skill's
  own job — fix it there, not in `CLAUDE.md`. A skill should only contain
  its own internal-approval language when the approval gates that skill's
  own terminal, hard-to-reverse action (e.g. `blog-publish`'s commit-
  message approval before `git push`) — never as a restatement of an
  inter-skill handoff `CLAUDE.md` already governs.
- **Caller independence**: does a skill's behavior change based on *which
  skill invoked it*, rather than *what was asked*? That's a violation —
  scope comes from the request's shape (a full brief vs. a narrow
  fact-lookup; a draft vs. a specific data point), never from caller
  identity. The inverse is fine: a skill declaring "I may invoke skill X
  for purpose Y" describes its own capability and is not a violation.
- **Redundancy**: does the fix duplicate a rule already stated elsewhere
  (in the same file, or a different one)? Consolidate into one place
  rather than restating the same clarification twice — a rule split
  across sections is harder to keep consistent under future edits, not
  more thorough.
- **Description clarity**: does the frontmatter `description:` still
  accurately reflect when and how the skill is invoked after the fix
  (including any new invocation mode)? Stale descriptions are how a skill
  stops getting picked for cases it now actually handles.
- **Best practices**: is the new rule stated as a general principle with
  its reasoning (so future edge cases can be judged), not as a one-off
  patch describing exactly what happened in the triggering post?
- **Orchestration impact**: does this change alter what `CLAUDE.md`
  documents (the stage diagram, checkpoint definitions, the count/list of
  pipeline skills)? Only touch `CLAUDE.md` if the answer is genuinely yes.

## Process

1. Start from the concrete failure — quote what went wrong in the actual
   post/draft, not an abstract description.
2. Trace it to the specific skill(s) or `CLAUDE.md` section responsible,
   using the checklist above to place it correctly.
3. Present findings and a proposed plan (which file(s), what changes, one
   line of reasoning each) to the author. This is a hard stop — editing a
   skill file changes how every future post gets produced, which makes it
   this skill's own terminal, hard-to-reverse action. Never edit before
   the author explicitly approves the plan, the same way `blog-publish`
   never commits before the commit message is approved.
4. Apply exactly the approved edits. Don't fold in unrelated cleanup
   noticed along the way — flag it separately instead.

## Scope

Never runs `git add`, `git commit`, or `git push` — editing skill files is
not exempt from the project's standing git-safety rules. If the author
wants the changes committed, that's a separate, explicit request handled
the normal way, not something this skill does on its own.

## Handoff

Nothing downstream. This skill is invoked on demand, not as a pipeline
stage — after it finishes, the author resumes whatever post-production
work prompted the feedback (which may mean re-running an earlier stage
under the corrected rules).
