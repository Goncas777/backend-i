from fastapi import FastAPI, HTTPException
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

items = {1: 'Goncalo', 3: 'Tomas', 2: 'Troll'} 

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the FastAPI API!"}

@app.post("/items/")
async def create_item(item: dict):
    logger.info(f"Item received: {item}")
    # A simple validation example
    if "name" not in item:
        logger.error("Item does not contain 'name'")
        raise HTTPException(status_code=400, detail="Item must have a name")
    return {"item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item_name: str):
    logger.info(f"Updating item with ID: {item_id}")
    if item_id not in items.keys:
        logger.error(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item_name
    return {"item_id": item_id, "updated_item": items[item_id]}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f"Deleting item with id {item_id}")
    if item_id not in items.keys():
        logger.error(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
 
    del items[item_id]
    return {"message": "Item deleted successfully"}


# Run the application using Uvicorn with:
# poetry run uvicorn main:app --reload