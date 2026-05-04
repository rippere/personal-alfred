---
title: Personal Alfred - Project Summary
source: project_analysis
created: 2026-03-13
---

# Personal Alfred

## Overview
Personal Alfred is a grounded personal AI assistant built on verified life data, inspired by David Szabo-Stuban's architecture. It uses an Obsidian vault as the single source of truth with a strict ontology to maintain data integrity.

## Purpose
Create a personal AI assistant that:
- Operates exclusively on verified, grounded life data
- Maintains strict ontological structure in an Obsidian vault
- Uses vector embeddings and clustering for knowledge organization
- Provides chatbot interface with 30-minute heartbeat check-ins
- Automatically ingests data from multiple life sources

## Technologies
- Python 3.11+
- Obsidian vault for knowledge base storage
- ChromaDB for vector storage
- sentence-transformers (e5-large-v2) for embeddings
- OPTICS clustering from scikit-learn
- Claude API (claude-sonnet-4-6)
- FastAPI for potential chatbot interface

## Ontology Design
**Entity Types (8):**
- Person, Project, Decision, Concept, Event, Note, Source, Goal

**Relationship Types (14):**
- related_to, source_of, participant_in, decided_by, influenced_by, implements, conflicts_with, supports, derived_from, next_action, blocked_by, prerequisite_of, achieves, measured_by

## Implementation Phases
- **Phase 0** (Current): Foundation - ontology definition + Notion MCP ingest
- **Phase 1**: Embedding pipeline with ChromaDB + OPTICS clustering
- **Phase 2**: Knowledge enrichment using Claude for labeling
- **Phase 3**: Alfred chatbot CLI with 30-min heartbeat
- **Phase 4**: Automation - cron jobs, deduplication
- **Phase 5**: Future integrations (EMM, Canvas, conversation exports)

## Integration Points
Will ingest from:
- **Notion MCP** - Tasks, projects, knowledge nodes
- **Executive Mind Matrix** - Decision data and behavioral patterns
- **Canvas Autopilot** - Course notes and lectures
- **Conversation exports** - Claude/ChatGPT conversations

## Current Status
Active implementation started 2026-03-04. Phase 0 in progress with comprehensive 605-line ARCHITECTURE.md defining full system.

## Vault Location
/mnt/external/obsidian-vault/ (configured in config.yaml)

## Key Decisions
- Chose Obsidian over custom database for human readability and portability
- Selected e5-large-v2 embeddings for quality/cost balance
- Implemented OPTICS clustering over k-means for adaptive cluster discovery
- Decided on strict ontology enforcement to prevent data drift
- Used YAML frontmatter for structured metadata
- Implemented vault-first architecture (vault is source of truth, not cache)
