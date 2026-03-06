# Personal Alfred — Grounded Personal AI

**Status:** Pinned for later
**Inspired by:** https://substack.com/@ssdavid/note/c-207136535

---

## Core Concept

Build a personal AI ("Alfred") grounded in actual life data rather than hallucinated context. The system continuously ingests conversations, notes, and documents, discovers semantic relationships, and provides a chatbot interface with verified personal context.

---

## Reference Architecture (David Szabo-Stuban)

- **4,000+** conversations/documents → Obsidian vault
- **e5-large embeddings** (vectorization) on GPU
- **OPTICS clustering** → 1M+ potential relationships discovered
- **Qwen 2.5 7B** → labels/categorizes top 2,000 relationships (~85 min)
- **Cron jobs** → continuous ingestion, deduplication, ontological consistency
- **"Alfred"** → Clawdbot fork with 30-min context refreshes from personal data

---

## My Stack Equivalent

| Component | Tool |
|-----------|------|
| Knowledge base | Obsidian (installed) |
| Embeddings | e5-large via Ollama or sentence-transformers |
| Clustering | OPTICS (scikit-learn) |
| Relationship labeling | Claude API or local 7B model |
| Ingestion pipeline | Python cron job |
| Chatbot interface | Claude API + personal context injection |
| Ontology seed | EMM behavioral data + canvas notes + trading research |

---

## Key Insight

The bottleneck isn't compute — it's **data collection over time**. Value compounds as the vault grows with conversations, decisions, and research.

**Unique opportunity:** Cross-link EMM behavioral data + Canvas notes + trading research + Obsidian vault into a unified personal ontology. Alfred would have real context about decision patterns, not generic knowledge.

---

## Hardest Part

Ontology design upfront — defining the entity types and relationship schema before ingestion begins.

---

## Next Steps (when returning)

1. Define ontology schema (entity types: people, projects, decisions, concepts, events)
2. Set up Obsidian vault structure mirroring the ontology
3. Build ingestion pipeline for Claude conversation exports
4. Implement e5-large embedding + OPTICS clustering
5. Wire up Alfred chatbot with context injection
6. Connect EMM as a live data source
