# Database MCP Server
import asyncio
import sqlite3
import json
from typing import List, Dict, Any
from mcp.server import Server
from mcp.types import Tool, TextContent

class DatabaseMCPServer:
    def __init__(self):
        self.server = Server("database-mcp")
        self.connections = {}
        self._setup_handlers()
    
    def _setup_handlers(self):
        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            return [
                Tool(name="sqlite_connect", description="Connect to SQLite database",
                    inputSchema={"type": "object", "properties": {"path": {"type": "string"}}}),
                Tool(name="sqlite_query", description="Execute SQLite query",
                    inputSchema={"type": "object", "properties": {"query": {"type": "string"}}}),
                Tool(name="sqlite_tables", description="List SQLite tables",
                    inputSchema={"type": "object", "properties": {}}),
                Tool(name="postgres_connect", description="Connect to PostgreSQL",
                    inputSchema={"type": "object", "properties": {"database": {"type": "string"}}}),
                Tool(name="postgres_query", description="Execute PostgreSQL query",
                    inputSchema={"type": "object", "properties": {"query": {"type": "string"}}}),
                Tool(name="mongo_connect", description="Connect to MongoDB",
                    inputSchema={"type": "object", "properties": {"uri": {"type": "string"}}}),
                Tool(name="mongo_find", description="Find documents in MongoDB",
                    inputSchema={"type": "object", "properties": {"collection": {"type": "string"}}}),
                Tool(name="db_disconnect", description="Disconnect from database",
                    inputSchema={"type": "object", "properties": {}}),
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            try:
                if name == "sqlite_connect":
                    path = arguments.get("path", ":memory:")
                    conn = sqlite3.connect(path)
                    conn.row_factory = sqlite3.Row
                    self.connections["default"] = {"type": "sqlite", "conn": conn}
                    return [TextContent(type="text", text=f"Connected to SQLite: {path}")]
                
                elif name == "sqlite_query":
                    if "default" not in self.connections:
                        return [TextContent(type="text", text="Error: Not connected")]
                    query = arguments.get("query", "")
                    cursor = self.connections["default"]["conn"].cursor()
                    cursor.execute(query)
                    if query.strip().upper().startswith("SELECT"):
                        rows = cursor.fetchall()
                        return [TextContent(type="text", text=json.dumps([dict(r) for r in rows]))]
                    self.connections["default"]["conn"].commit()
                    return [TextContent(type="text", text=f"Rows affected: {cursor.rowcount}")]
                
                elif name == "sqlite_tables":
                    if "default" not in self.connections:
                        return [TextContent(type="text", text="Error: Not connected")]
                    cursor = self.connections["default"]["conn"].cursor()
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                    return [TextContent(type="text", text=json.dumps([r[0] for r in cursor.fetchall()]))]
                
                elif name == "db_disconnect":
                    if "default" in self.connections:
                        self.connections["default"]["conn"].close()
                        del self.connections["default"]
                    return [TextContent(type="text", text="Disconnected")]
                
                return [TextContent(type="text", text=f"Unknown tool: {name}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
    
    async def run(self):
        from mcp.server.stdio import stdio_server
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(read_stream, write_stream, {})

async def main():
    await DatabaseMCPServer().run()

if __name__ == "__main__":
    asyncio.run(main())
