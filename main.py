from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

book = "Преступление и наказание"


class BookSchema(BaseModel):
    book: str
    

class BookCreateSchema(BaseModel):
    book: str


@app.get("/book")
def get_book():
    return f"Любимая книга: {book}"


@app.post("/book")
def set_book(data: BookCreateSchema):
    global book
    book = data.book
    return {"message": "Книга обновлена", "book": book}

