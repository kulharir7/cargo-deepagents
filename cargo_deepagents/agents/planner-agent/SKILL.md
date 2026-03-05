---
name: planner-agent
description: "INVOKE THIS SKILL for planning tasks. Triggers: 'plan', 'architecture', 'design', 'roadmap', 'milestones'."
---

<oneliner>
Planning agent for project architecture, roadmaps, and task breakdown.
</oneliner>

<setup>
## Planning Types
- Project architecture
- Task breakdown
- Sprint planning
- Roadmap creation
- Risk assessment
</setup>

<workflow>
## Planning Process
1. **Define Goals** - What to achieve
2. **Break Down** - Split into tasks
3. **Identify Dependencies** - Order of tasks
4. **Estimate Time** - Duration
5. **Assign Resources** - Who does what
6. **Plan Risks** - What could go wrong
</workflow>

<template>
## Project: [Name]

### Goals
- Primary goal
- Secondary goals

### Architecture
`mermaid
graph TD
    A[Frontend] --> B[API Gateway]
    B --> C[Service 1]
    B --> D[Service 2]
    C --> E[Database]
    D --> E
`

### Milestones
1. **Phase 1**: Setup (Week 1-2)
   - [ ] Task 1
   - [ ] Task 2
2. **Phase 2**: Core (Week 3-4)
   - [ ] Task 3
   - [ ] Task 4

### Risks
- Risk 1: Mitigation strategy
- Risk 2: Mitigation strategy
</template>

<breakdown>
`markdown
## Sprint Planning

### Sprint 1 (Week 1-2)
| Task | Est | Owner | Status |
|------|-----|-------|--------|
| Setup project | 4h | Dev A | Done |
| Create API | 8h | Dev B | In Progress |

### Dependencies
- Task 3 depends on Task 1
- Task 5 depends on Task 2, 3
`
</breakdown>

<tips>
1. Start with goals, not tasks
2. Break into phases
3. Identify dependencies early
4. Plan for risks
5. Include buffer time
6. Make tasks specific and measurable
</tips>

<triggers>
- 'plan', 'architecture', 'design'
- 'roadmap', 'breakdown', 'milestones'
- 'sprint', 'project plan', 'timeline'
</triggers>
