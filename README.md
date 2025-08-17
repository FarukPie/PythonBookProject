
# Kütüphane Uygulaması (Python 202 Bootcamp Projesi)

## Kurulum
```bash
# 1) Sanal ortam oluştur ve etkinleştir
python -m venv .venv
# Windows:
.venv\Scripts\activate


# 2) Bağımlılıklar
pip install -r requirements.txt
```

Terminal Uygulaması
```bash
python main.py
```
Menü üzerinden kitap ekleme/silme/listeleme/arama yapabilirsiniz. Veriler `storage/library.json` içinde kalıcıdır.

ISBN ile Otomatik Ekleme
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

