---
title: Memecoin Sentiment Analyzer - Project Summary
source: project_analysis
created: 2026-03-13
---

# Memecoin Sentiment Analyzer

## Overview
Educational data science project analyzing correlations between social media hype and meme coin price movements. Features comprehensive multi-source data collection, sentiment analysis, and correlation tracking.

## Purpose
Explore and demonstrate correlations between:
- Social media sentiment and volume
- Influencer activity
- Meme coin price movements
- Bot detection and quality metrics

Educational goal: Learn data pipeline architecture, web scraping, sentiment analysis, and financial data integration.

## Tracked Coins
DOGE, PEPE, SHIB, BONK, FLOKI, WIF

## Technologies
- Python 3.11+
- FastAPI for backend API
- Next.js for frontend dashboard
- SQLite database with SQLAlchemy ORM
- Selenium for web scraping
- VADER for sentiment analysis
- Tweepy for Twitter API
- CoinGecko API for price data

## Data Sources
- **Price Data**: CoinGecko API (15-minute intervals)
- **Social Media**: TikTok scraper, Reddit scraper, Twitter API
- **News**: Aggregated news sources

## Advanced Features
- Sentiment analysis with VADER
- Bot detection algorithms
- Influencer tracking system
- Quality monitoring
- Volume spike detection
- Correlation analysis engine

## Architecture
- `/collectors/` - Data collection modules
- `/scrapers/` - Selenium-based scrapers with anti-detection base class
- `/analysis/` - Correlation and volume analysis
- `/frontend/` - Next.js React dashboard
- `/api/` - FastAPI backend with rate limiting
- `/database/` - SQLAlchemy models

## Integration Points
- **Observability Stack** - Designed to use observability stack for monitoring
- **nw_wrld VJ Project** - Potential data visualization integration

## Current Status
Development/Educational project with comprehensive documentation in CLAUDE.md. Complete test suite with pytest.

## Key Decisions
- Chose educational focus over production deployment
- Selected VADER over transformer models for speed and interpretability
- Used Selenium over APIs for platforms without official API access
- Implemented anti-detection measures in scraper base class
- Selected SQLite over PostgreSQL for simplicity and portability
- Built comprehensive test suite to learn testing best practices
