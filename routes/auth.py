from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user

from models import db
from models.user import User
from utils.validators import is_valid_email, is_valid_username, is_valid_password

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":
        identifier = request.form.get("identifier", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter(
            (User.email == identifier) | (User.username == identifier)
        ).first()

        if user and user.check_password(password):
            login_user(user, remember=True)
            flash("Login berhasil. Selamat datang kembali!", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.dashboard"))

        flash("Username/Email atau password salah.", "danger")

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not is_valid_username(username):
            flash("Username minimal 3 karakter dan hanya huruf/angka.", "danger")
        elif not is_valid_email(email):
            flash("Format email tidak valid.", "danger")
        elif not is_valid_password(password):
            flash("Password minimal 6 karakter.", "danger")
        elif password != confirm_password:
            flash("Konfirmasi password tidak cocok.", "danger")
        elif User.query.filter_by(username=username).first():
            flash("Username sudah digunakan.", "danger")
        elif User.query.filter_by(email=email).first():
            flash("Email sudah terdaftar.", "danger")
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash("Registrasi berhasil! Silakan login.", "success")
            return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Anda berhasil logout.", "info")
    return redirect(url_for("main.landing"))
