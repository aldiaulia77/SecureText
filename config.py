import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Konfigurasi utama aplikasi SecureText."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "securetext-super-secret-key-ganti-di-production")

    # ------------------------------------------------------------------
    # Database MySQL (XAMPP)
    # ------------------------------------------------------------------
    DB_USER = os.environ.get("DB_USER", "root")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "3306")
    DB_NAME = os.environ.get("DB_NAME", "securetext")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ------------------------------------------------------------------
    # Session
    # ------------------------------------------------------------------
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 60 * 60 * 24 * 7  # 7 hari
