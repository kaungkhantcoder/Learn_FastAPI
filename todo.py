from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Minimal Sample API")

class SimpleTodo(BaseModel):
    name: str

todos_list: List[str] = ["Learn FastAPI basics", "Build a simple app"]

@app.get("/")
def read_root():
    return {"message": "Welcome to the minimal Todo API"}

@app.get("/todos")
def get_todos():
    return {"todos": todos_list}

@app.get("todos/{id}")
def get_todo_with_id():
    return {"todos": "todos_list_id"}

@app.post("/todos")
def create_todo(todo: SimpleTodo):
    todos_list.append(todo.name)

    return {
        "message": f"Task '{todo.name}' added successfully",
        "current_total": len(todos_list)
    }