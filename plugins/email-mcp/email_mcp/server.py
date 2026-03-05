import asyncio
from mcp.server import Server
from mcp.types import Tool, TextContent

class EmailMCPServer:
    def __init__(self):
        self.server = Server('email-mcp')
    async def run(self): pass
