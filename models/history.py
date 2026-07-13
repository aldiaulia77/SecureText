from datetime import datetime

from models import db


class CryptoHistory(db.Model):
    __tablename__ = "crypto_history"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    algorithm = db.Column(db.String(50), nullable=False)       # caesar, vigenere, railfence, aes, rsa
    process_type = db.Column(db.String(10), nullable=False)    # encrypt / decrypt

    input_text = db.Column(db.Text, nullable=False)
    output_text = db.Column(db.Text, nullable=False)
    key_used = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<CryptoHistory {self.algorithm} {self.process_type}>"
