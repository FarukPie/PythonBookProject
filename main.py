
from library.library import Library
from library.models import Book

def menu() -> None:
    print("\n--- KÜTÜPHANE ---")
    print("1. Kitap Ekle (ISBN ile otomatik)")
    print("2. Kitap Ekle (Elle)")
    print("3. Kitap Sil")
    print("4. Kitapları Listele")
    print("5. Kitap Ara")
    print("6. Çıkış")

def run() -> None:
    lib = Library()
    while True:
        menu()
        choice = input("Seçimin: ").strip()
        if choice == "1":
            isbn = input("ISBN: ").strip()
            try:
                book = lib.add_book(isbn)
                if book:
                    print(f"Eklendi: {book}")
                else:
                    print("Kitap bulunamadı veya ağ hatası.")
            except ValueError as e:
                print(e)
        elif choice == "2":
            title = input("Başlık: ").strip()
            author = input("Yazar: ").strip()
            isbn = input("ISBN: ").strip()
            try:
                book = lib.add_book_manual(Book(title=title, author=author, isbn=isbn))
                print(f"Eklendi: {book}")
            except ValueError as e:
                print(e)
        elif choice == "3":
            isbn = input("Silinecek ISBN: ").strip()
            if lib.remove_book(isbn):
                print("Silindi.")
            else:
                print("Bulunamadı.")
        elif choice == "4":
            books = lib.list_books()
            if not books:
                print("Hiç kitap yok.")
            for b in books:
                print("-", b)
        elif choice == "5":
            isbn = input("Aranan ISBN: ").strip()
            b = lib.find_book(isbn)
            print(b if b else "Bulunamadı.")
        elif choice == "6":
            print("Görüşürüz!")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    run()
