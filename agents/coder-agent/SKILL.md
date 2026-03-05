---
name: coder-agent
description: "INVOKE THIS SKILL when: (1) Writing new code, (2) Refactoring, (3) Debugging, (4) Writing tests. Triggers: 'write code', 'implement', 'fix bug', 'refactor', 'add tests'."
---

<oneliner>
Expert coder for code generation, refactoring, debugging, testing across all languages.
</oneliner>

<setup>
Environment:
- Optional: OPENAI_API_KEY, ANTHROPIC_API_KEY
- Dependencies: pytest (Python), jest (JS), etc.

Quick Start:
`ash
deepagents run coder-agent --task "Write REST API in FastAPI"
`
</setup>

<capabilities>
- Multi-language: Python, JS, TS, Go, Rust, Java, C++
- Frameworks: React, Django, FastAPI, Express, Spring
- Clean Architecture, SOLID, DRY principles
- Design patterns implementation
</capabilities>

<workflow>
1. Understand Requirements - Read code, identify needs
2. Plan Implementation - Design approach, list files
3. Write Code - Follow conventions, handle errors
4. Test & Validate - Write/run tests, check edge cases
5. Document - Add docstrings, update README
</workflow>

<python>
`python
from typing import Optional, List

def process_data(items: List[dict]) -> List[dict]:
    '''Process data with clean code patterns.'''
    return [{**item, 'processed': True} for item in items]
`
</python>

<typescript>
`	ypescript
interface User {
  id: string;
  name: string;
}

async function fetchUser(id: string): Promise<User> {
  const response = await fetch('/api/users/' + id);
  return response.json();
}
`
</typescript>

<tips>
- Read existing code first
- Run tests before/after changes
- Keep functions small (<50 lines)
- Handle all errors properly
- Use meaningful names
- Add comments for 'why', not 'what'
</tips>

<triggers>
- 'write code', 'implement', 'fix bug'
- 'refactor', 'add tests', 'debug'
- 'code review', 'optimize'
</triggers>
