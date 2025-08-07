# Personas Guide

Understanding and using the 11 intelligent personas in SuperClaude.

## Overview

Personas are specialized AI behavior patterns that auto-activate based on context or can be manually triggered. Each persona has unique expertise, decision frameworks, and tool preferences.

## The 11 Personas

### 🏗️ Architect
**System architecture specialist**

- **Focus**: Long-term design, scalability, maintainability
- **Auto-activates**: Architecture discussions, system design, complex refactoring
- **Best for**: System design, API architecture, database design
- **Flag**: `--persona-architect`

### 🎨 Frontend
**UI/UX and accessibility specialist**

- **Focus**: User experience, accessibility, performance
- **Auto-activates**: Component creation, UI tasks, responsive design
- **Best for**: React/Vue/Angular components, CSS, accessibility
- **Flag**: `--persona-frontend`

### ⚙️ Backend
**Server-side and reliability engineer**

- **Focus**: APIs, data integrity, reliability
- **Auto-activates**: API development, database work, server logic
- **Best for**: REST APIs, GraphQL, microservices, data processing
- **Flag**: `--persona-backend`

### 🔒 Security
**Vulnerability and threat specialist**

- **Focus**: Security, compliance, threat modeling
- **Auto-activates**: Auth implementation, security reviews, vulnerability fixes
- **Best for**: Authentication, authorization, security audits
- **Flag**: `--persona-security`

### ⚡ Performance
**Optimization specialist**

- **Focus**: Speed, efficiency, resource usage
- **Auto-activates**: Performance issues, optimization requests
- **Best for**: Performance tuning, caching, load optimization
- **Flag**: `--persona-performance`

### 🔍 Analyzer
**Root cause investigator**

- **Focus**: Evidence-based analysis, debugging
- **Auto-activates**: Bug investigation, complex debugging
- **Best for**: Troubleshooting, root cause analysis, system investigation
- **Flag**: `--persona-analyzer`

### ✅ QA
**Quality assurance specialist**

- **Focus**: Testing, quality, edge cases
- **Auto-activates**: Test creation, quality checks
- **Best for**: Test strategies, E2E testing, quality gates
- **Flag**: `--persona-qa`

### 🔧 Refactorer
**Code quality specialist**

- **Focus**: Clean code, technical debt, simplicity
- **Auto-activates**: Refactoring requests, code cleanup
- **Best for**: Code improvement, technical debt reduction
- **Flag**: `--persona-refactorer`

### 🚀 DevOps
**Infrastructure and deployment specialist**

- **Focus**: Automation, CI/CD, infrastructure
- **Auto-activates**: Deployment tasks, Docker, CI/CD
- **Best for**: Deployment pipelines, containerization, monitoring
- **Flag**: `--persona-devops`

### 📚 Mentor
**Educational and knowledge transfer specialist**

- **Focus**: Teaching, documentation, explanations
- **Auto-activates**: Learning requests, explanations
- **Best for**: Code explanations, learning paths, documentation
- **Flag**: `--persona-mentor`

### ✍️ Scribe
**Documentation and communication specialist**

- **Focus**: Clear writing, documentation, localization
- **Auto-activates**: Documentation tasks, commit messages
- **Best for**: README files, API docs, user guides
- **Flag**: `--persona-scribe=[language]`

## Auto-Activation

Personas automatically activate based on:

1. **Keywords**: Specific terms trigger relevant personas
2. **Context**: Current task and project state
3. **Complexity**: Problem complexity influences selection
4. **History**: Previous successful patterns

### Auto-Activation Examples

```bash
# "implement user authentication" → Security + Backend personas
# "create responsive navbar" → Frontend persona
# "why is this slow?" → Analyzer + Performance personas
# "document the API" → Scribe persona
# "deploy to production" → DevOps persona
```

## Manual Activation

Force specific personas with flags:

```bash
/analyze --persona-architect      # Architecture focus
/implement --persona-frontend     # UI implementation
/improve --persona-performance    # Performance optimization
```

## Persona Combinations

Personas work together for complex tasks:

### Full-Stack Feature
```bash
/implement user dashboard --persona-frontend --persona-backend
```

### Secure API
```bash
/build api --persona-backend --persona-security
```

### Performance Audit
```bash
/analyze --persona-performance --persona-architect
```

## Persona Priorities

Each persona has different priorities:

| Persona | Priority Order |
|---------|---------------|
| Architect | Maintainability > Scalability > Performance |
| Frontend | User Experience > Accessibility > Performance |
| Backend | Reliability > Security > Performance |
| Security | Security > Compliance > Usability |
| Performance | Speed > Efficiency > Simplicity |
| QA | Quality > Coverage > Speed |

## Best Practices

### 1. Let Auto-Activation Work
The system is intelligent - it usually picks the right personas automatically.

### 2. Combine for Complex Tasks
Use multiple personas for multi-faceted problems:
```bash
/analyze --persona-architect --persona-security
```

### 3. Override When Needed
If auto-activation isn't ideal, manually specify:
```bash
/implement --persona-backend  # Force backend perspective
```

### 4. Use Language-Specific Scribe
For localized documentation:
```bash
/document --persona-scribe=es  # Spanish documentation
/document --persona-scribe=ja  # Japanese documentation
```

## Persona Integration

### With MCP Servers

Each persona has preferred MCP servers:
- **Architect**: Sequential (analysis), Context7 (patterns)
- **Frontend**: Magic (UI), Playwright (testing)
- **Security**: Sequential (threat modeling)
- **Performance**: Playwright (metrics)

### With Commands

Personas enhance commands:
- `/analyze` + Architect = System-wide analysis
- `/implement` + Frontend = UI components
- `/improve` + Performance = Speed optimization
- `/test` + QA = Comprehensive test suite

### With Flags

Personas work with thinking flags:
```bash
--persona-architect --ultrathink  # Deep architectural analysis
--persona-security --validate     # Security validation
--persona-performance --loop      # Iterative optimization
```

## Advanced Usage

### Context-Aware Switching
Personas can switch mid-task:
1. Architect designs the system
2. Backend implements the API
3. Frontend creates the UI
4. QA validates everything

### Domain-Specific Activation
```yaml
frontend_triggers:
  - "component", "UI", "responsive", "accessibility"
  - Files: *.jsx, *.tsx, *.vue, *.css

backend_triggers:
  - "API", "database", "server", "endpoint"
  - Files: controllers/*, models/*, *.py, *.go

security_triggers:
  - "auth", "vulnerability", "encryption", "OWASP"
  - Files: *auth*, *security*, *.pem
```

## Troubleshooting

### Persona Not Activating
1. Check if keywords match the domain
2. Use manual flag to force activation
3. Verify with `--verbose` flag

### Wrong Persona Active
1. Manually specify the correct persona
2. Use more specific keywords
3. Combine with appropriate commands

### Multiple Personas Needed
1. Use multiple persona flags
2. Let the system coordinate them
3. Use wave mode for complex scenarios

## Tips

1. **Trust the system**: Auto-activation is usually correct
2. **Be specific**: Clear requests trigger better personas
3. **Combine wisely**: Multiple personas for complex tasks
4. **Override when needed**: Manual control is always available
5. **Learn patterns**: Observe which personas activate for your work