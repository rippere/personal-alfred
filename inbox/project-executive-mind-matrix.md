---
title: Executive Mind Matrix - Project Summary
source: project_analysis
created: 2026-03-13
---

# Executive Mind Matrix

## Overview
Executive Mind Matrix (EMM) is a production AI-powered decision intelligence system that uses adversarial agent dialectics to analyze decisions. Currently deployed on Railway at https://web-production-3d888.up.railway.app.

## Purpose
EMM acts as an AI-powered decision co-pilot using three AI agent personas that debate and analyze decisions from different perspectives:
- **The Entrepreneur** - Growth and opportunity focus
- **The Quant** - Risk analysis and quantitative assessment
- **The Auditor** - Governance and compliance oversight

The system automatically triages inputs:
- Strategic items → Executive Intents
- Operational items → Tasks
- Reference material → Knowledge Nodes

## Technologies
- Python 3.11+
- FastAPI and Uvicorn for API
- Anthropic Claude API (claude-3-haiku with upgradability to Sonnet)
- Notion API for database integration
- Pydantic for data validation
- APScheduler for task scheduling
- Railway for deployment

## Key Features
- 2-minute polling cycle on 10 connected Notion databases
- Adversarial dialectic flow for decision analysis
- Training data capture system (logs diff between AI suggestions and human edits)
- Comprehensive test suite with pytest (80%+ coverage requirement)
- Behavioral tracking for personal decision patterns

## Integration Points
- **Notion** - Primary database and user interface
- **Personal Alfred** - Future integration target (will ingest EMM decision data)
- **nw_wrld VJ Project** - Planned visualization of system metadynamics

## Current Status
Production deployment, actively running with live Notion integration.

## Key Decisions
- Chose adversarial dialectic approach over single-agent analysis for richer decision insights
- Selected Notion as primary interface for user familiarity and ease of use
- Deployed on Railway for cost-effective hosting
- Implemented training data capture to improve future AI models
- Started with Haiku for cost efficiency with planned Sonnet upgrade path
