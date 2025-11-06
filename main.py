
from fastapi import FastAPI
from pydantic import BaseModel
from data.books import books  # 👈 import your data
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "Worl "}   


@app.get("/greet/{name}")
async def read_item(name: str , age:int =0):
    return {"Hello": name, "age": age}


# post request 
# Step 1: Define a data model
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True  # optional, default value

# Step 2: Create POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "Item created successfully!",
        "item_data": item
    }

# -----------------------CRUD on books----------------------



@app.get("/books")
def get_books():
    return {
        "result": books
    }


class Book(BaseModel):
    title: str
    author:str
    publisher: str
    publish_date: str
    page_count: int
    language: str


@app.post("/books")
def create_book(book:Book):
    new_book = book.model_dump()
    new_book["id"] = len(books) +1 
    books.append(new_book)
    return {
        "result" : books
    }