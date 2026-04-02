#!/usr/bin/env python3
"""
Epistemic Consolidator

Consolidates fragmented epistemic records (assumption, decision, synthesis, constraint, contradiction)
into thematic collections without losing knowledge.

Strategy:
1. Group by project (records linked to same project)
2. Group by auto-extraction (merge auto-extracted records)
3. Create consolidated markdown files with table of contents
4. Move originals to external archive
5. Preserve all content with heading-based anchors for wikilinks
"""

import re
import yaml
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Any, Optional


VAULT_PATH = Path.home() / "Projects" / "obsidian-vault"
ARCHIVE_PATH = Path.home() / "Projects" / "obsidian-vault-archives" / "epistemic_originals"

EPISTEMIC_TYPES = ["assumption", "decision", "synthesis", "constraint", "contradiction"]


def log(msg: str):
    """Log with timestamp"""
    ts = datetime.now().isoformat()
    print(f"[{ts}] {msg}", flush=True)


class EpistemicConsolidator:
    """Consolidate fragmented epistemic records"""

    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.stats = defaultdict(lambda: defaultdict(int))

    def analyze(self):
        """Analyze epistemic records and plan consolidation"""
        log("Analyzing epistemic records...")

        for record_type in EPISTEMIC_TYPES:
            record_dir = VAULT_PATH / record_type
            if not record_dir.exists():
                continue

            files = list(record_dir.glob("*.md"))
            log(f"\n{record_type}/: {len(files)} files")

            # Group by project
            by_project = defaultdict(list)
            auto_extracted = []

            for file in files:
                metadata = self._load_record(file)

                if metadata.get("extracted_by") == "consolidator":
                    auto_extracted.append(file)

                project = metadata.get("project", "")
                if project:
                    # Extract project name from wikilink
                    if isinstance(project, list):
                        project = project[0] if project else ""
                    project_name = re.sub(r'\[\[|\]\]|project/', '', str(project)).strip()
                    by_project[project_name].append(file)

            log(f"  Auto-extracted: {len(auto_extracted)}")
            log(f"  Linked to projects: {sum(len(v) for v in by_project.values())}")
            log(f"  Orphaned: {len(files) - len(auto_extracted) - sum(len(v) for v in by_project.values())}")

            # Show top projects
            if by_project:
                sorted_projects = sorted(by_project.items(), key=lambda x: len(x[1]), reverse=True)
                log(f"  Top projects:")
                for proj, recs in sorted_projects[:5]:
                    log(f"    - {proj}: {len(recs)} records")

            self.stats[record_type]["total"] = len(files)
            self.stats[record_type]["auto_extracted"] = len(auto_extracted)
            self.stats[record_type]["with_project"] = sum(len(v) for v in by_project.values())

    def consolidate_auto_extracted(self):
        """Delete auto-extracted low-value records"""
        log("\nConsolidating auto-extracted records...")

        for record_type in EPISTEMIC_TYPES:
            record_dir = VAULT_PATH / record_type
            if not record_dir.exists():
                continue

            files = list(record_dir.glob("*.md"))
            deleted = 0

            for file in files:
                metadata = self._load_record(file)

                if metadata.get("extracted_by") == "consolidator" and metadata.get("tags") == ["auto-extracted"]:
                    # Check if it's a low-value auto-extraction
                    content = file.read_text(encoding='utf-8', errors='ignore')
                    body = self._extract_body(content)

                    # If it's just "review this session" or similar boilerplate, delete
                    if any(phrase in body.lower() for phrase in [
                        "review this session manually",
                        "update this handoff document",
                        "transcript: home"
                    ]):
                        if self.dry_run:
                            log(f"  [DRY-RUN] Would delete: {file.name}")
                        else:
                            file.unlink()
                            log(f"  Deleted: {file.name}")
                        deleted += 1

            log(f"{record_type}/: Deleted {deleted} auto-extracted boilerplate records")

    def consolidate_by_project(self, record_type: str):
        """Consolidate records by project"""
        log(f"\nConsolidating {record_type}/ by project...")

        record_dir = VAULT_PATH / record_type
        if not record_dir.exists():
            return

        files = list(record_dir.glob("*.md"))

        # Group by project
        by_project = defaultdict(list)
        orphaned = []

        for file in files:
            metadata = self._load_record(file)
            project = metadata.get("project", "")

            if project:
                if isinstance(project, list):
                    project = project[0] if project else ""
                project_name = re.sub(r'\[\[|\]\]|project/', '', str(project)).strip().replace(".md", "")
                # Clean project name for filename
                project_slug = re.sub(r'[^\w\s-]', '', project_name).replace(' ', '-')
                by_project[project_slug].append(file)
            else:
                orphaned.append(file)

        # Create consolidated files for projects with 5+ records
        consolidated_count = 0
        for project_slug, project_files in by_project.items():
            if len(project_files) >= 5:  # Only consolidate if 5+ records
                self._create_consolidated_file(record_type, project_slug, project_files)
                consolidated_count += len(project_files)

        log(f"  Consolidated {consolidated_count} records into {len([p for p, f in by_project.items() if len(f) >= 5])} project files")

    def _create_consolidated_file(self, record_type: str, project_slug: str, files: List[Path]):
        """Create a consolidated file for a project"""
        consolidated_name = f"{project_slug}-{record_type}s.md"
        consolidated_path = VAULT_PATH / record_type / consolidated_name

        if consolidated_path.exists():
            log(f"  Skipping {consolidated_name} (already exists)")
            return

        # Build consolidated content
        frontmatter = {
            "type": record_type,
            "status": "active",
            "created": datetime.now().strftime("%Y-%m-%d"),
            "consolidated": True,
            "source_count": len(files),
            "project": f"[[project/{project_slug}]]"
        }

        body_parts = [f"# {project_slug} {record_type.title()}s\n"]
        body_parts.append(f"Consolidated from {len(files)} individual records.\n")
        body_parts.append("## Table of Contents\n")

        # Table of contents
        for i, file in enumerate(files, 1):
            title = file.stem.replace('-', ' ').title()[:50]
            body_parts.append(f"{i}. [[#{title}]]\n")

        body_parts.append("\n---\n")

        # Individual records
        for file in files:
            content = file.read_text(encoding='utf-8', errors='ignore')
            metadata = self._load_record_from_content(content)
            body = self._extract_body(content)

            title = file.stem.replace('-', ' ').title()[:50]
            body_parts.append(f"\n## {title}\n")
            body_parts.append(f"**Source**: `{file.name}`  \n")
            body_parts.append(f"**Created**: {metadata.get('created', 'unknown')}  \n")
            body_parts.append(f"\n{body}\n")

        # Create consolidated file
        fm_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        full_content = f"---\n{fm_yaml}---\n\n{''.join(body_parts)}"

        if self.dry_run:
            log(f"  [DRY-RUN] Would create: {consolidated_name}")
        else:
            consolidated_path.write_text(full_content, encoding='utf-8')
            log(f"  Created: {consolidated_name}")

            # Archive originals
            for file in files:
                self._archive_original(file)

    def _archive_original(self, file: Path):
        """Move original file to external archive"""
        ARCHIVE_PATH.mkdir(parents=True, exist_ok=True)

        archive_subdir = ARCHIVE_PATH / file.parent.name
        archive_subdir.mkdir(parents=True, exist_ok=True)

        archive_file = archive_subdir / file.name

        if not self.dry_run:
            shutil.move(str(file), str(archive_file))

    def _load_record(self, file: Path) -> Dict[str, Any]:
        """Load record metadata"""
        content = file.read_text(encoding='utf-8', errors='ignore')
        return self._load_record_from_content(content)

    def _load_record_from_content(self, content: str) -> Dict[str, Any]:
        """Load record metadata from content"""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    return yaml.safe_load(parts[1]) or {}
                except:
                    pass
        return {}

    def _extract_body(self, content: str) -> str:
        """Extract body from markdown file"""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                return parts[2].strip()
        return content.strip()


def main():
    """Main execution"""
    import sys

    dry_run = "--execute" not in sys.argv

    if dry_run:
        log("Running in DRY-RUN mode (use --execute to apply changes)")
    else:
        log("Running in EXECUTE mode")

    consolidator = EpistemicConsolidator(dry_run=dry_run)

    # Phase 1: Analyze
    consolidator.analyze()

    # Phase 2: Delete auto-extracted boilerplate
    if not dry_run or "--analyze-only" not in sys.argv:
        consolidator.consolidate_auto_extracted()

    # Phase 3: Consolidate by project
    if not dry_run or "--analyze-only" not in sys.argv:
        for record_type in ["decision", "assumption", "synthesis"]:
            consolidator.consolidate_by_project(record_type)

    log("\nConsolidation complete!")


if __name__ == "__main__":
    main()
