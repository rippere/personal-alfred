---
title: GitHub Cleanup & Cross-Machine Claude Sync Setup
source: claude_code_hook
created: 2026-05-01
alfred: process
---

# GitHub Cleanup & Cross-Machine Claude Sync Setup

Session completed on laptop on 2026-05-01. Full cleanup of public GitHub presence and setup of cross-machine Claude Code tooling sync. No action required — this is a briefing for Alfred to update relevant project records and note the new workflow.

---

## What Was Done

### GitHub Presence

**Repos made private:**
- `l1b3rt4s` — AI jailbreak prompt collection, was public. Now private.
- `Projects` — empty placeholder repo. Now private.
- `Obsidian-Vault` — personal notes, not a project. Now private.
- `system-configs` — eduroam config, not relevant. Now private.

**Profile created:**
- `rippere/rippere` profile README repo created and populated with bio, project table, and stack
- GitHub profile bio, name, and location set via API

**READMEs rewritten:**
- `executive-mind-matrix` — complete rewrite explaining adversarial agent system, architecture, stack, Notion schema, real-world fraternity use case
- `Memecoin-Sentiment-Analyzer` — rewritten as proper data science project with research questions, methodology, architecture
- `personal-alfred` — new README written explaining vault workers and record schema
- `crm-agentic` — already solid, no changes needed

**Topics added** to all public repos.

**Repos cleaned of internal artifacts:**
- `executive-mind-matrix`: removed `.claude/` session notes, ~40 all-caps planning docs, sync-conflict duplicates, and misplaced VJ project files (`nw_wrld_data/`, 3D models, fonts). `.gitignore` updated.
- `Memecoin-Sentiment-Analyzer`: removed `CLAUDE.md`, planning docs, status reports, test output JSON files, `sync_to_github.sh`. `.gitignore` updated.
- `crm-agentic`: removed `CLAUDE.md` and `PROGRESS.md`. `.gitignore` updated.

### Cross-Machine Claude Tooling Sync

`claude-config` private repo restructured and is now the sync mechanism for Claude Code tooling across machines.

**New structure:**
- `claude/` → `~/.claude/` (CLAUDE.md, settings.json)
- `config/` → `~/.config/claude/` (session-handoff hooks, scripts, handoff-config.json)
- `config/waybar-scripts/` → `~/.config/waybar/scripts/` (claude-session-logger.sh etc.)
- `gitignore_global` → `~/.gitignore_global`
- `memory/` → `~/.claude/projects/-home-rippere/memory/`
- `projects/` → per-project CLAUDE.md files

**Two scripts added:**
- `collect.sh` — gathers all config from system into repo, commits, pushes
- `sync.sh` — deploys repo config to system, sets git globals, deploys per-project files

**Global gitignore** (`~/.gitignore_global`) now blocks `.claude/`, `CLAUDE.md`, `HANDOFF.md`, `PROGRESS.md`, and `*.sync-conflict-*` across all repos globally.

---

## Desktop Sync Checklist

When back on the desktop, run these in order:

```bash
# 1. Get Claude tooling synced first (global gitignore, hooks, CLAUDE.md)
cd ~/Desktop/claude-config && git pull && ./sync.sh

# 2. Pull cleaned state of each public project repo
cd ~/Projects/Projects/executive-mind-matrix && git pull
cd ~/Projects/Projects/crm-agentic && git pull
cd ~/Projects/Projects/Memecoin-Sentiment-Analyzer && git pull  # or your path

# 3. Verify global gitignore is active
git config --global core.excludesfile  # should return ~/.gitignore_global
```

**Note:** `handoff-config.json` vault path is hardcoded to `/home/rippere/Projects/obsidian-vault`. If the desktop vault path differs, update `~/.config/claude/handoff-config.json` after syncing.

---

## LinkedIn

LinkedIn About section was written but not yet pasted in — needs to be done manually. Content is in the conversation history from this session. Key line: "Most people building AI come from CS. I come from the science of how people actually make decisions."

---

## Open Items

- [ ] Personal website still to be built (deferred, agreed to focus on GitHub first)
- [ ] LinkedIn bio and About section need to be manually updated on linkedin.com
- [ ] Paste LinkedIn content into profile (was written in session, not auto-applied)
