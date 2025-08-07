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

### For Alfred Voice
The alfred voice pack requires:
1. `mode: "sounds"` (not "voice")
2. `voice: "alfred"` (lowercase)

Example `settings.json`:
```json
{
  "notifications": {
    "mode": "sounds",
    "voice": "alfred",
    "sound_theme": "default"
  }
}
```

### Dependencies
- **Required**: Python with pygame for sound playback
- **Recommended**: uv package manager

Install pygame:
```bash
# With uv (recommended)
uv add pygame

# With pip
pip install pygame
```

## Troubleshooting 🔍

### Alfred Voice Not Working?

1. **Check handler.py version**:
```bash
grep "alfred" .claude/hooks/voice_notifications/handler.py
```
If no results, you need the advanced handler.

2. **Verify settings.json**:
- Must use `"mode": "sounds"` (not "voice")
- Must use `"voice": "alfred"` (lowercase)

3. **Check sound files**:
```bash
ls .claude/hooks/voice_notifications/sounds/alfred/ | wc -l
```
Should show 55 files.

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