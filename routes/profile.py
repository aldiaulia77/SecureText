from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from models import db
from utils.validators import is_valid_password

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        old_password = request.form.get("old_password", "")
        new_password = request.form.get("new_password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not current_user.check_password(old_password):
            flash("Password lama salah.", "danger")
        elif not is_valid_password(new_password):
            flash("Password baru minimal 6 karakter.", "danger")
        elif new_password != confirm_password:
            flash("Konfirmasi password baru tidak cocok.", "danger")
        else:
            current_user.set_password(new_password)
            db.session.commit()
            flash("Password berhasil diperbarui.", "success")
            return redirect(url_for("profile.profile"))

    total_history = current_user.histories.count()
    return render_template("profile.html", total_history=total_history)
