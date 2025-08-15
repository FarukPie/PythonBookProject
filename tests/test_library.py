
import json
import os
from library.library import Library
from library.models import Book

def test_add_list_remove(tmp_path):
    data_file = tmp_path / "lib.json"
    lib = Library(data_file=str(data_file))
    assert lib.list_books() == []
    b = Book(title="Test", author="Ben", isbn="123")
    lib.add_book_manual(b)
    assert lib.find_book("123") is not None
    assert len(lib.list_books()) == 1
    assert os.path.exists(data_file)
    assert json.loads(data_file.read_text(encoding="utf-8"))[0]["isbn"] == "123"
    lib.remove_book("123")
    assert lib.find_book("123") is None


