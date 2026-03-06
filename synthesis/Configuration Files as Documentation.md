---
cluster_sources:
- '[[decision/Comment Out Conflicting Environment Variables Rather Than Delete]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
confidence: high
created: '2026-03-06'
name: Configuration Files as Documentation
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
status: active
supports: []
tags: []
type: synthesis
---

# Configuration Files as Documentation

## Insight

Configuration files (`.env`, config.yaml, etc.) can serve dual purpose as both runtime configuration and inline documentation of system behavior, especially when they preserve historical decisions through comments.

This pattern treats config files as living documentation rather than minimal runtime specifications.

## Evidence

**[[decision/Comment Out Conflicting Environment Variables Rather Than Delete]]:**
- Decision to comment out `ANTHROPIC_API_KEY` rather than delete it
- Rationale: "Preserves historical context, shows what was tried and why it didn't work"
- Recommendation: Add inline comments explaining *why* it's disabled

**[[note/Environment Variable Precedence in Multi-Auth Systems]]:**
- Documents precedence rules for multi-auth systems
- Best practices include: "Document which auth method is preferred/recommended"
- Suggests using config files to make precedence explicit

## Implications

**For configuration management:**

**Preserve failed approaches:**
```bash
# ANTHROPIC_API_KEY disabled - conflicts with Claude Code OAuth
# Use OAuth instead (configured in ~/.config/claude-code/)
# ANTHROPIC_API_KEY=sk-ant-...
```

**Document precedence:**
```bash
# Auth methods (in precedence order):
# 1. ANTHROPIC_API_KEY environment variable (if set)
# 2. OAuth flow (default)
# 3. ~/.anthropic_api_key file (fallback)
```

**Explain non-obvious choices:**
```bash
# VAULT_PATH must be absolute, not relative
# Subprocess calls don't inherit CWD
ALFRED_VAULT_PATH=/home/user/vault
```

**For system design:**
- Treat config files as onboarding documentation
- New team members should be able to understand system behavior by reading configs
- Config comments should explain *why*, not *what* (the key name already says *what*)

**For debugging:**
- Commented-out configs show what's been tried
- Inline comments preserve institutional knowledge
- Configuration history visible in version control

## Applicability

This applies to:
- **Multi-auth systems** - document which method is active and why
- **Environment-dependent configs** - explain differences between dev/staging/prod
- **Migration scenarios** - preserve old config during transition
- **Complex precedence rules** - make implicit behavior explicit

**Anti-patterns to avoid:**
- Over-commenting obvious settings (`PORT=3000 # the port`)
- Leaving outdated comments when config changes
- Using comments instead of external documentation for complex topics

**Best practices:**
- Comment the *why* and the *precedence*, not the *what*
- Preserve failed approaches with explanation
- Version control config files to track evolution
- Review comments during config changes

![[synthesis.base#Sources]]
![[synthesis.base#Related]]

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
