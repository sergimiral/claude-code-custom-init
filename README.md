# Claude Code Custom Init 🚀

Complete initialization package for Claude Code with alfred voice notifications and standard agents.

## Features ✨

- **5 Standard Agents**: PRD writer, system architect, UI designer, Python backend dev, React TypeScript specialist
- **Alfred Voice Pack**: 55+ contextual sounds for different operations
- **Smart Update Mode**: Won't overwrite your existing customizations
- **Complete Hook System**: Voice notifications with context-aware sounds
- **Custom Commands**: `/init-custom` and `/create-agent` commands

## Quick Install 🎯

### One-Line Install
```bash
curl -sSL https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh | bash
```

### Manual Install

1. Clone this repository:
```bash
git clone https://github.com/sergimiral/claude-code-custom-init.git
cd claude-code-custom-init
```

2. Copy the `.claude` directory to your project:
```bash
cp -r .claude /path/to/your/project/
```

3. In Claude Code, run:
```
/init-custom
```

4. Then create your project context:
```
/init
```

## What's Included 📦

### Agents
- **CLAUDE.md**: Global agent configuration
- **prd-writer.md**: Product Requirements Document specialist
- **system-architect.md**: System design and architecture expert
- **ui-designer.md**: UI/UX design specialist
- **python-backend-dev.md**: Python backend development expert
- **react-typescript-specialist.md**: React and TypeScript expert

### Alfred Voice Pack
55+ contextual sounds including:
- File operations (read, edit, write)
- Git operations (status, commit, diff)
- Task management (start, complete, update)
- Alerts and notifications
- Language-specific sounds (Python, TypeScript, etc.)

### Commands
- **/init-custom**: Smart initialization that detects existing setups
- **/create-agent**: Create custom agents for your specific needs

## Configuration 🔧

### Understanding Voice Modes

Claude Code supports two notification modes:

#### 1. Sound Packs Mode (`mode: "sounds"`)
Pre-recorded MP3 files with contextual sounds for different operations.

**Available sound packs:**
- **alfred**: 55+ contextual sounds (Python, TypeScript, git operations, etc.)
- **jarvis**: (if installed)
- **ding**: (if installed)

**Configuration for alfred:**
```json
{
  "notifications": {
    "mode": "sounds",
    "voice": "alfred",
    "sound_theme": "default"
  }
}
```

#### 2. System Voice Mode (`mode: "voice"`)
Uses macOS text-to-speech voices to speak notifications.

**Available system voices** (check yours with `say -v '?'`):
- **Standard**: Daniel, Samantha, Alex, Karen, Moira, Fiona
- **Premium**: Zoe, Jamie (require macOS download)
- **International**: Amélie (French), Daria (Russian), etc.

**Configuration for system voice:**
```json
{
  "notifications": {
    "mode": "voice",
    "voice": "Zoe",  // or "Daniel", "Samantha", etc.
    "sound_theme": "default"
  }
}
```

**To download premium voices on macOS:**
1. System Settings → Accessibility → Spoken Content
2. System Voice → Manage Voices...
3. Download Zoe (Premium) or other voices

### Quick Switch Examples

**For contextual sounds (recommended):**
```json
{ "mode": "sounds", "voice": "alfred" }
```

**For spoken notifications:**
```json
{ "mode": "voice", "voice": "Zoe" }  // Premium voice
{ "mode": "voice", "voice": "Daniel" }  // Standard voice
```

## System Requirements 📋

### Minimum Requirements
- **Python**: 3.9 or higher
- **pygame**: For audio playback (auto-installed by installer)
- **Operating System**: macOS, Linux, or Windows
- **Claude Code**: Latest version

### Recommended Setup
- **Python**: 3.11+ for best compatibility
- **Package Manager**: uv (for fast, reliable package management)
- **Memory**: 100MB free space for sounds and scripts

## Installation Details 🛠️

