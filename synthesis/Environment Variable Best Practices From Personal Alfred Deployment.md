---
cluster_sources:
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
confidence: high
created: '2026-03-24'
name: Environment Variable Best Practices From Personal Alfred Deployment
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
status: active
supports: []
tags: []
type: synthesis
---

# Environment Variable Best Practices From Personal Alfred Deployment

## Insight

The personal-alfred deployment revealed a comprehensive set of best practices for environment variable management in subprocess-based architectures. These practices address both **override conflicts** and **propagation failures**.

## Evidence

Three debugging sessions revealed systematic patterns:

1. **[[note/Personal Alfred API Key Bug Fix]]** — Environment variable overriding application auth
2. **[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]** — Environment variable failing to propagate
3. **[[note/Environment Variable Precedence in Multi-Auth Systems]]** — General pattern synthesis

## Implications

### For `.env` Files

**Use comments as documentation:**
```bash
# Commented out 2026-03-24: Was overriding Claude Code OAuth
# ANTHROPIC_API_KEY=sk-...

# Required for alfred-vault subprocess operations
ALFRED_VAULT_PATH=/home/user/obsidian-vault
```

**Benefits:**
- Preserves history of configuration changes
- Documents WHY a variable was disabled
- Provides reference for future debugging

### For Subprocess Spawning

**Explicitly declare environment propagation:**
```python
# Bad: Implicit environment inheritance
subprocess.run(['alfred', 'vault', 'list'])

# Good: Explicit environment propagation
env = os.environ.copy()
env['ALFRED_VAULT_PATH'] = vault_path
subprocess.run(['alfred', 'vault', 'list'], env=env)
```

### For Multi-Auth Systems

**Document precedence explicitly:**
```
Authentication method selection:
1. OAuth token (if present) — for interactive use
2. ANTHROPIC_API_KEY env var — for automation
3. Config file API key — legacy support

To force a specific method, set AUTH_METHOD=oauth
```

### For System Integration

**Three-phase validation:**
1. **Before integration:** Document environment requirements
2. **At startup:** Validate environment and log active configuration
3. **On failure:** Error messages should indicate which env vars were checked

## Applicability

These patterns apply to:
- CLI tools that spawn other CLI tools
- Agent systems that spawn sub-agents
- Any system with subprocess boundaries
- Multi-tenant or multi-user deployments where environment isolation matters

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
