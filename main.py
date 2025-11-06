
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "Worl "}   


@app.get("/greet/{name}")
async def read_item(name: str , age:int =0):
    return {"Hello": name, "age": age}