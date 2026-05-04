---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-05-04'
decided_by:
- '[[person/Ben Ripper]]'
janitor_note: ''
name: Antigravity Is VSCode-Family IDE with Claude Code as Native Extension
project: []
related: []
session: crm-agentic-2026-04-30
source: crm-agentic session 2026-04-30
source_date: '2026-04-30'
status: final
supports: []
tags: []
type: decision
---

# Antigravity Is VSCode-Family IDE with Claude Code as Native Extension

## Context

During the NovaCRM Agentic session (2026-04-30), "Antigravity" was referenced in context of Claude Code. It was initially unclear whether Antigravity referred to a Claude Code feature, plugin, or mode.

## Options Considered

1. **Antigravity as a Claude Code feature/mode** — some internal capability within Claude Code itself
2. **Antigravity as a separate IDE** — a distinct VSCode-family IDE that ships with Claude Code installed as a native extension

## Decision

Antigravity is the name of a VSCode-family IDE in which Claude Code is installed as a native extension — not a Claude Code feature.

## Rationale

User confirmed this directly in the 2026-04-30 session. The goal of that session was to observe Claude Code operating in real-time from a separate terminal window while it worked inside the Antigravity IDE environment.

## Consequences

- References to "Antigravity" in session notes should be read as IDE context, not Claude Code feature flags
- Claude Code's behavior inside Antigravity may differ from standard terminal invocation (native extension vs. CLI)
- Observing Claude Code from an external terminal while it runs in Antigravity is a valid workflow pattern
