---
based_on:
- '[[session/personal-alfred—2026-05-01—system-audit-and-repo-setup]]'
confidence: high
created: '2026-05-04'
name: Vault Sync Timer Configured for 15-Minute Interval
project:
- '[[project/Personal Alfred]]'
related:
- '[[synthesis/Multi-System Sync Requires Consistent Automation Across All Nodes]]'
- '[[synthesis/Obsidian Vault Sync Across Multiple Machines Requires Identical Automation
  Deployment]]'
source: 2026-05-01 system audit
source_date: '2026-05-01'
status: confirmed
type: assumption
---

# Vault Sync Timer Configured for 15-Minute Interval

## Claim
The obsidian-vault-sync systemd timer is configured to run on a 15-minute automated interval, triggering git sync between the local vault and the GitHub remote (personal-alfred-vault repo).

## Basis
The 2026-05-01 system audit session explicitly noted "15-min git sync to personal-alfred-vault GitHub repo" and confirmed the timer was "active" with the last confirmed push at 09:55 that day.

## Evidence Trail
2026-05-01: Confirmed in system audit — vault sync timer active, 15-min interval, push at 09:55.

## Impact
Decisions about cross-machine freshness depend on this interval. Any change made on one machine will appear on another within at most 15 minutes, assuming both machines have active timers running.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
