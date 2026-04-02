# Knowledge Consolidator Worker

**Part of the Personal Alfred Agent Ecosystem**

## Overview

The Knowledge Consolidator is a worker daemon that intelligently consolidates vault content (especially `ai-dialogue/` sessions) without losing important information.

It runs alongside Alfred's other workers (Curator, Janitor, Distiller) to maintain a clean, organized vault while preserving all valuable knowledge.

---

## How It Fits Into Personal Alfred

### The Worker Ecosystem

```
Personal Alfred System
├── Alfred Main Daemon (curator, janitor, distiller)
├── llm_ingest.py (ingests Claude Code sessions → ai-dialogue/)
└── consolidator.py (consolidates ai-dialogue/ → extracts knowledge + archives)
```

### Worker Responsibilities

| Worker | Role | Runs | Output |
|--------|------|------|--------|
| **Curator** | Processes inbox files | Continuous (5s poll) | Files routed to proper record types |
| **Janitor** | Fixes structural issues | Hourly | Vault repairs, orphan cleanup |
| **Distiller** | Extracts knowledge from sources | Hourly | decision/, assumption/, synthesis/ records |
| **llm_ingest** | Ingests Claude Code sessions | Continuous (30s poll) | ai-dialogue/ session files |
| **Consolidator** | Consolidates sessions | Daily (24h) | Extracted knowledge + consolidated archives |

---

## What It Does

### Phase 1: Analysis (Current Implementation)

**Every 24 hours:**

1. **Scans** all files in `ai-dialogue/`
2. **Calculates value score** for each session:
   - Has decisions? +10 points
   - Has wikilinks? +2 per link (max 20)
   - Has code/architecture? +8 points
   - Has blockers/questions? +5 points
   - Long session (>100 lines)? +3 points
   - Has project link? +5 points
   - High interaction (>50 turns)? +4 points

3. **Categorizes** sessions:
   - **Score ≥15:** KEEP as individual file (high value)
   - **Score 5-14:** EXTRACT knowledge + archive (medium value)
   - **Score <5:** CONSOLIDATE directly (low value)

4. **Identifies extractable knowledge:**
   - Decisions → `decision/` records
   - Tasks → `task/` records
   - Assumptions → `assumption/` records
   - Insights → `synthesis/` records

5. **Logs results** to `data/consolidator_state.json`

### Phase 2: Execution (TODO - Future)

**When enabled:**

1. **Extract knowledge** to proper record types
2. **Consolidate** low/medium value sessions into archives
3. **Archive originals** (never delete!) to `archive/ai-dialogue/`
4. **Update wikilinks** to point to consolidated files

---

## Configuration

### In `config.yaml`

```yaml
consolidator:
  sweep:
    interval_seconds: 86400  # 24 hours - run daily
    value_threshold_keep: 15  # Score >= 15: keep
    value_threshold_extract: 5  # Score >= 5: extract
    enabled: true
  state:
    path: ./data/consolidator_state.json
    max_sweep_history: 20
```

### Thresholds

**You can adjust these in config.yaml:**

- `value_threshold_keep: 15` - Sessions with score ≥15 are kept as-is
- `value_threshold_extract: 5` - Sessions with score 5-14 have knowledge extracted
- Sessions with score <5 are consolidated directly

**To make it more/less aggressive:**

- **More aggressive** (consolidate more): Increase thresholds (e.g., keep=20, extract=10)
- **Less aggressive** (keep more): Decrease thresholds (e.g., keep=10, extract=3)

---

## Running the Consolidator

### As Part of Alfred System

**Start everything:**
```bash
cd /mnt/external/personal-alfred
./start.sh
```

This launches:
- Alfred main daemon (curator, janitor, distiller)
- llm_ingest daemon
- **consolidator daemon** ← New!

### Standalone (for testing)

**Run a single sweep:**
```bash
cd ~/Projects/personal-alfred
source .venv/bin/activate
python consolidator.py
```

