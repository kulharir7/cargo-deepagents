---
name: base-agent
description: "INVOKE THIS SKILL as the foundation for all other agents. Provides core capabilities, common patterns, and shared utilities. Base class for specialized agents."
---

<oneliner>
Foundation agent providing core capabilities, patterns, and utilities for all specialized agents.
</oneliner>

<setup>
## Environment Variables
`ash
DEEPAGENTS_MODEL=default        # Model selection
DEEPAGENTS_LOG_LEVEL=info      # Logging level
`

## Dependencies
`ash
pip install deepagents
`

## Quick Start
`ash
deepagents run base-agent --task "Your task here"
`
</setup>

<capabilities>
## Core Capabilities
- Task understanding and execution
- Response formatting
- Error handling
- Context management
- State tracking

## Shared Patterns
- Input validation
- Output formatting
- Progress tracking
- Result aggregation
</capabilities>

<workflow>
## Execution Flow
`
1. Receive task -> Parse and understand
2. Plan execution -> Identify steps
3. Execute steps -> Apply capabilities
4. Validate output -> Check constraints
5. Return result -> Format response
`
</workflow>

<error_handling>
## Error Patterns
`python
try:
    result = execute_task(task)
except ValidationError as e:
    return format_error("validation", e)
except ExecutionError as e:
    return format_error("execution", e)
except Exception as e:
    return format_error("unknown", e)
finally:
    cleanup_resources()
`
</error_handling>

<state_management>
## State Pattern
`python
class AgentState:
    task: str
    context: dict
    history: list
    result: any
    
    def update(self, key: str, value: any):
        self.context[key] = value
        self.history.append({key: value})
`
</state_management>

<tips>
## Important Tips
1. Always validate inputs before processing
2. Keep state minimal and focused
3. Log important state changes
4. Handle errors gracefully
5. Return structured responses
</tips>

<inheritance>
## Inheriting from Base Agent
`python
class SpecializedAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.capabilities += ['specialized_task']
    
    def execute(self, task):
        # Pre-processing
        validated = self.validate(task)
        # Core logic
        result = self.process(validated)
        # Post-processing
        return self.format(result)
`
</inheritance>
