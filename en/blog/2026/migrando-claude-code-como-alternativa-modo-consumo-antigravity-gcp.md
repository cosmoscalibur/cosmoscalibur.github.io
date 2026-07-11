---
date: 2026-07-11
tags: antigravity, claude code, google workspace, opinion
category: technology
language: en
---

# Migrating to Claude Code as an Alternative to Antigravity's Pay-As-You-Go Mode on GCP

I found out through a pop-up in Antigravity's own interface that the
tool would stop being included in corporate Google Workspace licenses.
The change took effect on July 7, 2026, and my work account was
capped at the same quota as any free user. I had already written
enthusiastically about
[what's new in Antigravity 2](/en/blog/2026/antigravity-2-novedades-para-el-desarrollo-agentico.md),
but this billing change made me rethink my entire agentic
development stack, both at work and personally.

The cutback wasn't a minor quota adjustment. As documented in a
[Google AI community thread](https://discuss.ai.google.dev/t/antigravity-seems-to-be-soft-deprecated/143615/3),
Google notified Workspace administrators, around May 5, 2026, that it
would discontinue the AI Ultra Access add-on — the Workspace plan
(~$250/month) that included the Antigravity, Gemini CLI, and Gemini
Code Assist plugin developer tools. Without administrator action, the
organization automatically migrates to the much cheaper AI Expanded
Access add-on ($24/month), which doesn't include those developer
tools. The change applies from July 7, 2026 for flexible plans, and
from the next renewal on or after that date for annual plans. Losing
that add-on leaves no middle ground: there is no paid corporate
subscription plan for Antigravity as such.

## Pay-as-you-go: higher bills, no Claude

The change forces a choice between two paths, and neither is free or
convenient. The first is enabling consumption-based billing: activate
the Agent Platform API on your own or your organization's Google
Cloud (GCP) project, link a billing account, and sign in to
Antigravity using that project as the backing account. Usage then gets
billed per token and per compute time in the agent's sandbox,
instead of being bundled with the Workspace license — the bill goes
up, no exceptions.

But the real problem with this path isn't just the added cost: per
[Antigravity's model documentation](https://antigravity.google/docs/models),
Enterprise plans — the ones consumption mode falls under — only offer
Gemini models. Anthropic models are available exclusively on personal
plans. For any corporate team relying on Claude for its agentic
workflow, this is the critical point — the "official" path to keep
using Antigravity as a business leaves you, in practice, without
access to Anthropic.

It's a real SLA problem: Google acts as a router to a third party's
infrastructure that it doesn't host or operate directly, and that's
why it can't extend to its Enterprise customers the same service
guarantee it would offer over its own infrastructure.

## Personal accounts: Claude 4.6, no update in sight

The second path is skipping consumption mode and sticking with a paid
personal account. Claude does show up in the picker there — but the
newest available Anthropic model is still Claude 4.6, with no mention
of an upcoming update, while Anthropic is already three versions
ahead: 4.7, 4.8, and 5.

This is the most frustrating part, because Antigravity's developer
experience still feels better than Claude Code's in several ways:
native multirepo project support, per-conversation worktree
management with no manual intervention, the ability to leave inline
comments directly on the agent's artifacts, and standards already
shared with Claude Code like AGENTS.md. But all of those tooling
advantages become irrelevant — even counterproductive — if the model
behind them isn't up to the task. A brilliant IDE orchestrating an
outdated model still produces worse code than a more austere CLI
orchestrating the best model available.

Given the lack of up-to-date Anthropic models — whether because
consumption mode simply doesn't offer Claude, or because the personal
account leaves it stuck on 4.6 — I seriously tried using Gemini Flash
and Gemini Pro as the main engine inside Antigravity for real
development tasks. The experience wasn't pleasant: on refactoring
tasks with broad context, on following project-specific code style
instructions, and on the overall quality of proposed diffs, both
models consistently landed below what I was already getting from
Claude in the same IDE. This isn't a blanket dismissal of Google's
models — they likely perform well for other tasks — but for the kind
of agentic coding work I do daily, the difference was noticeable
enough to rule them out as a primary option.

## My decision: migrating to Claude Code

With both paths exhausted — consumption mode without Claude, or a
personal account with Claude stuck in place — the decision was
simple, if uncomfortable: I'm migrating my workflow, both personal and
corporate, to Claude Code.

I'd rather deal with the learning curve and friction of stricter
step-by-step control, backed by an up-to-date model, than enjoy a
superior IDE tied to a model catalog that either doesn't include
Claude at all or leaves it outdated. This doesn't close the door on
Antigravity — if Google wires Claude into consumption mode and
updates the personal-account cap, the equation could change again.
But for now, the relationship between tooling and model is what
decides which tool I use, not the other way around.

## Conclusion

Antigravity's cutback for Workspace accounts on July 7 was just the
entry point to a deeper problem: neither consumption mode nor a
personal account gets you an up-to-date Claude inside Antigravity.
That limitation is an SLA problem — a consequence of depending on a
third party Google doesn't operate directly — and a matter of
Google's product roadmap. As long as that gap exists, no amount of
tooling advantage — however good — makes up for working without the
best model available.

## References

- [Antigravity — Model availability by plan](https://antigravity.google/docs/models).
  Google.
- [Antigravity seems to be soft-deprecated](https://discuss.ai.google.dev/t/antigravity-seems-to-be-soft-deprecated/143615/3).
  Google AI Developers Forum.
- [Antigravity 2: What's New for Agent-Driven Development](/en/blog/2026/antigravity-2-novedades-para-el-desarrollo-agentico.md).
  Cosmoscalibur.
