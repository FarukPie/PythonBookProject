
# Kütüphane Uygulaması (Python 202 Bootcamp Projesi)

Bu repo; OOP ile terminal uygulaması, Open Library ile veri çekme ve FastAPI ile web servisi oluşturma adımlarını içeren **tamamlanmış bir başlangıç iskeleti** içerir.

## Kurulum
```bash
# 1) Sanal ortam oluştur ve etkinleştir
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Bağımlılıklar
pip install -r requirements.txt
```

## Aşama 1 — Terminal Uygulaması
```bash
python main.py
```
Menü üzerinden kitap ekleme/silme/listeleme/arama yapabilirsiniz. Veriler `storage/library.json` içinde kalıcıdır.

## Aşama 2 — ISBN ile Otomatik Ekleme
Menüde **“Kitap Ekle (ISBN ile otomatik)”** seçeneğini kullanın. İnternet yoksa veya ISBN bulunamazsa program hata fırlatmaz, açıklayıcı mesaj verir.

## Aşama 3 — FastAPI
```bash
uvicorn api:app --reload
```
Ardından tarayıcıdan `http://127.0.0.1:8000/docs` adresine gidin ve endpoint'leri deneyin.

### API Uçları
- `GET /books` — Tüm kitaplar
- `POST /books` — Body: `{ "isbn": "9780141182803" }`
- `DELETE /books/{isbn}` — ISBN'e göre siler

## Test
```bash
pytest -q
```

## Dosya Yapısı
```
library-bootcamp-project/
├─ library/
│  ├─ __init__.py
│  ├─ models.py
│  └─ library.py
├─ storage/
│  └─ library.json
├─ tests/
│  ├─ test_library.py
│  └─ test_api.py
├─ api.py
├─ main.py
├─ requirements.txt
└─ README.md
```
