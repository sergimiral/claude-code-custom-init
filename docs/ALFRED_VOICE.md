# Alfred Voice Documentation 🎵

The alfred voice pack provides context-aware audio feedback for Claude Code operations.

## Overview

Alfred is a collection of 55+ contextual voice clips that play different sounds based on what Claude Code is doing. Instead of generic beeps, you hear specific sounds for reading Python files, committing to git, completing tasks, etc.

## How It Works

### Sound Mapping

The system uses three levels of sound selection:

1. **Context-Aware Patterns**: Specific file + operation combinations
   - `.py` + `Read` → `starting_python_read.mp3`
   - `.ts` + `Edit` → `starting_typescript_edit.mp3`
   - `git status` command → `starting_git_status.mp3`

2. **Tool Defaults**: Generic tool sounds when no pattern matches
   - `Read` → `file_read.mp3`
   - `Edit` → `code_edit.mp3`
   - `Bash` → `system_command.mp3`

3. **Event Sounds**: Sounds for Claude Code events
   - Task completion → `task_complete.mp3`
   - Error → `error.mp3`
   - Waiting for input → `awaiting_response.mp3`

## Complete Sound List

### File Operation Sounds
- `file_read.mp3` - Generic file reading
- `code_edit.mp3` - Generic code editing
- `starting_python_read.mp3` - Reading Python files
- `starting_python_edit.mp3` - Editing Python files
- `starting_typescript_read.mp3` - Reading TypeScript files
- `starting_typescript_edit.mp3` - Editing TypeScript files
- `starting_config_read.mp3` - Reading configuration files
- `starting_config_edit.mp3` - Editing configuration files

### Git Operation Sounds
- `starting_git_status.mp3` - Git status command
- `starting_git_commit.mp3` - Git commit
- `starting_git_diff.mp3` - Git diff
- `starting_git_staging.mp3` - Git add/staging
- `starting_git_history.mp3` - Git log

### Task Management Sounds
- `task_started.mp3` - Starting a new task
- `task_complete.mp3` - Task completed
- `updating_todo_list.mp3` - Updating todos
- `managing_tasks.mp3` - Task management operations
- `assignment_finished.mp3` - Assignment completed
- `work_finished.mp3` - Work session complete
- `work_concluded.mp3` - Work concluded

### Status & Alert Sounds
- `alert.mp3` - General alert
- `attention.mp3` - Needs attention
- `error.mp3` - Error occurred
- `notification.mp3` - General notification
- `awaiting_approval.mp3` - Waiting for approval
- `awaiting_response.mp3` - Waiting for user input
- `authorization_needed.mp3` - Authorization required
- `permission_request.mp3` - Permission requested
- `plan_ready.mp3` - Plan completed
- `request_fulfilled.mp3` - Request fulfilled

### Beginning Operation Sounds
- `beginning_changes_save.mp3`
- `beginning_config_check.mp3`
- `beginning_config_update.mp3`
- `beginning_docs_review.mp3`
- `beginning_file_staging.mp3`
- `beginning_guidance_update.mp3`
- `beginning_log_check.mp3`
- `beginning_python_access.mp3`
- `beginning_python_changes.mp3`
- `beginning_status_check.mp3`
- `beginning_typescript_access.mp3`
- `beginning_typescript_changes.mp3`
- `beginning_typescript_creation.mp3`

### Search & System Sounds
- `search.mp3` - Search operations
- `search_variation1.mp3` - Alternative search sound
- `system_command.mp3` - System commands
- `system_command_v1.mp3` - Alternative system sound
- `tracking_progress.mp3` - Progress tracking
- `waiting_for_input.mp3` - Waiting for input

### Special Operation Sounds
- `starting_instructions_read.mp3` - Reading CLAUDE.md
- `starting_instructions_edit.mp3` - Editing CLAUDE.md
- `starting_readme_read.mp3` - Reading README
- `starting_log_read.mp3` - Reading log files
- `starting_typescript_write.mp3` - Writing TypeScript files

## Configuration

### Correct Settings

```json
{
  "notifications": {
    "mode": "sounds",     // MUST be "sounds", not "voice"
    "voice": "alfred",    // lowercase "alfred"
    "sound_theme": "default"  // NOT "alfred" here
  }
}
```

### Common Mistakes

❌ **Wrong**: `"mode": "voice"` - This uses text-to-speech, not alfred sounds
❌ **Wrong**: `"voice": "Alfred"` - Must be lowercase
❌ **Wrong**: `"sound_theme": "alfred"` - Theme should be "default"

## Creating Custom Mappings

You can customize which sounds play by editing `sound_mapping.json`:

```json
{
  "alfred": {
    "patterns": {
      ".yml:Edit": "starting_config_edit",
      "Dockerfile:*": "system_command",
      "test*.py:Read": "starting_python_read"
    },
    "tools": {
      "YourCustomTool": "alert"
    }
  }
}
```

## Troubleshooting

### No Sounds Playing?

1. Check `mode` is set to `"sounds"`
2. Verify alfred sounds exist: `ls .claude/hooks/voice_notifications/sounds/alfred/`
3. Check pygame is installed: `python3 -c "import pygame"`
4. Look at debug.log for errors

### Wrong Sounds Playing?

1. Check sound_mapping.json has alfred section
2. Verify handler.py supports alfred (grep for "alfred")
3. Check pattern matching in sound_mapping.json

### Falls Back to TTS Voice?

This means `mode` is set to `"voice"` instead of `"sounds"`. The alfred pack is a collection of sound files, not a TTS voice.

## Technical Details

### Handler Requirements

The handler.py must have alfred support built in. The basic handler only supports "default" and "classic" themes. Check with:

```bash
grep "alfred" .claude/hooks/voice_notifications/handler.py
```

### File Format

All alfred sounds are MP3 files, approximately 20-50KB each. Total size is about 1.8MB for all 55+ sounds.

### Context Detection

The handler detects context from:
- File extensions (`.py`, `.ts`, `.json`)
- File names (`README`, `CLAUDE.md`, `Dockerfile`)
- Tool names (`Read`, `Edit`, `Bash`)
- Command content (`git status`, `npm install`)

This allows alfred to play the most appropriate sound for each operation.