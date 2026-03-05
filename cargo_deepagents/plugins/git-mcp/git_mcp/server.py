# Git MCP Server
import asyncio
import subprocess
from typing import List, Dict, Any
from mcp.server import Server
from mcp.types import Tool, TextContent

class GitMCPServer:
    def __init__(self):
        self.server = Server("git-mcp")
        self._setup_handlers()
    
    def _run_git(self, repo: str, args: List[str]):
        cmd = ["git"] + args
        result = subprocess.run(cmd, cwd=repo, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    
    def _setup_handlers(self):
        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            return [
                Tool(name="git_status", description="Show working tree status",
                    inputSchema={"type": "object", "properties": {"repo": {"type": "string"}}}),
                Tool(name="git_add", description="Add files to staging",
                    inputSchema={"type": "object", "properties": {"repo": {"type": "string"}, "files": {"type": "array"}}}),
                Tool(name="git_commit", description="Commit changes",
                    inputSchema={"type": "object", "properties": {"repo": {"type": "string"}, "message": {"type": "string"}}}),
                Tool(name="git_push", description="Push to remote",
                    inputSchema={"type": "object", "properties": {"repo": {"type": "string"}, "remote": {"type": "string"}}}),
                Tool(name="git_pull", description="Pull from remote",
                    inputSchema={"type": "object", "properties": {"repo": {"type": "string"}, "remote": {"type": "string"}}}),
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            repo = arguments.get("repo", ".")
            if name == "git_status":
                code, out, err = self._run_git(repo, ["status"])
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "git_add":
                files = arguments.get("files", ["."])
                code, out, err = self._run_git(repo, ["add"] + files)
                return [TextContent(type="text", text="Added files" if code == 0 else err)]
            elif name == "git_commit":
                msg = arguments.get("message", "Update")
                code, out, err = self._run_git(repo, ["commit", "-m", msg])
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "git_push":
                remote = arguments.get("remote", "origin")
                code, out, err = self._run_git(repo, ["push", remote])
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "git_pull":
                remote = arguments.get("remote", "origin")
                code, out, err = self._run_git(repo, ["pull", remote])
                return [TextContent(type="text", text=out if code == 0 else err)]
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
    
    async def run(self):
        from mcp.server.stdio import stdio_server
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(read_stream, write_stream, {})

async def main():
    await GitMCPServer().run()

if __name__ == "__main__":
    asyncio.run(main())
