from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Silakan login terlebih dahulu untuk mengakses halaman ini."
login_manager.login_message_category = "warning"


def init_app(app):
    """Inisialisasi ekstensi database & login manager ke aplikasi Flask."""
    db.init_app(app)
    login_manager.init_app(app)

    # Import model di sini agar terdaftar sebelum create_all()
    from models.user import User
    from models.history import CryptoHistory  # noqa: F401

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return db
