from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, create_engine, Session, select
from session_13.models import Task
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# Database connection string using Postgres container (host 'db' will be defined in docker-compose)
DATABASE_URL = "postgresql://postgres:password@db:5432/postgres"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

# ----- Logic Layer (Business Logic) -----

def create_Task_logic(session: Session, Task: Task) -> Task:
    logger.info("Creating a new Task in the database")
    session.add(Task)
    session.commit()
    session.refresh(Task)
    return Task

def update_Task_logic(session: Session, Task_id: int, new_Task: Task) -> Task:
    logger.info(f"Updating Task with id {Task_id}")
    statement = select(Task).where(Task.id == Task_id)
    existing_Task = session.exec(statement).one_or_none()
    if not existing_Task:
        raise HTTPException(status_code=404, detail="Task not found")
    existing_Task.name = new_Task.name
    existing_Task.description = new_Task.description
    session.add(existing_Task)
    session.commit()
    session.refresh(existing_Task)
    return existing_Task

def delete_Task_logic(session: Session, Task_id: int) -> dict:
    logger.info(f"Deleting Task with id {Task_id}")
    statement = select(Task).where(Task.id == Task_id)
    Task = session.exec(statement).one_or_none()
    if not Task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(Task)
    session.commit()
    return {"message": f"Task {Task_id} deleted successfully"}

def search_Task_logic(session: Session, Task_title: str) -> Task:
    logger.info(f"Searching for task/tasks with name {Task_title}")
    statement = select(Task).where(Task.name == Task_title)
    existing_Task = session.exec(statement).one_or_none()
    if not existing_Task:
        raise HTTPException(status_code=404, detail="Task not found")
    return existing_Task

# ----- API Endpoints -----

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    logger.info("Database tables created")

@app.post("/Tasks/", response_model=Task)
def create_Task(Task: Task, session: Session = Depends(get_session)):
    return create_Task_logic(session, Task)

@app.get("/Tasks/{Task_id}", response_model=Task)
def read_Task(Task_id: int, session: Session = Depends(get_session)):
    statement = select(Task).where(Task.id == Task_id)
    result = session.exec(statement)
    Task = result.one_or_none()
    if not Task:
        raise HTTPException(status_code=404, detail="Task not found")
    return Task

@app.put("/Tasks/{Task_id}", response_model=Task)
def update_Task(Task_id: int, Task: Task, session: Session = Depends(get_session)):
    return update_Task_logic(session, Task_id, Task)

@app.delete("/Tasks/{Task_id}")
def delete_Task(Task_id: int, session: Session = Depends(get_session)):
    return delete_Task_logic(session, Task_id)

@app.get("/Tasks/search/{Task_title}", response_model=list[Task])
def search_Task(Task_title: str, session: Session = Depends(get_session)):
    return search_Task_logic(session, Task_title)