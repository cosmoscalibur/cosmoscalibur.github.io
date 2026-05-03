---
date: 2026-05-02
tags: coding agents, artificial intelligence, context engineering, antigravity
category: programming
language: en
---

# Behavioral Guidelines for Coding Agents

In my article on the
[agent readiness framework](/en/blog/2026/marco-de-preparacion-para-agentes-de-codigo.md)
I explained how to evaluate and improve a repository so AI agents can
work effectively. But preparing the environment is only half the
problem. The other half is **telling the agent *how* to behave** inside
that environment.

After months of using coding agents —Antigravity, AmpCode, Opencode— I
have noticed recurring error patterns that no linter catches: silent
overengineering, unsolicited cosmetic changes, hidden assumptions that
blow up three commits later. It turns out I am not the only one. Andrej
Karpathy
[documented exactly these problems](https://x.com/karpathy/status/2015883857489522876)
and the community turned them into a set of guidelines with over 100,000
stars on GitHub.

I have integrated those guidelines into my
[template repository](https://github.com/cosmoscalibur/template) as
part of the `AGENTS.md` file, adapting them into a generic format that
works with any agent. This article explains the rationale behind each
principle and how to apply it in practice.

## Why do agents need behavioral guidelines?

Language models are powerful tools for generating code, but they have
systematic biases that affect output quality:

- **They assume silently.** When an instruction is ambiguous, the model
  picks an interpretation and moves forward without asking. It does not
  manage its own confusion or present alternatives.
- **They overengineer.** They favor abstractions, configuration layers,
  and error handling for impossible scenarios. Where 50 lines would
  suffice, they write 200.
- **They touch adjacent code.** While implementing what you asked, they
  "improve" comments, reformat nearby functions, or remove code they do
  not fully understand.

These behaviors are not model bugs — they are its nature. LLMs are
trained to be helpful and thorough, which in code translates to doing
*more than necessary*. A behavioral guide is the counterweight: a set
of rules that enforce precision over enthusiasm.

## Karpathy's four principles

The guidelines I integrated into the template are based on Karpathy's
observations, systematized by the
[andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
project. They boil down to four principles.

### 1. Think before coding

> State your assumptions explicitly. If multiple interpretations exist,
> present them — don't pick silently. If something is unclear, stop and
> ask.

This principle attacks the most expensive problem: the agent that
starts implementing based on an incorrect assumption. When the agent
verbalizes what it assumes, you can correct it before it writes a
single line of code.

In practice, this means your `AGENTS.md` should instruct the agent to
make its interpretations explicit at the start of each task, not after
it has already implemented something.

### 2. Simplicity first

> No features beyond what was asked. No abstractions for single-use
> code. No error handling for impossible scenarios. If you write 200
> lines and it could be 50, rewrite it. Ask yourself: "Would a senior
> engineer say this is overcomplicated?" If yes, simplify.

Overengineering is the favorite sin of LLMs. This principle establishes
a concrete test: would a senior consider it excessive? It is a
surprisingly effective filter because it forces the model to evaluate
its own output against the standard of an experienced professional.

### 3. Surgical changes

> Don't "improve" adjacent code, comments, or formatting. Don't
> refactor things that aren't broken. Match existing style. Remove only
> imports, variables, or functions that YOUR changes made unused. Every
> changed line should trace directly to the user's request.

This principle protects the codebase from entropy. Without it, every
agent task leaves a trail of unsolicited changes that pollute diffs,
complicate code review, and potentially introduce regressions.

The direct-tracing rule ("every changed line should trace to the
request") is particularly valuable in teams: if a pull request contains
changes nobody asked for, something went wrong.

### 4. Goal-driven execution

> Transform tasks into verifiable goals:
>
> - "Add validation" → "Write tests for invalid inputs, then make them
>   pass"
> - "Fix the bug" → "Write a test that reproduces it, then make it
>   pass"
> - "Refactor X" → "Ensure tests pass before and after"

As Karpathy noted: "LLMs are exceptionally good at looping until they
meet specific goals. Don't tell it what to do, give it success criteria
and watch it go." This principle leverages that strength: instead of
imperative instructions, you give verification criteria the agent can
evaluate on its own.

## How to integrate the guidelines into your project

The guidelines are integrated directly into the `AGENTS.md` of the
[template repository](https://github.com/cosmoscalibur/template). If
you use the template as a base for new projects, you get them
automatically.

If you already have an existing project, integration is
straightforward. Add a `## Behavioral Guidelines` section to your
`AGENTS.md` (or your agent's equivalent instruction file) with the
four rules:

```{code} markdown
## Behavioral Guidelines

- **Think before coding.** State assumptions explicitly. If multiple
  interpretations exist, present them — don't pick silently.
- **Simplicity first.** No features beyond what was asked. No
  abstractions for single-use code.
- **Surgical changes.** Don't "improve" adjacent code. Match existing
  style. Every changed line should trace to the user's request.
- **Goal-driven execution.** Transform tasks into verifiable goals
  with tests as success criteria.
```

Since all major agents —including Antigravity since March 2026—
support `AGENTS.md` natively, these guidelines work uniformly
regardless of which tool you use.

## A note on balance

An important point from the original project that I preserved in the
template: these guidelines bias toward caution over speed. For trivial
tasks — typo fixes, obvious one-liners — the agent should use judgment
and not apply full rigor.

The goal is reducing costly mistakes on non-trivial work, not slowing
down simple tasks.

## Conclusion

Preparing a repository for coding agents requires two complementary
layers: the **infrastructure** (documentation, tests, linting, CI —
covered by the
[readiness framework](/en/blog/2026/marco-de-preparacion-para-agentes-de-codigo.md))
and the **behavior** (how the agent decides what to do and what not to
do). Karpathy's guidelines cover this second layer with four simple
principles that address the most frequent LLM problems in code
generation.

If you have already evaluated your repository with the
[agent readiness skill](https://github.com/cosmoscalibur/template/tree/main/.agents/skills/agent-readiness)
and reached Level 2 or above, adding these behavioral guidelines is
the natural next step. The
[cosmoscalibur/template](https://github.com/cosmoscalibur/template)
repository includes them ready to use.

## References

- [Andrej Karpathy on LLM coding pitfalls](https://x.com/karpathy/status/2015883857489522876).
  Andrej Karpathy, X.
- [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills).
  Forrest Chang. GitHub.
- [Agent-Ready Repository Template](https://github.com/cosmoscalibur/template).
  Cosmoscalibur. GitHub.
- [Agent Readiness Framework for Coding Projects](/en/blog/2026/marco-de-preparacion-para-agentes-de-codigo.md).
  Cosmoscalibur.
