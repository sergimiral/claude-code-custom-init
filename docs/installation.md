# Installation Guide

Detailed instructions for installing Claude Code Custom Init.

## Prerequisites

- **Claude Code**: Latest version installed
- **Python**: Version 3.9 or higher
- **Git**: For project detection
- **Operating System**: macOS, Linux, or Windows

## Installation Methods

### Method 1: Quick Install (Recommended)

Run these three commands in your project directory:

```bash
curl -O https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh
chmod +x install.sh
./install.sh .
```

### Method 2: Clone and Install

```bash
git clone https://github.com/sergimiral/claude-code-custom-init.git
cd claude-code-custom-init
./install.sh /path/to/your/project
```

### Method 3: Manual Installation

1. Download the repository
2. Copy the `.claude` folder to your project root
3. Copy the `scripts` folder to your project root
4. Install Python dependencies:
   ```bash
   pip install pygame pyaudio pyttsx3
   ```

## What Gets Installed

```
your-project/
├── .claude/
│   ├── agents/          # Agent configurations
│   ├── commands/        # Custom commands
│   ├── hooks/           # Voice notifications
│   ├── templates/       # Configuration templates
│   ├── settings.json    # Main settings
│   └── settings.local.json  # Local overrides
└── scripts/
    ├── alfred_voice.py  # Voice engine
    ├── test-alfred-voice.py  # Test script
    └── verify-setup.py  # Verification script
```

## Post-Installation

### 1. Verify Installation
In Claude Code:
```
/init-custom
```

### 2. Initialize Project Context
```
/init
```
This creates CLAUDE.md with your project context.

### 3. Test Voice Notifications
```bash
python scripts/test-alfred-voice.py
```

## Python Version Compatibility

The installer automatically handles Python 3.9+ compatibility. If you encounter issues:

```bash
python scripts/fix-python39-compatibility.py
```

## Package Managers

The installer supports multiple package managers in this order:
1. **uv** (fastest, recommended)
2. **pip** (universal fallback)

To install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Updating

To update to the latest version:
```bash
curl -O https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh
chmod +x install.sh
./install.sh . --update
```

## Uninstalling

To remove Claude Code Custom Init:
```bash
rm -rf .claude scripts/alfred_voice.py scripts/test-*.py
```

## Troubleshooting

See [Troubleshooting Guide](troubleshooting.md) for common issues and solutions.