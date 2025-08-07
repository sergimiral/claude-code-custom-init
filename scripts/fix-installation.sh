#!/bin/bash

# Fix existing Claude Code Custom Init installations
# This script fixes installations where settings files are in the wrong location

set -e

echo "🔧 Claude Code Custom Init - Installation Fixer"
echo "=============================================="
echo ""

# Check if .claude directory exists
if [ ! -d ".claude" ]; then
    echo "❌ No .claude directory found in current directory."
    echo "   Please run this script from a project with Claude Code Custom Init installed."
    exit 1
fi

echo "📂 Found .claude directory. Checking configuration..."

# Function to fix settings file location
fix_settings_file() {
    local filename=$1
    local fixed=false
    
    # Check if file is in templates directory but not in root
    if [ -f ".claude/templates/$filename" ] && [ ! -f ".claude/$filename" ]; then
        echo "📝 Moving $filename from templates/ to .claude/ root..."
        mv ".claude/templates/$filename" ".claude/$filename"
        echo "✅ Moved $filename to correct location"
        fixed=true
    elif [ -f ".claude/$filename" ]; then
        echo "✅ $filename already in correct location"
    elif [ -f ".claude/templates/$filename" ]; then
        echo "⚠️  $filename exists in both locations. Keeping the one in .claude/ root"
    else
        echo "⚠️  $filename not found. You may need to reinstall."
    fi
    
    if [ "$fixed" = true ]; then
        return 0
    else
        return 1
    fi
}

# Fix settings files
changes_made=false
if fix_settings_file "settings.json"; then
    changes_made=true
fi

if fix_settings_file "settings.local.json"; then
    changes_made=true
fi

# Verify hook handler exists
echo ""
echo "🔍 Verifying hook handler..."
if [ -f ".claude/hooks/voice_notifications/handler.py" ]; then
    echo "✅ Voice notification handler found"
    
    # Check if the hook paths in settings.json are correct
    if [ -f ".claude/settings.json" ]; then
        if grep -q "uv run .claude/hooks/voice_notifications/handler.py" ".claude/settings.json"; then
            echo "✅ Hook paths in settings.json are correct"
        else
            echo "⚠️  Hook paths in settings.json may need updating"
            echo "   Expected: 'uv run .claude/hooks/voice_notifications/handler.py'"
        fi
    fi
else
    echo "❌ Voice notification handler not found at expected location"
    echo "   Expected: .claude/hooks/voice_notifications/handler.py"
    echo "   You may need to reinstall Claude Code Custom Init"
fi

# Check for alfred sounds
if [ -d ".claude/hooks/voice_notifications/sounds/alfred" ]; then
    echo "✅ Alfred sound pack found"
else
    echo "⚠️  Alfred sound pack not found. Voice notifications may not work."
fi

echo ""
if [ "$changes_made" = true ]; then
    echo "✨ Installation fixed!"
    echo ""
    echo "Next steps:"
    echo "1. Restart Claude Code if it's running"
    echo "2. Run: /init-custom (to verify setup)"
    echo "3. Test with any command to hear Alfred's voice"
else
    echo "ℹ️  No changes needed - installation appears correct"
    echo ""
    echo "If you're still having issues:"
    echo "1. Check that Python and pygame are installed"
    echo "2. Try removing .claude/ and running the installer again"
    echo "3. Check the troubleshooting guide"
fi