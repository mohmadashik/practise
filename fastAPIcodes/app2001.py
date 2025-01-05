from fastapi import FastAPI

app = FastAPI()

@app.get('/{name}')
async def index(name:str):
    return f'hello world {name}'

# fast api is fast to develop
# includes inbuilt data validation
# in built documentation support at /docs /redoc
# fast running performance
# less time to write code, few bugs
# pip3 install fastapi
# pip3 install uvicorn
# uvicorn app:app --reload
