# Troubleshooting Guide 🔧

Common issues and solutions for Claude Code Custom Init.

## Installation Issues

### `.claude` directory already exists

**Problem**: The installer says `.claude` already exists.

**Solution**: 
- Run `/init-custom` in Claude Code to update missing components
- Or remove `.claude` and run installer for fresh install:
```bash
rm -rf .claude
./install.sh
```

### Command not found: /init-custom

**Problem**: Claude Code doesn't recognize `/init-custom` command.

**Solution**:
1. Copy command manually:
```bash
cp .claude/commands/init-custom.md ~/.claude/commands/
```
2. Restart Claude Code
3. Try the command again

## Alfred Voice Issues

### No sounds playing at all

**Problem**: Alfred voice enabled but no sounds play.

**Diagnosis**:
```bash
# Check mode setting
grep '"mode"' .claude/settings.json
# Should show: "mode": "sounds"

# Check voice setting
grep '"voice"' .claude/settings.json  
# Should show: "voice": "alfred"

# Check sounds exist
ls .claude/hooks/voice_notifications/sounds/alfred/ | wc -l
# Should show: 55
```

**Solutions**:
1. Fix settings.json:
```json
{
  "notifications": {
    "mode": "sounds",    // NOT "voice"
    "voice": "alfred",   // lowercase
    "sound_theme": "default"
  }
}
```

2. Verify pygame installed:
```bash
python3 -c "import pygame" || pip install pygame
```

### Falls back to TTS voice instead of alfred sounds

**Problem**: You hear text-to-speech instead of alfred sounds.

**Cause**: `mode` is set to `"voice"` instead of `"sounds"`

**Solution**: 
```json
{
  "notifications": {
    "mode": "sounds",    // Change from "voice" to "sounds"
    "voice": "alfred"
  }
}
```

### Handler doesn't support alfred

**Problem**: Sounds play but uses default/classic instead of alfred.

**Diagnosis**:
```bash
grep "alfred" .claude/hooks/voice_notifications/handler.py
```
If no results, handler doesn't support alfred.

**Solution**: 
Copy the advanced handler from this repository:
```bash
cp ~/Repos/claude-code-custom-init/.claude/hooks/voice_notifications/handler.py .claude/hooks/voice_notifications/
```

### Missing alfred section in sound_mapping.json

**Problem**: Handler supports alfred but mappings are missing.

**Diagnosis**:
```bash
grep '"alfred"' .claude/hooks/voice_notifications/sound_mapping.json
```

**Solution**:
Add alfred section to sound_mapping.json (see init-custom.md for complete mappings).

## Dependency Issues

### pygame not found

**Problem**: `ModuleNotFoundError: No module named 'pygame'`

**Solutions**:

With uv (recommended):
```bash
uv add pygame
```

With pip:
```bash
pip install pygame
# or
python3 -m pip install pygame
```

With conda:
```bash
conda install pygame
```

### Python not found

**Problem**: Voice notifications require Python but it's not installed.

**Solutions**:
- macOS: `brew install python3`
- Ubuntu/Debian: `sudo apt install python3 python3-pip`
- Windows: Download from python.org

## Permission Issues

### Permission denied errors

**Problem**: Claude Code can't execute certain commands.

**Solution**: 
Add permissions to `.claude/settings.local.json`:
```json
{
  "permissions": {
    "allow": [
      "Bash(uv:*)",
      "Bash(pip:*)",
      "Bash(python:*)",
      "Bash(python3:*)"
    ]
  }
}
```

## Configuration Issues

### CLAUDE.md not created

**Problem**: `/init-custom` doesn't create CLAUDE.md.

**Explanation**: This is intentional. CLAUDE.md should contain project-specific context.

**Solution**: 
Run `/init` after `/init-custom` to create CLAUDE.md with your project's context.

### Settings not taking effect

**Problem**: Changed settings.json but nothing changes.

**Solutions**:
1. Restart Claude Code session
2. Check for syntax errors in JSON:
```bash
python3 -m json.tool .claude/settings.json
```
3. Ensure hooks are configured correctly

## Update Issues

### How to update to latest version

**To update alfred sounds only**:
```bash
rm -rf .claude/hooks/voice_notifications/sounds/alfred
cp -r ~/Repos/claude-code-custom-init/.claude/hooks/voice_notifications/sounds/alfred .claude/hooks/voice_notifications/sounds/
```

**To update everything**:
Run `/init-custom` - it will detect existing setup and only add missing components.

## Debug Information

### Check debug log

Voice notification debug log location:
```bash
.claude/hooks/voice_notifications/debug.log
```

View recent errors:
```bash
tail -50 .claude/hooks/voice_notifications/debug.log | grep ERROR
```

### Validate setup

Run this to check your setup:
```bash
# Check structure
[ -d .claude ] && echo "✓ .claude exists" || echo "✗ .claude missing"
[ -f .claude/settings.json ] && echo "✓ settings.json exists" || echo "✗ settings.json missing"
[ -d .claude/hooks/voice_notifications/sounds/alfred ] && echo "✓ alfred sounds exist" || echo "✗ alfred sounds missing"

# Count files
echo "Agents: $(ls .claude/agents/*.md 2>/dev/null | wc -l)/5"
echo "Alfred sounds: $(ls .claude/hooks/voice_notifications/sounds/alfred/*.mp3 2>/dev/null | wc -l)/55"

# Check configuration
grep '"mode"' .claude/settings.json
grep '"voice"' .claude/settings.json
```

## Getting Help

If you're still having issues:

1. Check the debug log
2. Run the validation script above
3. Open an issue on GitHub with:
   - Your settings.json (remove sensitive data)
   - Output of validation script
   - Error messages from debug.log
   - Claude Code version

## Common Mistakes to Avoid

❌ Using `"mode": "voice"` with alfred (use `"sounds"`)
❌ Capitalizing "Alfred" in settings (use lowercase)
❌ Setting `"sound_theme": "alfred"` (use `"default"`)
❌ Forgetting to install pygame
❌ Not copying the advanced handler.py
✅ Correct: `"mode": "sounds"`, `"voice": "alfred"`