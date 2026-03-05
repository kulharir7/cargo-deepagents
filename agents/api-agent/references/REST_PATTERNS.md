# REST Patterns

## Resource Naming

Good:
GET /users
GET /users/123
GET /users/123/orders

Bad:
GET /getUsers
GET /user?id=123

## Status Codes

200 - Success
201 - Created
204 - No Content (for DELETE)
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
422 - Validation Error
500 - Server Error

## Response Format

{
    "data": { ... },
    "meta": {
        "page": 1,
        "total": 100
    },
    "links": {
        "next": "/users?page=2",
        "prev": null
    }
}

## Error Response

{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid email format",
        "details": {...}
    }
}
