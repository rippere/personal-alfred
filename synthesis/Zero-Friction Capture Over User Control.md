---
cluster_sources:
- '[[Start Here]]'
- '[[decision/Session Detection Should Be Automated Not Manual]]'
confidence: high
created: '2026-03-06'
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions. ORPHAN001 — Foundational synthesis,
  no inbound links expected.
name: Zero-Friction Capture Over User Control
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
status: active
supports: []
tags: []
type: synthesis
---

# Zero-Friction Capture Over User Control

## Insight

Alfred OS consistently prioritizes automatic capture with zero user friction over giving users explicit control. This pattern appears in multiple design decisions: automated session detection, auto-generated base views, and the alfred_instructions inline command queue.

## Evidence

- Sessions: "You don't manually start or stop sessions" — fully automated
- Base views: "No maintenance — the data IS the view" — auto-generated
- Alfred instructions: "Zero friction, no context switching" — inline commands vs. separate UI
- The guide emphasizes "no manual maintenance," "automatically," "live queries"

This reveals a consistent design philosophy: minimize interruption to flow, maximize capture, accept reduced user control.

## Implications

- Power users who want fine-grained control may find the system limiting
- System must have high-quality inference to avoid bad automatic decisions
- Users must trust the system's automation to adopt it
- Edge cases where automation fails will be more frustrating because no manual override exists
- Design reviews should always ask: "Can this be automatic? Should user intervention be optional, not required?"

## Applicability

This is a core design philosophy for Alfred OS. All feature development should be evaluated against this principle. When adding new features, default to automation and only add manual controls when automation is provably insufficient.

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
