---
name: document-agent
description: "INVOKE THIS SKILL for document processing and RAG retrieval. Triggers: 'document', 'PDF', 'index', 'search', 'retrieve', 'RAG', 'citation', 'PageIndex'."
---

<oneliner>
Document processing agent with PageIndex integration for high-accuracy RAG retrieval (98.7% accuracy, no vector DB needed).
</oneliner>

<setup>
## Dependencies
`ash
pip install pageindex-mcp
pip install pypdf openpyxl
`

## Environment
`ash
# Optional: OpenAI API for reasoning
OPENAI_API_KEY=your_key
`

## Quick Start
`ash
deepagents run document-agent --task "Index this PDF and answer questions"
`
</setup>

<capabilities>
## Document Processing
- PDF indexing and retrieval
- Markdown indexing
- URL content extraction
- Text indexing

## RAG Retrieval
- Reasoning-based search
- Page-level retrieval
- Context extraction
- Citation generation

## PageIndex Features
- 98.7% accuracy (FinanceBench)
- No vector database required
- No chunking needed
- Tree-traversal search
- Always provides citations
</capabilities>

<workflow>
## Document Workflow

### 1. Index Documents
`python
# Index PDF
index_pdf(pdf_path="report.pdf", doc_name="financial_report")

# Index Markdown
index_md(md_path="docs/guide.md", doc_name="user_guide")

# Index URL
index_url(url="https://example.com/article", doc_name="web_article")
`

### 2. Search Documents
`python
# Reasoning-based search
search(query="What are the revenue projections?", top_k=5)

# Search specific documents
search(query="Revenue trends", doc_names=["financial_report"], top_k=3)
`

### 3. Retrieve Information
`python
# Get specific page
retrieve_page(doc_name="financial_report", page_number=5)

# Get context around query
get_context(query="Revenue", context_pages=2)

# Get table of contents
get_toc(doc_name="financial_report")
`

### 4. Citations
`python
# Generate citation
get_citation(
    doc_name="financial_report",
    page_number=5,
    format="apa"  # or "mla", "chicago"
)
`
</workflow>

<examples>
## Example 1: Index and Search PDF
`python
# Index the document
result = index_pdf(pdf_path="annual_report.pdf", doc_name="annual_2024")
# Output: "Indexed PDF: annual_2024"

# Search for information
results = search(query="What is the revenue growth?", top_k=3)
# Output: [
#   {"doc": "annual_2024", "page": 12, "relevance": "high"},
#   {"doc": "annual_2024", "page": 45, "relevance": "medium"}
# ]

# Get citation
citation = get_citation(doc_name="annual_2024", page_number=12, format="apa")
# Output: "annual_2024, p.12. (APA format)"
`

## Example 2: Multi-Document Search
`python
# Index multiple documents
index_pdf(pdf_path="q1_report.pdf", doc_name="Q1")
index_pdf(pdf_path="q2_report.pdf", doc_name="Q2")

# Search across all documents
results = search(query="Revenue comparison", top_k=5)

# Get specific page from Q2
page_content = retrieve_page(doc_name="Q2", page_number=15)
`

## Example 3: Research with Citations
`python
# Index research papers
index_pdf(pdf_path="paper1.pdf", doc_name="study_A")
index_pdf(pdf_path="paper2.pdf", doc_name="study_B")

# Search with citations
results = search(query="methodology used in studies")
for result in results:
    citation = get_citation(
        doc_name=result["doc"],
        page_number=result["page"],
        format="apa"
    )
    print(f"Source: {citation}")
`
</examples>

<best_practices>
## Best Practices

1. **Document Naming**
   - Use descriptive names
   - Include dates for reports
   - Keep names short but meaningful

2. **Search Optimization**
   - Start with broad queries
   - Refine based on initial results
   - Use get_context for detailed info

3. **Citation Management**
   - Always cite sources
   - Use appropriate format
   - Include page numbers

4. **Document Organization**
   - Use get_toc to understand structure
   - Index related documents together
   - Remove outdated documents

5. **Context Retrieval**
   - Use context_pages parameter
   - Values 2-4 work well
   - More pages = more context, slower retrieval
</best_practices>

<comparison>
## PageIndex vs Traditional RAG

| Feature | PageIndex | Traditional RAG |
|---------|-----------|----------------|
| Vector DB | Not needed | Required |
| Chunking | Not needed | Required |
| Accuracy | 98.7% | 70-80% |
| Speed | Fast | Depends on DB |
| Citations | Always | Sometimes |
| Hallucination | Minimal | Common |

## Why PageIndex is Better
- No infrastructure (no vector DB)
- Higher accuracy
- Simpler deployment
- True page-level retrieval
- Reasoning-based search
</comparison>

<tips>
1. Start by indexing all relevant documents
2. Use list_docs to see available documents
3. Use specific queries for better results
4. Always cite your sources
5. Remove old documents when outdated
</tips>

<triggers>
- 'index this document', 'PDF', 'markdown', 'RAG'
- 'search documents', 'retrieve page', 'find in document'
- 'citation', 'source', 'reference'
- 'PageIndex', 'document processing', 'knowledge base'
</triggers>
