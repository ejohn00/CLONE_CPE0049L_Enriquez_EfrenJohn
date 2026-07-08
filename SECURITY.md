ENRIQUEZ, EFREN JOHN 08/07/2026 MIGRATION REPORT

# SECURITY REPORT

## Dependency Pinning

All third-party dependencies are pinned to exact versions.

Example:

```
PyJWT==2.10.1
requests==2.32.3
bcrypt==4.2.0
```

This prevents unexpected behavior caused by automatic package updates.

---

## Mock Vulnerability Scan

The following potential issues were identified during a simulated security review.

| Package | Possible Risk | Recommendation |
|----------|---------------|----------------|
| requests | Older versions may contain security fixes | Keep updated |
| PyJWT | Weak secret keys may allow token forgery | Use strong secret keys |
| bcrypt | Low work factor weakens password security | Use recommended rounds |

---

## Security Recommendations

- Use HTTPS
- Store JWT secret in environment variables
- Validate all user input
- Pin dependency versions
- Regularly update packages


User
   |
   | Login (username/password)
   |
Server
   |
   | Verify credentials
   |
Generate JWT Token
   |
Return Token
   |
Client stores token
   |
Future Requests
   |
Authorization: Bearer <token>