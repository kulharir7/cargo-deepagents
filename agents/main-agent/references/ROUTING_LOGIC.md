# Routing Logic Reference

## Decision Tree

### Step 1: Analyze Request Type

```
                    ┌─────────────────┐
                    │   User Request   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Analyze Intent  │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐         ┌────▼────┐        ┌────▼────┐
    │  FILE   │         │  CODE   │        │  PLAN   │
    │  OPS    │         │  TASK   │        │  TASK   │
    └────┬────┘         └────┬────┘        └────┬────┘
         │                   │                   │
         ▼                   ▼                   ▼
    BASE AGENT          CODER AGENT       PLANNER AGENT
```

### Step 2: Keyword Matching

| Keywords | Agent | Confidence |
|----------|-------|------------|
| file, read, write, edit, list, ls | base-agent | High |
| run, execute, command, shell | base-agent | High |
| search, find, web, browse | base-agent | High |
| code, implement, function, class | coder-agent | High |
| bug, fix, debug, error, exception | coder-agent | High |
| refactor, clean, optimize, improve | coder-agent | High |
| test, unit test, integration test | coder-agent | High |
| plan, roadmap, steps, phases | planner-agent | High |
| estimate, how long, timeline | planner-agent | High |
| break down, decompose, analyze | planner-agent | Medium |

### Step 3: Phrase Detection

#### Base Agent Triggers

```
Phrases:
- "read <file>"
- "write <file>"
- "edit <file>"
- "list files in"
- "run <command>"
- "execute <command>"
- "search for"
- "find on web"
```

#### Coder Agent Triggers

```
Phrases:
- "write code to"
- "implement a"
- "create a function"
- "fix the bug"
- "debug this"
- "refactor the"
- "add unit tests"
- "write tests for"
- "optimize the code"
```

#### Planner Agent Triggers

```
Phrases:
- "create a plan"
- "plan the implementation"
- "break down this task"
- "what are the steps"
- "how to approach"
- "estimate the time"
- "create a roadmap"
- "how long will it take"
```

## Ambiguity Resolution

### When Intent is Unclear

```
Score each agent:
- Base: Count matching file/shell/web keywords
- Coder: Count matching code/debug/test keywords  
- Planner: Count matching plan/estimate keywords

Select highest score.
If tie: Ask user for clarification.
```

### Example Ambiguity

```
User: "fix the config"

Analysis:
- "fix" → Coder Agent (debugging)
- "config" → Could be file operation

Scores:
- Base Agent: 1 (file operation)
- Coder Agent: 2 (fix, config issue)
- Planner Agent: 0

Decision: Route to Coder Agent
Reason: "fix" strongly suggests debugging
```

## Multi-Agent Detection

### When Multiple Agents Needed

```
Multi-agent indicators:
- "and", "then", "after that"
- "first", "second", "third"
- "also", "additionally"
- Multiple action verbs

Example: "read the file and fix the bug"
Actions: [read, fix]
Agents: [Base, Coder]
```

### Detection Algorithm

```
def detect_multi_agent(request):
    actions = extract_actions(request)
    agents = []
    
    for action in actions:
        agent = classify_action(action)
        if agent and agent not in agents:
            agents.append(agent)
    
    if len(agents) > 1:
        return SEQUENTIAL, agents
    else:
        return SINGLE, agents[0]
```

## Routing Examples

### Example 1: Simple Routing

```
Request: "read the file config.yaml"

Analysis:
- Action: read
- Object: file
- Keywords: read, file, yaml

Decision:
- Agent: base-agent
- Confidence: 100%
- Reason: Clear file operation
```

### Example 2: Code Task

```
Request: "write a function to validate email"

Analysis:
- Action: write
- Object: function
- Keywords: write, function, validate

Decision:
- Agent: coder-agent
- Confidence: 95%
- Reason: Clear code generation task
```

### Example 3: Planning Task

```
Request: "how to build a REST API"

Analysis:
- Keywords: how to, build
- Intent: Seeking guidance/plan

Decision:
- Agent: planner-agent
- Confidence: 90%
- Reason: Planning/guidance request
```

### Example 4: Multi-Agent

```
Request: "read the requirements and implement the feature"

Analysis:
- Action 1: read (base-agent)
- Action 2: implement (coder-agent)
- Sequence: Sequential

Decision:
- Type: SEQUENTIAL
- Agents: [base-agent, coder-agent]
- Order: Base first, then Coder
```

### Example 5: Ambiguous

```
Request: "do something with the database"

Analysis:
- Keywords: database
- No clear action verb
- No specific task

Decision:
- Type: CLARIFICATION_NEEDED
- Response: "What would you like to do with the database?
             (read, modify, optimize, etc.)"
```

## Fallback Rules

### When No Agent Matches

```
1. Try partial match based on nouns
2. Check conversation context
3. Use Main Agent directly
4. Ask user for clarification
```

### Priority Order

```
1. Exact keyword match → Confident routing
2. Phrase pattern match → High confidence routing
3. Partial match → Route with note
4. No match → Main Agent handles or asks
```

## Confidence Thresholds

| Score | Action |
|-------|--------|
| > 80% | Route directly |
| 60-80% | Route with explanation |
| 40-60% | Ask for confirmation |
| < 40% | Ask for clarification |

---

*Routing Logic v1.0*
