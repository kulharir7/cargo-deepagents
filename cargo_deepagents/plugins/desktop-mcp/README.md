# Desktop MCP Server

A Model Context Protocol (MCP) server for desktop automation using PyAutoGUI.

## Features

### Keyboard Tools
- keyboard_type - Type text
- keyboard_press - Press keys
- keyboard_hotkey - Press hotkey combinations

### Mouse Tools
- mouse_click - Click at position
- mouse_move - Move to coordinates
- mouse_drag - Drag from A to B
- mouse_scroll - Scroll wheel
- mouse_position - Get current position

### Screen Tools
- screen_capture - Take screenshot
- screen_size - Get screen resolution
- screen_locate - Find image on screen

## Installation

```bash
pip install desktop-mcp
```

## Usage with Claude Desktop

Add to claude_desktop_config.json:

```json
{
  ""mcpServers"": {
    ""desktop"": {
      ""command"": ""python"",
      ""args"": [""-m"", ""desktop_mcp""]
    }
  }
}
```

## Example Usage

### Keyboard
- Type ""Hello World""
- Press Ctrl+C
- Hotkey: Ctrl+Shift+Esc

### Mouse
- Click at (100, 200)
- Move to (1920/2, 1080/2)
- Scroll up 5 clicks

### Screen
- Capture screenshot
- Get screen resolution
- Find button.png on screen

## License

MIT
