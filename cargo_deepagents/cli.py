#!/usr/bin/env python3
"""
Cargo DeepAgents CLI
Command line interface for DeepAgents with 14 agents and 11 MCP plugins
Version: 1.1.0
"""

import os
import sys
import argparse
from pathlib import Path

# Package info
VERSION = "1.1.0"
AGENTS = [
    "coder", "tester", "security", "devops", "database",
    "api", "frontend", "docs", "research", "planner",
    "debug", "base", "main", "document"
]
PLUGINS = [
    "pageindex", "desktop", "database", "git", "docker", 
    "cloud", "browser", "api", "calendar", "email", "file"
]

def get_workspace():
    """Get workspace directory"""
    # Use DEEPAGENTS_WORKSPACE env var or default to ~/.deepagents
    workspace = os.environ.get("DEEPAGENTS_WORKSPACE", "")
    if workspace:
        return Path(workspace)
    return Path.home() / ".deepagents"

def get_skill_path(agent: str) -> Path:
    """Get path to agent SKILL.md file"""
    workspace = get_workspace()
    return workspace / "agent" / "skills" / f"{agent}-agent" / "SKILL.md"

def read_skill(agent: str) -> str:
    """Read agent SKILL.md content"""
    path = get_skill_path(agent)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"Agent {agent} not found. Run: deepagents install"

def get_vpath(agent: str) -> str:
    """Get virtual path for display (avoids Windows path issues)"""
    return f"/workspace/.deepagents/agent/skills/{agent}-agent/SKILL.md"

def list_agents():
    """List all available agents"""
    workspace = get_workspace()
    print("\nAvailable Agents:")
    print("="*50)
    for agent in AGENTS:
        path = get_skill_path(agent)
        status = "OK" if path.exists() else "NOT INSTALLED"
        print(f"  {agent}-agent".ljust(20) + f"[{status}]")
    print(f"\nWorkspace: {workspace}")
    print()

def list_plugins():
    """List all available plugins"""
    workspace = get_workspace()
    print("\nAvailable Plugins:")
    print("="*50)
    for plugin in PLUGINS:
        plugin_path = workspace / "mcp" / f"{plugin}-mcp"
        status = "OK" if plugin_path.exists() else "NOT INSTALLED"
        print(f"  {plugin}-mcp".ljust(20) + f"[{status}]")
    print()

def show_agent(agent: str):
    """Show agent details"""
    agent_name = agent.replace("-agent", "")
    if agent_name not in AGENTS:
        print(f"Unknown agent: {agent}")
        print(f"Available: {', '.join(AGENTS)}")
        return
    
    content = read_skill(agent_name)
    print(content)
    print(f"\n[Virtual path: {get_vpath(agent_name)}]")

def run_agent(agent: str, task: str, model: str = None):
    """Run an agent with a task"""
    agent_name = agent.replace("-agent", "")
    if agent_name not in AGENTS:
        print(f"Unknown agent: {agent}")
        print(f"Available: {', '.join(AGENTS)}")
        return
    
    workspace = get_workspace()
    print(f"\n{'='*50}")
    print(f"Running: {agent_name}-agent")
    print(f"Task: {task}")
    print(f"Workspace: {workspace}")
    print(f"{'='*50}")
    
    # Load skill
    skill_content = read_skill(agent_name)
    
    # Extract oneliner
    if "<oneliner>" in skill_content:
        start = skill_content.find("<oneliner>") + 10
        end = skill_content.find("</oneliner>")
        oneliner = skill_content[start:end].strip()
        print(f"\n?? Agent: {oneliner}\n")
    
    # Extract triggers
    if "<triggers>" in skill_content:
        start = skill_content.find("<triggers>") + 10
        end = skill_content.find("</triggers>")
        triggers = skill_content[start:end].strip()
        print(f"?? Triggers: {triggers}\n")
    
    # Load config
    config_path = workspace / "config.toml"
    if config_path.exists():
        print(f"Config: {config_path}")
    
    print(f"\n[Skill loaded: {get_vpath(agent_name)}]")
    print("\n? Ready to connect to LLM")
    print("   Set model in config.toml or via --model flag")
    
    # Return info for programmatic use
    return {
        "agent": agent_name,
        "task": task,
        "skill_path": str(get_skill_path(agent_name)),
        "virtual_path": get_vpath(agent_name),
        "workspace": str(workspace)
    }

def install_package():
    """Install agents and plugins to user directory"""
    import shutil
    
    workspace = get_workspace()
    
    print("\nInstalling Cargo DeepAgents...")
    print("="*50)
    print(f"Workspace: {workspace}")
    print()
    
    # Create directories
    (workspace / "agent" / "skills").mkdir(parents=True, exist_ok=True)
    (workspace / "mcp").mkdir(parents=True, exist_ok=True)
    
    # Find package location
    try:
        import cargo_deepagents
        pkg_dir = Path(cargo_deepagents.__file__).parent
    except:
        pkg_dir = Path(__file__).parent
    
    agents_dir = pkg_dir / "agents"
    plugins_dir = pkg_dir / "plugins"
    
    # Copy agents
    if agents_dir.exists():
        for agent_dir in agents_dir.iterdir():
            if agent_dir.is_dir():
                dst = workspace / "agent" / "skills" / agent_dir.name
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(agent_dir, dst)
                print(f"  ? {agent_dir.name}")
    else:
        print("  ??  Agents directory not found")
    
    # Copy plugins
    if plugins_dir.exists():
        for plugin_dir in plugins_dir.iterdir():
            if plugin_dir.is_dir():
                dst = workspace / "mcp" / plugin_dir.name
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(plugin_dir, dst)
                print(f"  ? {plugin_dir.name}")
    else:
        print("  ??  Plugins directory not found")
    
    # Create config
    config_path = workspace / "config.toml"
    if not config_path.exists():
        config_content = """# DeepAgents Configuration
# Set your model and API keys here

[model]
provider = "openai"
name = "gpt-4"
# api_key = "your-api-key-here"

[agents]
workspace = ".deepagents"
default = "coder"

[plugins]
enabled = ["pageindex", "database", "git", "desktop"]
"""
        config_path.write_text(config_content)
        print("  ? config.toml created")
    
    print("\n" + "="*50)
    print("Installation complete!")
    print()
    print("Next steps:")
    print("  1. Edit ~/.deepagents/config.toml")
    print("  2. Add your LLM API key")
    print("  3. Run: deepagents run coder 'your task'")
    print("="*50)

def show_config():
    """Show current configuration"""
    workspace = get_workspace()
    config_path = workspace / "config.toml"
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
    parser.add_argument("--workspace", "-w", help="Workspace directory")
    parser.add_argument("--model", "-m", help="Model to use")
    
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
    
    # Set workspace if provided
    if hasattr(args, 'workspace') and args.workspace:
        os.environ["DEEPAGENTS_WORKSPACE"] = args.workspace
    
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
        run_agent(args.agent, task, args.model if hasattr(args, 'model') else None)
    elif args.command == "config":
        show_config()
    else:
        parser.print_help()
        print("\nQuick Start:")
        print("  deepagents install          # Install agents")
        print("  deepagents list --agents    # List agents")
        print("  deepagents run coder 'task' # Run agent")

if __name__ == "__main__":
    main()
