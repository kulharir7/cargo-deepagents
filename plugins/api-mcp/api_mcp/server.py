import asyncio
from mcp.server import Server
from mcp.types import Tool, TextContent

class APIMCPServer:
    def __init__(self):
        self.server = Server('api-mcp')
    async def run(self): pass
