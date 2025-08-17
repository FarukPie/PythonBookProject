
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    isbn: str

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
