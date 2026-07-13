from flask import Flask

from config import Config
from models import init_app, db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_app(app)

    # ------------------------------------------------------------------
    # Registrasi Blueprint
    # ------------------------------------------------------------------
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.crypto import crypto_bp
    from routes.history_actions import history_actions_bp
    from routes.profile import profile_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(crypto_bp)
    app.register_blueprint(history_actions_bp)
    app.register_blueprint(profile_bp)

    # ------------------------------------------------------------------
    # Buat seluruh tabel database secara otomatis jika belum ada
    # ------------------------------------------------------------------
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
