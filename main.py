from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(title="Todo API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.get("/")
def read_root():
    return {"message": "Hello World", "status": "FastAPI is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Temporary in-memory todos for testing
todos = [
    {"id": 1, "name": "Learn FastAPI", "completed": False},
    {"id": 2, "name": "Deploy to Vercel", "completed": True}
]

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return {"error": "Todo not found"}

@app.post("/todos")
def create_todo(todo_data: dict):
    new_id = max([t["id"] for t in todos]) + 1 if todos else 1
    new_todo = {
        "id": new_id,
        "name": todo_data.get("name", ""),
        "completed": todo_data.get("completed", False)
    }
    todos.append(new_todo)
    return new_todo

# Explicit ASGI application export for deployment platforms
application = app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)