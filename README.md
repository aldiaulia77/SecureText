# SecureText — Super Encryption Web Application

Aplikasi web kriptografi berbasis Flask yang mengimplementasikan pipeline
**Modified Vigenere Cipher (substitusi)** + **Columnar Transposition Cipher
(permutasi)**.

## Teknologi
- Python 3 + Flask (Blueprint architecture)
- MySQL (XAMPP) + SQLAlchemy ORM + PyMySQL
- Flask-Login (autentikasi & session)
- Werkzeug security (hashing password)

## Cara Menjalankan (Windows + XAMPP)

1. **Aktifkan MySQL di XAMPP Control Panel.**

2. **Buat database** — buka phpMyAdmin lalu jalankan isi `database.sql`,
   atau cukup jalankan:
   ```sql
   CREATE DATABASE securetext;
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **(Opsional) Set kredensial database** lewat environment variable jika
   berbeda dari default (`root` tanpa password):
   ```bash
   set DB_USER=root
   set DB_PASSWORD=
   set DB_HOST=localhost
   set DB_NAME=securetext
   ```

5. **Jalankan aplikasi:**
   ```bash
   python app.py
   ```
   Tabel `users` dan `crypto_history` akan otomatis dibuat oleh SQLAlchemy
   saat pertama kali dijalankan.

6. Buka browser ke **http://127.0.0.1:5000**

## Struktur Proyek
```
SecureText/
├── app.py                 # Entry point & app factory
├── config.py               # Konfigurasi (DB, secret key)
├── requirements.txt
├── database.sql
├── models/
│   ├── user.py              # Model User (auth)
│   └── history.py           # Model CryptoHistory (riwayat)
├── routes/
│   ├── auth.py               # Login / Register / Logout
│   ├── main.py                # Landing / Dashboard / Tentang
│   ├── crypto.py               # Encrypt / Decrypt / Analysis / History
│   ├── history_actions.py       # Hapus log / Bersihkan semua
│   └── profile.py                # Profil & ubah password
├── services/
│   ├── vigenere_service.py        # Modified Vigenere (27 karakter)
│   ├── transposition_service.py    # Columnar Transposition
│   ├── super_encryption_service.py  # Pipeline gabungan
│   └── frequency_service.py          # Analisis frekuensi huruf
├── utils/
│   └── validators.py
├── static/
│   ├── css/style.css
│   └── js/main.js
└── templates/
    ├── base.html / app_base.html
    ├── landing.html, login.html, register.html
    ├── dashboard.html, encrypt.html, decrypt.html
    ├── analysis.html, history.html, profile.html, about.html
```

## Alur Aplikasi
Landing Page → Register/Login → Dashboard → Enkripsi / Dekripsi / Analisis
Frekuensi / Riwayat / Profil → Logout.

## Algoritma
- **Modified Vigenere**: alfabet 27 karakter (A-Z + `@` sebagai spasi),
  `Ci = (Pi + Ki) mod 27` (enkripsi), `Pi = (Ci - Ki) mod 27` (dekripsi).
- **Columnar Transposition**: teks disusun ke matriks sejumlah kolom (kunci),
  padding `X`, dibaca kolom demi kolom kiri→kanan.
- Kedua kunci wajib diisi user pada form Enkripsi/Dekripsi.
