---
authority: Syncthing file permission enforcement
created: '2026-05-04'
name: Syncthing Synchronization Blocked by Individual File Permission Errors
project:
- '[[project/Home System Configuration]]'
related:
- '[[session/Desktop Systemd Setup and Syncthing Path Discovery.md]]'
source: Desktop Systemd Setup and Syncthing Path Discovery session (2026-03-28)
source_date: '2026-03-28'
status: active
type: constraint
---

# Syncthing Synchronization Blocked by Individual File Permission Errors

## Constraint

Syncthing can be completely blocked from syncing a folder when any single file within it has permission errors preventing Syncthing from reading it. The failure affects the entire folder sync — not just the problematic file — and is not immediately obvious without active debugging.

## Source

During the Desktop Systemd Setup session (2026-03-28), a permission issue on `memecoin.db` on the laptop was blocking Syncthing from syncing the obsidian-vault folder entirely. The fix required identifying and correcting that specific file's permissions before sync resumed.

## Implications

- A permission issue on any single file can silently prevent the entire parent folder from syncing on all connected devices
- Debugging stalled Syncthing sync requires checking individual file permissions, not just folder-level access or service health
- Automated processes that create files in synced directories must ensure proper permissions to avoid breaking sync for all peers
- The existing Syncthing health monitor (checks service running state) may not surface this failure mode — it checks connectivity, not per-file error state

## Expiry / Review

Ongoing — applies as long as Syncthing is used for vault/projects sync across laptop and desktop.

![[constraint.base#Affected Projects]]
![[constraint.base#Related]]