**Check logs:**
```bash
tail -f ~/Projects/personal-alfred/data/consolidator.log
```

**Check state:**
```bash
cat ~/Projects/personal-alfred/data/consolidator_state.json
```

---

## State File

The consolidator maintains state in `data/consolidator_state.json`:

```json
{
  "last_sweep": "2026-04-01T16:30:00",
  "total_sessions_analyzed": 220,
  "total_extracted": 0,
  "total_consolidated": 0,
  "sweep_history": [
    {
      "timestamp": "2026-04-01T16:30:00",
      "sessions_analyzed": 220,
      "keep": 77,
      "extract": 141,
      "consolidate": 2,
      "extractables": 486,
      "dry_run": true
    }
  ]
}
```

### What's Tracked

- **last_sweep:** When the last consolidation sweep ran
- **total_sessions_analyzed:** Total sessions ever analyzed
- **sweep_history:** Last 20 sweeps (timestamp, counts, dry_run status)

---

## Integration with Other Workers

### Works With Distiller

**Distiller:**
- Extracts knowledge from various source types (conversations, sessions, notes)
- Runs hourly
- Creates `assumption/`, `decision/`, `synthesis/` records

**Consolidator:**
- Specifically targets `ai-dialogue/` sessions
- Runs daily (less frequent, more targeted)
- Also extracts knowledge **before** consolidating
- Archives originals, doesn't delete

**They complement each other:**
- Distiller: Broad knowledge extraction across vault
- Consolidator: Focused on session cleanup + extraction

### Works With Janitor

**Janitor:**
- Fixes structural issues (frontmatter, orphans, stubs)
- Runs hourly
- Repairs vault integrity

**Consolidator:**
- Reduces bulk in `ai-dialogue/`
- Creates cleaner vault structure
- Makes Janitor's job easier (fewer files to scan)

### Works With llm_ingest

**llm_ingest:**
- Ingests new Claude Code sessions
- Writes to `ai-dialogue/`
- Runs continuously

**Consolidator:**
- Cleans up old sessions written by llm_ingest
- Runs daily (after new sessions have accumulated)
- Maintains `ai-dialogue/` hygiene

**Perfect pairing:**
- llm_ingest adds new sessions
- Consolidator cleans up old ones
- Vault stays organized

---

## Safety Mechanisms

### 1. Dry Run by Default

**Currently:** All sweeps are dry-run only (analysis, no changes)

**To enable execution:**
```python
# In consolidator.py, line ~140
consolidator.run_sweep(dry_run=False)  # Enable actual consolidation
```

### 2. Never Deletes

**When execution is enabled:**
- Originals moved to `archive/ai-dialogue/`
- Nothing is ever deleted
- Fully reversible

### 3. Knowledge Extracted First

**Extraction happens BEFORE consolidation:**
1. Extract decisions → `decision/`
2. Extract tasks → `task/`
3. Extract assumptions → `assumption/`
4. **Then** consolidate session

**Result:** Knowledge preserved even if consolidation fails

### 4. State Tracking

- Every sweep logged
- Can review history
- Can audit what was done

---

## Monitoring

### Check if Running

```bash
ps aux | grep consolidator
```

### View Logs

```bash
tail -f ~/Projects/personal-alfred/data/consolidator.log
```

### Check Last Sweep

```bash
cat ~/Projects/personal-alfred/data/consolidator_state.json | jq '.last_sweep'
```

### View Sweep History

```bash
cat ~/Projects/personal-alfred/data/consolidator_state.json | jq '.sweep_history'
```

---

## Troubleshooting

### Consolidator Not Running

**Check:**
1. Is it launched by `start.sh`?
   ```bash
   cat /mnt/external/personal-alfred/start.sh | grep consolidator
   ```

2. Check PID file:
   ```bash
   cat ~/Projects/personal-alfred/data/consolidator.pid
   ```

3. Check logs:
   ```bash
   tail -50 ~/Projects/personal-alfred/data/consolidator.log
   ```

### No Sweeps Happening

