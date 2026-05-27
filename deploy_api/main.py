from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
    x: float
    y: float

app = FastAPI()

@app.get("/")
async def index():
    return {
        "message": "Hello World"
    }

@app.post("/")
async def cluc(data: Data):
    z = data.x * data.y
    return {"result": z}