# 🚀 Quick Start Guide

## Installation

### Windows
```powershell
# Clone the repository
git clone https://github.com/YOUR_USERNAME/deepagents.git
cd deepagents

# Run installer
python scripts/install.py
```

### Linux/Mac
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/deepagents.git
cd deepagents

# Run installer
python scripts/install.py
```

## First Steps

### 1. Configure Model
Edit ~/.deepagents/config.toml:
```toml
[models]
default = "glm-5:cloud"  # or "openai:gpt-4"
```

### 2. Try an Agent
```bash
deepagents run coder-agent --task "Write a Python function to sort a list"
```

### 3. Use MCP Plugin
```python
# File operations
file_read(path="config.yaml")
file_write(path="output.txt", content="Hello World")
```

## Available Agents

| Agent | Purpose | Example |
|-------|---------|---------|
| coder | Write code | "Write a REST API" |
| tester | Write tests | "Write unit tests" |
| security | Security audit | "Check for SQL injection" |
| devops | Deploy | "Create Dockerfile" |
| database | SQL/NoSQL | "Write SQL query" |

## Troubleshooting

### Model Issues
- Check your API key in environment
- Verify model name in config

### Plugin Issues
- Run pip install -e ~/.deepagents/mcp/PLUGIN_NAME
- Check plugin config in config.toml

## Need Help?
- Open an issue: https://github.com/YOUR_USERNAME/deepagents/issues
- Read docs: https://github.com/YOUR_USERNAME/deepagents/wiki
