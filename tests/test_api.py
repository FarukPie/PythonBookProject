
from fastapi.testclient import TestClient
import api as api_module
from library.library import Library
from library.models import Book

def make_test_client(tmp_path, monkeypatch):
    lib = Library(data_file=str(tmp_path / "lib.json"))
    monkeypatch.setattr(api_module, "library", lib)
    return TestClient(api_module.app), lib

def test_get_books_empty(tmp_path, monkeypatch):
    client, lib = make_test_client(tmp_path, monkeypatch)
    r = client.get("/books")
    assert r.status_code == 200
    assert r.json() == []

def test_post_and_delete_book(tmp_path, monkeypatch):
    client, lib = make_test_client(tmp_path, monkeypatch)

    def fake_fetch(isbn):
        return Book(title="X", author="Y", isbn=isbn)

    monkeypatch.setattr(lib, "_fetch_book_from_openlibrary", fake_fetch)
    r = client.post("/books", json={"isbn": "111"})
    assert r.status_code == 200
    assert r.json()["isbn"] == "111"

    r2 = client.get("/books")
    assert any(b["isbn"] == "111" for b in r2.json())

    r3 = client.delete("/books/111")
    assert r3.status_code == 200
