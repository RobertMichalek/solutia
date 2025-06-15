from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()
BOOKS_FILE = "books.json"


# Definice Book modelu podle dat ve tvém JSON
class Book(BaseModel):
    title: str
    price: float


# Inicializace souboru, pokud neexistuje
def initialize_books_file():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w") as f:
            json.dump([], f)


# Načtení knih ze souboru
def load_books() -> List[dict]:
    with open(BOOKS_FILE, "r") as f:
        return json.load(f)


# Uložení knih do souboru
def save_books(books: List[dict]):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)


# Inicializace souboru při startu aplikace
initialize_books_file()


# CREATE - přidání nové knihy
@app.post("/books/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    books = load_books()

    # Kontrola, zda již kniha s daným názvem neexistuje (volitelné)
    if any(b["title"].lower() == book.title.lower() for b in books):
        raise HTTPException(status_code=400, detail="Book with this title already exists")

    books.append(book.dict())
    save_books(books)
    return book


# READ ALL - získání všech knih
@app.get("/books/", response_model=List[Book])
def read_all_books():
    return load_books()


# READ ONE - získání knihy podle titulu
@app.get("/books/{title}", response_model=Book)
def read_book_by_title(title: str):
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# UPDATE - aktualizace knihy podle titulu
@app.put("/books/{title}", response_model=Book)
def update_book(title: str, updated_book: Book):
    books = load_books()
    for index, book in enumerate(books):
        if book["title"].lower() == title.lower():
            books[index] = updated_book.dict()
            save_books(books)
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


# DELETE - smazání knihy podle titulu
@app.delete("/books/{title}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(title: str):
    books = load_books()
    for index, book in enumerate(books):
        if book["title"].lower() == title.lower():
            del books[index]
            save_books(books)
            return
    raise HTTPException(status_code=404, detail="Book not found")


# Root endpoint pro základní kontrolu
@app.get("/")
def root():
    return {"message": "Welcome to the Book API"}
