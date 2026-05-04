---
authority: System architecture decision
created: '2026-03-07'
janitor_note: ''
location: []
name: Must Support Both OAuth and API Key Auth Methods
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Integration requirements
source_date: '2026-02-16'
status: active
tags: []
type: constraint
---

# Must Support Both OAuth and API Key Auth Methods

## Constraint

The personal-alfred system must support both OAuth and API key authentication methods for Anthropic Claude integration. This is not optional — different components require different auth strategies.

## Source

System architecture: Claude Code uses OAuth for interactive sessions, while automated/programmatic access requires API keys. The integration layer must accommodate both.

## Implications

**For configuration:**
- Cannot standardize on a single auth method across all components
- Must document which component uses which method
- Must handle precedence when both are configured (environment variables vs OAuth)

**For development:**
- Code must detect which auth method is active
- Error messages must distinguish between auth method failures vs credential failures
- Testing must cover both auth paths

**For deployment:**
- Environment setup must configure the correct auth method for each component
- .env files and environment variables must not conflict with OAuth flows
- Documentation must explain when to use each method

## Expiry / Review

Active constraint until architecture changes. Review if Anthropic Claude changes auth methods or if personal-alfred architecture consolidates on a single integration pattern.

![[constraint.base#Affected Projects]]
![[constraint.base#Related]]

---
![[constraint.base#Affected Projects]]

![[constraint.base#Related]]
