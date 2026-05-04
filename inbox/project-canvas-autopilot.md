---
title: Canvas Autopilot - Project Summary
source: project_analysis
created: 2026-03-13
---

# Canvas Autopilot

## Overview
Canvas Autopilot is an automated Canvas LMS scraper, Notion syncer, and assignment submitter that streamlines academic workflow by automatically syncing Canvas data to Notion.

## Purpose
Automate the tedious process of:
- Scraping assignments, quizzes, and lectures from Canvas LMS
- Syncing all academic data to Notion for better organization
- Managing course materials and deadlines
- Uploading and organizing lecture content

## Technologies
- Python 3.11+
- Playwright for browser automation
- Notion Client API for database sync
- Requests and BeautifulSoup4 for web scraping
- Click for CLI interface
- Rich for terminal UI

## Key Features
- Automated scraping of Canvas LMS data
- Bidirectional sync with Notion databases
- CLI tool (`emm` command)
- Support for assignments, quizzes, and lecture materials
- Recent activity includes lecture upload scripts for 404 lectures

## Integration Points
- **Canvas LMS** - Source of academic data
- **Notion** - Target database for organization
- **Personal Alfred** - Future integration (will ingest course notes and lectures)

## Predecessor Project
Built upon lessons learned from "Canvas Notion Integ" - an older version with:
- Systemd timer automation (runs every 6 hours)
- Universal pagination handling
- Smart delta sync updates
- 100% coverage validation
- Exponential backoff error handling

## Current Status
Active development with recent lecture upload functionality. The older "Canvas Notion Integ" version is still running with systemd timer (logs show activity as of 2026-03-13).

## Package Structure
- `canvas/` - Canvas scraping modules
- `notion/` - Notion API integration
- `automation/` - Automation workflows

## Key Decisions
- Chose Playwright over Selenium for more reliable browser automation
- Implemented incremental sync to reduce API calls
- Used Click for CLI to maintain consistency with other tools
- Kept old version running while developing new version for stability
