"""Calendar MCP Server - Google/Outlook"""
import asyncio
import json
from datetime import datetime
from typing import List, Dict, Any
from mcp.server import Server
from mcp.types import Tool, TextContent

class CalendarMCPServer:
    def __init__(self, name="calendar-mcp"):
        self.server = Server(name)
        self.events = []
        self._setup_handlers()
    
    def _setup_handlers(self):
        @self.server.list_tools()
        async def list_tools():
            return [
                Tool(name="calendar_list_events", description="List events", inputSchema={"type": "object", "properties": {}}),
                Tool(name="calendar_create_event", description="Create event", inputSchema={"type": "object", "properties": {"summary": {"type": "string"}, "start": {"type": "string"}, "end": {"type": "string"}}, "required": ["summary", "start", "end"]}),
                Tool(name="calendar_update_event", description="Update event", inputSchema={"type": "object", "properties": {"event_id": {"type": "string"}}, "required": ["event_id"]}),
                Tool(name="calendar_delete_event", description="Delete event", inputSchema={"type": "object", "properties": {"event_id": {"type": "string"}}, "required": ["event_id"]}),
                Tool(name="calendar_free_busy", description="Free/busy", inputSchema={"type": "object", "properties": {}}),
                Tool(name="calendar_find_slots", description="Find slots", inputSchema={"type": "object", "properties": {}}),
                Tool(name="calendar_today", description="Today events", inputSchema={"type": "object", "properties": {}}),
                Tool(name="calendar_week", description="Week events", inputSchema={"type": "object", "properties": {}})
            ]
        
        @self.server.call_tool()
        async def call_tool(name, arguments):
            if name == "calendar_list_events":
                return [TextContent(type="text", text=json.dumps({"events": self.events}, indent=2))]
            elif name == "calendar_create_event":
                event_id = f"evt_{len(self.events) + 1}"
                event = {"id": event_id, "summary": arguments.get("summary", ""), "start": arguments.get("start", ""), "end": arguments.get("end", "")}
                self.events.append(event)
                return [TextContent(type="text", text=json.dumps({"status": "created", "event": event}, indent=2))]
            elif name == "calendar_update_event":
                return [TextContent(type="text", text=json.dumps({"status": "updated"}, indent=2))]
            elif name == "calendar_delete_event":
                self.events = [e for e in self.events if e.get("id") != arguments.get("event_id")]
                return [TextContent(type="text", text=json.dumps({"status": "deleted"}, indent=2))]
            elif name == "calendar_free_busy":
                return [TextContent(type="text", text=json.dumps({"busy": []}, indent=2))]
            elif name == "calendar_find_slots":
                return [TextContent(type="text", text=json.dumps({"slots": [{"start": "09:00", "end": "10:00"}]}, indent=2))]
            elif name == "calendar_today":
                return [TextContent(type="text", text=json.dumps({"date": datetime.now().isoformat(), "events": []}, indent=2))]
            elif name == "calendar_week":
                return [TextContent(type="text", text=json.dumps({"events": self.events}, indent=2))]
            return [TextContent(type="text", text=f"Unknown: {name}")]
    
    async def run(self):
        from mcp.server.stdio import stdio_server
        async with stdio_server() as (rs, ws):
            await self.server.run(rs, ws, {})

async def main():
    await CalendarMCPServer().run()

if __name__ == "__main__":
    asyncio.run(main())
