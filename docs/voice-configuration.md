# Voice Configuration Guide

Setting up and customizing voice notifications in Claude Code.

## Overview

Claude Code supports two notification modes:
1. **Sound Packs** - Pre-recorded contextual sounds
2. **System Voice** - Text-to-speech using system voices

## Sound Packs Mode

### Alfred Voice Pack (Default)

The alfred voice pack includes 55+ contextual sounds:

- **File Operations**: read, write, edit, delete
- **Git Operations**: status, commit, push, pull
- **Task Management**: start, complete, update
- **Language-Specific**: Python, TypeScript, JavaScript
- **Alerts**: errors, warnings, success

### Configuration

Edit `.claude/settings.json`:

```json
{
  "notifications": {
    "mode": "sounds",
    "voice": "alfred",
    "sound_theme": "default"
  }
}
```

### Testing Sounds

```bash
python scripts/test-alfred-voice.py
```

This will play sample sounds from each category.

## System Voice Mode

### Available Voices

#### macOS Standard Voices
- Daniel, Samantha, Alex, Karen, Moira, Fiona

#### macOS Premium Voices
- Zoe, Jamie (require download)

#### International Voices
- Amélie (French), Daria (Russian), Thomas (French)

### Configuration

```json
{
  "notifications": {
    "mode": "voice",
    "voice": "Zoe",
    "sound_theme": "default"
  }
}
```

### Installing Premium Voices (macOS)

1. Open System Settings
2. Go to Accessibility → Spoken Content
3. Click System Voice → Manage Voices
4. Download desired voices (Zoe recommended)

## Creating Custom Voice Packs

### Step 1: Create Directory

```bash
mkdir -p .claude/hooks/voice_notifications/sounds/myvoice
```

### Step 2: Add Sound Files

Create MP3 files with these exact names:

```
task_complete.mp3
task_start.mp3
file_read.mp3
file_write.mp3
file_edit.mp3
git_commit.mp3
error.mp3
warning.mp3
success.mp3
```

### Step 3: Update Configuration

```json
{
  "notifications": {
    "mode": "sounds",
    "voice": "myvoice"
  }
}
```

## Sound Mapping

The `sound_mapping.json` file controls which sounds play for which operations:

```json
{
  "task_complete": ["task_complete.mp3", "success.mp3"],
  "file_read": ["file_read.mp3", "read.mp3"],
  "git_operations": {
    "commit": "git_commit.mp3",
    "push": "git_push.mp3",
    "pull": "git_pull.mp3"
  }
}
```

## Volume Control

### Global Volume

Set in `.claude/settings.local.json`:

```json
{
  "notifications": {
    "volume": 0.7
  }
}
```

### Per-Sound Volume

In `sound_mapping.json`:

```json
{
  "task_complete": {
    "file": "task_complete.mp3",
    "volume": 0.5
  }
}
```

## Disabling Notifications

### Temporarily

```json
{
  "notifications": {
    "enabled": false
  }
}
```

### For Specific Operations

```json
{
  "notifications": {
    "disabled_operations": ["file_read", "file_write"]
  }
}
```

## Debugging

### Enable Debug Logging

```bash
tail -f .claude/hooks/voice_notifications/debug.log
```

### Common Log Messages

- `🎵 Attempting to play: [sound]` - Sound triggered
- `✅ Successfully played: [sound]` - Sound played
- `❌ pygame not available` - Audio library issue
- `⚠️ Sound file not found` - Missing file

## Platform-Specific Notes

### macOS
- Requires Python 3.9+
- May need audio permissions
- Premium voices require download

### Linux
- Install `python3-pygame` package
- May need `pulseaudio` or `alsa`
- Check audio permissions

### Windows
- Install pygame via pip
- Windows Defender may block first run
- Check audio output device

## Troubleshooting

### No Sound Playing

1. Check pygame installation:
```bash
python -c "import pygame; print('OK')"
```

2. Test audio system:
```bash
python scripts/test-alfred-voice.py
```

3. Check volume settings:
```bash
grep volume .claude/settings*.json
```

### Wrong Voice Playing

1. Verify configuration:
```bash
grep -A3 notifications .claude/settings.json
```

2. Check available voices:
```bash
ls .claude/hooks/voice_notifications/sounds/
```

### Delayed Notifications

1. Check system performance
2. Reduce sound file sizes
3. Disable debug logging

## Best Practices

1. **Use appropriate volume**: 0.5-0.7 is usually ideal
2. **Choose contextual sounds**: Alfred for development feedback
3. **Test after changes**: Run test script to verify
4. **Keep files small**: Under 100KB for quick playback
5. **Organize custom sounds**: Follow naming conventions

## Advanced Configuration

### Conditional Sounds

Based on operation context:

```json
{
  "conditional_sounds": {
    "git_commit": {
      "success": "git_success.mp3",
      "failure": "git_error.mp3"
    }
  }
}
```

### Sound Sequences

Chain multiple sounds:

```json
{
  "sequences": {
    "build_complete": [
      "build_done.mp3",
      "success.mp3"
    ]
  }
}
```

### Time-Based Sounds

Different sounds by time of day:

```json
{
  "time_based": {
    "morning": "gentle_chime.mp3",
    "evening": "soft_bell.mp3"
  }
}
```