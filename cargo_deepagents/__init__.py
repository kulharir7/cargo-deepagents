'''
Cargo DeepAgents
AI Agent System with 13 specialized agents and 10 MCP plugins
'''

__version__ = "1.0.0"
__author__ = "kulharir7"

# Agent names
AGENTS = [
    "coder-agent", "tester-agent", "security-agent", "devops-agent",
    "database-agent", "api-agent", "frontend-agent", "docs-agent",
    "research-agent", "planner-agent", "debug-agent", "base-agent",
    "main-agent"
]

# Plugin names
PLUGINS = [
    "desktop-mcp", "database-mcp", "git-mcp", "docker-mcp",
    "cloud-mcp", "browser-mcp", "api-mcp", "calendar-mcp",
    "email-mcp", "file-mcp"
]

from .cli import main

__all__ = ["AGENTS", "PLUGINS", "main"]
