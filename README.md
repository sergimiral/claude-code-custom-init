# Claude Code Custom Init

Supercharge your Claude Code experience with the SuperClaude framework - intelligent personas, smart commands, and voice notifications.

## 🚀 Quick Start

Run these three commands in your project directory:

```bash
curl -O https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh
chmod +x install.sh
./install.sh .
```

That's it! Open Claude Code and run `/init-custom` to verify the installation.

## ✨ What You Get

- **🧠 11 Intelligent Personas** - Auto-activated specialists for different domains
- **🎯 Smart Commands** - `/analyze`, `/build`, `/implement`, `/improve` and more  
- **🎵 Voice Notifications** - Alfred voice pack with 55+ contextual sounds
- **⚡ Performance Optimizations** - Token-efficient modes and parallel processing
- **🔧 MCP Integration** - Enhanced capabilities with Context7, Sequential, Magic, and Playwright

## 📖 Features

### Smart Commands
- `/analyze` - Deep code analysis with architecture insights
- `/build` - Intelligent project building with framework detection
- `/implement` - Feature implementation with persona activation
- `/improve` - Code optimization and quality enhancement
- [See all commands →](docs/commands.md)

### Intelligent Personas
- **Architect** - System design and scalability
- **Frontend** - UI/UX and accessibility
- **Backend** - APIs and reliability
- **Security** - Vulnerability assessment
- [See all personas →](docs/personas.md)

### Voice Notifications
The alfred voice pack provides audio feedback:
- Task completion announcements
- Error notifications
- Progress updates with 55+ contextual sounds

## 🛠️ Installation Options

### For Existing Projects
Use the quick start commands above.

### For New Projects
Create a new project with Claude Code Custom Init pre-configured:
```bash
./install.sh /path/to/new-project
```

## 📚 Documentation

- [Installation Guide](docs/installation.md) - Detailed setup instructions
- [Commands Reference](docs/commands.md) - All available commands
- [Personas Guide](docs/personas.md) - Understanding personas
- [Voice Configuration](docs/voice-configuration.md) - Setting up notifications
- [Troubleshooting](docs/troubleshooting.md) - Common issues and solutions

## 🎯 Example Usage

```bash
# Analyze your entire codebase
/analyze --comprehensive

# Build with optimal settings
/build --optimize

# Implement a new feature
/implement user authentication system

# Improve code quality
/improve --focus performance
```

## 🔧 Requirements

- Claude Code (latest version)
- Python 3.9+ (for voice notifications)
- Git (for project detection)

## Configuration

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

## How to Use 📝

### Installation + Setup (2 steps)
1. **Install**: Run the one-line installer above
2. **Initialize**: Run `/init` in Claude Code

That's it! Alfred sounds will play automatically.

### Optional Commands
- `/create-agent [name] [specialty]` - Create custom agents
- `/init-custom` - Re-run setup if needed

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

## 📝 License

Open source - feel free to use, modify, and share!

## 🤝 Contributing

Contributions welcome! Feel free to submit issues and pull requests.

## 📞 Support

- [GitHub Issues](https://github.com/sergimiral/claude-code-custom-init/issues)
- [Documentation](docs/)

---

Created by [@sergimiral](https://github.com/sergimiral)