from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from models import db
from models.history import CryptoHistory
from services import super_encryption_service, frequency_service

crypto_bp = Blueprint("crypto", __name__)


@crypto_bp.route("/encrypt", methods=["GET", "POST"])
@login_required
def encrypt():
    result = None

    if request.method == "POST":
        plaintext = request.form.get("plaintext", "").strip()
        vigenere_key = request.form.get("vigenere_key", "").strip()
        transposition_key = request.form.get("transposition_key", "").strip()

        if not plaintext or not vigenere_key or not transposition_key:
            flash("Semua field parameter masukan wajib diisi.", "danger")
        else:
            try:
                result = super_encryption_service.super_encrypt(
                    plaintext, vigenere_key, transposition_key
                )

                history = CryptoHistory(
                    user_id=current_user.id,
                    algorithm="modified_vigenere+columnar_transposition",
                    process_type="encrypt",
                    input_text=plaintext,
                    output_text=result["ciphertext"],
                    key_used=f"vigenere={vigenere_key}; transposisi={transposition_key}",
                )
                db.session.add(history)
                db.session.commit()

                flash("Enkripsi berhasil dijalankan.", "success")
            except ValueError as e:
                flash(str(e), "danger")

    return render_template("encrypt.html", result=result)


@crypto_bp.route("/decrypt", methods=["GET", "POST"])
@login_required
def decrypt():
    result = None

    if request.method == "POST":
        ciphertext = request.form.get("ciphertext", "").strip()
        vigenere_key = request.form.get("vigenere_key", "").strip()
        transposition_key = request.form.get("transposition_key", "").strip()

        if not ciphertext or not vigenere_key or not transposition_key:
            flash("Semua field parameter masukan wajib diisi.", "danger")
        else:
            try:
                result = super_encryption_service.super_decrypt(
                    ciphertext, vigenere_key, transposition_key
                )

                history = CryptoHistory(
                    user_id=current_user.id,
                    algorithm="modified_vigenere+columnar_transposition",
                    process_type="decrypt",
                    input_text=ciphertext,
                    output_text=result["plaintext"],
                    key_used=f"vigenere={vigenere_key}; transposisi={transposition_key}",
                )
                db.session.add(history)
                db.session.commit()

                flash("Dekripsi berhasil dijalankan.", "success")
            except ValueError as e:
                flash(str(e), "danger")

    return render_template("decrypt.html", result=result)


@crypto_bp.route("/analysis", methods=["GET", "POST"])
@login_required
def analysis():
    report = None
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("input_text", "").strip()
        if not input_text:
            flash("Teks untuk dianalisis tidak boleh kosong.", "danger")
        else:
            report = frequency_service.analyze(input_text)

    return render_template("analysis.html", report=report, input_text=input_text)


@crypto_bp.route("/history")
@login_required
def history():
    logs = (
        CryptoHistory.query.filter_by(user_id=current_user.id)
        .order_by(CryptoHistory.created_at.desc())
        .all()
    )
    return render_template("history.html", logs=logs)
