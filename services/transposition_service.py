"""
Columnar Transposition Cipher - SecureText

Mengacak posisi karakter dengan menyusun teks input ke dalam matriks
berdasarkan jumlah kolom (kunci), lalu dibaca kolom demi kolom
dari kiri ke kanan. Sisa sel yang kosong diisi padding 'X'.

Contoh (Kolom = 5):
    Input : TEKNIK@INFORMATIKA (length 18)

    T E K N I
    K @ I N F
    O R M A T
    I K A X X   (X = padding)

    Output (baca kolom demi kolom): TKOIE@RKKIMANNAXIFTX
"""

PADDING_CHAR = "X"


def _parse_key(key: str) -> int:
    try:
        cols = int(key)
    except (TypeError, ValueError):
        raise ValueError("Kunci Transposisi harus berupa angka jumlah kolom (contoh: 5).")
    if cols < 2:
        raise ValueError("Kunci Transposisi minimal 2 kolom.")
    return cols


def encrypt(text: str, key: str) -> str:
    cols = _parse_key(key)
    rows = -(-len(text) // cols)  # ceil division
    padded = text + PADDING_CHAR * (rows * cols - len(text))

    matrix = [padded[r * cols:(r + 1) * cols] for r in range(rows)]

    output_chars = []
    for c in range(cols):
        for r in range(rows):
            output_chars.append(matrix[r][c])

    return "".join(output_chars)


def decrypt(ciphertext: str, key: str) -> str:
    cols = _parse_key(key)
    if len(ciphertext) % cols != 0:
        raise ValueError("Panjang ciphertext tidak sesuai dengan kunci transposisi.")

    rows = len(ciphertext) // cols
    matrix = [["" for _ in range(cols)] for _ in range(rows)]

    idx = 0
    for c in range(cols):
        for r in range(rows):
            matrix[r][c] = ciphertext[idx]
            idx += 1

    plain = "".join("".join(row) for row in matrix)
    return plain.rstrip(PADDING_CHAR)
