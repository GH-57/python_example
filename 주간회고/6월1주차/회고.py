from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    price: float
    year: int


books_db = {}



@app.get("/books") # 모든 도서 목록 조회
def get_books():
    return list(books_db.values())


@app.post("/books", status_code=201) # 새 도서 목록 추가
def create_book(book: Book):
    book_id = str(uuid4())
    new_book = {"id": book_id, **book.model_dump()}
    books_db[book_id] = new_book
    return new_book


@app.get("/books/{book_id}") # 특정 도서 조회
def get_book(book_id: str):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]


@app.put("/books/{book_id}") # 도서 정보 수정
def update_book(book_id: str, updated_book: Book):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id] = {"id": book_id, **updated_book.model_dump()}
    return books_db[book_id]


@app.delete("/books/{book_id}", status_code=204) # 도서 삭제
def delete_book(book_id: str):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    del books_db[book_id]
