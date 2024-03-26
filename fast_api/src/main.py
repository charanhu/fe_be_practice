from fastapi import FastAPI

# define app
app = FastAPI()

@app.get('/')
async def read_root():
    return {"message":"Hello, I'm Charan"}

@app.get('/item/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}