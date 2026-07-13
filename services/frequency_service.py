"""
Analisis Frekuensi Karakter - SecureText

Menghitung distribusi kemunculan huruf (A-Z) pada suatu teks (plaintext
maupun ciphertext) untuk membantu mengidentifikasi pola statistik.
"""

import string


def analyze(text: str) -> list:
    text = text.upper()
    letters = [c for c in text if c in string.ascii_uppercase]
    total = len(letters)

    counts = {letter: 0 for letter in string.ascii_uppercase}
    for c in letters:
        counts[c] += 1

    report = []
    for letter in string.ascii_uppercase:
        jumlah = counts[letter]
        if jumlah == 0:
            continue
        persentase = round((jumlah / total) * 100, 1) if total else 0
        report.append({
            "karakter": letter,
            "jumlah": jumlah,
            "persentase": persentase,
        })

    return report
