---
date: 2026-05-28
tags: antigravity, code agents, artificial intelligence, ide
category: technology
language: en
---

# Antigravity 2: What's New for Agent-Driven Development

I had already shared my experience with
[Antigravity as an AI development environment](/en/blog/2026/herramientas-de-ia-gratuita-para-desarrolladores-en-2026.md),
covering models, quotas, and basic workflows. But since the launch of
Antigravity 2.0 in May 2026, the tool took a leap that changed how I
work with code agents. It is no longer just an IDE with a built-in
agent — it is now a platform for orchestrating autonomous agents.

In this article, I share the new features that have had the most
impact on my daily workflow, an honest comparison with Claude Code,
and how to install everything on Arch and Manjaro.

## Antigravity as a Modular Product

The first thing to understand about Antigravity 2 is that it is no
longer a monolithic product. It now consists of three complementary
pieces sharing the same agent engine:

- **Antigravity 2.0** (desktop application): the command center for
  agent orchestration. A powerful, versatile GUI, ideal for those who
  prefer visual interfaces or lack familiarity with CLI-mode editors.
- **Antigravity CLI**: a TUI built in Go, lightweight and fast. Native
  integration with existing terminals and editors like Neovim or tmux,
  and works perfectly over SSH. Sessions are interchangeable with the
  desktop application.
- **Antigravity IDE**: a VS Code fork with deep agent integration for
  those who prefer that ecosystem.

All three share the same backend, rules, skills, hooks, and project
concept. This modularity is key because it means Antigravity covers
both the visual developer and the terminal purist, without forcing a
single workflow.

## Key Features in Antigravity 2

### Native Worktrees for Parallel Development

Before version 2, developing simultaneous features in the same
repository was an exercise in patience. The typical flow involved
constant `git checkout` to jump between branches, or manually managing
worktrees with `git worktree add`. Both options disrupted the agent's
and the developer's context.

Antigravity 2 integrates worktrees natively. When starting a
conversation, you can select worktree mode and the IDE automatically
provisions an isolated directory in the background. This allows
multiple agents to work on separate branches simultaneously without
interference.

In practice, this means I can have one agent fixing a bug on
`fix/auth-error` while another develops a new feature on
`feature/dashboard`, each in its own worktree, without one stepping
on the other's changes. When done, the worktree is cleaned up
automatically.

### Multi-Repository Project Concept

Many real-world projects do not live in a single repository. A backend
on one side, a frontend on another, perhaps a shared library in a
third. Before Antigravity 2, each repository was an isolated context,
and coordinating interventions across them required manual effort.

The project concept in Antigravity 2 groups multiple folders into a
logical unit with shared agent configuration, rules, and permissions.
This is especially useful for full-stack projects where a backend API
change requires a coordinated frontend update.

Additionally, the project works as a persistent memory layer across
sessions. The project context — preferences, previous decisions,
relevant codebase facts — is maintained and injected into new
sessions. This avoids having to re-explain the context every time I
start a conversation, something that in tools without this concept
creates constant friction.

### Hook Management and Asynchronous Tasks

In the previous version, running a build, executing tests, or any
long-running process blocked the conversation. The agent would wait
for the command output and could not proceed with other tasks. It was
a silent but real bottleneck.

Antigravity 2 introduces JSON hooks that intercept and control the
agent's behavior for certain events. Combined with asynchronous task
management, the main agent can keep working while a build or test
suite runs in the background. When finished, a notification with the
result is received.

This drastically reduces idle time. Instead of sitting and waiting
for a CI pipeline to finish before asking the agent to fix the errors,
the flow is continuous: the agent monitors, gets notified, and acts.

### Dynamic Subagents for Clean Context

This is probably the most transformative change. In long, complex
conversations, context inevitably gets polluted. The agent accumulates
information from completed subtasks, failed attempts, and intermediate
decisions that are no longer relevant but occupy space in the context
window and can confuse future responses.

Dynamic subagents solve this by delegating subtasks to specialized
agents with their own isolated context. The main agent defines a
subagent, assigns it a specific task, and receives the result without
inheriting all the intermediate context.

The advantage is twofold:

- **Clean context**: the main agent keeps its context window focused
  on the high-level task.
- **Parallel execution**: multiple subagents can work simultaneously
  on independent tasks.

