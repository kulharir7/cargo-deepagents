#!/usr/bin/env python3
'''
DeepAgents Simple Installer
Run this after cloning the repo
'''

import os
import sys
import shutil
from pathlib import Path

def main():
    print("="*50)
    print("DeepAgents Installer")
    print("="*50)
    
    # Get paths
    script_dir = Path(__file__).parent
    home = Path.home()
    target = home / ".deepagents"
    
    print(f"\nInstalling to: {target}")
    
    # Create directories
    target.mkdir(parents=True, exist_ok=True)
    (target / "agent" / "skills").mkdir(parents=True, exist_ok=True)
    (target / "mcp").mkdir(parents=True, exist_ok=True)
    
    # Copy agents
    print("\n[1/3] Installing agents...")
    agents_dir = script_dir / "agents"
    if agents_dir.exists():
        for agent in agents_dir.iterdir():
            if agent.is_dir():
                dst = target / "agent" / "skills" / agent.name
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(agent, dst)
                print(f"  ✓ {agent.name}")
    
    # Copy plugins
    print("\n[2/3] Installing plugins...")
    plugins_dir = script_dir / "plugins"
    if plugins_dir.exists():
        for plugin in plugins_dir.iterdir():
            if plugin.is_dir():
                dst = target / "mcp" / plugin.name
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(plugin, dst)
                print(f"  ✓ {plugin.name}")
    
    # Copy config
    print("\n[3/3] Setting up config...")
    config_src = script_dir / "config.example.toml"
    config_dst = target / "config.toml"
    if config_src.exists():
        shutil.copy(config_src, config_dst)
        print("  ✓ config.toml")
    
    # Done
    print("\n" + "="*50)
    print("Installation Complete!")
    print("="*50)
    print("\nNext steps:")
    print("  1. Edit ~/.deepagents/config.toml")
    print("  2. Add your API key")
    print("  3. Use agents with your LLM")
    print("\nAgents location: ~/.deepagents/agent/skills/")
    print("Plugins location: ~/.deepagents/mcp/")
    print("="*50)

if __name__ == "__main__":
    main()
