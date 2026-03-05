# Base Agent Capabilities Reference

## File Operations Reference

### ls - List Directory

```
ls                    # Current directory
ls path/to/dir        # Specific directory
ls -la                # Detailed view (hidden files)
```

### read - Read File

```
read file.txt                    # Read text file
read image.png                   # Read image (returns base64)
read --limit=100 large_file.txt  # Limit lines
read --offset=50 file.txt        # Start from line 50
```

Supports: `.txt`, `.py`, `.js`, `.md`, `.json`, `.yaml`, `.png`, `.jpg`, `.gif`

### write - Create/Overwrite File

```
write path/to/file.py "content"
write --append file.txt "more content"
```

### edit - Targeted Edit

```
edit file.py "old_code" "new_code"
edit --regex file.py "pattern.*" "replacement"
```

**Important:** `oldText` must match exactly.

### glob - Find Files

```
glob **/*.py         # All Python files
glob src/**/*.js     # JS files in src
glob *test*.py       # Test files
```

### grep - Search in Files

```
grep "function" src/       # Search for 'function'
grep -r "import" .         # Recursive search
grep -i "TODO" src/        # Case-insensitive
```

---

## Shell Commands Reference

### Execution

```
!command              # Run and show output
!command arg1 arg2   # With arguments
```

### Common Commands

| Command | Purpose |
|---------|---------|
| `!python file.py` | Run Python |
| `!pip install pkg` | Install package |
| `!npm run build` | Build project |
| `!git status` | Git status |
| `!docker ps` | List containers |

### Safety

- Destructive commands require user approval
- Background commands supported
- Timeout handling for long operations

---

## Web Tools Reference

### web_search

```
web_search("query")
web_search("query", count=10)
web_search("query", country="US")
```

Returns: titles, URLs, snippets

### fetch_url

```
fetch_url("https://example.com")
fetch_url(url, extractMode="markdown")
fetch_url(url, extractMode="text")
```

Returns: Page content as markdown or text

---

## Browser Automation

### Commands

| Command | Example |
|---------|---------|
| `browser start` | Open browser |
| `browser navigate url` | Go to URL |
| `browser click selector` | Click element |
| `browser type selector text` | Type text |
| `browser screenshot` | Capture screen |
| `browser wait selector` | Wait for element |

### Selectors

```
#id           # By ID
.class        # By class
[attr=val]    # By attribute
text=Hello    # By text
```

---

## Task Management

### write_todos

```
write_todos([
  {"content": "Task 1", "status": "pending"},
  {"content": "Task 2", "status": "completed"}
])
```

### Task Delegation

```
task("Write unit tests for auth module")
task("Create API documentation", agent="coder")
```

---

*Load this reference when needing detailed tool documentation*
