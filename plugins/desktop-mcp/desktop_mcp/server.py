\"""
Desktop MCP Server Implementation
Provides desktop automation via PyAutoGUI.
\"""

import asyncio
import base64
from io import BytesIO
from typing import Optional, List, Dict, Any
import pyautogui
from mcp.server import Server
from mcp.types import Tool, TextContent, ImageContent

# Configure pyautogui
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1


class DesktopMCPServer:
    \"""
    MCP Server for desktop automation.
    Keyboard, Mouse, Screen operations.
    \"""
    
    def __init__(self, name: str = "desktop-mcp"):
        self.server = Server(name)
        self._setup_handlers()
    
    def _setup_handlers(self):
        \"""Setup all MCP handlers.\"""
        
        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            \"""List all available desktop automation tools.\"""
            return [
                # Keyboard Tools
                Tool(
                    name="keyboard_type",
                    description="Type text using the keyboard",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "text": {"type": "string", "description": "Text to type"},
                            "interval": {"type": "number", "description": "Interval between keystrokes", "default": 0.05}
                        },
                        "required": ["text"]
                    }
                ),
                Tool(
                    name="keyboard_press",
                    description="Press keyboard keys (e.g., enter, ctrl+c)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "keys": {"type": "string", "description": "Keys to press, use + for combinations"}
                        },
                        "required": ["keys"]
                    }
                ),
                Tool(
                    name="keyboard_hotkey",
                    description="Press keyboard hotkey combination",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "keys": {"type": "array", "items": {"type": "string"}, "description": "Keys for hotkey"}
                        },
                        "required": ["keys"]
                    }
                ),
                # Mouse Tools
                Tool(
                    name="mouse_click",
                    description="Click mouse at position",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "x": {"type": "number", "description": "X coordinate"},
                            "y": {"type": "number", "description": "Y coordinate"},
                            "button": {"type": "string", "enum": ["left", "right", "middle"], "default": "left"},
                            "clicks": {"type": "number", "description": "Number of clicks", "default": 1}
                        }
                    }
                ),
                Tool(
                    name="mouse_move",
                    description="Move mouse to coordinates",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "x": {"type": "number", "description": "X coordinate"},
                            "y": {"type": "number", "description": "Y coordinate"},
                            "duration": {"type": "number", "description": "Movement duration", "default": 0.1}
                        },
                        "required": ["x", "y"]
                    }
                ),
                Tool(
                    name="mouse_drag",
                    description="Drag mouse from one position to another",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "start_x": {"type": "number"},
                            "start_y": {"type": "number"},
                            "end_x": {"type": "number"},
                            "end_y": {"type": "number"},
                            "duration": {"type": "number", "default": 0.5}
                        },
                        "required": ["start_x", "start_y", "end_x", "end_y"]
                    }
                ),
                Tool(
                    name="mouse_scroll",
                    description="Scroll mouse wheel",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "clicks": {"type": "number", "description": "Scroll clicks (positive=up, negative=down)"}
                        },
                        "required": ["clicks"]
                    }
                ),
                Tool(
                    name="mouse_position",
                    description="Get current mouse position",
                    inputSchema={"type": "object", "properties": {}}
                ),
                # Screen Tools
                Tool(
                    name="screen_capture",
                    description="Capture screenshot",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "x": {"type": "number"},
                            "y": {"type": "number"},
                            "width": {"type": "number"},
                            "height": {"type": "number"},
                            "save_path": {"type": "string"},
                            "base64": {"type": "boolean", "default": True}
                        }
                    }
                ),
                Tool(
                    name="screen_size",
                    description="Get screen resolution",
                    inputSchema={"type": "object", "properties": {}}
                ),
                Tool(
                    name="screen_locate",
                    description="Locate an image on screen",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "image_path": {"type": "string", "description": "Path to image file"},
                            "confidence": {"type": "number", "description": "Matching confidence (0-1)", "default": 0.9}
                        },
                        "required": ["image_path"]
                    }
                ),
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent | ImageContent]:
            \"""Execute a desktop automation tool.\"""
            try:
                # Keyboard Tools
                if name == "keyboard_type":
                    text = arguments["text"]
                    interval = arguments.get("interval", 0.05)
                    pyautogui.typewrite(text, interval=interval)
                    return [TextContent(type="text", text=f"Typed: {text}")]
                
                elif name == "keyboard_press":
                    keys = arguments["keys"]
                    if "+" in keys:
                        key_list = keys.split("+")
                        pyautogui.hotkey(*key_list)
                    else:
                        pyautogui.press(keys)
                    return [TextContent(type="text", text=f"Pressed: {keys}")]
                
                elif name == "keyboard_hotkey":
                    keys = arguments["keys"]
                    pyautogui.hotkey(*keys)
                    return [TextContent(type="text", text=f"Hotkey: {'+'.join(keys)}")]
                
                # Mouse Tools
                elif name == "mouse_click":
                    x = arguments.get("x")
                    y = arguments.get("y")
                    button = arguments.get("button", "left")
                    clicks = arguments.get("clicks", 1)
                    if x is not None and y is not None:
                        pyautogui.click(x=x, y=y, button=button, clicks=clicks)
                    else:
                        pyautogui.click(button=button, clicks=clicks)
                    return [TextContent(type="text", text=f"Clicked {button} {clicks}x")]
                
                elif name == "mouse_move":
                    x, y = arguments["x"], arguments["y"]
                    duration = arguments.get("duration", 0.1)
                    pyautogui.moveTo(x, y, duration=duration)
                    return [TextContent(type="text", text=f"Moved to ({x}, {y})")]
                
                elif name == "mouse_drag":
                    sx, sy = arguments["start_x"], arguments["start_y"]
                    ex, ey = arguments["end_x"], arguments["end_y"]
                    duration = arguments.get("duration", 0.5)
                    pyautogui.moveTo(sx, sy)
                    pyautogui.drag(ex - sx, ey - sy, duration=duration)
                    return [TextContent(type="text", text=f"Dragged ({sx},{sy}) to ({ex},{ey})")]
                
                elif name == "mouse_scroll":
                    clicks = arguments["clicks"]
                    pyautogui.scroll(clicks)
                    direction = "up" if clicks > 0 else "down"
                    return [TextContent(type="text", text=f"Scrolled {direction} {abs(clicks)}")]
                
                elif name == "mouse_position":
                    x, y = pyautogui.position()
                    return [TextContent(type="text", text=f"Position: ({x}, {y})")]
                
                # Screen Tools
                elif name == "screen_capture":
                    region = None
                    if all(k in arguments for k in ["x", "y", "width", "height"]):
                        region = (arguments["x"], arguments["y"], arguments["width"], arguments["height"])
                    screenshot = pyautogui.screenshot(region=region)
                    
                    if "save_path" in arguments:
                        screenshot.save(arguments["save_path"])
                        return [TextContent(type="text", text=f"Saved to {arguments['save_path']}")]
                    
                    buffer = BytesIO()
                    screenshot.save(buffer, format="PNG")
                    img_b64 = base64.b64encode(buffer.getvalue()).decode()
                    return [ImageContent(type="image", data=img_b64, mimeType="image/png")]
                
                elif name == "screen_size":
                    w, h = pyautogui.size()
                    return [TextContent(type="text", text=f"Screen: {w}x{h}")]
                
                elif name == "screen_locate":
                    path = arguments["image_path"]
                    conf = arguments.get("confidence", 0.9)
                    loc = pyautogui.locateOnScreen(path, confidence=conf)
                    if loc:
                        return [TextContent(type="text", text=f"Found at: {loc}")]
                    return [TextContent(type="text", text="Not found")]
                
                return [TextContent(type="text", text=f"Unknown tool: {name}")]
            
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
    
    async def run(self):
        \"""Run the MCP server.\"""
        from mcp.server.stdio import stdio_server
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )


async def main():
    \"""Main entry point.\"""
    server = DesktopMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
