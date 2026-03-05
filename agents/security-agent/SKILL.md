---
name: security-agent
description: "INVOKE THIS SKILL for security analysis. Triggers: 'security', 'vulnerability', 'OWASP', 'audit', 'penetration test'."
---

<oneliner>
Security expert for vulnerability analysis, code audits, and security best practices.
</oneliner>

<setup>
## Security Tools
`ash
pip install bandit safety
npm install -g npm-audit
`

## OWASP Top 10 Checklist
- Injection
- Broken Auth
- Sensitive Data
- XXE
- Broken Access
- Security Misconfig
- XSS
- Insecure Deserialization
- Known Vulnerabilities
- Insufficient Logging
</setup>

<vulnerabilities>
## Common Vulnerabilities

### SQL Injection
`python
# BAD
query = f"SELECT * FROM users WHERE id = {user_input}"

# GOOD
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_input,))
`

### XSS
`python
# BAD
return f"<div>{user_input}</div>"

# GOOD
from markupsafe import escape
return f"<div>{escape(user_input)}</div>"
`

### Path Traversal
`python
# BAD
path = os.path.join(base, user_input)

# GOOD
path = os.path.join(base, os.path.basename(user_input))
if not os.path.abspath(path).startswith(os.path.abspath(base)):
    raise SecurityError("Path traversal")
`
</vulnerabilities>

<checklist>
## Security Checklist
- [ ] Input validation
- [ ] Output encoding
- [ ] Parameterized queries
- [ ] Auth/Authorization
- [ ] Session management
- [ ] Cryptography
- [ ] Error handling
- [ ] Logging/Monitoring
- [ ] Secrets management
</checklist>

<tips>
- Never trust user input
- Principle of least privilege
- Defense in depth
- Fail securely
- Log security events
</tips>

<triggers>
- 'security', 'vulnerability', 'OWASP'
- 'audit', 'penetration test', 'exploit'
</triggers>
