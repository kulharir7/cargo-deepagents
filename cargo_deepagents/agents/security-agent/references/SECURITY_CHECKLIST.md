# Security Checklist

## Authentication
- [ ] Strong password hashing (bcrypt/argon2)
- [ ] Session management
- [ ] Rate limiting
- [ ] MFA support
- [ ] Password reset flow

## Authorization  
- [ ] Role-based access control
- [ ] Resource-level permissions
- [ ] API endpoint protection

## Input Validation
- [ ] Sanitize all inputs
- [ ] Validate data types
- [ ] Check length limits
- [ ] Encode output

## Data Protection
- [ ] Encryption at rest
- [ ] Encryption in transit (HTTPS)
- [ ] Secrets in environment variables
- [ ] PII handling policy

## Infrastructure
- [ ] Firewall configured
- [ ] Minimal attack surface
- [ ] Regular updates
- [ ] Audit logging
