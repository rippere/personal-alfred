---
title: Sector Flow Analyzer - Project Summary
source: project_analysis
created: 2026-03-13
---

# Sector Flow Analyzer

## Overview
Financial analysis tool that visualizes money flows between market sectors using covariance metrics and network-based visualization. Tracks 11 GICS sectors through their SPDR ETF proxies.

## Purpose
Visualize and analyze:
- Money flow between market sectors
- Sector correlation patterns
- Network-based sector relationships
- Statistical significance of sector movements

## Tracked Sectors (via SPDR ETFs)
XLK (Technology), XLF (Financials), XLE (Energy), XLV (Healthcare), XLY (Consumer Discretionary), XLP (Consumer Staples), XLI (Industrials), XLB (Materials), XLRE (Real Estate), XLU (Utilities), XLC (Communications)

## Technologies
- Python 3.10+
- FastAPI and Uvicorn for API
- Dash for interactive dashboards
- yfinance for market data
- pandas, numpy, scipy for data processing
- scikit-learn and statsmodels for analysis
- plotly and networkx for visualization
- SQLAlchemy with SQLite

## Key Features
- Covariance matrix computation
- Network-based flow visualization
- Statistical analysis of sector correlations
- Real-time sector ETF price data
- RESTful API for data access

## Architecture
- `/collectors/` - Market data collection
- `/models/` - Analysis and computation
- `/visualizations/` - Dash dashboards
- `/api/` - FastAPI endpoints
- `/database/` - SQLAlchemy models

## Implementation Roadmap
7-phase plan (currently in Phase 1):
1. Foundation & data collection
2. Covariance computation
3. Flow detection algorithms
4. Network visualization
5. Statistical testing
6. Dashboard development
7. API refinement

## Integration Points
- **Observability Stack** - Designed to use for metrics and monitoring
- **nw_wrld VJ Project** - Planned real-time sector flow visualization

## Current Status
Phase 1 in active development. Educational/demonstration project.

## Key Decisions
- Selected SPDR sector ETFs as sector proxies for liquidity and coverage
- Chose covariance over correlation for magnitude information
- Used network visualization to show flow directionality
- Implemented Dash over custom frontend for rapid prototyping
- Selected yfinance over paid APIs for cost efficiency
