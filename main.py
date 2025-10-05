from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index() -> dict[str, str]:
    return {"Hello, World"}

@app.get('/about')
async def about() -> str:
    return 'About Our Company'