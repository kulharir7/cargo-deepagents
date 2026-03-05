---
name: main-agent
description: "INVOKE THIS SKILL as the primary orchestrator. Routes tasks to specialized agents and coordinates complex workflows."
---

<oneliner>
Main orchestrator agent that routes tasks to specialized agents and aggregates results.
</oneliner>

<setup>
## Available Agents
| Agent | Purpose | Priority |
|-------|---------|----------|
| coder-agent | Code tasks | 2 |
| tester-agent | Testing | 3 |
| security-agent | Security | 3 |
| devops-agent | Infrastructure | 3 |
| database-agent | Databases | 3 |
| api-agent | APIs | 3 |
| frontend-agent | UI | 3 |
| docs-agent | Documentation | 3 |
| research-agent | Research | 3 |
| planner-agent | Planning | 1 |
| debug-agent | Debugging | 2 |
| base-agent | Foundation | 1 |
</setup>

<routing>
## Task Routing Logic

\\\python
def route_task(task: str) -> Agent:
    task_lower = task.lower()
    
    # Code-related
    if any(w in task_lower for w in ['code', 'implement', 'function', 'class']):
        return coder_agent
    
    # Testing
    if any(w in task_lower for w in ['test', 'coverage', 'unit']):
        return tester_agent
    
    # Security
    if any(w in task_lower for w in ['security', 'vulnerability', 'audit']):
        return security_agent
    
    # Infrastructure
    if any(w in task_lower for w in ['deploy', 'docker', 'kubernetes', 'ci/cd']):
        return devops_agent
    
    # Database
    if any(w in task_lower for w in ['sql', 'database', 'query', 'table']):
        return database_agent
    
    # API
    if any(w in task_lower for w in ['api', 'rest', 'endpoint', 'graphql']):
        return api_agent
    
    # Frontend
    if any(w in task_lower for w in ['ui', 'react', 'vue', 'component']):
        return frontend_agent
    
    # Documentation
    if any(w in task_lower for w in ['readme', 'docs', 'guide']):
        return docs_agent
    
    # Research
    if any(w in task_lower for w in ['research', 'find', 'compare']):
        return research_agent
    
    # Planning
    if any(w in task_lower for w in ['plan', 'architecture', 'roadmap']):
        return planner_agent
    
    # Debugging
    if any(w in task_lower for w in ['debug', 'error', 'fix', 'issue']):
        return debug_agent
    
    # Default
    return base_agent
\\\
</routing>

<workflow>
## Orchestration Workflow

1. **Receive Task** - Parse user request
2. **Analyze Intent** - Determine task type
3. **Route to Agent** - Select appropriate agent
4. **Execute** - Run agent with task
5. **Review Result** - Validate output
6. **Aggregate** - Combine if multiple agents
7. **Return Response** - Format and deliver
</workflow>

<coordination>
## Multi-Agent Coordination

\\\python
async def execute_complex_task(task: str):
    # 1. Plan the approach
    plan = await planner_agent.create_plan(task)
    
    # 2. Execute in parallel where possible
    results = await asyncio.gather(
        coder_agent.execute(plan.code_tasks),
        tester_agent.execute(plan.test_tasks),
        docs_agent.execute(plan.doc_tasks)
    )
    
    # 3. Aggregate results
    return {
        "code": results[0],
        "tests": results[1],
        "docs": results[2]
    }
\\\
</coordination>

<tips>
1. Be specific in task descriptions
2. Let specialists handle details
3. Provide context when asked
4. Review aggregated results
5. Ask for clarification if needed
</tips>

<triggers>
- Any general task requiring coordination
- Multi-step workflows
- Tasks involving multiple domains
</triggers>
