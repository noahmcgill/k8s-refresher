from fastapi import FastAPI, Depends, HTTPException, APIRouter
from .db import get_db
import pg8000
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    age: int


class ItemResponse(Item):
    id: int

    class Config:
        from_attributes = True

api_router = APIRouter(prefix="/api/v1", tags=["v1"])

@api_router.post("/items")
async def create_item(item: Item, db: pg8000.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO item (name, age) VALUES (%s, %s)",
            (item.name, item.age)
        )
        db.commit()  # Make sure to commit the transaction
        return {"message": "Item created successfully!", "name": item.name, "age": item.age}
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@api_router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: pg8000.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT id, name, age FROM item WHERE id = %s", (item_id,))
        item = cursor.fetchone()
        
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        # Return the item as a response model
        return ItemResponse(id=item[0], name=item[1], age=item[2])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
