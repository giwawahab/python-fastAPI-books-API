from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)


BOOKS = [
    Book(1, "Computer Science", "Giwa Wahab", "Introduction to Computing", 5),
    Book(2, "General Studies", "Tommy Soft", "General Knowledge", 3),
    Book(3, "Engineering Basics", "Giwa Wahab", "Engineering for Beginners", 4),
    Book(4, "Music Intro", "Micheal Jackson", "Advance Music Studies", 4),
    Book(5, "Biology of Plant", "Ben Perez", "Plant Anatomy", 3),
    Book(6, "Artificial Intelligence", "Alao Tomiwa", "Beginner to Advance AI Knowledge", 5)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_abook(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book