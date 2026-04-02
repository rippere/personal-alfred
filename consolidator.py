#!/usr/bin/env python3
"""
consolidator.py

Knowledge Consolidation Worker for Personal Alfred

Intelligently consolidates vault content (especially ai-dialogue sessions) without losing information.
Extracts standing knowledge to proper record types before consolidating session logs.

Workflow:
1. Periodically scan ai-dialogue/ for consolidation opportunities
2. Calculate value scores for each session
3. Extract knowledge (decisions, tasks, assumptions) to proper records
4. Consolidate low-value sessions into archives
5. Preserve everything (originals moved to archive/, never deleted)
"""

import json
import re
import time
import yaml
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Any, Optional


# Configuration (loaded from config.yaml)
CONFIG_FILE = Path(__file__).parent / "config.yaml"
VAULT_PATH = None
AI_DIALOGUE_DIR = None
ARCHIVE_DIR = None
STATE_FILE = None
CONSOLIDATE_INTERVAL = 86400  # 24 hours default


def log(msg: str):
    """Log with timestamp."""
    ts = datetime.now().isoformat()
    print(f"[{ts}] [CONSOLIDATOR] {msg}", flush=True)


def load_config():
    """Load configuration from config.yaml"""
    global VAULT_PATH, AI_DIALOGUE_DIR, ARCHIVE_DIR, STATE_FILE, CONSOLIDATE_INTERVAL

    if not CONFIG_FILE.exists():
        log(f"Config file not found: {CONFIG_FILE}")
        return False

    try:
        with open(CONFIG_FILE) as f:
            config = yaml.safe_load(f)

        VAULT_PATH = Path(config["vault"]["path"])
        AI_DIALOGUE_DIR = VAULT_PATH / "ai-dialogue"

        # Archive outside vault for graph performance
        ARCHIVE_DIR = Path.home() / "Projects" / "obsidian-vault-archives" / "archive" / "ai-dialogue"

        # Consolidator-specific config
        consolidator_config = config.get("consolidator", {})
        STATE_FILE = Path(consolidator_config.get("state", {}).get("path", "./data/consolidator_state.json"))
        CONSOLIDATE_INTERVAL = consolidator_config.get("sweep", {}).get("interval_seconds", 86400)

        log(f"Config loaded: vault={VAULT_PATH}, interval={CONSOLIDATE_INTERVAL}s")
        return True
    except Exception as e:
        log(f"Failed to load config: {e}")
        return False


