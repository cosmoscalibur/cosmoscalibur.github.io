---
date: 2026-03-07
tags: AGENTS.md, antigravity, artificial intelligence, coding agents, context engineering,
  factory ai
category: programming
language: en
---------------------

# Agent Readiness Framework for Coding Projects

Coding agents are here, and they are not going away. But after months of
using them —Antigravity, AmpCode, Opencode, Zed's built-in agent— I have
reached an uncomfortable conclusion: **the problem is usually not the
agent, it is the project**. A poorly prepared repository will defeat any
agent, regardless of how advanced its underlying model is.

I wrote about
[context engineering](/en/blog/2026/ingenieria-de-prompt-habilidad-o-estafa.md)
before, and about which
[free AI tools](/en/blog/2026/herramientas-de-ia-gratuita-para-desarrolladores-en-2026.md)
are available for developers. This post connects both ideas: if context
is king, your repository needs to be a kingdom worth exploring.

The framework I present here is based on the *Agent Readiness Model* by
[Factory AI](https://factory.ai/news/agent-readiness), which defines five
maturity levels and nine technical pillars for evaluating how ready a
repository is for autonomous development. I adapt it with my practical
experience and a note for Antigravity users, whose context system differs
from the `AGENTS.md` standard.

## What is the agent readiness framework?

It is a maturity model that measures how prepared your repository is for
AI agents to work autonomously. It does not evaluate the agent —it
evaluates the project: its documentation, tooling, tests, security, and
conventions.

The fundamental premise is that **the agent is not magic**. It is only as
good as the environment you provide. A repository with pre-commit hooks,
fast tests, and clear documentation lets the agent iterate in seconds. One
without those foundations forces the agent to guess, wait minutes for CI
feedback, and repeat mistakes that a local check would have caught
instantly.

The best part: every improvement you make for agents equally benefits
the human developers working on the project.

## The five readiness levels

The model defines five progressive levels. To unlock the next one, you
need to pass at least 80% of the criteria at the current level.

### Level 1: Functional

The code compiles and runs, but requires manual setup and lacks automated
validation. This is the baseline every repository should meet.

**Key criteria:**

- {file}`README.md` with setup and run instructions.
- Linter configured (e.g., {program}`ruff` for Python, {program}`eslint`
  for JavaScript).
- Type checker (e.g., {program}`pyright`, TypeScript strict mode).
- Unit tests that exist and run locally.
- Code formatter configured.

**Without this:** The agent cannot verify its own work. It generates code,
waits for CI (if it exists), fails, and iterates blindly.

### Level 2: Documented

Basic documentation and processes exist. Workflows are written down and
some automation is in place.

**Key criteria:**

- `AGENTS.md` or equivalent agent instruction file with commands,
  conventions, and boundaries.
- Devcontainer or reproducible development environment.
- Pre-commit hooks configured.
- Branch protection enabled.
- Environment variables documented (e.g., {file}`.env.example`).

**Without this:** The agent has to figure out how your project works on
its own. It guesses conventions, does not know which commands to run, and
has no security guardrails.

### Level 3: Standardized

Clear processes defined, documented, and enforced through automation.
**This is the minimum target for productive agent work.**

**Key criteria:**

- Integration and/or end-to-end tests.
- Secret scanning enabled.
- Distributed tracing and metrics (observability).
- Documentation maintained and up to date.
- {file}`CODEOWNERS` configured.

**Without this:** The agent can handle simple tasks but introduces subtle
bugs in complex flows that only integration tests would catch.

### Level 4: Optimized

Fast feedback loops and data-driven improvement. Systems are designed for
productivity and measured continuously.

**Key criteria:**

- CI with fast feedback (minutes, not hours).
- Regular deployment frequency.
- Flaky test detection.
- Team performance metrics.

**Without this:** The agent works, but slowly. It waits too long for
feedback and cannot iterate at the speed its capability allows.

### Level 5: Autonomous

Self-improving systems with sophisticated orchestration. Complex
requirements decompose automatically into parallelized execution.

This level represents the long-term goal: the agent not only implements
but discovers work, prioritizes, executes, and verifies autonomously.

## The nine technical pillars

Each level is evaluated across nine pillars covering the fundamental
dimensions of a repository:

1. **Style & validation**: Linters, formatters, type checkers, pre-commit
   hooks.
2. **Build system**: Deterministic commands, pinned dependencies,
   documented builds.
3. **Testing**: Unit, integration, locally runnable, coverage tracking.
4. **Documentation**: README, `AGENTS.md`, architecture guides, coding
   conventions.
5. **Development environment**: Devcontainer, environment templates,
   local services setup.
6. **Debugging & observability**: Structured logging, distributed tracing,
   metrics.
7. **Security**: Branch protection, secret scanning, CODEOWNERS.
8. **Task discovery**: Issue templates, labeling system, PR templates.
9. **Product & experimentation**: Analytics, feature flags, experiment
   infrastructure.

```{tip}
You do not need to cover all pillars to start. Focus on the Level 1 and
Level 2 pillars first: style, build, testing, and documentation. These
have the highest impact on agent output quality.
```

## Agent documentation: AGENTS.md and alternatives

A core component of Level 2 is the agent instruction file. `AGENTS.md`
has become the emerging standard, adopted by over 60,000 GitHub
repositories and stewarded by the Agentic AI Foundation under the Linux
Foundation.

A good `AGENTS.md` includes:

- Copy-pasteable build, test, and lint commands.
- Coding conventions and preferred patterns.
- Project structure and key file locations.
- Boundaries: what the agent should never touch, which architecture
  decisions are non-negotiable.
- Testing instructions and git workflow.

`CLAUDE.md` was the predecessor created by Anthropic for Claude Code, and
`AGENTS.md` is its standardized evolution that works with most agents:
GitHub Copilot, AmpCode, Cursor, Opencode, Zed, and others.

### A note for Antigravity users

If you use Antigravity as your primary IDE (as I do), there is an
important detail: **Antigravity does not read `AGENTS.md` or `CLAUDE.md`
automatically**. Its context system uses {file}`.agent/rules/` for
workspace rules and {file}`~/.gemini/GEMINI.md` for global configuration.

This does not invalidate the framework —the five levels and nine pillars
apply regardless— but it requires an adaptation in how you provide
context to the agent:

1. **Maintain documentation in {file}`README.md` and {file}`docs/`** as
   the shared source of truth for humans and agents alike.
2. **Create an agent rule** in {file}`.agent/rules/` that explicitly
   instructs the agent to read that documentation before acting.
3. **Optionally, keep `AGENTS.md`** for tools that support it. The source
   of truth remains your documentation.

An example rule at {file}`.agent/rules/documentation-first.md`:

```{code} markdown
Before starting any task in this project, read the following files:
- README.md for project overview and setup
- docs/architecture.md for system architecture
- docs/conventions.md for coding conventions
Follow the guidelines in these documents for all code generation.
```

This way, a single set of documentation serves all agents and every
human developer.

## Evaluate your repository

I have created an
[agent skill](https://github.com/cosmoscalibur/template/tree/main/.agents/skills/agent-readiness)
that automates the readiness evaluation. The skill audits all nine
pillars, scores each criterion (✅ pass / ⚠️ partial / ❌ fail),
determines the current level, and generates a phased improvement plan.

The skill is designed as a standard agent skill, compatible with
Antigravity and other agents that support the skills format. You can
copy it into your project and run it from your agent.

It includes:

- Automatic ecosystem detection (Python, Rust, Node, Go, etc.).
- Detailed evaluation of all nine pillars with evidence per criterion.
- Content quality evaluation of agent context (not just whether the file
  exists, but whether the content is useful).
- Modernization recommendations (e.g., migrate from {program}`pylint` to
  {program}`ruff`, from {program}`pip` to {program}`uv`).
- Phased implementation plan with `[NEW]` / `[MODIFY]` / `[DELETE]`
  change markers.

## Conclusion

Agent readiness is not an abstract concept. It is a concrete set of
practices you can measure, improve iteratively, and that benefit everyone
working on the project —humans and agents alike.

The Agent Readiness Model provides a clear roadmap: start at Level 1,
reach Level 3 as the minimum viable bar for productive agent work, and
keep advancing. The investment is never wasted when you switch agents or
tools, because you are improving the project, not optimizing for a
prompt.

As I wrote in my article on
[context engineering](/en/blog/2026/ingenieria-de-prompt-habilidad-o-estafa.md):
the skills that get you good results from AI are the same skills that
make you a good professional. This framework is the practical expression
of that idea.

## References

- [Introducing Agent Readiness](https://factory.ai/news/agent-readiness).
  Factory AI.
- [Agent Readiness Overview](https://docs.factory.ai/web/agent-readiness/overview).
  Factory AI Documentation.
- [AGENTS.md](https://agents.md/). AGENTS.md.
- [How to write a great agents.md: Lessons from over 2,500 repositories](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/).
  GitHub Blog.
- [Is your repo ready for the AI Agents revolution? Checklist](https://domizajac.medium.com/is-your-repo-ready-for-the-ai-agents-revolution-926e548da528).
  Dominika Zając.
- [Rules / Workflows](https://antigravity.google/docs/rules-workflows).
  Google Antigravity Documentation.
- [Agent Readiness Skill](https://github.com/cosmoscalibur/template/tree/main/.agents/skills/agent-readiness).
  Cosmoscalibur.
