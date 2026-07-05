from fastapi import Body, FastAPI

app = FastAPI()

class Books:
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


BOOKS = [
    Books(1, "Computer Science", "Giwa Wahab", "Introduction to Computing", 5),
    Books(2, "General Studies", "Tommy Soft", "General Knowledge", 3),
    Books(3, "Engineering Basics", "Giwa Wahab", "Engineering for Beginners", 4),
    Books(4, "Music Intro", "Micheal Jackson", "Advance Music Studies", 4),
    Books(5, "Biology of Plant", "Ben Perez", "Plant Anatomy", 3),
    Books(6, "Artificial Intelligence", "Alao Tomiwa", "Beginner to Advance AI Knowledge", 5)
]


@app.get("/books")
async def read_all_books():
    return BOOKS