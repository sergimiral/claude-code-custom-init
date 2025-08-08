#\!/bin/bash
# Cross-platform hook runner for Claude Code
# Tries different Python execution methods in order of preference

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="$(dirname "$SCRIPT_DIR")"

# Try different Python approaches
if [ -f "$CLAUDE_DIR/.venv/bin/python" ]; then
    # Unix/macOS virtual environment
    "$CLAUDE_DIR/.venv/bin/python" "$CLAUDE_DIR/$1"
elif [ -f "$CLAUDE_DIR/.venv/Scripts/python.exe" ]; then
    # Windows virtual environment  
    "$CLAUDE_DIR/.venv/Scripts/python.exe" "$CLAUDE_DIR/$1"
elif command -v python3 >/dev/null 2>&1; then
    # System Python 3
    python3 "$CLAUDE_DIR/$1"
elif command -v python >/dev/null 2>&1; then
    # System Python (could be 2 or 3)
    python "$CLAUDE_DIR/$1"
else
    echo "Error: No Python found for Claude hooks" >&2
    echo "Please ensure Python is installed or run install.sh again" >&2
    exit 1
fi
EOF < /dev/null