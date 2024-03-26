from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

fake_items_db = []

@app.get('/')
async def read_root():
    return {"message":"Hello, this is Charan"}

@app.get("/items", response_model=List[Item])
async def read_items():
    return fake_items_db

@app.post('/items', response_model=Item)
async def create_item(item: Item):
    fake_items_db.append(item)
    return item