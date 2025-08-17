
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library.library import Library

class BookModel(BaseModel):
    title: str
    author: str
    isbn: str

class ISBNRequest(BaseModel):
    isbn: str

app = FastAPI(title="Library API")
library = Library()

@app.get("/books", response_model=list[BookModel])
def get_books():
    return [BookModel(**b.__dict__) for b in library.list_books()]

@app.post("/books", response_model=BookModel)
def post_book(req: ISBNRequest):
    try:
        book = library.add_book(req.isbn)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    if book is None:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı veya ağ hatası.")
    return BookModel(**book.__dict__)

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    ok = library.remove_book(isbn)
    if not ok:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
    return {"status": "deleted", "isbn": isbn}