class KnowledgeConsolidator:
    """
    Intelligent knowledge consolidation worker for Personal Alfred.

    Periodically scans ai-dialogue/ and consolidates sessions while
    preserving important knowledge in proper record types.
    """

    def __init__(self):
        self.state = {
            "last_sweep": None,
            "total_sessions_analyzed": 0,
            "total_extracted": 0,
            "total_consolidated": 0,
            "sweep_history": []
        }
        self.load_state()

    def load_state(self):
        """Load state from disk"""
        if STATE_FILE and STATE_FILE.exists():
            try:
                with open(STATE_FILE) as f:
                    self.state = json.load(f)
                log(f"State loaded: {self.state.get('total_sessions_analyzed', 0)} sessions analyzed total")
            except Exception as e:
                log(f"Failed to load state: {e}, starting fresh")

    def save_state(self):
        """Save state to disk"""
        if not STATE_FILE:
            return

        try:
            STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(STATE_FILE, "w") as f:
                json.dump(self.state, f, indent=2)
        except Exception as e:
            log(f"Failed to save state: {e}")

    def should_run_sweep(self) -> bool:
        """Determine if it's time to run a consolidation sweep"""
        if not self.state.get("last_sweep"):
            return True  # Never run before

        last_sweep = datetime.fromisoformat(self.state["last_sweep"])
        elapsed = (datetime.now() - last_sweep).total_seconds()

        return elapsed >= CONSOLIDATE_INTERVAL

    def run_sweep(self, dry_run=False):
        """Run a consolidation sweep"""
        log(f"Starting consolidation sweep (dry_run={dry_run})...")

        if not AI_DIALOGUE_DIR or not AI_DIALOGUE_DIR.exists():
            log(f"ai-dialogue directory not found: {AI_DIALOGUE_DIR}")
            return

        sessions = list(AI_DIALOGUE_DIR.glob("*.md"))
        log(f"Found {len(sessions)} sessions to analyze")

        analysis_results = {}
        extractables_total = 0

        # Analyze each session
        for session_file in sessions:
            try:
                session_data = self._load_session(session_file)
                score = self._calculate_value_score(session_data)
                extractables = self._identify_extractable_knowledge(session_data)
                group = self._determine_consolidation_group(session_data)
                action = self._recommend_action(score, extractables)

                analysis_results[session_file.name] = {
                    "score": score,
                    "extractables": len(extractables),
                    "group": group,
                    "action": action["action"]
                }

                extractables_total += len(extractables)

            except Exception as e:
                log(f"Error analyzing {session_file.name}: {e}")
                continue

        # Summarize results
        keep_count = sum(1 for r in analysis_results.values() if r["action"] == "KEEP")
        extract_count = sum(1 for r in analysis_results.values() if r["action"] == "EXTRACT_AND_ARCHIVE")
        consolidate_count = sum(1 for r in analysis_results.values() if r["action"] == "CONSOLIDATE")

        log(f"Analysis complete:")
        log(f"  - KEEP: {keep_count}")
        log(f"  - EXTRACT+ARCHIVE: {extract_count}")
        log(f"  - CONSOLIDATE: {consolidate_count}")
        log(f"  - Total extractable knowledge: {extractables_total} items")

        # Update state
        self.state["last_sweep"] = datetime.now().isoformat()
        self.state["total_sessions_analyzed"] = len(sessions)
        self.state["sweep_history"].append({
            "timestamp": datetime.now().isoformat(),
            "sessions_analyzed": len(sessions),
            "keep": keep_count,
            "extract": extract_count,
            "consolidate": consolidate_count,
            "extractables": extractables_total,
            "dry_run": dry_run
        })

        # Keep only last 20 sweeps in history
        if len(self.state["sweep_history"]) > 20:
            self.state["sweep_history"] = self.state["sweep_history"][-20:]

        self.save_state()

        if dry_run:
            log("Dry run complete - no changes made")
        else:
            # Execute consolidation
            log("Executing consolidation...")

            # Process each session according to its action
            for session_name, result in analysis_results.items():
                session_file = AI_DIALOGUE_DIR / session_name
                action = result["action"]

                try:
                    if action == "KEEP":
                        # Keep as-is, do nothing
                        continue

                    elif action == "EXTRACT_AND_ARCHIVE":
                        # Extract knowledge, then archive
                        session_data = self._load_session(session_file)
                        extractables = self._identify_extractable_knowledge(session_data)

                        if extractables:
                            self._extract_knowledge_to_files(session_data, extractables)

                        self._archive_session(session_file)
                        self.state["total_extracted"] += 1

                    elif action == "CONSOLIDATE":
                        # Just archive (consolidation grouping will be Phase 3)
                        self._archive_session(session_file)
                        self.state["total_consolidated"] += 1

                except Exception as e:
                    log(f"Error processing {session_name}: {e}")
                    continue

            log(f"Execution complete: {self.state['total_extracted']} extracted, {self.state['total_consolidated']} consolidated")
            self.save_state()

    def _load_session(self, session_file: Path) -> Dict[str, Any]:
        """Load and parse a session file"""
        content = session_file.read_text(encoding='utf-8', errors='ignore')

        # Parse frontmatter
        frontmatter = {}
        body = content

        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                    body = parts[2].strip()
                except:
                    pass

        return {
            "path": session_file,
            "filename": session_file.name,
            "frontmatter": frontmatter,
            "body": body,
            "size": len(content),
            "lines": content.count('\n') + 1
        }

    def _calculate_value_score(self, session_data: Dict[str, Any]) -> int:
        """Calculate session value score"""
        score = 0
        body = session_data.get("body", "")
        frontmatter = session_data.get("frontmatter", {})

        # Has key decisions
        if "## Key Decisions" in body or "## Decisions" in body:
            score += 10

        # Count wikilinks
        wikilinks = re.findall(r'\[\[(.*?)\]\]', body)
        score += min(len(wikilinks) * 2, 20)

        # Contains code/architecture
        if "```" in body or "architecture" in body.lower():
            score += 8

        # Has blockers/questions
        if "## Blockers" in body or "## Open Questions" in body:
            score += 5

        # Session length
        if session_data.get("lines", 0) > 100:
            score += 3

        # Has project link
        if frontmatter.get("project"):
            score += 5

        # High turn count
        turns = frontmatter.get("turns", 0)
        if turns and turns > 50:
            score += 4

        return score

    def _identify_extractable_knowledge(self, session_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify extractable knowledge items"""
        extractables = []
        body = session_data.get("body", "")

        # Extract decisions
        if "## Key Decisions" in body:
            decisions_section = self._extract_section(body, ["## Key Decisions", "## Decisions"])
            if decisions_section:
                items = re.findall(r'[-*]\s*(.+?)(?=\n[-*]|\n\n|$)', decisions_section, re.DOTALL)
                for item in items:
                    if len(item.strip()) > 10:
                        extractables.append({"type": "decision", "content": item.strip()})

        # Extract tasks from Next Steps
        if "## Next Steps" in body:
            next_steps = self._extract_section(body, ["## Next Steps"])
            if next_steps:
                items = re.findall(r'[-*\d.]\s*(.+?)(?=\n[-*\d.]|\n\n|$)', next_steps, re.DOTALL)
                for item in items:
                    if len(item.strip()) > 10:
                        extractables.append({"type": "task", "content": item.strip()})

        return extractables

    def _extract_section(self, content: str, headers: List[str]) -> Optional[str]:
        """Extract content under specific headers"""
        for header in headers:
            if header in content:
                pattern = re.escape(header) + r'(.*?)(?=\n##|\Z)'
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    return match.group(1).strip()
        return None

    def _determine_consolidation_group(self, session_data: Dict[str, Any]) -> str:
        """Determine consolidation group (project/year-month)"""
        frontmatter = session_data.get("frontmatter", {})

        # Get project
        project = frontmatter.get("project", "")
        if project:
            project = re.sub(r'\[\[|\]\]', '', project).strip()
            project = project.replace("project/", "").replace(".md", "")
            project = re.sub(r'[^\w\s-]', '', project).replace(' ', '-').lower()
        else:
            project = "misc"

        # Get date
        created = frontmatter.get("created", "")
        if created:
            try:
                date_str = str(created)
                year_month = date_str[:7] if len(date_str) >= 7 else datetime.now().strftime("%Y-%m")
            except:
                year_month = datetime.now().strftime("%Y-%m")
        else:
            year_month = "unknown"

        return f"{project}/{year_month}"

    def _recommend_action(self, score: int, extractables: List[Dict]) -> Dict[str, Any]:
        """Recommend action for this session"""
        if score >= 15:
            return {"action": "KEEP", "reason": f"High value (score: {score})"}
        elif score >= 5 or len(extractables) > 0:
            return {"action": "EXTRACT_AND_ARCHIVE", "reason": f"Medium value (score: {score})"}
        else:
            return {"action": "CONSOLIDATE", "reason": f"Low value (score: {score})"}

    def _extract_knowledge_to_files(self, session_data: Dict[str, Any], extractables: List[Dict[str, Any]]):
        """Extract knowledge items to proper record type files"""
        frontmatter = session_data.get("frontmatter", {})
        session_file = session_data.get("path")
        project = frontmatter.get("project", "")
        created = frontmatter.get("created", datetime.now().strftime("%Y-%m-%d"))

        for item in extractables:
            item_type = item["type"]
            content = item["content"]

            # Determine target directory
            if item_type == "decision":
                target_dir = VAULT_PATH / "decision"
            elif item_type == "task":
                target_dir = VAULT_PATH / "task"
            elif item_type == "assumption":
                target_dir = VAULT_PATH / "assumption"
            else:
                continue

            target_dir.mkdir(parents=True, exist_ok=True)

            # Generate filename from content
            slug = re.sub(r'[^\w\s-]', '', content[:50]).strip().replace(' ', '-').lower()
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"{slug}-{timestamp}.md"
            target_file = target_dir / filename

            # Create record
            record_content = self._create_record(
                record_type=item_type,
                content=content,
                source=f"[[ai-dialogue/{session_file.name}]]",
                project=project,
                created=created
            )

            target_file.write_text(record_content, encoding='utf-8')
            log(f"  Extracted {item_type}: {filename}")

    def _create_record(self, record_type: str, content: str, source: str, project: str, created: str) -> str:
        """Create a record file with frontmatter"""
        frontmatter = {
            "type": record_type,
            "status": "todo" if record_type == "task" else "active",
            "created": created,
            "source": source,
            "extracted_by": "consolidator",
            "tags": ["auto-extracted"]
        }

        if project:
            frontmatter["project"] = project

        # Serialize frontmatter
        fm_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)

        return f"---\n{fm_yaml}---\n\n{content}\n"

    def _archive_session(self, session_file: Path):
        """Move session file to archive"""
        if not ARCHIVE_DIR:
            log(f"Archive directory not configured, skipping archive of {session_file.name}")
            return

        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

        archive_path = ARCHIVE_DIR / session_file.name

        # If archive file already exists, add timestamp
        if archive_path.exists():
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            stem = session_file.stem
            archive_path = ARCHIVE_DIR / f"{stem}-{timestamp}.md"

        shutil.move(str(session_file), str(archive_path))
        log(f"  Archived: {session_file.name} -> {archive_path.relative_to(VAULT_PATH)}")


def main():
    """Main daemon loop"""
    log("Knowledge Consolidator starting...")

    # Load configuration
    if not load_config():
        log("Failed to load configuration, exiting")
        return 1

    # Initialize consolidator
    consolidator = KnowledgeConsolidator()

    log(f"Consolidator initialized, sweep interval: {CONSOLIDATE_INTERVAL}s ({CONSOLIDATE_INTERVAL/3600:.1f}h)")

    # Main loop
    try:
        while True:
            if consolidator.should_run_sweep():
                log("Time for consolidation sweep")
                consolidator.run_sweep(dry_run=False)  # Execute actual consolidation
            else:
                last_sweep = consolidator.state.get("last_sweep", "never")
                log(f"Not time yet (last sweep: {last_sweep})")

            # Sleep for a bit before checking again (every hour)
            time.sleep(3600)

    except KeyboardInterrupt:
        log("Shutting down gracefully...")
        consolidator.save_state()
        return 0
    except Exception as e:
        log(f"Fatal error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
