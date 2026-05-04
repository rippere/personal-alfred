#!/bin/bash
# Vault Auto-Sync Script
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

echo "🔄 Syncing vault..."

# Stage all changes first (before pulling)
git add -A

# Commit local changes if any exist
if ! git diff --cached --quiet; then
    timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    git commit -m "Auto-sync: $timestamp"
    echo "✅ Committed local changes"
fi

# Fetch latest changes
git fetch origin master

# Check for remote changes
if ! git diff --quiet HEAD origin/master; then
    echo "📥 Pulling remote changes..."
    if ! git pull --no-rebase origin master; then
        echo "❌ CONFLICT DETECTED!"
        git status
        exit 1
    fi
fi

echo "📤 Pushing to GitHub..."
git push origin master

echo "✅ Sync complete!"
