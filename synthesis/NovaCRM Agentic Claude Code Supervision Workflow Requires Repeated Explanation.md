---
cluster_sources:
- '[[session/crm-agentic 2026-04-28 0dd11c01]]'
- '[[session/crm-agentic 2026-04-30 0dd11c01]]'
confidence: medium
created: '2026-05-04'
name: NovaCRM Agentic Claude Code Supervision Workflow Requires Repeated Explanation
project:
- '[[project/NovaCRM Agentic]]'
status: active
type: synthesis
---

# NovaCRM Agentic Claude Code Supervision Workflow Requires Repeated Explanation

## Insight

The same IDE orientation and real-time observation workflow was explained in two separate sessions two days apart (2026-04-28 and 2026-04-30). Both sessions had nearly identical goals: understand how to watch Claude Code work in real-time and navigate the Antigravity IDE. The first session did not produce durable retention of the workflow.

## Evidence

- Session 2026-04-28: Goals include "understand how to watch Claude Code work in real-time" and "get orientation of the Antigravity IDE"
- Session 2026-04-30: Goals include "understand how to watch Claude Code work in real-time from the terminal" and "learn how to navigate and utilize an IDE"
- Both sessions reached identical conclusions: Antigravity = VSCode-family IDE, Claude Code = native extension, observation via stream-json/git diff/split pane

## Implications

The supervision workflow for agentic development (streaming JSON, split pane file watching, git diff) is not intuitive enough to retain from a single explanation. New operators of Claude Code in an agentic context need reference documentation, not just verbal walkthrough. A durable "how to supervise Claude" runbook would eliminate repeated onboarding overhead.

## Applicability

Applies to any project where Ben Rippere or other non-technical operators are supervising Claude Code's agentic development work. The pattern may recur on other projects.

![[synthesis.base#Sources]]
![[synthesis.base#Related]]
