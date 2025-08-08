---
description: Initialize a complete Claude Code project with agents, hooks, and configurations
argument-hint: "(no arguments needed)"
allowed-tools: Write, Edit, Read, Bash, Glob, Grep, LS, TodoWrite
---

# Initialize Custom Claude Code Project

You are tasked with setting up a complete Claude Code project environment with all the bells and whistles - agents, hooks, voice notifications, and proper configuration.

## ⚠️ STOP - MANDATORY FIRST CHECK ⚠️

Before doing ANYTHING else, you MUST check if `.claude` directory already exists using Bash:

```bash
# RUN THIS BASH COMMAND FIRST - NO EXCEPTIONS:
Bash command="[ -d .claude ] && echo 'EXISTS' || echo 'NOT_FOUND'"
```

## DECISION TREE BASED ON BASH OUTPUT:

### IF OUTPUT IS "EXISTS":
→ `.claude` directory EXISTS - Enter UPDATE MODE
→ Say: "📦 Found existing .claude/ directory. Checking for missing components..."
→ Use LS to check contents: `LS path=".claude"`
→ Only add missing components, don't recreate existing files

### IF OUTPUT IS "NOT_FOUND":
→ `.claude` directory MISSING - Enter FRESH INSTALL MODE  
→ Say: "🆕 No .claude/ directory found. Creating fresh setup..."
→ Create complete new setup from scratch

## ⚠️ IMPORTANT: LS CANNOT SEE HIDDEN DIRECTORIES ⚠️
The LS tool in Claude Code cannot see hidden directories (those starting with a dot like `.claude`).
That's why we MUST use the Bash command above to check if `.claude` exists.

