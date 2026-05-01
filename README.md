# Personal Alfred — Vault Workers

Python workers that run on top of an Obsidian knowledge vault, maintaining a living graph of decisions, projects, people, and epistemic records across 20 structured record types.

The vault itself is the single source of truth. These workers keep it clean, connected, and useful — without manual maintenance.

## What the workers do

**Consolidator** — Scans `ai-dialogue/` session logs, extracts standing knowledge (decisions, tasks, assumptions) into proper typed records, then compresses low-value sessions into archives. Nothing is deleted; originals move to `archive/`.

**Epistemic Consolidator** — Handles the Learn record types (`assumption`, `constraint`, `contradiction`, `synthesis`). Clusters related epistemic records by semantic similarity, then calls Claude to synthesize them into higher-order insights and update confidence levels.

**LLM Ingest** — Processes raw inbox items (emails, voice memos, conversation summaries) through a Claude-backed curation pipeline that extracts entities and creates typed records in the right directories.

## Vault Structure

```
ai-dialogue/        AI conversation sessions (type: conversation, subtype: ai-dialogue)
assumption/         Tracked beliefs with confidence levels
constraint/         Known limits and hard stops
contradiction/      Conflicting records flagged for resolution
decision/           Recorded choices with rationale
synthesis/          Claude-generated insight clusters
project/            Active and historical projects
task/               Tasks linked to projects and people
person/, org/       CRM-style relationship records
inbox/              Unprocessed inbound items
```

## Record Schema

Every file is a markdown record with YAML frontmatter. The `type` field drives everything — filtering, sorting, linking, and worker behavior.

```yaml
---
type: decision
status: active
project: "[[project/Executive Mind Matrix]]"
created: "2026-03-04"
confidence: high
---
```

Workers use `file.hasLink(this.file)` pattern — each project/person page shows only records linked to it, via embedded base views.

## Setup

```bash
git clone https://github.com/rippere/personal-alfred
cd personal-alfred

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt  # anthropic, pyyaml, pathlib

cp config.yaml.example config.yaml
# Set vault.path to your Obsidian vault directory
# Set anthropic.api_key

# Run consolidation pass
python consolidator.py

# Run epistemic consolidation
python epistemic_consolidator.py

# Or start all workers
bash start.sh
```

## Stack

Python · Anthropic Claude API · Obsidian (markdown + YAML frontmatter) · PyYAML
