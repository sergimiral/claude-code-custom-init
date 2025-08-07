# MCP (Model Context Protocol) Configuration Guide

MCP servers extend Claude Code's capabilities with specialized tools for documentation, browser automation, complex reasoning, and more.

## Important: CLI vs GUI Configuration

Claude has two separate configuration systems:

- **Claude CLI** (`claude` command): Uses `~/.claude.json`
- **Claude Code GUI**: Uses `~/.claude/settings.json` (currently not working for MCPs)

⚠️ **Current Status**: MCP configuration in `~/.claude/settings.json` doesn't work as expected. Use the CLI method below instead.

## Configuration Hierarchy

Claude Code supports three levels of MCP configuration:

1. **User Scope** (Global) - Available across all projects
2. **Project Scope** - Shared with team via `.mcp.json`
3. **Local Scope** - Project-specific, private to you

Priority: Local > Project > User (local overrides global)

## Setting Up Global MCP Servers (CLI Method)

Use the Claude CLI to add MCP servers globally:

```bash
# Add playwright globally
claude mcp add --scope user playwright npx @playwright/mcp@latest

# Add context7 globally
claude mcp add --scope user context7 npx -y @upstash/context7-mcp -e CONTEXT7_API_TOKEN=your-token

# List configured MCPs
claude mcp list

# Remove an MCP
claude mcp remove playwright
```

These commands update `~/.claude.json` and work immediately in new Claude sessions.

## Setting Up Project MCP Servers

Create `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

Project MCP servers:
- Are shared with your team (commit to version control)
- Can use environment variables with `${VAR}` or `${VAR:-default}`
- Require user approval when first opened

## Available MCP Servers

### Browser Automation
**playwright** - Cross-browser testing and automation
```json
{
  "playwright": {
    "command": "npx",
    "args": ["@playwright/mcp@latest"]
  }
}
```

### Documentation & Code Examples
**context7** - Library documentation and patterns
```json
{
  "context7": {
    "command": "npx",
    "args": ["-y", "@upstash/context7-mcp"],
    "env": {
      "CONTEXT7_API_TOKEN": "${CONTEXT7_API_TOKEN}"
    }
  }
}
```
Get your free API token at: https://context7.ai

### Complex Reasoning
**sequentialthinking** - Multi-step problem solving
```json
{
  "sequentialthinking": {
    "type": "stdio",
    "command": "npx",
    "args": ["@modelcontextprotocol/server-sequential-thinking"]
  }
}
```

### Web Scraping
**puppeteer** - Headless browser automation
```json
{
  "puppeteer": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
  }
}
```

### Task Management
**taskmaster-ai** - Task decomposition and management
```json
{
  "taskmaster-ai": {
    "command": "npx",
    "args": ["-y", "--package=task-master-ai", "task-master-ai"],
    "env": {
      "MODEL": "claude-code/sonnet",
      "MAX_TOKENS": "64000",
      "TEMPERATURE": "0.2"
    }
  }
}
```

### GitHub Integration
**github** - Repository interaction
```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
    }
  }
}
```

### Memory & Persistence
**memory** - Cross-session memory
```json
{
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"]
  }
}
```

### File System Access
**filesystem** - Controlled directory access
```json
{
  "filesystem": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/path/to/allowed/directory"
    ]
  }
}
```

## Adding MCP Servers

### To All Projects (Global)
1. Edit `~/.claude/settings.json`
2. Add server to `mcpServers` section
3. Restart Claude Code

### To Current Project
1. Create/edit `.mcp.json` in project root
2. Add server configuration
3. Reload project or restart Claude Code

### Example: Adding Multiple Servers
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {
        "CONTEXT7_API_TOKEN": "${CONTEXT7_API_TOKEN}"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

## Environment Variables

MCP configurations support environment variable expansion:

- `${VAR}` - Uses environment variable VAR
- `${VAR:-default}` - Uses VAR or "default" if not set

Set environment variables before starting Claude Code:
```bash
export GITHUB_TOKEN="your-token-here"
export CONTEXT7_API_TOKEN="your-api-token"
claude-code
```

## Troubleshooting

### MCP Server Not Loading
1. Check JSON syntax is valid
2. Verify environment variables are set
3. Restart Claude Code after configuration changes
4. Check Claude Code logs for errors

### Server Commands Failing
1. Ensure `npx` is in your PATH
2. Check internet connection (servers download on first use)
3. Verify API tokens/credentials are correct

### Project MCP Not Working
1. Ensure `.mcp.json` is in project root
2. Accept the approval prompt when opening project
3. Check for syntax errors in JSON

## Security Best Practices

1. **Never commit API keys** - Use environment variables
2. **Review project MCPs** - Check `.mcp.json` before accepting
3. **Limit filesystem access** - Only allow necessary directories
4. **Rotate tokens regularly** - Update API keys periodically

## Quick Start Examples

### For Web Development Projects
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {
        "CONTEXT7_API_TOKEN": "${CONTEXT7_API_TOKEN}"
      }
    }
  }
}
```

### For GitHub Projects
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "sequentialthinking": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

## Further Resources

- [MCP Documentation](https://docs.anthropic.com/en/docs/claude-code/mcp)
- [MCP Server List](https://github.com/modelcontextprotocol/servers)
- [Creating Custom MCP Servers](https://modelcontextprotocol.io/docs/concepts/servers)