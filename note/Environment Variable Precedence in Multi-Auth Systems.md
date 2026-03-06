---
created: '2026-03-06'
description: Technical learning about environment variable precedence causing authentication
  conflicts in systems with multiple auth methods
janitor_note: LINK001 — Base view embed reference missing _bases/ directory. System
  must create _bases/ with base view definitions.
name: Environment Variable Precedence in Multi-Auth Systems
project: '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[synthesis/API Key Verification for AI Systems]]'
- '[[synthesis/Environment Variable Propagation in Subprocess Calls]]'
- '[[synthesis/Subprocess Environment Debugging Pattern]]'
relationships: []
session: null
status: active
subtype: learning
tags: []
type: note
---

# Environment Variable Precedence in Multi-Auth Systems

## Problem Pattern

When integrating systems that support multiple authentication methods (e.g., API keys, OAuth, session tokens), environment variables can create unexpected precedence conflicts.

## Concrete Example: personal-alfred Setup

**Scenario:**
- Claude Code uses OAuth authentication by default
- personal-alfred reads environment variables from `.env`
- `.env` contained `ANTHROPIC_API_KEY=invalid_key`

**Result:**
The invalid API key in the environment variable **overrode** Claude Code's OAuth authentication, causing authentication failures.

**Solution:**
Comment out or remove the `ANTHROPIC_API_KEY` from `.env` to allow the OAuth mechanism to function.

## General Principle

**Environment variables typically have higher precedence than configuration files or application defaults.** This means:

1. An environment variable will often override built-in authentication mechanisms
2. Invalid or outdated environment variables can break working systems
3. When debugging auth issues, check environment variables first — even if you expect a different auth method to be in use

## Best Practices

**For system design:**
- Document which auth method is preferred/recommended for each component
- Make environment variable precedence explicit in documentation
- Consider warning users when multiple auth methods are detected

**For debugging:**
- Check for conflicting environment variables when auth fails
- Look in `.env`, `.bashrc`, `.zshrc`, and other env config files
- Test with a clean environment to isolate the issue

**For integration:**
- Use a single auth method per integration point when possible
- If multiple methods are supported, document the precedence order clearly
- Consider using separate environment namespaces (e.g., `CLAUDE_API_KEY` vs `ALFRED_API_KEY`)

## Applicability

This applies to any system that:
- Supports multiple authentication methods
- Reads configuration from environment variables
- Integrates multiple tools with different auth patterns

Common examples:
- CLI tools with both API key and OAuth support
- Containerized applications reading secrets from env vars
- CI/CD pipelines with multiple secret sources
- Development environments with mixed production/development credentials

## Related
![[related.base#All]]