In my typical flow, I use subagents for codebase research while the
main agent implements code. The research subagent reads files, searches
the web, and reports findings — all without polluting the
implementation context.

### Scheduled Tasks with Cron and Timers

This feature solved a very specific problem for me that perfectly
illustrates its usefulness. I was iterating on the development of an
API integration whose free quota was very limited. After exhausting
the quota, I would normally have had to abandon the session and pick
up the work hours later, rebuilding the entire context.

With Antigravity 2's scheduled tasks, instead, I set a timer for the
exact quota renewal time. The agent did not simply fire a deferred
command — it stayed aware, resumed the iteration automatically, and
continued the development cycle without human intervention.

The difference from a simple `sleep` or a system cron is fundamental:
here the agent maintains the full task context, understands what it was
doing before the pause, and knows how to continue. It is the
difference between delegating to a colleague who remembers the entire
project and setting an alarm to remind yourself.

## Antigravity 2 vs. Claude Code

Both tools lead the agentic coding space, but with very different
philosophies. After using both extensively, here is my assessment.

### Antigravity Advantages

- **Profile coverage**: GUI (desktop app), CLI (terminal), and IDE
  (VS Code) — one engine for every developer type. Claude Code only
  offers CLI.
- **Multi-model support**: Gemini, Claude, and GPT in a single
  environment, no need to switch tools to leverage each model's
  strengths.
- **Shared standards**: adoption of AGENTS.md and MCP as
  interoperability protocols.
- **Advanced orchestration**: dynamic subagents, native worktrees,
  multi-repository projects with persistent memory, and scheduled
  tasks — all natively integrated.
- **Terminal parity**: {program}`antigravity-cli` matches Claude Code
  in terminal integration, editor support, and lightweight resource
  footprint. The argument that Claude Code is "lighter" does not hold
  when compared to the CLI.

### Claude Code Advantages

- **Strict sequential control**: its explicit step-by-step approval
  model is very predictable, ideal for production environments where
  supervision must be rigorous.
- **Mature MCP ecosystem**: due to its longer track record, it has
  more third-party integrations and MCP servers available.
- **Auto-memory maturity**: although Antigravity's project concept
  offers equivalent functionality, Claude Code's automatic memory has
  more refinement iterations.

### When to Choose Each

My personal take: Antigravity covers both the visual developer and
the terminal one, while Claude Code only serves the latter. For
anyone already in the Google ecosystem or needing multi-agent
orchestration, Antigravity is the natural choice. Claude Code shines
when you need granular step-by-step control and work exclusively in
the terminal.

## Installing Antigravity on Arch and Manjaro from the AUR

Antigravity's modular philosophy is reflected in its distribution.
Each component has its own AUR package, allowing you to install
exactly what you need:

- {program}`antigravity` — desktop application, command center.
- {program}`antigravity-cli` — terminal agent.
- {program}`antigravity-ide` — VS Code fork with integrated agents.

Installation from the AUR is done with {program}`pamac`:

```{code} bash
pamac build antigravity antigravity-cli antigravity-ide
```

```{tip}
If the application opens with a blank window on Wayland, launch it
with the `--ozone-platform-hint=auto` flag. To make it permanent,
edit the corresponding `.desktop` file and append the flag to the
`Exec=` field.
```

For other Linux distributions, general installation is done by
downloading the tar file from the
[official download page](https://antigravity.google/download).

## Conclusion

Antigravity 2 is not an incremental update. Native worktrees, the
project concept, dynamic subagents, and scheduled tasks fundamentally
transform the relationship between developer and agent. It is no
longer about asking for help line by line — it is about orchestrating
a team of autonomous agents working in parallel while you maintain
the high-level vision.

The future of IDEs is not just to assist, but to orchestrate.

## References

- [Antigravity — Official documentation](https://antigravity.google/).
  Google.
- [Antigravity 2.0 — What's new](https://antigravity.google/whats-new).
  Google.
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code).
  Anthropic.
- [Antigravity AUR packages](https://aur.archlinux.org/packages?K=antigravity).
  Arch Linux.
- [Free AI Tools for Developers in 2026](/en/blog/2026/herramientas-de-ia-gratuita-para-desarrolladores-en-2026.md).
  Cosmoscalibur.
