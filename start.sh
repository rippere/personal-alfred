#!/bin/bash
# CRITICAL: unset CLAUDECODE to prevent nested claude session issues
env -u CLAUDECODE /mnt/external/personal-alfred/.venv/bin/alfred up
