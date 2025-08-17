
import json
import os
from typing import List, Optional
from .models import Book

class Library:
    def __init__(self, data_file: str = "storage/library.json") -> None:
        self.data_file = data_file
        self.books: List[Book] = []
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        self.load_books()

    # --- Aşama 1: Elle ekleme ---
    def add_book_manual(self, book: Book) -> Book:
        if self.find_book(book.isbn):
            raise ValueError("Bu ISBN zaten kayıtlı.")
        self.books.append(book)
        self.save_books()
        return book

    # --- Aşama 2: Open Library'den çekerek ekleme ---
    def _fetch_book_from_openlibrary(self, isbn: str) -> Optional[Book]:
        import httpx  # lazımsa import ediyoruz
        base = "https://openlibrary.org"
        url = f"{base}/isbn/{isbn}.json"
        try:
            r = httpx.get(url, timeout=10.0)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            data = r.json()
            title = data.get("title") or "Bilinmeyen Başlık"
            # author isimlerini almak için tek tek detay endpoint'ine gidiyoruz
            names = []
            for a in data.get("authors", []):
                key = a.get("key")
                if not key:
                    continue
                ar = httpx.get(f"{base}{key}.json", timeout=10.0)
                if ar.status_code == 200:
                    names.append(ar.json().get("name"))
            author_name = ", ".join([n for n in names if n]) or "Bilinmeyen Yazar"
            return Book(title=title, author=author_name, isbn=isbn)
        except httpx.RequestError:
            return None
        except httpx.HTTPStatusError:
            return None

    def add_book(self, isbn: str) -> Optional[Book]:
        if self.find_book(isbn):
            raise ValueError("Bu ISBN zaten kayıtlı.")
        book = self._fetch_book_from_openlibrary(isbn)
        if book is None:
            return None
        self.books.append(book)
        self.save_books()
        return book

    # --- Ortak operasyonlar ---
    def remove_book(self, isbn: str) -> bool:
        before = len(self.books)
        self.books = [b for b in self.books if b.isbn != isbn]
        removed = len(self.books) != before
        if removed:
            self.save_books()
        return removed

    def list_books(self) -> List[Book]:
        return list(self.books)

    def find_book(self, isbn: str) -> Optional[Book]:
        return next((b for b in self.books if b.isbn == isbn), None)

    def load_books(self) -> None:
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump([], f)
        with open(self.data_file, "r", encoding="utf-8") as f:
            raw = json.load(f)
        self.books = [Book(**item) for item in raw]

    def save_books(self) -> None:
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([b.__dict__ for b in self.books], f, ensure_ascii=False, indent=2)
