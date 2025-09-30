from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index() -> dict[str, str]:
    return {'hello': 'world'}

@app.get('/about')
async def about() -> str:
    return 'An Exceptional Company'

@app.get('/bio')
async def bio() -> list:
    return [2, 4, 6, 8]

@app.post('/add')
async def add(item):
    item_dict = item.model_dump()
    return {"message": "Item created successfully", "item": item_dict}

@app.delete('/remove', status_code = 204)
async def remove(item_id: int):
    return item_id