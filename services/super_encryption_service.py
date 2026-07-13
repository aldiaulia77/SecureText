"""
Super Encryption Pipeline - SecureText

Menggabungkan dua lapis kriptografi:
    Layer 1 (Confusion) : Modified Vigenere Cipher (substitusi)
    Layer 2 (Diffusion)  : Columnar Transposition Cipher (permutasi)

Alur ENKRIPSI:
    Plaintext -> [Vigenere Substitusi] -> Intermediary -> [Transposisi Kolom] -> Ciphertext Akhir

Alur DEKRIPSI (kebalikan urutan):
    Ciphertext -> [De-Transposisi Kolom] -> Intermediary -> [De-Vigenere] -> Plaintext Akhir
"""

from services import vigenere_service, transposition_service


def super_encrypt(plaintext: str, vigenere_key: str, transposition_key: str) -> dict:
    """Menjalankan pipeline enkripsi dan mengembalikan setiap tahapan."""
    intermediary = vigenere_service.encrypt(plaintext, vigenere_key)
    final_ciphertext = transposition_service.encrypt(intermediary, transposition_key)

    return {
        "plaintext": plaintext,
        "intermediary": intermediary,
        "ciphertext": final_ciphertext,
    }


def super_decrypt(ciphertext: str, vigenere_key: str, transposition_key: str) -> dict:
    """Menjalankan pipeline dekripsi (urutan terbalik) dan mengembalikan setiap tahapan."""
    de_transposition = transposition_service.decrypt(ciphertext, transposition_key)
    final_plaintext = vigenere_service.decrypt(de_transposition, vigenere_key)

    # Kembalikan simbol '@' menjadi spasi agar pesan asli terbaca utuh
    final_plaintext_readable = final_plaintext.replace("@", " ")

    return {
        "ciphertext": ciphertext,
        "de_transposition": de_transposition,
        "plaintext": final_plaintext_readable,
    }
