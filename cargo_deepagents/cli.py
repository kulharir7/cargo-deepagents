#!/usr/bin/env python3
'''
Cargo DeepAgents CLI
Command line interface for DeepAgents with 13 agents and 10 MCP plugins
'''

import os
import sys
import argparse
from pathlib import Path

# Package info
VERSION = "1.0.0"
AGENTS = [
    "coder", "tester", "security", "devops", "database",
    "api", "frontend", "docs", "research", "planner",
    "debug", "base", "main"
]
PLUGINS = [
    "desktop", "database", "git", "docker", "cloud",
    "browser", "api", "calendar", "email", "file"
]

def get_skill_path(agent: str) -> Path:
    '''Get path to agent SKILL.md file'''
    home = Path.home()
    return home / ".deepagents" / "agent" / "skills" / f"{agent}-agent" / "SKILL.md"

def read_skill(agent: str) -> str:
    '''Read agent SKILL.md content'''
    path = get_skill_path(agent)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"Agent {agent} not found. Run: deepagents install"

def list_agents():
    '''List all available agents'''
    print("\\nAvailable Agents:")
    print("="*50)
    for agent in AGENTS:
        path = get_skill_path(agent)
        status = "OK" if path.exists() else "NOT INSTALLED"
        print(f"  {agent}-agent".ljust(20) + f"[{status}]")
    print()

def list_plugins():
    '''List all available plugins'''
    print("\\nAvailable Plugins:")
    print("="*50)
    for plugin in PLUGINS:
        print(f"  {plugin}-mcp")
    print()

def show_agent(agent: str):
    '''Show agent details'''
    if agent.replace("-agent", "") not in AGENTS:
        print(f"Unknown agent: {agent}")
        print(f"Available: {', '.join(AGENTS)}")
        return
    content = read_skill(agent.replace("-agent", ""))
    print(content)

def run_agent(agent: str, task: str):
    '''Run an agent with a task'''
    if agent.replace("-agent", "") not in AGENTS:
        print(f"Unknown agent: {agent}")
        return
    
    print(f"\\nRunning {agent}-agent...")
    print(f"Task: {task}")
    print("="*50)
    
    skill_content = read_skill(agent.replace("-agent", ""))
    
    # Print oneliner if available
    if "<oneliner>" in skill_content:
        start = skill_content.find("<oneliner>") + 10
        end = skill_content.find("</oneliner>")
        oneliner = skill_content[start:end].strip()
        print(f"\\nAgent: {oneliner}")
    
    print(f"\\n[Skill loaded from ~/.deepagents/agent/skills/{agent}-agent/SKILL.md]")
    print("\\n[This is a framework - connect to your LLM to process tasks]")
    print(f"\\nModel config: ~/.deepagents/config.toml")

def install_package():
    '''Install agents and plugins to user directory'''
    import shutil
    
    home = Path.home()
    target = home / ".deepagents"
    
    print("\\nInstalling Cargo DeepAgents...")
    print("="*50)
    
    # Create directories
    (target / "agent" / "skills").mkdir(parents=True, exist_ok=True)
    (target / "mcp").mkdir(parents=True, exist_ok=True)
    
    # Find package location
    try:
        import cargo_deepagents
        pkg_dir = Path(cargo_deepagents.__file__).parent
    except:
        pkg_dir = Path(__file__).parent
    
    # Copy agents
    agents_src = pkg_dir / "agents"
    if agents_src.exists():
        for agent_dir in agents_src.iterdir():
            if agent_dir.is_dir():
                dst = target / "agent" / "skills" / agent_dir.name
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(agent_dir, dst)
                print(f"  Installed: {agent_dir.name}")
    
    # Copy plugins
    plugins_src = pkg_dir / "plugins"
    if plugins_src.exists():
        for plugin_dir in plugins_src.iterdir():
            if plugin_dir.is_dir():
                dst = target / "mcp" / plugin_dir.name
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(plugin_dir, dst)
                print(f"  Installed: {plugin_dir.name}")
    
    # Copy config
    config_src = pkg_dir.parent / "config.example.toml"
    config_dst = target / "config.toml"
    if config_src.exists() and not config_dst.exists():
        shutil.copy(config_src, config_dst)
        print("  Created: config.toml")
    
    print("\\n" + "="*50)
    print("Installation complete!")
    print("\\nNext steps:")
    print("  1. Edit ~/.deepagents/config.toml")
    print("  2. Add your LLM API key")
    print("  3. Run: deepagents run coder 'your task'")
    print("="*50)

def show_config():
    '''Show current configuration'''
    config_path = Path.home() / ".deepagents" / "config.toml"
    if config_path.exists():
        print(config_path.read_text())
    else:
        print("Config not found. Run: deepagents install")

def main():
    parser = argparse.ArgumentParser(
        description="Cargo DeepAgents CLI - AI Agent System",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--version", "-v", action="version", version=f"%(prog)s {VERSION}")
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Install command
    subparsers.add_parser("install", help="Install agents and plugins")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List agents or plugins")
    list_parser.add_argument("--agents", action="store_true", help="List agents")
    list_parser.add_argument("--plugins", action="store_true", help="List plugins")
    
    # Show command
    show_parser = subparsers.add_parser("show", help="Show agent details")
    show_parser.add_argument("agent", help="Agent name (e.g., coder, tester)")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run an agent")
    run_parser.add_argument("agent", help="Agent name (e.g., coder)")
    run_parser.add_argument("task", nargs="+", help="Task description")
    
    # Config command
    subparsers.add_parser("config", help="Show configuration")
    
    args = parser.parse_args()
    
    if args.command == "install":
        install_package()
    elif args.command == "list":
        if args.plugins:
            list_plugins()
        else:
            list_agents()
    elif args.command == "show":
        show_agent(args.agent)
    elif args.command == "run":
        task = " ".join(args.task) if isinstance(args.task, list) else args.task
        run_agent(args.agent, task)
    elif args.command == "config":
        show_config()
    else:
        parser.print_help()
        print("\\nQuick Start:")
        print("  deepagents install          # Install agents")
        print("  deepagents list --agents    # List agents")
        print("  deepagents run coder 'task' # Run agent")

if __name__ == "__main__":
    main()
