#!/usr/bin/env python3
"""
Backup and Rollback System for Knowledge Consolidator

Creates timestamped backups before consolidation and provides rollback capability.
"""

import shutil
import json
from pathlib import Path
from datetime import datetime


VAULT_PATH = Path.home() / "Projects" / "obsidian-vault"
AI_DIALOGUE_DIR = VAULT_PATH / "ai-dialogue"
BACKUP_DIR = VAULT_PATH / "archive" / "consolidator_backups"
BACKUP_MANIFEST = BACKUP_DIR / "backup_manifest.json"


def create_backup(description="Pre-consolidation backup"):
    """
    Create a complete backup of ai-dialogue/ directory.

    Returns:
        backup_id: Unique identifier for this backup
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_id = f"backup_{timestamp}"
    backup_path = BACKUP_DIR / backup_id

    print(f"Creating backup: {backup_id}")
    print(f"Source: {AI_DIALOGUE_DIR}")
    print(f"Destination: {backup_path}")

    # Create backup directory
    backup_path.mkdir(parents=True, exist_ok=True)

    # Count files before backup
    files = list(AI_DIALOGUE_DIR.glob("*.md"))
    print(f"Files to backup: {len(files)}")

    # Copy all files
    copied = 0
    for file in files:
        try:
            shutil.copy2(file, backup_path / file.name)
            copied += 1
        except Exception as e:
            print(f"⚠️  Error backing up {file.name}: {e}")

    print(f"✓ Copied {copied}/{len(files)} files")

    # Create manifest
    manifest_entry = {
        "backup_id": backup_id,
        "timestamp": datetime.now().isoformat(),
        "description": description,
        "source": str(AI_DIALOGUE_DIR),
        "backup_path": str(backup_path),
        "files_backed_up": copied,
        "total_files": len(files)
    }

    # Load existing manifest
    manifest = []
    if BACKUP_MANIFEST.exists():
        with open(BACKUP_MANIFEST) as f:
            manifest = json.load(f)

    # Add new entry
    manifest.append(manifest_entry)

    # Save manifest
    with open(BACKUP_MANIFEST, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"✓ Backup complete: {backup_id}")
    print(f"✓ Manifest updated: {BACKUP_MANIFEST}")

    return backup_id


def list_backups():
    """List all available backups"""
    if not BACKUP_MANIFEST.exists():
        print("No backups found")
        return []

    with open(BACKUP_MANIFEST) as f:
        manifest = json.load(f)

    print("\n📦 Available Backups:")
    print("="*70)

    for i, backup in enumerate(manifest, 1):
        print(f"\n{i}. {backup['backup_id']}")
        print(f"   Created: {backup['timestamp']}")
        print(f"   Description: {backup['description']}")
        print(f"   Files: {backup['files_backed_up']}")
        print(f"   Path: {backup['backup_path']}")

    print("\n" + "="*70)

    return manifest


def rollback(backup_id=None):
    """
    Rollback to a specific backup (or latest if not specified).

    This will:
    1. Create a backup of current state (in case rollback was a mistake)
    2. Restore files from the specified backup
    """
    if not BACKUP_MANIFEST.exists():
        print("❌ No backups available for rollback")
        return False

    with open(BACKUP_MANIFEST) as f:
        manifest = json.load(f)

    if not manifest:
        print("❌ No backups in manifest")
        return False

    # Find backup to restore
    if backup_id:
        backup = next((b for b in manifest if b["backup_id"] == backup_id), None)
        if not backup:
            print(f"❌ Backup not found: {backup_id}")
            return False
    else:
        # Use latest backup
        backup = manifest[-1]
        backup_id = backup["backup_id"]

    print(f"\n🔄 Rolling back to: {backup_id}")
    print(f"Created: {backup['timestamp']}")
    print(f"Files in backup: {backup['files_backed_up']}")

    # Safety: Create backup of current state before rollback
    print("\n⚠️  Creating safety backup of current state...")
    safety_backup_id = create_backup(f"Pre-rollback safety backup (rolling back to {backup_id})")

    # Get backup path
    backup_path = Path(backup["backup_path"])

    if not backup_path.exists():
        print(f"❌ Backup path not found: {backup_path}")
        return False

    # Clear current ai-dialogue/
    print(f"\n🗑️  Clearing current ai-dialogue/...")
    current_files = list(AI_DIALOGUE_DIR.glob("*.md"))
    for file in current_files:
        file.unlink()
    print(f"✓ Removed {len(current_files)} files")

    # Restore from backup
    print(f"\n📥 Restoring from backup...")
    backup_files = list(backup_path.glob("*.md"))
    restored = 0

    for file in backup_files:
        try:
            shutil.copy2(file, AI_DIALOGUE_DIR / file.name)
            restored += 1
        except Exception as e:
            print(f"⚠️  Error restoring {file.name}: {e}")

    print(f"✓ Restored {restored}/{len(backup_files)} files")

    # Verify restoration
    final_count = len(list(AI_DIALOGUE_DIR.glob("*.md")))
    print(f"\n✅ Rollback complete!")
    print(f"Files in ai-dialogue/: {final_count}")
    print(f"Safety backup created: {safety_backup_id}")
    print(f"(In case you need to undo this rollback)")

    return True


def verify_backup(backup_id):
    """Verify a backup is intact"""
    if not BACKUP_MANIFEST.exists():
        print("❌ No manifest found")
        return False

    with open(BACKUP_MANIFEST) as f:
        manifest = json.load(f)

    backup = next((b for b in manifest if b["backup_id"] == backup_id), None)
    if not backup:
        print(f"❌ Backup not found: {backup_id}")
        return False

    backup_path = Path(backup["backup_path"])

    if not backup_path.exists():
        print(f"❌ Backup directory missing: {backup_path}")
        return False

    files = list(backup_path.glob("*.md"))
    expected = backup["files_backed_up"]

    print(f"\n🔍 Verifying backup: {backup_id}")
    print(f"Expected files: {expected}")
    print(f"Actual files: {len(files)}")

    if len(files) == expected:
        print("✅ Backup verified - all files present")
        return True
    else:
        print(f"⚠️  Backup incomplete - missing {expected - len(files)} files")
        return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python consolidator_backup.py create [description]")
        print("  python consolidator_backup.py list")
        print("  python consolidator_backup.py rollback [backup_id]")
        print("  python consolidator_backup.py verify <backup_id>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "create":
        description = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "Manual backup"
        backup_id = create_backup(description)
        print(f"\n✅ Backup ID: {backup_id}")
        print(f"\nTo rollback: python consolidator_backup.py rollback {backup_id}")

    elif command == "list":
        list_backups()

    elif command == "rollback":
        backup_id = sys.argv[2] if len(sys.argv) > 2 else None
        if rollback(backup_id):
            print("\n✅ Rollback successful!")
        else:
            print("\n❌ Rollback failed")

    elif command == "verify":
        if len(sys.argv) < 3:
            print("❌ Backup ID required")
            sys.exit(1)
        backup_id = sys.argv[2]
        verify_backup(backup_id)

    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)
