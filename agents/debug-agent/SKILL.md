---
name: debug-agent
description: "INVOKE THIS SKILL for debugging tasks. Triggers: 'debug', 'error', 'fix', 'issue', 'not working'."
---

<oneliner>
Debug agent for error analysis, root cause investigation, and fix implementation.
</oneliner>

<setup>
## Debug Tools
- Error message analysis
- Stack trace reading
- Log inspection
- Reproduction steps
- Breakpoint debugging
</setup>

<workflow>
## Debug Process
1. **Identify** - Read error message carefully
2. **Locate** - Find in code
3. **Reproduce** - Create minimal case
4. **Analyze** - Understand root cause
5. **Fix** - Implement solution
6. **Verify** - Test fix works
7. **Document** - Prevent recurrence
</workflow>

<common_errors>
## Common Errors

**TypeError: 'NoneType' object is not iterable**
`python
# Cause: Function returning None instead of list
# Fix: Add None check
result = get_items() or []
for item in result:
    process(item)
`

**KeyError: 'key'**
`python
# Cause: Missing key in dict
# Fix: Use .get() with default
value = data.get('key', 'default')
`

**ImportError: No module named 'X'**
`python
# Cause: Missing dependency
# Fix: Install package
pip install X
`

**IndexError: list index out of range**
`python
# Cause: Accessing non-existent index
# Fix: Check length first
if i < len(items):
    return items[i]
`
</common_errors>

<debugging_pattern>
`python
import logging
logger = logging.getLogger(__name__)

def debug_issue(data):
    # Add logging
    logger.debug(f"Input: {data}")
    
    try:
        result = process(data)
        logger.debug(f"Output: {result}")
        return result
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        raise
`
</debugging_pattern>

<tips>
1. Read error message carefully
2. Check the stack trace
3. Reproduce with minimal case
4. Fix root cause, not symptoms
5. Add regression test
6. Document the fix
</tips>

<triggers>
- 'debug', 'error', 'fix this'
- 'issue', 'problem', 'not working'
- 'Exception', 'Traceback', 'failed'
</triggers>
