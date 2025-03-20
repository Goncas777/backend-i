#Create a test file named test_main.py:
import random
from fastapi.testclient import TestClient
from session_11.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI API!"}

def test_create_item_success():
    response = client.post("/items/", json={"name": "Test Item"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Test Item"}}

def test_create_item_failure():
    response = client.post("/items/", json={"description": "No name provided"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Item must have a name"

def test_delete_item():
    item_id = random.randint(1,3)
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()== {"message": "Item deleted successfully"}