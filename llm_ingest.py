#!/usr/bin/env python3
"""
llm_ingest.py

Batch ingests Claude Code sessions from ~/.claude/projects/**/*.jsonl into Obsidian vault.
Processes unprocessed sessions, then watches for new ones continuously.

Workflow:
1. Scan ~/.claude/projects for all JSONL files
2. Check state file to skip already-processed ones
3. Call Ollama Mistral to summarize each
4. Write to /mnt/external/obsidian-vault/ai-dialogue/
5. Update state file
6. Enter watch loop (poll every 30s for new files)
"""

import json
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Optional, Set
import os
import hashlib

# Configuration
OLLAMA_MODEL = "mistral:latest"
OLLAMA_TIMEOUT = 120
OLLAMA_ENDPOINT = "http://localhost:11434"
VAULT_PATH = Path("/mnt/external/obsidian-vault")
AI_DIALOGUE_DIR = VAULT_PATH / "ai-dialogue"
CLAUDE_PROJECTS_DIR = Path.home() / ".claude" / "projects"
STATE_FILE = Path("/mnt/external/personal-alfred/data/llm_ingest_state.json")
WATCH_INTERVAL = 30  # seconds between checks for new files

# State tracking
state = {
    "processed_sessions": {},  # {file_hash: {"path": str, "session_id": str, "timestamp": str}}
    "last_scan": None,
}


def log(msg: str):
    """Log with timestamp."""
    ts = datetime.now().isoformat()
    print(f"[{ts}] {msg}", flush=True)


def load_state():
    """Load processed sessions from state file."""
    global state
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE) as f:
                state = json.load(f)
            log(f"Loaded state: {len(state.get('processed_sessions', {}))} sessions processed")
        except Exception as e:
            log(f"Failed to load state: {e}, starting fresh")
            state = {"processed_sessions": {}, "last_scan": None}
    else:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        save_state()


def save_state():
    """Save processed sessions to state file."""
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        log(f"Failed to save state: {e}")


def file_hash(path: Path) -> str:
    """Quick hash of file for change detection."""
    try:
        return hashlib.md5(str(path.stat().st_mtime_ns).encode()).hexdigest()[:8]
    except:
        return "unknown"


def find_all_sessions() -> list[Path]:
    """Find all JSONL files in ~/.claude/projects, excluding subagent files."""
    sessions = []
    if not CLAUDE_PROJECTS_DIR.exists():
        log(f"Projects dir not found: {CLAUDE_PROJECTS_DIR}")
        return sessions

    for jsonl_file in CLAUDE_PROJECTS_DIR.rglob("*.jsonl"):
        # Skip subagent files
        if "/subagents/" in str(jsonl_file):
            continue
        # Skip compact files
        if "compact" in jsonl_file.name:
            continue
        sessions.append(jsonl_file)

    log(f"Found {len(sessions)} root session files")
    return sessions


def extract_session_metadata(jsonl_path: Path) -> dict:
    """Extract basic metadata from JSONL file."""
    metadata = {
        "session_id": "unknown",
        "model": "unknown",
        "turn_count": 0,
        "tool_calls": 0,
    }

    try:
        with open(jsonl_path) as f:
            for i, line in enumerate(f):
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                except:
                    continue

                # Extract session ID from first message
                if i == 0:
                    metadata["session_id"] = obj.get("session_id", "unknown")

                # Count turns
                if obj.get("type") == "user":
                    metadata["turn_count"] += 1

                # Count tool calls
                if obj.get("type") == "assistant":
                    content = obj.get("message", {}).get("content", [])
                    if isinstance(content, list):
                        tool_uses = [
                            c for c in content if isinstance(c, dict) and c.get("type") == "tool_use"
                        ]
                        metadata["tool_calls"] += len(tool_uses)

                # Extract model
                if "model" in obj:
                    metadata["model"] = obj["model"]
    except Exception as e:
        log(f"Error extracting metadata from {jsonl_path}: {e}")

    return metadata


def condense_transcript(jsonl_path: Path, max_lines: int = 30) -> str:
    """Create a condensed transcript for Ollama."""
    lines = []
    try:
        with open(jsonl_path) as f:
            for obj in f:
                if not obj.strip():
                    continue
                try:
                    msg = json.loads(obj)
                except:
                    continue

                msg_type = msg.get("type")
                if msg_type not in ("user", "assistant"):
                    continue

                content = msg.get("message", {}).get("content", "")

                # Condense text
                if isinstance(content, str):
                    text = content[:150].replace("\n", " ")
                elif isinstance(content, list):
                    parts = []
                    for block in content:
                        if isinstance(block, dict):
                            if block.get("type") == "text":
                                parts.append(block["text"][:100])
                            elif block.get("type") == "tool_use":
                                parts.append(f"[{block.get('name', 'tool')}]")
                    text = " ".join(parts)[:150]
                else:
                    continue

                role = "USER" if msg_type == "user" else "ASST"
                lines.append(f"{role}: {text}")
                if len(lines) >= max_lines:
                    break
    except Exception as e:
        log(f"Error reading {jsonl_path}: {e}")

    return "\n".join(lines)


