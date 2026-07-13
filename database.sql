-- Jalankan query ini di phpMyAdmin / MySQL client (XAMPP) untuk membuat database.
-- Struktur tabel akan dibuat otomatis oleh SQLAlchemy (db.create_all()) saat app.py dijalankan.

CREATE DATABASE IF NOT EXISTS securetext
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
