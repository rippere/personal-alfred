# Personal Alfred — Grounded Personal AI: Full Architecture

**Status:** Active — Implementation starting 2026-03-04
**Inspired by:** David Szabo-Stuban's Substack architecture
**Primary author:** @rippere

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Ontology Schema](#2-ontology-schema)
3. [Obsidian Vault Structure](#3-obsidian-vault-structure)
4. [Tech Stack Decisions](#4-tech-stack-decisions)
5. [Codebase File/Folder Structure](#5-codebase-filefolder-structure)
6. [Phase 0 — Foundation](#phase-0--foundation)
7. [Phase 1 — Embedding Pipeline](#phase-1--embedding-pipeline)
8. [Phase 2 — Knowledge Enrichment](#phase-2--knowledge-enrichment)
9. [Phase 3 — Alfred Chatbot](#phase-3--alfred-chatbot)
10. [Phase 4 — Automation](#phase-4--automation)
11. [Phase 5 — Future Integrations](#phase-5--future-integrations)
12. [Critical Path](#12-critical-path)
13. [Key Metrics & Thresholds](#13-key-metrics--thresholds)

---

## 1. System Overview

Alfred is a personal AI grounded in verified life data rather than hallucinated context. It is NOT a general assistant. It is a context-aware interface to the semantic graph of your actual life: your decisions, your projects, your relationships, your intellectual trajectory.

The system operates as a pipeline:

```
Data Sources
    │
    ▼
[Ingest Layer]  ←── Notion MCP (now) / EMM (future) / Canvas (future)
    │
    ▼
[Obsidian Vault]  ←── Structured markdown with ontology-aware frontmatter
    │
    ▼
[Embedding Layer]  ←── e5-large → ChromaDB vector store
    │
    ▼
[Clustering Layer]  ←── OPTICS → relationship candidate pairs
    │
    ▼
[Enrichment Layer]  ←── Claude API labels + writes metadata back to vault
    │
    ▼
[Alfred Interface]  ←── Claude API + injected context from vault + 30-min heartbeat
```

The vault is the single source of truth. Everything writes to and reads from the vault.

---

## 2. Ontology Schema

This is the hardest part. Get this right before any ingestion begins. The schema is intentionally opinionated and will not cover every edge case on day one — that is fine. Ontologies grow.

### 2.1 Entity Types

| Entity Type | Description | Examples |
|---|---|---|
| `Person` | Any human actor in your life | Professor, collaborator, mentor, yourself |
| `Project` | A bounded effort with a goal and timeline | EMM, canvas-autopilot, thesis, personal-alfred |
| `Decision` | A moment where a path was chosen | "Chose Python over Rust for EMM", "Switched majors" |
| `Concept` | An idea, theory, or mental model you engage with | OPTICS clustering, predictive coding, behavioral finance |
| `Event` | A time-bounded occurrence | Course enrollment, job interview, conference |
| `Note` | An atomic piece of captured thinking | Meeting notes, fleeting thoughts, reading annotations |
| `Source` | An external artifact that informed you | Paper, book, Substack post, YouTube video |
| `Goal` | An intended future state | "Ship EMM to 10 users", "Publish thesis by May" |

### 2.2 Relationship Types

Relationships are directed: `(Subject) --[RELATIONSHIP]--> (Object)`

| Relationship | Subject Type | Object Type | Description |
|---|---|---|---|
| `WORKS_ON` | Person | Project | Active contributor relationship |
| `DECIDED_IN` | Decision | Project | Decision was made in context of project |
| `INFORMED_BY` | Decision | Source | Decision draws on external material |
| `APPLIES_CONCEPT` | Project | Concept | Project uses this concept as a foundation |
| `KNOWS` | Person | Person | Professional or personal connection |
| `MENTIONED_IN` | Concept | Note | Concept appears in a note |
| `LEADS_TO` | Decision | Decision | One decision caused or constrained another |
| `RELATED_TO` | Concept | Concept | Semantic similarity (auto-discovered by clustering) |
| `AUTHORED_BY` | Note | Person | Who wrote the note |
| `PART_OF` | Project | Project | Subproject relationship |
| `BLOCKS` | Project | Goal | Project is blocked by another |
| `ACHIEVES` | Project | Goal | Project, if completed, achieves this goal |
| `OCCURRED_DURING` | Event | Project | Event happened in context of a project |
| `CITED_IN` | Source | Note | Source is referenced in a note |

### 2.3 Ontology Design Principles (Palantir-inspired)

1. **Objects first, relationships second.** Never create a relationship node before both endpoint objects exist in the vault.
2. **Relationships are typed, not free-text.** Every edge in the graph has one of the 14 defined relationship types above. Free-text relationship descriptions go in a `description` field on the relationship record, not as the type itself.
3. **Every entity has a canonical ID.** Format: `{type_prefix}/{slug}` e.g. `proj/emm`, `person/david-szabo-stuban`, `concept/optics-clustering`.
4. **No orphan nodes.** A note with zero relationships has no value in the graph. The janitor job flags these for manual review.
5. **Temporal anchoring is mandatory.** Every entity carries `created_at` and `last_modified`. Every relationship carries `established_at`.

---

## 3. Obsidian Vault Structure

Vault root: `/mnt/external/obsidian-vault/` (separate from codebase)

```
obsidian-vault/
├── _meta/
│   ├── ontology.md              # Human-readable schema reference
│   ├── alfred-config.md         # Alfred's self-description, used in system prompt
│   └── CHANGELOG.md             # Log of structural changes to the vault
│
├── entities/
│   ├── people/
│   │   └── david-szabo-stuban.md
│   ├── projects/
│   │   ├── emm.md
│   │   ├── canvas-autopilot.md
│   │   └── personal-alfred.md
│   ├── decisions/
│   ├── concepts/
│   │   └── optics-clustering.md
│   ├── events/
│   ├── goals/
│   └── sources/
│
├── notes/
│   ├── notion-export/           # Raw ingested Notion notes (read-only after ingest)
│   ├── canvas-export/           # Future: Canvas ingestion landing zone
│   ├── conversations/           # Future: Claude/ChatGPT conversation exports
│   └── fleeting/                # Manual quick-capture notes
│
├── relationships/
│   └── graph.jsonl              # Flat JSONL relationship log (machine-written)
│
└── embeddings/
    └── .gitignore               # Embeddings NOT stored in vault, stored in ChromaDB
```

### 3.1 Frontmatter Schema

Every entity file uses YAML frontmatter strictly. Example for a Project:

```yaml
---
alfred_id: "proj/emm"
entity_type: project
name: "Executive Mind Matrix"
status: active
created_at: "2025-01-01"
last_modified: "2026-03-04"
tags: [behavioral-finance, notion, railway, python]
relationships:
  - type: WORKS_ON
    subject: "person/me"
    object: "proj/emm"
    established_at: "2025-01-01"
summary: >
  Production SaaS on Railway. Behavioral tracking system using Notion as
  a database. Goal: understand personal decision patterns over time.
source_system: manual
---
```

**Key frontmatter fields by entity type:**

- All entities: `alfred_id`, `entity_type`, `name`, `created_at`, `last_modified`, `relationships[]`, `summary`, `source_system`
- `Person`: `role`, `affiliation`, `contact_channel`
- `Project`: `status` (active/paused/complete), `tags`, `goal_ids[]`
- `Decision`: `date`, `outcome`, `context_project_id`, `confidence` (0-1 float)
- `Concept`: `domain`, `related_concept_ids[]`
- `Note`: `source_system` (notion/canvas/conversation/manual), `raw_content_hash`

---

## 4. Tech Stack Decisions

### 4.1 ChromaDB over FAISS

**Decision: ChromaDB.**

FAISS is a raw index — it gives you fast ANN search but zero metadata storage, zero persistence beyond what you build yourself, and no query interface. You would spend a week building the infrastructure that ChromaDB gives you on day one.

ChromaDB ships with: persistent SQLite backend, metadata filtering, collection management, a Python client that works locally with zero server setup, and direct integration with sentence-transformers. It handles the 10K-100K document scale of this project trivially on CPU.

FAISS becomes the right answer if you hit >1M vectors and need maximum throughput. Until then, ChromaDB is strictly better.

### 4.2 sentence-transformers over Ollama for embeddings

**Decision: sentence-transformers directly.**

Ollama is an excellent serving layer for generative models. For pure embedding workloads, it adds a local HTTP server, a process to manage, and a dependency that can go stale. The sentence-transformers library gives you `SentenceTransformer('intfloat/e5-large-v2')` in two lines of Python, GPU acceleration via PyTorch if a GPU is present, and clean CPU fallback if not.

GPU/CPU detection at runtime:

```python
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
model = SentenceTransformer("intfloat/e5-large-v2", device=device)
```

e5-large-v2 is 335M parameters. On CPU, expect ~2-5 seconds per document. On a mid-range GPU, ~50-200ms. For batch ingestion this is acceptable either way.

### 4.3 Claude API (claude-sonnet-4-6) over local 7B for relationship labeling

**Decision: Claude API.**

The reference architecture uses Qwen 2.5 7B locally and runs for 85 minutes — chosen to prioritize cost over quality. We flip this: relationship labeling happens once per batch. The quality of labels determines the quality of Alfred's context for months. Sonnet 4.6 produces dramatically better structured outputs than any 7B model, and the cost of labeling 2,000 relationships is under $5.

### 4.4 OPTICS over HDBSCAN or K-means

**Decision: OPTICS.**

K-means requires specifying k upfront. HDBSCAN is faster but OPTICS gives you the reachability plot — a visual diagnostic that tells you whether your embedding space has meaningful cluster structure at all. For a new vault with few documents, this diagnostic matters. Switch to HDBSCAN in Phase 4 if OPTICS becomes a bottleneck (it won't until >100K documents).

### 4.5 uv for package management

**Decision: uv.**

pip is slow and has no lockfile by default. Poetry adds complexity. uv is pip-compatible, generates a lockfile, and installs 10-100x faster.

### 4.6 CLI-first chatbot interface

**Decision: CLI for Phase 3, no web UI until Phase 5.**

A web UI is a distraction. A CLI using Python's `readline` library with history persistence is usable immediately and takes 50 lines of code. The hard part is context injection and the heartbeat — build those correctly first.

---

## 5. Codebase File/Folder Structure

```
/mnt/external/personal-alfred/
├── IDEA.md                      # Original concept note (existing)
├── ARCHITECTURE.md              # This file
├── README.md                    # Quick start guide
│
├── alfred/                      # Main Python package
│   ├── __init__.py
│   ├── config.py                # Central config loader (TOML-based)
│   │
│   ├── ingest/
│   │   ├── __init__.py
│   │   ├── notion_client.py     # Notion MCP wrapper → structured dicts
│   │   ├── notion_to_obsidian.py # Transform Notion pages → vault markdown
│   │   ├── canvas_client.py     # STUB — Phase 5
│   │   └── conversation_parser.py # STUB — Phase 5
│   │
│   ├── embeddings/
│   │   ├── __init__.py
│   │   ├── encoder.py           # SentenceTransformer wrapper (GPU/CPU auto-detect)
│   │   ├── store.py             # ChromaDB client wrapper
│   │   └── indexer.py           # Vault scan → embed → upsert pipeline
│   │
│   ├── clustering/
│   │   ├── __init__.py
│   │   ├── optics_runner.py     # OPTICS execution + reachability plot
│   │   └── relationship_extractor.py # Cluster → candidate relationship pairs
│   │
│   ├── enrichment/
│   │   ├── __init__.py
│   │   ├── labeler.py           # Claude API batch labeling of relationships
│   │   └── vault_writer.py      # Write enriched metadata back to vault frontmatter
│   │
│   ├── chatbot/
│   │   ├── __init__.py
│   │   ├── context_builder.py   # Assemble context window from vault + ChromaDB
│   │   ├── heartbeat.py         # 30-min context refresh scheduler
│   │   └── alfred_cli.py        # readline CLI interface
│   │
│   ├── janitor/
│   │   ├── __init__.py
│   │   ├── deduplicator.py      # Hash-based + semantic dedup of notes
│   │   ├── orphan_detector.py   # Find nodes with no relationships
│   │   └── ontology_validator.py # Check frontmatter schema compliance
│   │
│   └── utils/
│       ├── __init__.py
│       ├── frontmatter.py       # YAML frontmatter read/write helpers
│       ├── vault_scanner.py     # Walk vault directory tree → file list
│       └── logging.py           # Structured logging
│
├── scripts/
│   ├── ingest_notion.py         # Manual trigger: full Notion → vault sync
│   ├── run_embedding_pipeline.py # Manual trigger: embed all vault files
│   ├── run_clustering.py        # Manual trigger: OPTICS + relationship extraction
│   ├── run_enrichment.py        # Manual trigger: Claude labels top relationships
│   └── alfred.py                # Entry point: starts Alfred CLI
│
├── cron/
│   ├── ingest.sh                # Cron wrapper for ingest pipeline
│   ├── janitor.sh               # Cron wrapper for janitor pipeline
│   └── heartbeat.sh             # Cron wrapper for context refresh
│
├── config.toml                  # User configuration (gitignored)
├── config.toml.example          # Template config checked into git
├── pyproject.toml               # Package definition + uv dependencies
├── uv.lock                      # Lockfile (checked into git)
└── .gitignore
```

---

## Phase 0 — Foundation

**Goal:** Ontology designed, vault scaffolded, first Notion notes ingested.

### Step 0.1 — Initialize the project

```bash
cd /mnt/external/personal-alfred
uv init
uv add anthropic chromadb sentence-transformers scikit-learn \
       python-frontmatter pyyaml tomllib rich
```

### Step 0.2 — Create config.toml

```toml
[vault]
path = "/mnt/external/obsidian-vault"

[embeddings]
model = "intfloat/e5-large-v2"
chroma_path = "/mnt/external/personal-alfred/.chroma"

[claude]
model = "claude-sonnet-4-6"
max_context_tokens = 180000

[clustering]
min_samples = 5
xi = 0.05
min_cluster_size = 0.05

[cron]
ingest_schedule = "0 * * * *"
janitor_schedule = "30 * * * *"
heartbeat_interval_minutes = 30
```

### Step 0.3 — Scaffold the vault

Create the directory tree from Section 3. Create `_meta/ontology.md` as a human-readable copy of Section 2. This file is read by Alfred at startup as part of its system prompt.

### Step 0.4 — Build Notion → Obsidian ingestion

1. `notion_client.py` — calls Notion MCP to list all pages, retrieves each. Returns structured dicts.
2. `notion_to_obsidian.py` — maps each Notion page to an entity type (heuristic: check database name). Generates frontmatter YAML. Writes to appropriate vault location. Skips if `raw_content_hash` matches (dedup-safe).

Entity detection heuristic:
- Page in "Projects" database → `entities/projects/`
- All others → `notes/notion-export/`, tagged for review

Use `asyncio` with a semaphore (max 5 concurrent calls) to avoid Notion rate limiting.

**Exit criteria:** At least 20 notes ingested with valid frontmatter.

---

## Phase 1 — Embedding Pipeline

**Goal:** Every vault file embedded into ChromaDB. OPTICS run. Top 2,000 relationship candidates extracted.

### Step 1.1 — Encoder

`alfred/embeddings/encoder.py`:

```python
from sentence_transformers import SentenceTransformer
import torch

class VaultEncoder:
    def __init__(self, model_name: str):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(model_name, device=self.device)

    def encode_document(self, text: str, title: str) -> list[float]:
        # e5-large REQUIRES "passage: " prefix for documents
        return self.model.encode(f"passage: {title}\n\n{text}",
                                  normalize_embeddings=True).tolist()

    def encode_query(self, query: str) -> list[float]:
        # e5-large REQUIRES "query: " prefix for queries
        return self.model.encode(f"query: {query}",
                                  normalize_embeddings=True).tolist()
```

### Step 1.2 — ChromaDB store

```python
import chromadb

class VaultStore:
    def __init__(self, chroma_path: str):
        self.client = chromadb.PersistentClient(path=chroma_path)
        self.collection = self.client.get_or_create_collection(
            name="vault",
            metadata={"hnsw:space": "cosine"}
        )
```

### Step 1.3 — Indexer

Walks vault, checks `last_modified` vs ChromaDB metadata, upserts only changed documents. Full re-index never needed.

### Step 1.4 — OPTICS clustering

```python
from sklearn.cluster import OPTICS
optics = OPTICS(min_samples=5, xi=0.05, min_cluster_size=0.05,
                metric="cosine", n_jobs=-1)
optics.fit(embeddings_matrix)
```

Tune `xi` if clustering looks wrong: raise if one giant cluster, lower if hundreds of tiny clusters. Always inspect the reachability plot first.

### Step 1.5 — Relationship extraction

Pairs within same cluster with cosine similarity > 0.75 become candidates. Cap at 2,000 (top by similarity). Write to `candidates.jsonl`.

**Exit criteria:** ChromaDB populated. `candidates.jsonl` written with top 2,000 pairs.

---

## Phase 2 — Knowledge Enrichment

**Goal:** Claude labels each candidate. Labeled relationships written back to vault.

Claude batch prompt (20 pairs per call):

```
Given two documents from a personal vault, determine:
1. Relationship type (one of: RELATED_TO, APPLIES_CONCEPT, INFORMED_BY,
   MENTIONED_IN, PART_OF, LEADS_TO — or "NONE")
2. One-sentence description of WHY they are related
3. Confidence score (0.0 to 1.0)

Respond with JSON only: {"relationship_type": "...", "description": "...", "confidence": 0.0}
```

Accept only pairs where confidence > 0.6. Write accepted relationships to `relationships/graph.jsonl`. Update entity frontmatter `relationships[]` arrays.

Use `asyncio.Semaphore(10)` to cap concurrent Claude API calls.

**Exit criteria:** `graph.jsonl` populated (expect 400-1,200 accepted from 2,000 candidates).

---

## Phase 3 — Alfred Chatbot

**Goal:** Working CLI with context injection and 30-minute heartbeat.

### Context builder strategy

1. Semantic search: top 20 documents relevant to current query
2. Always include: active projects + decisions from last 90 days
3. Load relationship graph for top retrieved documents
4. Truncate assembled context to 40K tokens

### System prompt structure

```
You are Alfred, a personal AI assistant grounded in verified personal data.

CRITICAL RULES:
- Only assert facts that appear in the provided context.
- If you don't know something from the context, say so explicitly.
- Never hallucinate details about the user's projects, decisions, or relationships.
- When referencing a fact, cite the source entity ID (e.g., "per proj/emm...").

CURRENT KNOWLEDGE CONTEXT:
{assembled_context}
```

### Heartbeat

Background `threading.Thread` fires every 30 minutes, calls `context_builder` with a fixed "general status" query, caches result. User queries use cached context + fresh query-specific retrieval pass.

### CLI

Python `readline` with `~/.alfred_history` persistence. Commands: `exit`, `refresh` (force context reload).

**Exit criteria:** `python scripts/alfred.py` works. Alfred answers questions about active projects using vault data.

---

## Phase 4 — Automation

**Goal:** Cron jobs running. Dedup and validation operational.

### Cron jobs

```
0  * * * *  /mnt/external/personal-alfred/cron/ingest.sh   # hourly at :00
30 * * * *  /mnt/external/personal-alfred/cron/janitor.sh  # hourly at :30
```

Heartbeat runs inside the Alfred process (threading), NOT as cron.

### Dedup logic

- **Hash dedup:** Same `raw_content_hash` → delete newer, flag if metadata differs
- **Semantic dedup:** Cosine similarity > 0.95 → flag for manual review (never auto-delete)

### Ontology validator checks

- All required frontmatter fields present
- All `alfred_id` values follow `{type}/{slug}` format
- All relationship references point to existing vault entities
- Violations written to `_meta/VALIDATION_ERRORS.md`

---

## Phase 5 — Future Integrations

**Trigger:** EMM Railway API stable + canvas-autopilot operational.

### EMM hook

`alfred/ingest/emm_client.py` — calls Railway API. Maps EMM tasks → `Decision` entities, EMM projects → `Project` entities with `source_system: emm`.

Critical property names (from EMM): `status` (not select type), `"Auto Generated"` (space), `"Source Intent"` (space), `"Projects"` (plural).

### Canvas hook

`alfred/ingest/canvas_client.py` — reads canvas-autopilot output. Maps course notes → `Note` entities, courses → `Project` entities.

### Conversation export ingestion

`alfred/ingest/conversation_parser.py` — parse Claude/ChatGPT JSON exports. Extract user messages only (assistant responses are not personal knowledge). Semantic dedup before writing to `notes/conversations/`.

This is the highest-leverage future integration. After 6 months, the vault becomes deeply personal.

---

## 12. Critical Path

### Must be sequential

```
Ontology design
    → Vault scaffolding
    → Notion ingest
    → Embedding pipeline
    → OPTICS clustering
    → Claude enrichment
    → Alfred CLI
```

### Can be parallelized

- Ontology docs + vault directory scaffolding
- Encoder testing + ChromaDB store setup
- Phase 4 cron setup + Phase 3 heartbeat implementation
- Phase 5 EMM hook + Canvas hook

### Hard blockers to resolve before starting

1. **Confirm vault path** — `/mnt/external/obsidian-vault/`. Set it once, don't change it.
2. **Verify Notion MCP auth** — run a test query before building the ingest pipeline.
3. **Check GPU** — `python3 -c "import torch; print(torch.cuda.is_available())"`.

---

## 13. Key Metrics and Thresholds

| Metric | Green | Yellow | Red |
|---|---|---|---|
| Vault document count | >20 | 5-20 | <5 |
| Embedding coverage | >95% indexed | 80-95% | <80% |
| Relationship graph density | >200 labeled edges | 50-200 | <50 |
| Ingest cron last run | <2h ago | 2-24h ago | >24h ago |
| Orphan node count | 0 | 1-5 | >5 |
| Validation errors | 0 | 1-3 | >3 |
| Alfred context size | 20K-40K tokens | 10-20K | <10K or >150K |

Check with: `python scripts/alfred.py --status`

---

## Appendix A — e5-large-v2 Usage Notes

- Always use `intfloat/e5-large-v2` (not `e5-large` — different model, worse performance)
- Always prefix: documents with `passage: `, queries with `query: `
- Output: 1024-dimensional embeddings
- Use `normalize_embeddings=True` so cosine similarity equals dot product

## Appendix B — ChromaDB Persistence Notes

- PersistentClient writes to `.chroma/` (SQLite + HNSW index)
- Do NOT commit `.chroma/` to git
- After system move: re-run indexer (skips unchanged files via hash check)

## Appendix C — Claude API Rate Limits

- claude-sonnet-4-6 Tier 1: 50 req/min, 40K tokens/min input
- Relationship labeling: `asyncio.Semaphore(10)` to cap concurrent requests
- Alfred CLI: no batching needed — single request per user turn
