---
cluster_sources:
- '[[session/Remote Desktop Access and WOL Setup Session.md]]'
- '[[session/Desktop Systemd Setup and Syncthing Path Discovery.md]]'
confidence: medium
created: '2026-05-04'
name: Obsidian Vault Sync as Fallback Configuration Distribution Channel
project:
- '[[project/Home System Configuration]]'
related:
- '[[synthesis/Multi-System Configuration Deployment Via SSHFS Network Mounts.md]]'
- '[[synthesis/Distributed Systemd Service Deployment Via SSH Remote Administration.md]]'
status: active
type: synthesis
---

# Obsidian Vault Sync as Fallback Configuration Distribution Channel

## Insight

When SSH connectivity is unavailable between desktop and laptop (different networks, desktop offline), the Obsidian vault synced via Syncthing acts as an asynchronous fallback channel for distributing configuration files. Any file committed to the vault while both systems were last connected will be available on both systems even after they diverge to separate networks.

## Evidence

- Remote Desktop session (2026-04-01): Laptop (10.109.x.x) could not SSH to desktop (192.168.254.182) due to different network segments
- Extended CLAUDE.md (125 lines, synced from desktop) was already present on laptop at `~/Projects/obsidian-vault/CLAUDE.md`
- User copied it directly to `~/.claude/CLAUDE.md` without needing desktop access at all — the vault sync had pre-distributed it

## Implications

- Configuration files with multi-system relevance should be stored in the Obsidian vault, not only in `~/.config` or system paths
- Vault sync provides eventually-consistent configuration distribution as a complement to — and fallback from — direct SSH
- The vault copy of CLAUDE.md is the canonical extended version; the system copy at `~/.claude/CLAUDE.md` is a local deployment of it
- Network isolation does not block configuration sharing if both systems were recently connected to Syncthing relay

## Applicability

Applies to any configuration that must be accessible on both laptop and desktop independently — especially AI context files, scripts, and operational documents.

![[synthesis.base#Sources]]
![[synthesis.base#Related]]