## DO NOT:
- Use LS to check if .claude exists (it won't show hidden directories!)
- Check project type first
- Look for package.json first
- Make assumptions about the directory
- Skip the Bash check

## ALWAYS:
- Run the Bash command `[ -d .claude ] && echo 'EXISTS' || echo 'NOT_FOUND'` FIRST
- Base your decision ONLY on whether Bash outputs "EXISTS" or "NOT_FOUND"

## Your Mission

Set up a fully-configured `.claude/` directory in the current project with:
1. All standard agents (5 core agents)
2. Voice notification hooks with sounds
3. Proper settings and permissions
4. Project documentation
5. Required dependencies

## Step-by-Step Process

### 1. Check Current State & Mode Selection
**CRITICAL - USE BASH TO CHECK (LS doesn't show hidden directories!)**:
```bash
# THIS IS YOUR FIRST ACTION - RUN THIS BASH COMMAND:
Bash command="[ -d .claude ] && echo 'EXISTS' || echo 'NOT_FOUND'"
```

**DECISION BASED ON BASH OUTPUT**:

**If output is "EXISTS" → UPDATE MODE**:
- Say EXACTLY: "📦 Found existing .claude/ directory. Checking for missing components..."
- Check all components systematically:
  ```bash
  # Check subdirectories
  LS path=".claude"
  LS path=".claude/agents"
  LS path=".claude/hooks/voice_notifications/sounds/alfred"
  
  # IMPORTANT: Check if CLAUDE.md exists
  Bash command="[ -f CLAUDE.md ] && echo 'CLAUDE_EXISTS' || echo 'CLAUDE_MISSING'"
  ```
- Count and compare:
  - Agents: Should have 5 files (prd-writer.md, python-backend-dev.md, etc.)
  - Alfred sounds: Should have 55+ MP3 files (not empty directory)
  - Settings files: settings.json and settings.local.json
  - CLAUDE.md: Note if it exists or not for final message
- Report what's missing: "Missing: alfred sounds (0 of 55 files), 2 agents"
- Only add missing components, preserve existing files

**If output is "NOT_FOUND" → FRESH INSTALL MODE**:
- Say EXACTLY: "🆕 No .claude/ directory found. Creating fresh setup..."
- Create complete new setup from scratch
- Check project type by looking for: package.json, pyproject.toml, requirements.txt, Cargo.toml, go.mod
- Note the project structure for later suggestions

**WHY BASH WORKS**: The `[ -d .claude ]` bash test command can detect hidden directories that LS cannot see!

### 2. Handle Existing or Create New Structure

**For EXISTING setups (Update/Merge Mode)**:
Must check each component systematically using LS:
```bash
# Check agents
LS path=".claude/agents"
# Compare output with required: prd-writer.md, python-backend-dev.md, 
# react-typescript-specialist.md, system-architect.md, ui-designer.md

# Check alfred sounds
LS path=".claude/hooks/voice_notifications/sounds/alfred"
# Count files - should have 55+ MP3 files, not just empty directory

# Check settings
LS path=".claude"
# Look for settings.json and settings.local.json
```

Display checklist to user:
```
Checking existing setup:
✓ settings.json exists
✓ settings.local.json exists
✗ Missing: alfred voice sounds (found 0, need 55+ files)
✗ Missing: 2 agents (system-architect.md, ui-designer.md)
✓ hooks/voice_notifications exists
```

- For each missing component, add it without touching existing files
- For settings.json conflicts:
  - If hooks are missing: Add them
  - If hooks differ: Ask "Your hooks differ from standard setup. Keep yours (y) or update (n)?"
- Never overwrite existing agents or CLAUDE.md without asking

**For NEW setups (Fresh Install Mode)**:
Create the complete structure:
```
.claude/
├── settings.json
├── settings.local.json
├── CLAUDE.md
├── agents/
│   ├── CLAUDE.md
│   ├── prd-writer.md
│   ├── python-backend-dev.md
│   ├── react-typescript-specialist.md
│   ├── system-architect.md
│   └── ui-designer.md
├── commands/
│   └── create-agent.md
└── hooks/
    ├── common/
    │   ├── __init__.py
    │   ├── enums.py
    │   └── utils.py
    └── voice_notifications/
        ├── __init__.py
        ├── handler.py
        ├── sound_mapping.json
        ├── README.md
        └── sounds/
            ├── alfred/ (55+ voice files)
            ├── themes/
            │   ├── default/ (12 sound files)
            │   ├── classic/ (2 sound files)
            │   └── system/ (empty)
            ├── chime.mp3
            └── ding.wav
```

### 3. Copy Core Files

Copy these files from the global Claude configuration or reference project:

**Agents** (search for sources in this order):
1. GitHub: Download from claude-code-custom-init repository (most reliable)
2. Global: `~/.claude/agents/`
3. Reference projects: Search with `find ~/Repos -path "*/.claude/agents/*.md" 2>/dev/null | head -20`
4. If found, copy all 5 standard agents listed above

**Commands** (search for sources in this order):
1. GitHub: Download from claude-code-custom-init repository (most reliable)
2. Global: `~/.claude/commands/create-agent.md`
3. Reference projects: Search with `find ~/Repos -path "*/.claude/commands/create-agent.md" 2>/dev/null | head -1`
4. Copy `create-agent.md` from the first available source

**Hook System** (find and copy from a reference source):
First, try to locate a reference project with complete alfred setup:
```bash
# Option 1: Download from GitHub (RECOMMENDED)
echo "📥 Downloading alfred voice pack from GitHub..."
curl -L https://github.com/sergimiral/claude-code-custom-init/archive/main.zip -o /tmp/claude-init.zip
unzip -q /tmp/claude-init.zip -d /tmp/
cp -r /tmp/claude-code-custom-init-main/.claude/hooks/* .claude/hooks/
rm -rf /tmp/claude-init.zip /tmp/claude-code-custom-init-main

# Option 2: Check if there's a global reference
[ -d ~/.claude/reference/hooks ] && echo "FOUND_GLOBAL"

# Option 3: Check current user's repos for existing setup
find ~/Repos -name ".claude" -type d 2>/dev/null | head -5
# Look for projects that have .claude/hooks/voice_notifications/sounds/alfred/
```

**STREAMLINED: Copy Pre-built Components**

Simply copy the working templates that include everything needed:

```bash
# Find template source (repository or reference location)
TEMPLATE_SOURCE=$(find ~/Repos -path "*claude-code-custom-init*/.claude/templates" -type d 2>/dev/null | head -1)
if [ -z "$TEMPLATE_SOURCE" ]; then
  TEMPLATE_SOURCE=$(find ~/Repos -path "*/.claude/templates" -type d 2>/dev/null | head -1)
fi

# Copy pre-built hook system with alfred support
mkdir -p .claude/hooks/voice_notifications
if [ -n "$TEMPLATE_SOURCE" ]; then
  cp "$TEMPLATE_SOURCE/handler.py" .claude/hooks/voice_notifications/handler.py
  cp "$TEMPLATE_SOURCE/sound_mapping.json" .claude/hooks/voice_notifications/sound_mapping.json
  echo "✅ Copied pre-built handler and sound mapping"
fi

# Copy common utilities (if they exist)
if [ -d .claude/hooks/common ]; then
  echo "✅ Common utilities already exist"
else
  # Copy from reference or create minimal
  mkdir -p .claude/hooks/common
  # Copy from a working reference project
  SOURCE=$(find ~/Repos -path "*/.claude/hooks/common" -type d 2>/dev/null | head -1)
  if [ -n "$SOURCE" ]; then
    cp -r "$SOURCE"/* .claude/hooks/common/
  fi
fi

# Copy or reference existing sound files
if [ -d .claude/hooks/voice_notifications/sounds/alfred ]; then
  echo "✅ Alfred sounds already exist ($(ls .claude/hooks/voice_notifications/sounds/alfred/*.mp3 2>/dev/null | wc -l) files)"
else
  # Try to find existing alfred sounds
  SOURCE=$(find ~/Repos -path "*/sounds/alfred" -type d 2>/dev/null | head -1)
  if [ -n "$SOURCE" ]; then
    cp -r "$(dirname "$SOURCE")" .claude/hooks/voice_notifications/sounds
    echo "✅ Copied alfred sounds from existing project"
  else
    echo "⚠️  Alfred sounds not found. Voice will use basic sounds."
    mkdir -p .claude/hooks/voice_notifications/sounds/alfred
  fi
fi
```

**Sound Mapping Documentation**:
The alfred voice provides context-aware sounds for different operations:
- **File Operations**: Different sounds for reading Python vs TypeScript vs config files
- **Git Operations**: Unique sounds for status, commit, diff, staging
- **Task Management**: Sounds for starting tasks, completing them, updating todos
- **Alerts**: Special attention sounds when user input is needed
- **Errors**: Distinct error sound for failures

Users can create custom voices by:
1. Creating a new folder in `sounds/` (e.g., `sounds/jarvis/`)
2. Adding MP3/WAV files with the same names as alfred sounds
3. Setting `"voice": "jarvis"` in settings.json
4. The system will use their custom sounds for matching events

**IMPORTANT PATH ADJUSTMENTS**:
- In `settings.json`, all hook commands must use: `uv run .claude/hooks/voice_notifications/handler.py`
- The handler.py imports must reference the local common module
- Sound paths must be relative to the project

### 4. Configure Settings (Using Pre-built Templates)

Copy pre-built settings template:
```bash
# Find template source (repository or reference location)
TEMPLATE_SOURCE=$(find ~/Repos -path "*claude-code-custom-init*/.claude/templates" -type d 2>/dev/null | head -1)
if [ -z "$TEMPLATE_SOURCE" ]; then
  TEMPLATE_SOURCE=$(find ~/Repos -path "*/.claude/templates" -type d 2>/dev/null | head -1)
fi

if [ -n "$TEMPLATE_SOURCE" ]; then
  # Copy complete settings.json template
  cp "$TEMPLATE_SOURCE/settings.json" .claude/settings.json
  
  # Create run-hook script
  mkdir -p .claude/bin
  cp "$TEMPLATE_SOURCE/bin/run-hook.sh" .claude/bin/run-hook.sh
  chmod +x .claude/bin/run-hook.sh
  echo "✅ Copied settings and run-hook script from templates"
else
  echo "⚠️  Templates not found. Using fallback configuration."
  # Fallback: create minimal settings manually
fi
```

The template contains:
```json
{
  "permissions": {
    "allow": [],
    "deny": []
  },
  "notifications": {
    "mode": "sounds",
    "voice": "alfred",
    "sound_theme": "default",
    "quiet_hours": false,
    "_comment": "alfred is a sound pack - use mode='sounds' and voice='alfred' (lowercase)",
    "_available_modes": "voice (full speech), sounds (simple audio), off (silent)",
    "_available_themes": "default (generic sounds), classic (ding/chime), system (macOS)",
    "_available_voices_for_mode_voice": "Zoe (Premium), Jamie (Premium), albert, daniel, samantha",
    "_available_sound_packs_for_mode_sounds": "alfred (context-aware clips), default, classic"
  },
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/voice_notifications/handler.py"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/voice_notifications/handler.py"
          }
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/voice_notifications/handler.py"
          }
        ]
      }
    ]
  }
}
```

Create `settings.local.json`:
```json
{
  "permissions": {
    "allow": [
      "Bash(plutil:*)",
      "Bash(say:*)",
      "Bash(find:*)",
      "Bash(ls:*)",
      "Bash(mkdir:*)",
      "Bash(cp:*)",
      "Bash(uv init:*)",
      "Bash(uv add:*)"
    ],
    "deny": []
  }
}
```

### 5. Handle CLAUDE.md (Project Context)

**IMPORTANT**: CLAUDE.md is the project-specific context file that helps Claude understand your project.

**Decision Logic**:
- **If CLAUDE.md exists**: NEVER overwrite it - it contains custom project context
- **If CLAUDE.md doesn't exist**: Do NOT create it automatically
  
**Why not auto-create CLAUDE.md?**
- It should contain project-specific context, not generic content
- Better created through `/init` command or manually by the user
- Auto-generated content would be low-value placeholder text

**Recommended approach**:
```
"📝 No CLAUDE.md found. After this setup completes, run:
   /init - To create CLAUDE.md with project-specific context
   
Or create it manually with your project's:
- Architecture decisions
- Coding standards  
- Key components
- Development workflow"
```

### 6. Verify Alfred Voice Configuration

**CRITICAL STEP**: After copying files, verify alfred voice will work:

**Step 1: Verify handler.py supports alfred**:
```bash
# Check if handler.py has alfred support
Grep pattern="alfred|context.*aware.*pattern" path=".claude/hooks/voice_notifications/handler.py"
# If no matches, the handler doesn't support alfred!
# You MUST copy the advanced handler from the reference project
```

**Step 2: Verify sound_mapping.json has alfred mappings**:
```bash
# Check if sound_mapping.json has alfred section
Read file_path=".claude/hooks/voice_notifications/sound_mapping.json"
# Look for "alfred" key in the JSON

# If alfred section is missing, add it using Edit tool
# The alfred mappings are essential for the voice to work!
```

**Step 3: Verify settings.json configuration**:
```bash
# The settings should use:
# "mode": "sounds" (NOT "voice" - alfred is a sound pack, not TTS)
# "voice": "alfred" (lowercase)
# NOT "sound_theme": "alfred" - that's incorrect
```

**If handler.py doesn't support alfred**:
- The basic handler only supports "default" and "classic" themes
- You need the advanced handler with context-aware pattern matching
- Solutions:
  1. Look for another project with alfred support: `find ~/Repos -path "*/.claude/hooks/voice_notifications/handler.py" -exec grep -l "alfred" {} \;`
  2. Download from GitHub (if available): `curl -o handler.py [github_raw_url]`
  3. Manual fix: Add alfred support to handler by implementing context-aware pattern matching
  4. Fallback: Use "default" or "classic" themes until alfred handler is available

### 7. Configure MCP Servers (Optional)

Check if project needs MCP configuration:
```bash
# Check if .mcp.json exists
Bash command="[ -f .mcp.json ] && echo 'MCP_EXISTS' || echo 'MCP_MISSING'"
```

**If MCP_MISSING and it's a new project**:
- Ask: "Would you like to configure project-specific MCP servers? (y/n)"
- If yes, copy template:
  ```bash
  cp .claude/templates/mcp.json .mcp.json
  ```
- Inform user: "Created .mcp.json template. Edit it to add project-specific MCP servers."
- Note: "Global MCP servers (like playwright) are already configured in ~/.claude/settings.json"

**If MCP_EXISTS**:
- Say: "✓ Project MCP configuration found (.mcp.json)"

### 8. Install Dependencies (Isolated Environment)

Create isolated Python environment and install pygame:
```bash
# Create virtual environment inside .claude
python3 -m venv .claude/.venv

# Install pygame in isolation (no project pollution)
.claude/.venv/bin/pip install pygame --quiet

echo "✅ Python environment created: .claude/.venv/"
echo "✅ pygame installed in isolated environment"
```

This keeps all Python dependencies inside .claude/ without affecting your project.

### 9. Analyze and Suggest

After setup, analyze the project:

**For existing projects with code**:
- Look at the technology stack
- Suggest relevant custom agents based on:
  - API endpoints found → "api-endpoint-tester"
  - Database models → "database-migrator"
  - Frontend components → "component-generator"
  - Tests present → "test-coverage-analyzer"
  - Docker/K8s → "devops-automator"

**For empty projects**:
- Suggest starting points based on common patterns
- Mention `/build` command for quick starts
- Suggest creating first agent with `/create-agent`

### 10. Final Message

**For Fresh Install**:
```
✅ Claude Code project initialized successfully!

Setup includes:
• 5 standard agents (prd-writer, system-architect, ui-designer, python-backend-dev, react-typescript-specialist)
• Voice notifications with alfred voice (55+ contextual sounds)
• Create-agent command for custom agents
• Complete hook system with common utilities

Next steps:
1. Run /init to create CLAUDE.md with project context
2. [If existing code: "Based on your {technology} project, consider creating: {suggested agents}"]
3. [If empty project: "Ready to start building! Try /build to create your first component"]

🎵 Voice notifications are enabled. You'll hear sounds as I work!
💡 Create custom agents anytime with: /create-agent [name] [specialty]

📝 Recommended: Add Claude files to .gitignore:
   .claude/
   CLAUDE.md  
   .mcp.json

Quick add: echo -e '\n# Claude AI\n.claude/\nCLAUDE.md\n.mcp.json' >> .gitignore
```

**For Update/Merge**:
```
✅ Claude Code setup updated successfully!

Added/Updated:
• [List what was added, e.g., "✓ Added missing alfred voice sounds (55 files)"]
• [e.g., "✓ Added 2 missing agents: system-architect, ui-designer"]
• [e.g., "✓ Updated hooks configuration"]
• [e.g., "✓ Fixed sound_mapping.json with alfred voice mappings"]

Preserved:
• [Only list items that actually exist, e.g., "Your existing agents"]
• [Don't mention CLAUDE.md if it doesn't exist]

[If CLAUDE.md check returned "CLAUDE_MISSING":]
📝 No CLAUDE.md found - This is important!
   
Next step: Run /init to create CLAUDE.md with project-specific context
   
CLAUDE.md helps Claude understand:
- Your project's architecture and structure
- Coding standards and conventions
- Key components and their relationships
- Development workflow and guidelines

🎵 Voice notifications ready with alfred voice!
💡 Run /init next to complete your setup with project context.

📝 Recommended: Add Claude files to .gitignore:
   .claude/
   CLAUDE.md  
   .mcp.json

Quick add: echo -e '\n# Claude AI\n.claude/\nCLAUDE.md\n.mcp.json' >> .gitignore
```

## Important Implementation Notes

1. **Always use relative paths** in settings.json hooks
2. **Copy files, don't reference global paths** (except for reference/fallback)
3. **Check for uv availability** before using it
4. **Preserve existing CLAUDE.md** if it exists (ask before overwriting)
5. **Be smart about suggestions** - analyze the actual code present

## Error Handling

- If files already exist: Ask whether to backup, merge, or skip
- If uv not available: Provide pip alternative instructions
- If copy fails: Try to download from a GitHub repo as fallback
- Always provide clear error messages and recovery steps

## Common Issues & Fixes

### Alfred Voice Not Working
**Symptoms**: Falls back to TTS voice instead of playing alfred sounds

**Causes & Solutions**:
1. **Wrong handler.py version**: 
   - Basic handler doesn't support alfred
   - Solution: Copy advanced handler from reference project
   - Check: `grep "alfred" handler.py` should find matches

2. **Incorrect settings.json**:
   - Using `"mode": "voice"` instead of `"mode": "sounds"`
   - Solution: Set `"mode": "sounds"` and `"voice": "alfred"`
   - NOT `"sound_theme": "alfred"` - that's wrong

3. **Missing alfred mappings in sound_mapping.json**:
   - File doesn't have "alfred" section
   - Solution: Add the alfred mappings manually

4. **Sound files missing**:
   - Alfred folder empty or incomplete
   - Solution: Copy all 55+ MP3 files from reference

## Creating a Portable Reference Bundle

For sharing or distribution, create a reference bundle:
```bash
# Create a reference directory in global Claude config
mkdir -p ~/.claude/reference
cp -r .claude/agents ~/.claude/reference/
cp -r .claude/commands ~/.claude/reference/
cp -r .claude/hooks ~/.claude/reference/

# Or create a zip bundle for sharing
zip -r claude-alfred-bundle.zip .claude/agents .claude/commands .claude/hooks
```

This way, `/init-custom` can look for:
1. `~/.claude/reference/` (standard location)
2. `~/Downloads/claude-alfred-bundle.zip` (downloaded bundle)
3. Any project in `~/Repos` with complete setup

## Sound System Documentation

### How Sounds Map to Actions

The voice notification system uses `sound_mapping.json` to map Claude Code events to specific sounds. Here's how it works:

**Event Types**:
- `PreToolUse`: Before a tool runs (e.g., before reading a file)
- `PostToolUse`: After a tool completes (rarely used)
- `Stop`: When Claude finishes a response
- `Notification`: Special notifications

**Smart Context Mapping**:
The system is context-aware and chooses sounds based on:
1. **Tool + File Type**: Reading a Python file plays `starting_python_read.mp3`
2. **Tool + Operation**: Git status plays `starting_git_status.mp3`
3. **Tool Generic**: If no specific match, uses category sound (e.g., `search.mp3` for Grep)
4. **Event Default**: Falls back to event-specific defaults

**Alfred Voice Sound Categories**:
- **beginning_***: Starting operations (config check, file staging, etc.)
- **starting_***: Beginning specific file/tool operations
- **assignment_finished**: Task completion
- **awaiting_***: Waiting for user input/approval
- **attention/alert**: User attention needed
- **error**: Operation failed
- **work_finished/work_concluded**: Session/task complete

### Creating Custom Voices

To create your own voice pack:

1. **Create Voice Folder**: `.claude/hooks/voice_notifications/sounds/myvoice/`

2. **Required Sound Files** (minimum for basic operation):
   - `file_read.mp3` - Reading files
   - `code_edit.mp3` - Editing code
   - `search.mp3` - Searching/grepping
   - `system_command.mp3` - Running bash commands
   - `task_complete.mp3` - Finishing tasks
   - `error.mp3` - Errors
   - `alert.mp3` - Attention needed

3. **Optional Context-Aware Sounds** (for richer experience):
   - Language-specific: `starting_python_edit.mp3`, `starting_typescript_edit.mp3`
   - Git operations: `starting_git_status.mp3`, `starting_git_commit.mp3`
   - Config files: `starting_config_edit.mp3`, `beginning_config_check.mp3`
   - Task management: `updating_todo_list.mp3`, `managing_tasks.mp3`

4. **Activate Your Voice**:
   ```json
   {
     "notifications": {
       "mode": "sounds",
       "voice": "myvoice"
     }
   }
   ```

5. **Test Your Voice**:
   - Run any Claude Code command
   - Listen for your custom sounds
   - Check `debug.log` if sounds don't play

The alfred voice serves as a complete reference implementation with 55+ contextual sounds for nearly every Claude Code operation.

## Recommended Command Sequence

### For New Projects:
1. **`/init-custom`** - Sets up agents, hooks, sounds, configurations
2. **`/init`** - Creates CLAUDE.md with project-specific context
3. **`/create-agent [name]`** - Add project-specific agents as needed

### For Existing Projects:
1. **`/init-custom`** - Updates/adds missing components without overwriting
2. **`/init`** (if no CLAUDE.md) - Creates project context file
3. Review and customize as needed

### Why This Order?
- `/init-custom` provides the infrastructure (agents, hooks, sounds)
- `/init` analyzes your specific project and creates meaningful context
- This separation keeps infrastructure separate from project-specific content
- Existing projects can safely run `/init-custom` to add missing features

Now, execute this initialization for the current project!