The installer automatically:
1. ✅ Detects Python version and warns if < 3.9
2. ✅ Installs pygame using available package managers (uv, pip)
3. ✅ Fixes Python 3.9 compatibility issues
4. ✅ Configures alfred as the default voice
5. ✅ Sets up all 55 contextual sounds
6. ✅ Creates scripts for testing and verification

## Troubleshooting 🔍

### Common Issues and Solutions

#### 1. No Sound Playing
**Symptom**: Script says sounds play but you hear nothing

**Solutions**:
```bash
# Check pygame is installed
python3 -c "import pygame; print('pygame installed')"

# If not installed, install manually:
uv add pygame  # or pip install pygame

# Test sounds directly
python3 scripts/test-alfred-voice.py
```

**Check system volume** and ensure it's not muted.

#### 2. Python Version Issues
**Symptom**: `SyntaxError: invalid syntax` or `ImportError: cannot import name 'StrEnum'`

**Solution**: Run the compatibility fixer:
```bash
python3 scripts/fix-python39-compatibility.py
```

#### 3. Handler Not Supporting Alfred
**Symptom**: Always plays default sound instead of alfred voices

**Check handler.py has alfred support**:
```bash
grep "custom_voice_packs" .claude/hooks/voice_notifications/handler.py
```

If missing, the handler needs updating. Re-run installer:
```bash
curl -sSL https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh | bash
```

#### 4. Settings Configuration Wrong
**Symptom**: Alfred voice not activating

**Verify settings.json**:
```bash
cat .claude/settings.json | grep -A 3 notifications
```

Should show:
```json
"notifications": {
  "mode": "sounds",
  "voice": "alfred",
```

**Fix if needed**:
```bash
sed -i '' 's/"voice": ".*"/"voice": "alfred"/g' .claude/settings.json
```

#### 5. Missing Sound Files
**Symptom**: Some sounds don't play

**Verify all 55 files exist**:
```bash
ls .claude/hooks/voice_notifications/sounds/alfred/*.mp3 | wc -l
```

Should output: `55`

If missing, reinstall:
```bash
rm -rf .claude
curl -sSL https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh | bash
```

### Debug Mode

Enable debug logging to troubleshoot:
```bash
# Watch debug log in real-time
tail -f .claude/hooks/voice_notifications/debug.log
```

Look for:
- `🎵 Attempting to play:` - Shows what's being tried
- `✅ Successfully played:` - Sound played correctly
- `❌ pygame not available:` - pygame installation issue
- `⚠️ Sound file not found:` - Missing sound file

### Verification Script

Run the comprehensive test:
```bash
# Test all alfred sounds
python3 scripts/test-alfred-voice.py

# Verify setup (coming soon)
python3 scripts/verify-setup.py
```

## Project Structure 🏗️

```
.claude/
├── agents/                   # 5 standard agents
├── commands/                 # Custom commands
├── hooks/
│   ├── common/              # Shared utilities
│   └── voice_notifications/
│       ├── handler.py       # Advanced handler with alfred support
│       ├── sound_mapping.json
│       └── sounds/
│           ├── alfred/      # 55+ contextual sounds
│           └── themes/      # Default and classic themes
└── templates/               # Configuration templates
```

## Creating Custom Voices 🎤

You can create your own voice pack:

1. Create a folder in `.claude/hooks/voice_notifications/sounds/yourvoice/`
2. Add MP3 files with the same names as alfred sounds
3. Update `settings.json` to use your voice:
```json
{
  "notifications": {
    "mode": "sounds",
    "voice": "yourvoice"
  }
}
```

## Command Sequence 📝

### For New Projects:
1. `/init-custom` - Sets up agents, hooks, and sounds
2. `/init` - Creates CLAUDE.md with project context
3. `/create-agent [name]` - Add custom agents as needed

### For Existing Projects:
1. `/init-custom` - Updates missing components only
2. `/init` (if no CLAUDE.md) - Creates project context

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

MIT License - See LICENSE file for details

## Credits 👏

- Alfred voice pack created by [Your Name]
- Claude Code by Anthropic
- Community contributions

## Support 💬

For issues or questions, please open an issue on GitHub.

---

Made with ❤️ for the Claude Code community