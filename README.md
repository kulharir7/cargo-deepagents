# 🤖 DeepAgents Complete Package

> **One-Click Install** | 13 Agents + 10 MCP Plugins | Ready to Use

## 🚀 Quick Start (For New Users)

### Windows
```powershell
git clone https://github.com/YOUR_USERNAME/deepagents-complete.git
cd deepagents-complete
python install.py
```

### Linux/Mac
```bash
git clone https://github.com/YOUR_USERNAME/deepagents-complete.git
cd deepagents-complete
python install.py
```

**Done!** Everything installed in ~/.deepagents/

---

## 📦 What's Included

### 🎯 13 Specialized Agents

| Agent | Purpose | Example Usage |
|-------|---------|---------------|
| coder-agent | Write & refactor code | "Write a REST API" |
| 	ester-agent | Write tests | "Write unit tests" |
| security-agent | Security audit | "Check for SQL injection" |
| devops-agent | CI/CD & Docker | "Create Dockerfile" |
| database-agent | SQL & NoSQL | "Write SQL query" |
| pi-agent | REST & GraphQL | "Create FastAPI endpoint" |
| rontend-agent | React & Vue | "Create React component" |
| docs-agent | Documentation | "Write README" |
| esearch-agent | Web research | "Research best practices" |
| planner-agent | Architecture | "Create project roadmap" |
| debug-agent | Debug errors | "Fix this error" |
| ase-agent | Foundation | Base class for agents |
| main-agent | Orchestrator | Routes to specialists |

### 🔌 10 MCP Plugins (90+ Tools)

| Plugin | Tools | Description |
|--------|-------|-------------|
| desktop-mcp | 11 | Keyboard, Mouse, Screen |
| database-mcp | 13 | SQLite, PostgreSQL, MongoDB |
| git-mcp | 16 | Git operations |
| docker-mcp | 16 | Container management |
| cloud-mcp | 5 | AWS, GCP, Azure |
| rowser-mcp | 6 | Web automation |
| pi-mcp | 5 | REST, GraphQL |
| calendar-mcp | 5 | Google/Outlook Calendar |
| email-mcp | 5 | Email operations |
| ile-mcp | 8 | File operations |

---

## 📖 Usage Examples

### Using Agents

```python
# Ask coder agent
deepagents coder --task "Write a Python function to merge sorted arrays"

# Ask security agent
deepagents security --task "Audit this code for vulnerabilities"

# Ask database agent
deepagents database --task "Create an optimized SQL query for user orders"
```

### Using MCP Plugins

```python
# File operations
file_read(path="config.yaml")
file_write(path="output.txt", content="Hello World")

# Database operations
sqlite_connect(path="data.db")
sqlite_query(query="SELECT * FROM users")

# Git operations
git_status(repo=".")
git_commit(repo=".", message="Add feature")

# Docker operations
docker_ps(all=True)
docker_run(image="nginx", ports=["8080:80"])
```

---

## ⚙️ Configuration

Edit ~/.deepagents/config.toml:

```toml
[models]
default = "glm-5:cloud"  # or "openai:gpt-4", "anthropic:claude-3"

[mcp.desktop]
enabled = true

[mcp.database]
enabled = true

# ... more plugins
```

---

## 📁 Directory Structure

After installation:

``
~/.deepagents/
├── config.toml              # Your configuration
├── agent/
│   └── skills/              # 13 Agent SKILL.md files
│       ├── api-agent/
│       ├── coder-agent/
│       └── ...
├── mcp/                     # 10 MCP Plugins
│   ├── desktop-mcp/
│   ├── database-mcp/
│   └── ...
└── cli.py                   # CLI wrapper
```

---

## 🔧 Requirements

- Python 3.8+
- pip

Dependencies (auto-installed):
- mcp>=1.0.0
- psycopg2-binary (PostgreSQL)
- pymongo (MongoDB)
- requests

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit Pull Request

---

## 📝 License

MIT License - Use freely for any project.

---

## 🙏 Credits

- Inspired by [LangSmith Skills](https://github.com/langchain-ai/langsmith-skills)
- Built with MCP (Model Context Protocol)
- Compatible with various LLM providers

---

**Made with ❤️ for Developers**


## 🔥 NEW: PageIndex Integration (98.7% RAG Accuracy)

PageIndex is now integrated for high-accuracy document retrieval!

### Why PageIndex?
- **98.7% accuracy** on FinanceBench
- **No vector database** required
- **No chunking** needed
- **Reasoning-based retrieval**
- **Always provides citations**

### Document Agent

`ash
# Index a PDF
deepagents run document-agent --task "Index report.pdf and answer questions"

# Search documents
deepagents run document-agent --task "Search for revenue in annual_report.pdf"

# Get citations
deepagents run document-agent --task "Get citation for page 5 of report.pdf"
`

### PageIndex MCP Plugin

`python
# Index documents
index_pdf(pdf_path="report.pdf", doc_name="my_report")
index_md(md_path="guide.md", doc_name="user_guide")

# Search with reasoning
search(query="What is the revenue?", top_k=5)

# Retrieve pages
retrieve_page(doc_name="my_report", page_number=5)

# Get citations
get_citation(doc_name="my_report", page_number=5, format="apa")
`

## 📦 Complete Package

| Feature | Count |
|---------|-------|
| Agents | 14 (NEW: document-agent) |
| Plugins | 11 (NEW: pageindex-mcp) |
| Tools | 100+ |
| Accuracy | 98.7% |
