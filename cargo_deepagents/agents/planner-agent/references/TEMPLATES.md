# Planning Templates

## Feature Plan Template

```
# FEATURE: [Name]

## Overview
**Goal:** [What this feature accomplishes]
**Priority:** [High/Medium/Low]
**Estimate:** [Time/Points]
**Assignee:** [Who's working on it]

## Requirements
- Functional Requirement 1
- Functional Requirement 2
- Non-functional: [Performance, Security, etc.]

## Technical Design
**Architecture:** [High-level approach]
**Components:** [Main pieces]
**Database:** [Schema changes]
**APIs:** [New endpoints]

## Implementation Phases

### Phase 1: Foundation
- [ ] Setup infrastructure
- [ ] Create base components
- [ ] Database migrations

### Phase 2: Core Logic
- [ ] Implement business logic
- [ ] Add validation
- [ ] Error handling

### Phase 3: Integration
- [ ] Connect components
- [ ] API integration
- [ ] Third-party services

### Phase 4: Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

### Phase 5: Polish
- [ ] Code review
- [ ] Documentation
- [ ] Deployment

## Dependencies
- [External dependency 1]
- [External dependency 2]

## Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk] | [H/M/L] | [How to handle] |

## Success Criteria
- [ ] All requirements met
- [ ] Tests passing
- [ ] Performance acceptable
- [ ] Code reviewed
- [ ] Deployed successfully
```

---

## Bug Fix Plan Template

```
# BUG: [Title]

## Issue Description
**Symptom:** [What user sees]
**Impact:** [How it affects users]
**Severity:** [Critical/High/Medium/Low]
**Frequency:** [Always/Sometimes/Rare]

## Root Cause Analysis
**Investigation Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Root Cause:** [What's causing the bug]
**Why it happened:** [Process/system issue]

## Fix Plan

### Step 1: Reproduce
- [ ] Create minimal reproduction
- [ ] Document reproduction steps
- [ ] Verify environment

### Step 2: Identify
- [ ] Find problematic code
- [ ] Understand the logic
- [ ] Identify affected areas

### Step 3: Fix
- [ ] Implement fix
- [ ] Code review
- [ ] Test locally

### Step 4: Verify
- [ ] Write regression test
- [ ] Test edge cases
- [ ] Integration test

### Step 5: Deploy
- [ ] Review approval
- [ ] Merge to main
- [ ] Deploy to staging
- [ ] Verify in production

## Testing Checklist
- [ ] Original issue fixed
- [ ] No new bugs introduced
- [ ] Edge cases handled
- [ ] Performance unchanged

## Prevention
**How to prevent:**
- [Code review check]
- [Test to add]
- [Process change]
```

---

## Refactoring Plan Template

```
# REFACTORING: [Component]

## Motivation
**Current Issues:**
- [Issue 1 - e.g., hard to maintain]
- [Issue 2 - e.g., slow performance]
- [Issue 3 - e.g., coupling]

**Goals:**
- [Goal 1 - e.g., improve readability]
- [Goal 2 - e.g., reduce coupling]
- [Goal 3 - e.g., add tests]

## Scope
**Files Affected:** [List]
**Components:** [List]
**Breaking Changes:** [Yes/No - details]

## Current State
```python
# Current implementation
def old_function():
    # complicated logic
    pass
```

## Target State
```python
# New implementation
class NewImplementation:
    def clean_method(self):
        # clear logic
        pass
```

## Migration Strategy

### Phase 1: Preparation
- [ ] Add comprehensive tests
- [ ] Document current behavior
- [ ] Create feature flag

### Phase 2: Implementation
- [ ] Create new implementation
- [ ] Add behind feature flag
- [ ] Migrate callers gradually

### Phase 3: Transition
- [ ] Enable for testing
- [ ] Monitor metrics
- [ ] Enable for users

### Phase 4: Cleanup
- [ ] Remove old code
- [ ] Update documentation
- [ ] Remove feature flag

## Rollback Plan
If issues arise:
1. Disable feature flag
2. Revert deployment
3. Investigate issues

## Testing Strategy
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Performance tests
- [ ] Manual testing

## Timeline
| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Prep | [X days] | None |
| Implementation | [Y days] | Tests |
| Transition | [Z days] | Implementation |
| Cleanup | [W days] | Transition |

**Total:** [Total time]
```

---

## Sprint Planning Template

```
# SPRINT: [Number] - [Dates]

## Team Capacity
| Member | Availability | Focus Factor | Capacity |
|--------|--------------|--------------|----------|
| Dev 1 | 10 days | 0.8 | 8 days |
| Dev 2 | 10 days | 0.7 | 7 days |
| **Total** | | | **15 days** |

## Sprint Goals
1. [Primary goal]
2. [Secondary goal]
3. [Stretch goal]

## Backlog Items

### Must Have (P0)
- [ ] [Item 1] - [Points] pts
- [ ] [Item 2] - [Points] pts

### Should Have (P1)
- [ ] [Item 3] - [Points] pts

### Nice to Have (P2)
- [ ] [Item 4] - [Points] pts

**Total Planned:** [Points] pts
**Velocity:** [Points] pts

## Risks
| Risk | Probability | Impact | Owner |
|------|-------------|--------|-------|
| [Risk] | [H/M/L] | [H/M/L] | [Name] |

## Dependencies
- [Dependency 1] - [Status]
- [Dependency 2] - [Status]

## Daily Standup Time
[Time] [Timezone]
```

---

## Project Roadmap Template

```
# PROJECT: [Name]

## Vision
[One sentence describing the project]

## Objectives
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

## Timeline

### Phase 1: [Name] (Week 1-2)
**Goal:** [What we achieve]
**Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
**Milestone:** [Milestone description]

### Phase 2: [Name] (Week 3-4)
**Goal:** [What we achieve]
**Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

### Phase 3: [Name] (Week 5-6)
**Goal:** [What we achieve]
**Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

## Resources
| Role | Person | Allocation |
|------|--------|-------------|
| Lead | [Name] | 100% |
| Dev | [Name] | 100% |

## Success Metrics
- [Metric 1]: [Target]
- [Metric 2]: [Target]
```
