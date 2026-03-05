# Estimation Techniques Reference

## Time Estimation Methods

### 1. Three-Point Estimation

Use optimistic, pessimistic, and most likely estimates:

```
Optimistic (O): Best case scenario
Most Likely (M): Realistic scenario  
Pessimistic (P): Worst case scenario

Estimate = (O + 4M + P) / 6
```

**Example:**

```
Task: Implement user authentication

O = 4 hours (everything goes smoothly)
M = 8 hours (normal complexity)
P = 16 hours (issues, debugging)

Estimate = (4 + 4*8 + 16) / 6 = 9 hours
```

### 2. Planning Poker

Team-based estimation:

1. Each team member estimates silently
2. Reveal estimates simultaneously
3. Discuss differences
4. Converge on consensus

**Card Values:**
- 0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100, ? (story points)

### 3. T-Shirt Sizing

Quick relative estimation:

| Size | Hours | Criteria |
|------|-------|----------|
| XS | 0-2 | Trivial, no risk |
| S | 2-4 | Straightforward |
| M | 4-8 | Some complexity |
| L | 8-20 | Needs design |
| XL | 20-40 | Needs research |
| 2XL | 40+ | Requires breakdown |

### 4. Comparative Estimation

Compare to known tasks:

```
Reference: "User login" took 8 hours

New task: "Password reset"
- Similar complexity
- Same components
- Estimate: 6-8 hours

New task: "Two-factor auth"
- More complex
- New dependencies
- Estimate: 16-24 hours
```

---

## Complexity Factors

### Increases Complexity

- New technology/language
- Integration with external systems
- Performance requirements
- Security requirements
- Multi-team coordination
- Unclear requirements
- Technical debt
- Dependencies on others

### Decreases Complexity

- Familiar codebase
- Clear requirements
- Template/pattern exists
- Test coverage exists
- No external dependencies
- Experienced team

---

## Estimation Checklist

Before estimating, check:

- [ ] Requirements understood?
- [ ] Similar task done before?
- [ ] Dependencies identified?
- [ ] Technical constraints known?
- [ ] Team capacity known?
- [ ] Risk factors assessed?

---

## Common Estimation Mistakes

### 1. Optimism Bias

```
❌ "This should be quick"
✅ "This might take longer due to X"

❌ Estimate: 2 hours
✅ Estimate: 4 hours (buffer for unknowns)
```

### 2. Ignoring Non-Coding Time

```
❌ Only coding time
✅ Include: testing, review, deployment, meetings

Total = Coding + Testing + Review + Deploy + Buffer
```

### 3. Not Accounting for Context

```
❌ Same estimate for all team members
✅ Adjust for:
   - Experience level
   - Familiarity with code
   - Available time (meetings, etc.)
```

---

## Buffer Guidelines

### Standard Buffers

| Project Size | Buffer |
|-------------|--------|
| 1 day | +20% |
| 1 week | +30% |
| 2 weeks | +40% |
| 1 month | +50% |

### Uncertainty Multipliers

| Certainty Level | Multiplier |
|-----------------|------------|
| Done this exact thing | 1.0x |
| Done similar | 1.25x |
| New area, clear path | 1.5x |
| New area, unclear | 2.0x |
| Research needed | 3.0x |

---

## Velocity Tracking

### Calculate Velocity

```
Sprint 1: Planned 40 pts, Completed 35 pts
Sprint 2: Planned 40 pts, Completed 38 pts
Sprint 3: Planned 40 pts, Completed 40 pts

Average Velocity = (35 + 38 + 40) / 3 = 37.7 pts
```

### Use for Planning

```
Project: 150 story points
Team Velocity: 38 pts/sprint

Estimated Sprints = 150 / 38 = ~4 sprints

Timeline = 4 sprints = 8 weeks
```

---

## Example Estimation

### Task: Add payment processing

```
REQUIREMENTS:
- Integrate Stripe API
- Handle payments, refunds
- Store transaction history
- Send receipts

BREAKDOWN:
1. Stripe integration - 4h (familiar, docs available)
2. Payment flow - 8h (moderate complexity)
3. Refund logic - 4h (straightforward)
4. Transaction storage - 6h (new table, migrations)
5. Receipt emails - 4h (email service integration)
6. Testing - 8h (integration tests needed)
7. Review/polish - 4h

SUBTOTAL: 38h

UNCERTAINTY: New integration
BUFFER: 1.3x

FINAL ESTIMATE: 38 * 1.3 = 50h (~6-7 days)
```
