---
authority: Claude Code application design
created: '2026-03-07'
janitor_note: ''
location: []
name: Claude Code Requires OAuth Not API Keys
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Claude Code authentication architecture
source_date: '2026-03-07'
status: active
tags: []
type: constraint
---

# Claude Code Requires OAuth Not API Keys

## Constraint

Claude Code is designed to use OAuth authentication for user-facing operations. While the underlying Anthropic API supports API key authentication, Claude Code as an application expects OAuth flow.

## Source

This constraint comes from the Claude Code application architecture. It's not a regulatory or policy constraint, but a technical design constraint.

Discovered during Personal Alfred integration when `ANTHROPIC_API_KEY` environment variable caused authentication failures because it overrode Claude Code's OAuth mechanism.

## Implications

**For integration:**
- Systems integrating with Claude Code must not set `ANTHROPIC_API_KEY` environment variables that would override OAuth
- Configuration files (like `.env`) must not contain API keys for Anthropic services when used with Claude Code
- Other tools in the same environment might use API keys (for server-side automation), but Claude Code components must use OAuth

**For environment configuration:**
- Separate environment namespaces for different auth methods (e.g., `CLAUDE_*` vs `ANTHROPIC_*`)
- Document which components use which auth methods
- Test in isolated environments to prevent cross-contamination

## Expiry / Review

This constraint lasts as long as Claude Code maintains its current authentication architecture. If Claude Code adds API key support in the future, this constraint may be relaxed.

![[constraint.base#Affected Projects]]
![[constraint.base#Related]]

---
![[constraint.base#Affected Projects]]

![[constraint.base#Related]]
