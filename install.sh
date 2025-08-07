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

# Copy scripts directory if it exists
if [ -d "$TEMP_DIR/claude-code-custom-init-main/scripts" ]; then
    echo "📜 Installing helper scripts..."
    mkdir -p scripts
    cp -r "$TEMP_DIR/claude-code-custom-init-main/scripts/"*.py scripts/ 2>/dev/null || true
fi

# Move template files to .claude root
echo "📝 Setting up configuration files..."
if [ -f ".claude/templates/settings.json" ]; then
    mv ".claude/templates/settings.json" ".claude/settings.json"
    echo "✅ Moved settings.json to .claude/"
fi

if [ -f ".claude/templates/settings.local.json" ]; then
    mv ".claude/templates/settings.local.json" ".claude/settings.local.json"
    echo "✅ Moved settings.local.json to .claude/"
fi

# Ensure alfred is set as the default voice
echo "🎵 Configuring alfred voice..."
if [ -f ".claude/settings.json" ]; then
    # Update voice to alfred (macOS compatible sed command)
    sed -i '' 's/"voice": "classic"/"voice": "alfred"/g' ".claude/settings.json" 2>/dev/null || \
    sed -i 's/"voice": "classic"/"voice": "alfred"/g' ".claude/settings.json" 2>/dev/null || true
    echo "✅ Set alfred as default voice"
fi

# Fix Python 3.9 compatibility if needed
if [ -f "$TEMP_DIR/claude-code-custom-init-main/scripts/fix-python39-compatibility.py" ]; then
    echo "🔧 Checking Python compatibility..."
    cp "$TEMP_DIR/claude-code-custom-init-main/scripts/fix-python39-compatibility.py" scripts/ 2>/dev/null || mkdir -p scripts && cp "$TEMP_DIR/claude-code-custom-init-main/scripts/fix-python39-compatibility.py" scripts/
    
    if command -v python3 &> /dev/null; then
        python3 scripts/fix-python39-compatibility.py 2>/dev/null || true
    elif command -v python &> /dev/null; then
        python scripts/fix-python39-compatibility.py 2>/dev/null || true
    fi
fi

# Verify hooks directory exists and has the handler
if [ ! -f ".claude/hooks/voice_notifications/handler.py" ]; then
    echo "⚠️  Warning: Voice notification handler not found at expected location"
    echo "   Expected: .claude/hooks/voice_notifications/handler.py"
fi

# Copy init-custom command to global commands if possible
if [ -d "$HOME/.claude/commands" ]; then
    echo "📝 Installing /init-custom command globally..."
    cp "$TEMP_DIR/claude-code-custom-init-main/.claude/commands/init-custom.md" "$HOME/.claude/commands/" 2>/dev/null || true
fi

# Check for dependencies
echo ""
echo "🔍 Checking dependencies..."

# Check Python version
PYTHON_CMD=""
PYTHON_VERSION=""

if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    PYTHON_CMD="python"
fi

if [ -n "$PYTHON_CMD" ]; then
    echo "✅ Python $PYTHON_VERSION found"
    
    # Check if Python version is 3.9+
    if [ "$(echo "$PYTHON_VERSION >= 3.9" | bc)" -eq 0 ]; then
        echo "⚠️  Python 3.9+ required for voice notifications (found $PYTHON_VERSION)"
    fi
    
    # Check for pygame - try multiple methods
    PYGAME_INSTALLED=false
    
    # Method 1: Direct import
    if $PYTHON_CMD -c "import pygame" 2>/dev/null; then
        PYGAME_INSTALLED=true
    # Method 2: Check in virtual environment if it exists
    elif [ -f ".venv/bin/python" ] && .venv/bin/python -c "import pygame" 2>/dev/null; then
        PYGAME_INSTALLED=true
        echo "ℹ️  pygame found in virtual environment"
    fi
    
    if [ "$PYGAME_INSTALLED" = true ]; then
        echo "✅ pygame found"
    else
        echo "🎵 pygame not found - required for alfred voice notifications"
        echo ""
        echo "Installing pygame..."
        
        # Try to install pygame with available tools
        INSTALL_SUCCESS=false
        
        # Method 1: Try uv (preferred)
        if command -v uv &> /dev/null; then
            echo "🔧 Installing with uv..."
            
            # Initialize Python project if needed
            if [ ! -f "pyproject.toml" ]; then
                PROJECT_NAME=$(basename "$PWD" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g')
                uv init --name "$PROJECT_NAME" >/dev/null 2>&1 || true
            fi
            
            # Add pygame
            if uv add pygame >/dev/null 2>&1; then
                echo "✅ pygame installed with uv"
                INSTALL_SUCCESS=true
            fi
        fi
        
        # Method 2: Try pip if uv failed
        if [ "$INSTALL_SUCCESS" = false ] && command -v pip3 &> /dev/null; then
            echo "🔧 Installing with pip..."
            if pip3 install pygame --user >/dev/null 2>&1; then
                echo "✅ pygame installed with pip"
                INSTALL_SUCCESS=true
            fi
        fi
        
        # Method 3: Try pip without pip3
        if [ "$INSTALL_SUCCESS" = false ] && command -v pip &> /dev/null; then
            echo "🔧 Installing with pip..."
            if pip install pygame --user >/dev/null 2>&1; then
                echo "✅ pygame installed with pip"
                INSTALL_SUCCESS=true
            fi
        fi
        
        if [ "$INSTALL_SUCCESS" = false ]; then
            echo ""
            echo "⚠️  Could not install pygame automatically."
            echo ""
            echo "Please install manually with one of:"
            echo "  • uv add pygame (recommended)"
            echo "  • pip install pygame"
            echo "  • pip3 install pygame"
            echo "  • conda install pygame (if using conda)"
            echo ""
            echo "Note: pygame is required for alfred voice notifications to work"
        fi
    fi
else
    echo "❌ Python not found!"
    echo ""
    echo "Python 3.9+ is required for voice notifications."
    echo "Install Python from: https://www.python.org/downloads/"
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