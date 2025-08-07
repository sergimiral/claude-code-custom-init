#!/bin/bash

# Claude Code Custom Init Installer
# One-line installer for Claude Code with alfred voice support

set -e

echo "🚀 Claude Code Custom Init Installer"
echo "===================================="
echo ""

# Check if we're in a project directory
if [ ! -d ".git" ] && [ ! -f "package.json" ] && [ ! -f "pyproject.toml" ] && [ ! -f "go.mod" ]; then
    echo "⚠️  Warning: This doesn't look like a project directory."
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check if .claude already exists
if [ -d ".claude" ]; then
    echo "📦 Existing .claude directory found."
    echo "Run /init-custom in Claude Code to update missing components."
    echo ""
    echo "Or remove .claude and run this installer again for a fresh install."
    exit 0
fi

# Download from GitHub
echo "📥 Downloading Claude Code Custom Init..."
REPO_URL="https://github.com/sergimiral/claude-code-custom-init"
DOWNLOAD_URL="$REPO_URL/archive/main.zip"

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# Download and extract
curl -L "$DOWNLOAD_URL" -o "$TEMP_DIR/claude-init.zip" --progress-bar
echo "📦 Extracting files..."
unzip -q "$TEMP_DIR/claude-init.zip" -d "$TEMP_DIR"

# Copy .claude directory
echo "📂 Installing .claude directory..."
cp -r "$TEMP_DIR/claude-code-custom-init-main/.claude" .

# Copy init-custom command to global commands if possible
if [ -d "$HOME/.claude/commands" ]; then
    echo "📝 Installing /init-custom command globally..."
    cp "$TEMP_DIR/claude-code-custom-init-main/.claude/commands/init-custom.md" "$HOME/.claude/commands/" 2>/dev/null || true
fi

# Check for dependencies
echo ""
echo "🔍 Checking dependencies..."

# Check for Python
if command -v python3 &> /dev/null; then
    echo "✅ Python found"
    
    # Check for pygame
    if python3 -c "import pygame" 2>/dev/null; then
        echo "✅ pygame found"
    else
        echo "⚠️  pygame not found. Install with: pip install pygame or uv add pygame"
    fi
else
    echo "⚠️  Python not found. Voice notifications require Python with pygame."
fi

# Check for uv (optional but recommended)
if command -v uv &> /dev/null; then
    echo "✅ uv package manager found"
else
    echo "ℹ️  uv not found (optional). Install from: https://github.com/astral-sh/uv"
fi

echo ""
echo "✨ Installation complete!"
echo ""
echo "Next steps:"
echo "1. Open this project in Claude Code"
echo "2. Run: /init-custom (to verify setup)"
echo "3. Run: /init (to create CLAUDE.md with project context)"
echo ""
echo "🎵 Alfred voice notifications are ready!"
echo "💡 Create custom agents with: /create-agent [name] [specialty]"
echo ""
echo "For help, see: $REPO_URL"