**Check interval:**
```bash
cat ~/Projects/personal-alfred/config.yaml | grep -A3 "consolidator:"
```

Default is 86400 seconds (24 hours). If last sweep was recent, it won't run again yet.

**Force a sweep:**
```bash
# Delete state file to force immediate sweep
rm ~/Projects/personal-alfred/data/consolidator_state.json

# Restart consolidator
pkill -f consolidator.py
./start.sh  # Will relaunch with all other daemons
```

### Config Not Loading

**Verify config.yaml path:**
```bash
ls -la ~/Projects/personal-alfred/config.yaml
```

**Check for YAML syntax errors:**
```bash
python3 -c "import yaml; yaml.safe_load(open('/mnt/external/personal-alfred/config.yaml'))"
```

---

## Development Roadmap

### ✅ Phase 1: Analysis (DONE)

- [x] Value scoring system
- [x] Knowledge extraction identification
- [x] Consolidation grouping logic
- [x] State tracking
- [x] Dry-run sweeps
- [x] Integration with Alfred config

### 🚧 Phase 2: Execution (TODO)

- [ ] Extract knowledge to proper record types
- [ ] Create consolidated archive files
- [ ] Move originals to `archive/`
- [ ] Update wikilinks
- [ ] Validation checks

### 🔮 Phase 3: Intelligence (FUTURE)

- [ ] Use Claude API for better extraction
- [ ] Semantic similarity for consolidation grouping
- [ ] Auto-adjust thresholds based on vault size
- [ ] Dashboard/UI for reviewing consolidation plans

---

## Example Workflow

### Day 1: Install

```bash
cd ~/Projects/personal-alfred
# consolidator.py already in place
# config.yaml already configured
# start.sh already updated
./start.sh  # Launches all daemons including consolidator
```

### Day 2: First Sweep (24h later)

**Consolidator automatically:**
1. Scans all 220 `ai-dialogue/` sessions
2. Calculates value scores
3. Identifies 486 extractable knowledge items
4. Categorizes: 77 keep, 141 extract, 2 consolidate
5. Logs results to state file
6. **No changes made** (dry-run)

### Day 3: Review Results

```bash
# Check what would happen
cat ~/Projects/personal-alfred/data/consolidator_state.json

# Review sweep history
cat ~/ai-agents/CONSOLIDATION_RESULTS.md  # Detailed analysis
```

### Day 4: Enable Execution (Optional)

**If satisfied with analysis:**

```python
# Edit consolidator.py line ~140
consolidator.run_sweep(dry_run=False)
```

**Restart:**
```bash
pkill -f consolidator.py
./start.sh
```

**Next sweep will:**
- Extract 486 knowledge items
- Consolidate 143 sessions
- Archive originals

---

## Files Created

```
personal-alfred/
├── consolidator.py              ← The worker daemon
├── config.yaml                  ← Added consolidator section
├── start.sh                     ← Added consolidator launch
├── CONSOLIDATOR_README.md       ← This file
└── data/
    ├── consolidator_state.json  ← State tracking
    ├── consolidator.log         ← Execution logs
    └── consolidator.pid         ← Process ID
```

---

## Integration Checklist

- [x] Worker daemon created (`consolidator.py`)
- [x] Configuration added to `config.yaml`
- [x] Launch script updated (`start.sh`)
- [x] State tracking implemented
- [x] Logging implemented
- [x] Documentation created
- [x] Follows Personal Alfred patterns (like llm_ingest.py)
- [x] Works with existing vault structure
- [x] Respects Alfred ontology
- [ ] Execution phase (Phase 2)

---

## Summary

**The Knowledge Consolidator is now part of Personal Alfred!**

✅ Integrated with Alfred ecosystem
✅ Runs as daemon alongside other workers
✅ Configured via `config.yaml`
✅ Analyzes vault daily
✅ Safe (dry-run by default)
✅ Ready for Phase 2 (execution)

**Next step:** Run it, review first sweep results, decide if ready for execution.
