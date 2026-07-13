from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.history import CryptoHistory

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def landing():
    return render_template("landing.html")


@main_bp.route("/dashboard")
@login_required
def dashboard():
    total_encrypt = CryptoHistory.query.filter_by(
        user_id=current_user.id, process_type="encrypt"
    ).count()
    total_decrypt = CryptoHistory.query.filter_by(
        user_id=current_user.id, process_type="decrypt"
    ).count()

    recent_activity = (
        CryptoHistory.query.filter_by(user_id=current_user.id)
        .order_by(CryptoHistory.created_at.desc())
        .limit(5)
        .all()
    )

    return render_template(
        "dashboard.html",
        total_encrypt=total_encrypt,
        total_decrypt=total_decrypt,
        recent_activity=recent_activity,
    )


@main_bp.route("/about")
def about():
    return render_template("about.html")
