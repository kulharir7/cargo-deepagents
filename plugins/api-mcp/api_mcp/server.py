"""API MCP Server - HTTP Operations"""
import asyncio
import json
import urllib.request
from typing import List, Dict, Any
from mcp.server import Server
from mcp.types import Tool, TextContent

class APIMCPServer:
    def __init__(self, name="api-mcp"):
        self.server = Server(name)
        self._setup_handlers()
    
    def _request(self, url, method="GET", headers=None, body=None, timeout=30):
        req_headers = headers or {}
        if body and "Content-Type" not in req_headers:
            req_headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, method=method, headers=req_headers)
        if body:
            req.data = body.encode("utf-8")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.status, response.read().decode("utf-8"), None
        except Exception as e:
            return 0, "", str(e)
    
    def _setup_handlers(self):
        @self.server.list_tools()
        async def list_tools():
            return [
                Tool(name="api_get", description="HTTP GET", inputSchema={"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}),
                Tool(name="api_post", description="HTTP POST", inputSchema={"type": "object", "properties": {"url": {"type": "string"}, "body": {"type": "object"}}, "required": ["url"]}),
                Tool(name="api_put", description="HTTP PUT", inputSchema={"type": "object", "properties": {"url": {"type": "string"}, "body": {"type": "object"}}, "required": ["url"]}),
                Tool(name="api_delete", description="HTTP DELETE", inputSchema={"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}),
                Tool(name="api_patch", description="HTTP PATCH", inputSchema={"type": "object", "properties": {"url": {"type": "string"}, "body": {"type": "object"}}, "required": ["url"]}),
                Tool(name="api_head", description="HTTP HEAD", inputSchema={"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}),
                Tool(name="api_graphql", description="GraphQL query", inputSchema={"type": "object", "properties": {"url": {"type": "string"}, "query": {"type": "string"}}, "required": ["url", "query"]})
            ]
        
        @self.server.call_tool()
        async def call_tool(name, arguments):
            url = arguments.get("url", "")
            headers = arguments.get("headers", {})
            if name == "api_get":
                status, body, err = self._request(url, "GET", headers)
                return [TextContent(type="text", text=json.dumps({"status": status, "body": body}, indent=2))]
            elif name == "api_post":
                body_json = json.dumps(arguments.get("body", {}))
                status, body, err = self._request(url, "POST", headers, body_json)
                return [TextContent(type="text", text=json.dumps({"status": status, "body": body}, indent=2))]
            elif name == "api_put":
                body_json = json.dumps(arguments.get("body", {}))
                status, body, err = self._request(url, "PUT", headers, body_json)
                return [TextContent(type="text", text=json.dumps({"status": status, "body": body}, indent=2))]
            elif name == "api_delete":
                status, body, err = self._request(url, "DELETE", headers)
                return [TextContent(type="text", text=json.dumps({"status": status}, indent=2))]
            elif name == "api_patch":
                body_json = json.dumps(arguments.get("body", {}))
                status, body, err = self._request(url, "PATCH", headers, body_json)
                return [TextContent(type="text", text=json.dumps({"status": status, "body": body}, indent=2))]
            elif name == "api_head":
                status, body, err = self._request(url, "HEAD", headers)
                return [TextContent(type="text", text=json.dumps({"status": status}, indent=2))]
            elif name == "api_graphql":
                query = arguments.get("query", "")
                body_json = json.dumps({"query": query})
                status, body, err = self._request(url, "POST", headers, body_json)
                return [TextContent(type="text", text=json.dumps({"status": status, "body": body}, indent=2))]
            return [TextContent(type="text", text=f"Unknown: {name}")]
    
    async def run(self):
        from mcp.server.stdio import stdio_server
        async with stdio_server() as (rs, ws):
            await self.server.run(rs, ws, {})

async def main():
    await APIMCPServer().run()

if __name__ == "__main__":
    asyncio.run(main())
