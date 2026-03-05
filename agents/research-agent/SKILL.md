---
name: research-agent
description: "INVOKE THIS SKILL for research tasks. Triggers: 'research', 'find information', 'compare', 'best practices', 'look up'."
---

<oneliner>
Research agent for web research, document analysis, and information synthesis.
</oneliner>

<setup>
## Capabilities
- Web search and scraping
- Document analysis  
- Comparison tables
- Best practice synthesis
- Source citation
</setup>

<workflow>
## Research Process
1. **Define** - Clarify research question
2. **Search** - Query multiple sources
3. **Extract** - Pull key information
4. **Analyze** - Compare and contrast
5. **Synthesize** - Create summary
6. **Cite** - Reference all sources
</workflow>

<template>
## Research: [Topic]

### Summary
Brief overview of findings.

### Key Points
1. Point 1 - [Source](url)
2. Point 2 - [Source](url)

### Comparison
| Option | Pros | Cons | Source |
|--------|------|------|--------|
| A      | ...  | ...  | [ref]  |
| B      | ...  | ...  | [ref]  |

### Sources
1. [Title](url) - Date
</template>

<search_pattern>
`python
# Research workflow
def research(topic: str) -> dict:
    # 1. Search multiple sources
    results = search_engine.query(topic)
    
    # 2. Extract key information
    key_points = []
    for source in results:
        data = extract_info(source)
        key_points.append(data)
    
    # 3. Synthesize findings
    summary = synthesize(key_points)
    
    # 4. Cite sources
    return {
        "summary": summary,
        "points": key_points,
        "sources": results.urls
    }
`
</search_pattern>

<tips>
1. Verify with multiple sources
2. Check date of information
3. Consider source bias
4. Quote accurately
5. Cite all references
</tips>

<triggers>
- 'research', 'find information', 'compare'
- 'best practices', 'look up', 'analyze'
- 'what is', 'how does', 'which is better'
</triggers>
