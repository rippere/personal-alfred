---
based_on:
- '[[session/personal-alfred—2026-05-01—system-audit-and-repo-setup]]'
confidence: high
created: '2026-05-04'
name: Alfred Application Infrastructure Was Unversioned Before May 2026
project:
- '[[project/Personal Alfred]]'
related:
- '[[decision/Two-Repo Architecture for Personal Alfred Application Layer]]'
- '[[synthesis/Two-Repo Separation Pattern: Vault Content vs Application Infrastructure]]'
- '[[assumption/Desktop Missing Development Scripts Requires Manual Transfer]]'
source: 2026-05-01 system audit
source_date: '2026-05-01'
status: confirmed
type: assumption
---

# Alfred Application Infrastructure Was Unversioned Before May 2026

## Claim
The Alfred application layer — config.yaml, systemd service units, Claude Code session-capture hooks, and maintenance scripts — was never committed to version control before the 2026-05-01 system audit. It existed only as files on the desktop machine with no git history and no mechanism for propagation to other machines.

## Basis
The 2026-05-01 session audit explicitly found that "the Alfred application layer had never been version-controlled and only existed on this machine." This discovery motivated the two-repo architecture decision and the initialization of the personal-alfred git repo in that session.

## Evidence Trail
2026-05-01: System audit found application layer unversioned. personal-alfred git repo initialized and first commit made during the same session, becoming the first version-controlled state of the application infrastructure.

## Impact
Explains why the desktop was the single source of truth for infrastructure configuration, why the laptop was missing scripts like llm_ingest.py, and why other machines had incomplete Alfred setups. Any machine other than the original desktop lacked the application layer configuration entirely until the git repo was established.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
