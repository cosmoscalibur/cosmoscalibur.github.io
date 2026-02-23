---
date: 2026-02-23
tags: artificial intelligence, language model, prompt engineering, context engineering
category: opinion, technology
language: en
---

# Prompt Engineering: Technical Skill or Scam?

Prompt engineering was sold as the skill of the future. Courses, certifications,
job titles, books, and even graduate programs sprang up around the idea that
knowing *how* to talk to an AI was a differentiating technical competency. But
was it really, or was it just a temporary patch for the limitations of language
models?

## The Origin: A Patch for Deficient Models

To understand why prompt engineering existed, you need to remember what language
models were like just a couple of years ago. GPT-3 and the first open models had
limited natural language comprehension. They didn't understand ambiguous
instructions, lost context easily, and needed users to structure requests in
very specific ways to produce useful results.

That's where prompt engineering was born: a set of techniques —*few-shot
prompting*, *chain-of-thought*, *role prompting*, delimiters, explicit output
formats— designed to compensate for the models' comprehension deficiencies. It
wasn't a skill about *what* you needed, but about *how* to ask a model that
didn't understand you well.

In other words, prompt engineering was the user interface that models lacked. It
was the equivalent of memorizing terminal commands before graphical interfaces
existed: necessary at the time, but destined to be absorbed by technological
evolution.

## How You Ask Is No Longer the Problem

Today's language models —Gemini 3, Claude Sonnet 4.5, GPT-5, Llama 4— are
radically different. They understand natural language instructions without rigid
formats. They can handle extended contexts, maintain coherence across long
conversations, and most importantly, interpret the intent behind an imprecise
request.

Do you need to tell Claude Sonnet to "act as an expert in X" to get a good
answer? No. Do you need to structure your question with `###` delimiters and
*few-shot* examples for Gemini 3 Pro to understand what you want? No either.
Models are now capable enough to understand you if you tell them what you need
clearly, the way you would tell a competent colleague.

This doesn't mean that how you communicate with AI is irrelevant. But the
barrier is no longer technical. If you can express what you need clearly, the
model will understand you. The problem is no longer the *how*, but the *what*.

### The Exception: AI Development

There's an important nuance. For AI developers —those building processing
pipelines, autonomous agents, or RAG systems— prompt engineering remains
relevant as an optimization technique. In that context, structuring system
prompts, controlling temperature, using *few-shot* for classification tasks, or
defining JSON output formats are valid technical decisions that directly impact
system performance.

But this is software engineering, not a "skill of the future" for everyday
users. It's like saying that knowing how to configure a web server is a
universal skill because everyone uses the internet.

## From Prompt Engineering to Context Engineering

If prompt engineering was about *how* to ask the AI something, context
engineering is about *what* you need and *what information* the AI should work
with. This shift is fundamental.

Context engineering rests on two pillars:

### 1. Injected Context

Modern AI agents don't work solely with your message. They work with layers of
context that you configure beforehand:

- **Context files**: Define the general behavior, response style, constraints,
  and conventions the agent should always follow. They are configured globally
  or per project through files like `AGENTS.md`, `CLAUDE.md`, `.cursorrules` or
  `.agent/rules` (Antigravity), which the agent reads automatically to
  understand your code's conventions, architecture, and technical decisions.
- **Agent skills**: Specialized instructions for specific tasks that the agent
  loads when needed. For example, a skill for writing documentation, another for
  code review, another for generating tests. It's not a magic prompt: it's a
  workflow specification.

None of this requires knowing prompting techniques. It requires knowing how to
define clear rules, document conventions, and structure your project's
knowledge.

### 2. Clear Specifications in the Prompt

The second pillar is what you actually write in each interaction. And here's the
key: it's not about *how* to write it (that's prompt engineering), but *what* to
write. The skills you need are:

- **Spec design**: Knowing how to precisely describe what you want built.
  Functional requirements, constraints, edge cases, acceptance criteria. It's
  the same thing you'd do when writing a well-crafted ticket or user story.
- **Solution design**: Having a clear vision of how the solution should work.
  You don't need to implement it, but you do need to know which components are
  involved, what data flows, and what outcome you expect.
- **Solution architecture**: For complex tasks, knowing how to decompose the
  problem into manageable parts, define interfaces between components, and
  establish an execution order. This is engineering thinking, not prompting
  tricks.

In short: the skills that get you good results from AI are the same ones that
make you a good professional. Clarity, precision, structured thinking, and the
ability to decompose problems.

## So, Was It a Scam?

I wouldn't say it was a deliberate scam, but it was a skill with an expiration
date around which an entire industry was built. "Prompt engineering" courses
that promise to transform your career in 2026 are selling obsolete knowledge.
Prompting certifications are the current equivalent of a "web search"
certification in 2005.

What you actually need to learn has nothing to do with formatting tricks. You
need to learn to think clearly, to design solutions, to write specifications
that leave no ambiguity. And if you work with AI agents, you need to learn to
configure their context: rules, skills, and project documentation.

Prompt engineering is dead. Context engineering has replaced it. And the good
news is that the skills you need to master it are the ones that have always
defined a good professional.

## References

- [Context engineering](https://simonwillison.net/2025/Jun/27/context-engineering/).
  Simon Willison.
- [The New Skill in AI is Not Prompting, It's Context Engineering](https://www.philschmid.de/context-engineering).
  Philipp Schmid.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
  Anthropic.
