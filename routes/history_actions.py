from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user

from models import db
from models.history import CryptoHistory

history_actions_bp = Blueprint("history_actions", __name__)


@history_actions_bp.route("/history/delete/<int:log_id>", methods=["POST"])
@login_required
def delete_log(log_id):
    log = CryptoHistory.query.filter_by(id=log_id, user_id=current_user.id).first_or_404()
    db.session.delete(log)
    db.session.commit()
    flash("Log berhasil dihapus.", "info")
    return redirect(url_for("crypto.history"))


@history_actions_bp.route("/history/clear", methods=["POST"])
@login_required
def clear_logs():
    CryptoHistory.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash("Seluruh log berhasil dibersihkan.", "info")
    return redirect(url_for("crypto.history"))
