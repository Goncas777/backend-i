from fastapi import FastAPI
from session_12.models import Task

api = FastAPI(
    title="TODO Etic_Algarve API"
)

@api.get("/task", response_model=Task)
def list_task():
    pass

@api.post("/task")
def create_task():
    pass

@api.put("/task")
def edit_task():
    pass

@api.delete("/task")
def delete_task():
    pass

@api.patch("/task")
def close_task():
    pass
