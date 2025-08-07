# User Testing Guide 🧪

How to manually test Claude Code Custom Init with alfred voice notifications.

## Quick Start Test (5 minutes)

### 1. Fresh Install Test

```bash
# Create a new project directory
mkdir ~/test-claude-alfred
cd ~/test-claude-alfred

# Run the one-line installer
curl -sSL https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh | bash

# If prompted about empty directory, type 'y' and press Enter
```

### 2. Open in Claude Code

```bash
# Open the project
claude ~/test-claude-alfred
```

### 3. Initialize and Test

In Claude Code, run these commands:

```
/init
```
This creates your CLAUDE.md with project context.

### 4. Test Alfred Sounds

The alfred sounds should play automatically when Claude:
- Reads files (different sounds for .py, .ts, .json files)
- Edits code
- Runs git commands
- Completes tasks

To test manually:
```bash
# In terminal, run the test script
python3 scripts/test-alfred-voice.py
```

You should hear 7 different alfred sounds!

## Detailed Testing Scenarios

### Scenario A: Empty Project Installation

1. **Create empty project**:
```bash
mkdir ~/my-new-project
cd ~/my-new-project
git init  # Optional: prevents warning
```

2. **Install**:
```bash
curl -sSL https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh | bash
```

3. **Expected Results**:
- ✅ .claude directory created
- ✅ 55 alfred sound files installed
- ✅ pygame installed automatically (if you have pip/uv)
- ✅ settings.json configured with alfred voice
- ✅ 5 standard agents ready
- ✅ Helper scripts in scripts/ directory

### Scenario B: Existing Project Installation

1. **Navigate to existing project**:
```bash
cd ~/my-existing-project
```

2. **Install** (same command):
```bash
curl -sSL https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh | bash
```

3. **Expected Results**:
- ✅ Your existing files preserved
- ✅ .claude directory added
- ✅ No conflicts with existing package.json, README, etc.
- ✅ Alfred sounds ready to use

## Testing Different Voice Modes

### Test Alfred Sounds (Contextual MP3s)

Your settings.json should have:
```json
{
  "notifications": {
    "mode": "sounds",
    "voice": "alfred"
  }
}
```

Test with:
```bash
python3 scripts/test-alfred-voice.py
```

### Test System Voices (Text-to-Speech)

1. **Switch to Zoe (Premium) voice**:

Edit .claude/settings.json:
```json
{
  "notifications": {
    "mode": "voice",
    "voice": "Zoe"
  }
}
```

2. **Test Zoe**:
```bash
python3 scripts/test-zoe-voice.py
```

3. **Try other voices**:
- Daniel (standard)
- Samantha (standard)
- Alex (standard)

## Verification Checklist

Run the comprehensive verification:
```bash
python3 scripts/verify-setup.py
```

Should show:
- ✅ Python Version: PASS
- ✅ Pygame Library: PASS
- ✅ Directory Structure: PASS
- ✅ Alfred Sounds: PASS (55 files)
- ✅ Settings Config: PASS
- ✅ Handler Support: PASS
- ✅ Sound Mapping: PASS
- ✅ Sound Playback: PASS

## Troubleshooting During Testing

### No Sounds Playing?

1. **Check pygame**:
```bash
python3 -c "import pygame; print('pygame installed')"
```

If not installed:
```bash
uv add pygame  # or pip install pygame
```

2. **Check volume**: Make sure system volume isn't muted

3. **Check settings.json**:
```bash
cat .claude/settings.json | grep -A 2 notifications
```

Should show:
```json
"notifications": {
  "mode": "sounds",
  "voice": "alfred"
```

### Python Version Issues?

If you see syntax errors:
```bash
python3 scripts/fix-python39-compatibility.py
```

### Want to Remove Everything?

```bash
rm -rf .claude scripts/
```

## What Success Looks Like

When everything works correctly:

1. **In Claude Code**: You hear different contextual sounds for:
   - Python file operations (distinctive Python sound)
   - TypeScript operations (different sound)
   - Git commands (git-specific sounds)
   - Task completion (success sound)

2. **Sound Quality**: Clear, contextual audio feedback for each operation

3. **No Errors**: No Python errors or missing file warnings

## Report Issues

If something doesn't work:
1. Run `python3 scripts/verify-setup.py` and note which checks fail
2. Check `cat .claude/hooks/voice_notifications/debug.log` for errors
3. Report at: https://github.com/sergimiral/claude-code-custom-init/issues

## Advanced Testing

### Create Custom Agent
```
/create-agent code-reviewer "reviews code for best practices"
```

### Test All Sounds
```bash
# Lists all 55 sounds
ls .claude/hooks/voice_notifications/sounds/alfred/

# Play a specific sound
python3 -c "import pygame; pygame.mixer.init(); pygame.mixer.music.load('.claude/hooks/voice_notifications/sounds/alfred/file_read.mp3'); pygame.mixer.music.play(); import time; time.sleep(2)"
```

### Check Debug Logs
```bash
# Watch logs in real-time during Claude Code operations
tail -f .claude/hooks/voice_notifications/debug.log
```

---

**Ready to test?** Start with the Quick Start Test above! 🚀