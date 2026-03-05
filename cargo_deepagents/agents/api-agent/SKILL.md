---
name: api-agent
description: "INVOKE THIS SKILL for API development. Triggers: 'API', 'REST', 'GraphQL', 'endpoint', 'swagger', 'OpenAPI'."
---

<oneliner>
API specialist for REST, GraphQL, and WebSocket services with comprehensive documentation.
</oneliner>

<setup>
## Quick Start
`ash
# Python
pip install fastapi uvicorn

# Node.js
npm install express
`
</setup>

<rest>
`python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="My API", version="1.0.0")

class Item(BaseModel):
    name: str
    price: float

# CRUD Endpoints
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(404, "Not found")
    return items[item_id]

@app.post("/items/")
async def create_item(item: Item):
    new_id = len(items) + 1
    items[new_id] = item.dict()
    return {"id": new_id, **item.dict()}
`
</rest>

<graphql>
`python
import strawberry

@strawberry.type
class User:
    id: int
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        return get_user_from_db(id)

schema = strawberry.Schema(query=Query)
`
</graphql>

<best_practices>
## API Best Practices

1. **Versioning**
`python
@app.get("/v1/items")  # Version in path
# or
@app.get("/items", headers={"API-Version": "v1"})
`

2. **Error Handling**
`python
class APIError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

@app.exception_handler(APIError)
async def api_error(request, exc):
    return JSONResponse(
        status_code=exc.code,
        content={"error": exc.message}
    )
`

3. **Rate Limiting**
`python
from slowapi import Limiter
limiter = Limiter(key_func=get_user_id)

@app.get("/api/data")
@limiter.limit("100/hour")
async def get_data():
    return data
`
</best_practices>

<tips>
1. Use proper HTTP status codes
2. Document all endpoints (OpenAPI)
3. Implement rate limiting
4. Add authentication
5. Handle errors gracefully
6. Use pagination for lists
</tips>

<triggers>
- 'API', 'REST', 'GraphQL', 'endpoint'
- 'swagger', 'OpenAPI', 'webhook'
- 'FastAPI', 'Express', 'Flask'
</triggers>
