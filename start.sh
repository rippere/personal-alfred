#!/bin/bash
# CRITICAL: unset CLAUDECODE to prevent nested claude session issues

# Launch Alfred main daemon
env -u CLAUDECODE /mnt/external/personal-alfred/.venv/bin/alfred up &
ALFRED_PID=$!

# Launch llm_ingest daemon (continuous session ingestion)
env -u CLAUDECODE /mnt/external/personal-alfred/.venv/bin/python3 \
  /mnt/external/personal-alfred/llm_ingest.py >> \
  /mnt/external/personal-alfred/data/llm_ingest.log 2>&1 &
INGEST_PID=$!

# Launch consolidator daemon (knowledge consolidation)
env -u CLAUDECODE /mnt/external/personal-alfred/.venv/bin/python3 \
  /mnt/external/personal-alfred/consolidator.py >> \
  /mnt/external/personal-alfred/data/consolidator.log 2>&1 &
CONSOLIDATOR_PID=$!

echo "Started Alfred (PID $ALFRED_PID), llm_ingest (PID $INGEST_PID), and consolidator (PID $CONSOLIDATOR_PID)"
echo "$ALFRED_PID" > /mnt/external/personal-alfred/data/alfred.pid
echo "$INGEST_PID" > /mnt/external/personal-alfred/data/llm_ingest.pid
echo "$CONSOLIDATOR_PID" > /mnt/external/personal-alfred/data/consolidator.pid

# Wait for all
wait $ALFRED_PID $INGEST_PID $CONSOLIDATOR_PID
