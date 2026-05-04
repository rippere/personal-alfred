---
cluster_sources:
- '[[note/Executive Mind Matrix Pre-Public Repo Cleanup]]'
- '[[decision/Strip AI Co-Author Attribution from Git History]]'
- '[[decision/Move Notion UUIDs to Environment Variables]]'
- '[[decision/Switch GitHub Remote from HTTPS to SSH]]'
confidence: high
created: '2026-05-04'
name: AI-Assisted Repo Pre-Publication Cleanup Has Four Predictable Problem Categories
project:
- '[[project/Executive Mind Matrix]]'
status: active
type: synthesis
---

# AI-Assisted Repo Pre-Publication Cleanup Has Four Predictable Problem Categories

## Insight

Before making an AI-assisted code repository public, four distinct problem categories reliably require cleanup: (1) AI co-authorship attribution in git history, (2) sync-conflict artifacts in tracked files and branches, (3) hardcoded secrets and IDs that must be externalized to environment variables, (4) HTTPS remote auth that must migrate to SSH. Each category requires a specific remediation sequence.

## Evidence

The 2026-03-04 EMM pre-public cleanup revealed all four categories simultaneously: 48 commits with Co-Authored-By trailers stripped via git filter-branch, 22 sync-conflict files (17 tracked + 5 untracked + 2 conflict branches), 4 hardcoded Notion UUIDs across 2 source files externalized to config/settings.py, and HTTPS remote migrated to SSH for GitHub compatibility. Railway was re-deployed automatically after the force push; env vars required manual re-entry in the Railway dashboard.

## Implications

Any AI-assisted project being prepared for public release should run through this four-category checklist before pushing. Attribution removal requires git history rewrite, which forces a push --force and triggers any connected CI/CD redeployment. Platform env vars must be re-registered after secrets are externalized.

## Applicability

Applies to any project developed with AI pair-programming assistance, synced across devices with Syncthing, and targeting GitHub as the public host.

![[synthesis.base#Sources]]
![[synthesis.base#Related]]
