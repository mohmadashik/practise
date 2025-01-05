from fastapi import FastAPI

app = FastAPI()

@app.get('/{name}')
async def index(name:str):
    return f'hello world {name}'