def call_ollama(prompt: str) -> Optional[str]:
    """Call Ollama Mistral."""
    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=OLLAMA_TIMEOUT,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        log(f"Ollama error: {result.stderr[:200]}")
        return None
    except subprocess.TimeoutExpired:
        log("Ollama timeout (model may be loading)")
        return None
    except Exception as e:
        log(f"Ollama call failed: {e}")
        return None


def summarize_session(jsonl_path: Path) -> Optional[str]:
    """Generate summary for a session."""
    transcript = condense_transcript(jsonl_path)
    if not transcript:
        return "_No conversation content._"

    prompt = """You are summarizing a Claude Code development session for a knowledge management system.

Given the session transcript below, produce a structured summary with these sections:

## Goals
What the human wanted to accomplish (bullet points)

## Key Decisions
Important choices made during the session (bullet points)

## What Was Done
Concrete actions taken — files created/edited, commands run (bullet points)

## Current State
Where things stand at the end of the session

## Blockers / Open Questions
Anything unresolved or needing follow-up

## Next Steps
What should happen next session

Be concise. Max 3-5 bullets per section.

SESSION TRANSCRIPT:
""" + transcript

    return call_ollama(prompt)


def write_to_vault(
    summary: str,
    project_name: str,
    session_id: str,
    turn_count: int,
    tool_calls: int,
    model: str,
) -> bool:
    """Write summary to ai-dialogue in vault."""
    try:
        AI_DIALOGUE_DIR.mkdir(parents=True, exist_ok=True)

        date = datetime.now().strftime("%Y-%m-%d")
        slug = project_name.lower().replace(" ", "-").replace("_", "-").replace("/", "-")
        session_short = session_id[:8] if session_id != "unknown" else "unknown"

        # Use em-dash format for consistency with newer entries
        filename = f"{project_name}—{date}—{slug}-{session_short}.md"

        frontmatter = f"""---
type: conversation
subtype: ai-dialogue
status: active
channel: claude-code
subject: "Claude Code session on {project_name}"
project: "[[project/{project_name}]]"
session_id: "{session_id}"
turns: {turn_count}
model: "{model}"
created: "{date}"
tags: ["claude-code", "automated-handoff"]
metadata:
  tool_calls: {tool_calls}
  summary_status: "complete"
---

# {project_name} — {date} ({session_short})

{summary}
"""

        output_path = AI_DIALOGUE_DIR / filename
        with open(output_path, "w") as f:
            f.write(frontmatter)
        log(f"Wrote: {filename}")
        return True
    except Exception as e:
        log(f"Failed to write to vault: {e}")
        return False


def process_session(jsonl_path: Path) -> bool:
    """Process a single session."""
    try:
        metadata = extract_session_metadata(jsonl_path)
        log(f"Processing {jsonl_path.name} (ID: {metadata['session_id'][:8]})")

        summary = summarize_session(jsonl_path)
        if not summary:
            log(f"Failed to generate summary for {jsonl_path.name}")
            return False

        # Derive project name from path
        project_name = jsonl_path.parent.name.replace("-", " ").title()

        if not write_to_vault(
            summary=summary,
            project_name=project_name,
            session_id=metadata["session_id"],
            turn_count=metadata["turn_count"],
            tool_calls=metadata["tool_calls"],
            model=metadata["model"],
        ):
            return False

        # Mark as processed
        hsh = file_hash(jsonl_path)
        state["processed_sessions"][hsh] = {
            "path": str(jsonl_path),
            "session_id": metadata["session_id"],
            "timestamp": datetime.now().isoformat(),
        }
        save_state()
        return True
    except Exception as e:
        log(f"Error processing {jsonl_path}: {e}")
        return False


def run_batch():
    """Process all unprocessed sessions."""
    sessions = find_all_sessions()
    to_process = []

    for session_path in sessions:
        hsh = file_hash(session_path)
        if hsh not in state["processed_sessions"]:
            to_process.append(session_path)

    if not to_process:
        log("No new sessions to process")
        return

    log(f"Processing {len(to_process)} unprocessed sessions...")
    success_count = 0
    for session_path in to_process:
        if process_session(session_path):
            success_count += 1
        time.sleep(2)  # Stagger requests to Ollama

    log(f"Batch complete: {success_count}/{len(to_process)} processed successfully")
    state["last_scan"] = datetime.now().isoformat()
    save_state()


def run_watch():
    """Watch for new sessions continuously."""
    log("Entering watch mode (polling every 30s)...")
    last_known_files = set(find_all_sessions())

    while True:
        try:
            time.sleep(WATCH_INTERVAL)
            current_files = set(find_all_sessions())

            # Check for new files
            new_files = current_files - last_known_files
            for new_file in new_files:
                log(f"New session detected: {new_file.name}")
                process_session(new_file)

            last_known_files = current_files
        except KeyboardInterrupt:
            log("Watch mode interrupted")
            break
        except Exception as e:
            log(f"Watch loop error: {e}")
            time.sleep(WATCH_INTERVAL)


def main():
    load_state()

    if "--once" in sys.argv:
        # Batch mode: process all unprocessed, then exit
        run_batch()
        log("Batch mode complete")
        sys.exit(0)
    else:
        # Daemon mode: batch first, then watch
        run_batch()
        run_watch()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Shutting down...")
        sys.exit(0)
