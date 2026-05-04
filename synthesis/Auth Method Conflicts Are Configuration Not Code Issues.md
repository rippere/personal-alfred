---
cluster_sources:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
confidence: medium
created: '2026-03-07'
janitor_note: ''
name: Auth Method Conflicts Are Configuration Not Code Issues
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
status: active
supports: []
tags: []
type: synthesis
---

# Auth Method Conflicts Are Configuration Not Code Issues

## Insight

When a system supports multiple authentication methods, failures often manifest as configuration conflicts (environment variables, config files) rather than code bugs. The personal-alfred OAuth debugging revealed that the "broken" authentication wasn't a code issue — it was competing configuration sources.

## Evidence

- [[note/Personal Alfred API Key Bug Fix]] — System appeared broken but code was fine; .env file had ANTHROPIC_API_KEY that overrode OAuth
- [[note/Environment Variable Precedence in Multi-Auth Systems]] — Pattern analysis showing environment variables typically override application-default auth methods

## Implications

**For debugging:**
- When auth fails in multi-auth systems, audit configuration files first
- Check ALL potential config sources: .env, .bashrc, .zshrc, config.yaml, etc.
- Test with clean environment to isolate config from code issues

**For system design:**
- Document auth method precedence explicitly
- Consider warning users when multiple auth methods are detected
- Use distinct environment variable namespaces to avoid collisions

## Applicability

Applies to any system integrating multiple components with overlapping auth capabilities — especially when combining user-facing tools (OAuth) with automation tooling (API keys).

![[synthesis.base#Sources]]
![[synthesis.base#Related]]

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
