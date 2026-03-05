# Agent Coordination Patterns

## Overview

This document describes how agents work together to handle complex requests.

## Agent Capabilities Matrix

| Capability | Main | Base | Coder | Planner |
|------------|------|------|-------|---------|
| Receive requests | ✅ | ❌ | ❌ | ❌ |
| Route to agents | ✅ | ❌ | ❌ | ❌ |
| File operations | ✅ | ✅ | ✅ | ❌ |
| Shell execution | ✅ | ✅ | ❌ | ❌ |
| Web search | ✅ | ✅ | ❌ | ❌ |
| Code generation | ✅ | ❌ | ✅ | ❌ |
| Code review | ✅ | ❌ | ✅ | ❌ |
| Debugging | ✅ | ❌ | ✅ | ❌ |
| Testing | ✅ | ❌ | ✅ | ❌ |
| Planning | ✅ | ❌ | ❌ | ✅ |
| Estimation | ✅ | ❌ | ❌ | ✅ |

## Coordination Patterns

### Pattern 1: Sequential Pipeline

Execute agents one after another:

```
Request: "Read the code and add tests"

Step 1: Main → Base Agent
  Task: Read file
  Result: Code content

Step 2: Main → Coder Agent
  Task: Write tests for code
  Context: [Code from Step 1]
  Result: Test file

Step 3: Main
  Task: Synthesize
  Result: Both files ready
```

### Pattern 2: Parallel Execution

Execute agents simultaneously:

```
Request: "Create API with docs"

Step 1: Main (parallel)
  ├─ Coder Agent: Create API
  └─ Planner Agent: Create docs outline

Step 2: Main
  Task: Combine results
  Result: API + Docs together
```

### Pattern 3: Conditional Routing

Route based on conditions:

```
Request: "Fix the bug in auth"

Step 1: Main → Base Agent
  Task: Read auth file
  Result: File content

Step 2: Main: Analyze error
  If: Simple fix needed
    → Main handles directly
  If: Complex issue
    → Route to Coder Agent

Step 3: Return result
```

### Pattern 4: Iterative Refinement

Loop until goal achieved:

```
Request: "Optimize this code"

Step 1: Main → Coder Agent
  Task: Analyze and optimize
  Result: Optimized v1

Step 2: Main → Planner Agent
  Task: Check if more optimization possible
  
Step 3: If yes, loop to Step 1
  Else, return final result
```

## Context Passing

### Between Agents

When routing between agents, pass:

```
{
  "request": "Original user request",
  "context": {
    "files": ["Currently opened files"],
    "work_done": ["Steps already completed"],
    "constraints": ["User constraints"],
    "preferences": ["User preferences"]
  },
  "partial_result": "Result from previous agent"
}
```

### Example

```
User: "Read the config and add a new setting"

Step 1: Base Agent receives:
{
  "request": "Read config file",
  "context": {
    "files": ["config.yaml"]
  }
}

Step 2: Coder Agent receives:
{
  "request": "Add new setting",
  "context": {
    "files": ["config.yaml"],
    "partial_result": "Current config content..."
  }
}
```

## Error Recovery

### Agent Fails

If an agent fails:

```
1. Catch the error
2. Log the error
3. Try fallback:
   - If Coder fails → Try Base with simpler task
   - If Planner fails → Main provides basic plan
4. If all fail → Ask user for clarification
```

### Timeout Handling

```
If agent takes too long:
  1. Cancel after timeout (default: 60s)
  2. Inform user of timeout
  3. Offer alternatives:
     - Simpler task
     - Manual steps
     - Different approach
```

## Result Synthesis

### Combining Results

From multiple agents:

```
Results from agents:
- Base Agent: "File read successfully"
- Coder Agent: "Code generated"
- Planner Agent: "Plan created"

Synthesis:
"✅ Completed all steps:
 - Read configuration file
 - Generated code based on config
 - Created implementation plan
 
 Files created:
 - config.yaml (read)
 - service.py (created)
 - plan.md (created)"
```

## Best Practices

### For Main Agent

1. Always check agent availability before routing
2. Pass complete context to specialists
3. Handle errors gracefully
4. Provide progress updates for long tasks
5. Synthesize results clearly

### For Specialist Agents

1. Accept context from Main Agent
2. Return structured results
3. Report errors with details
4. Don't route to other agents (Main handles routing)

## Example Conversation

### Complex Request

```
User: "Build a login API with tests"

Main Agent:
  "I'll break this down and coordinate multiple agents."
  
  [Routes to Planner Agent]
  "Create API architecture plan..."
  
  [Receives plan]
  "Got plan: 3 endpoints, 2 models, auth setup."
  
  [Routes to Coder Agent]
  "Implement User model..."
  "Implement Auth service..."
  "Implement Login endpoint..."
  "Write unit tests..."
  
  [Synthesizes]
  "✅ Complete! Created:
   - models/user.py
   - services/auth.py  
   - routes/login.py
   - tests/test_auth.py
   
   Tests: 8 passing
   Coverage: 95%"
```

---

*Agent Coordination v1.0*
