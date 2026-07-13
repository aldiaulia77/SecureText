"""
Modified Vigenere Cipher - SecureText

Alfabet & Mapping (27 karakter):
    A-Z (0-25), @ = 26 (representasi spasi)

Spasi pada plaintext dikonversi menjadi '@' sebelum enkripsi.
Contoh: "TEKNIK INFORMATIKA" -> "TEKNIK@INFORMATIKA"

Formula matematis:
    Enkripsi : Ci = (Pi + Ki) mod 27
    Dekripsi : Pi = (Ci - Ki) mod 27

    Pi = indeks plaintext, Ki = indeks key, Ci = indeks ciphertext
"""

MOD = 27
SPACE_SYMBOL = "@"


def _char_to_index(ch: str) -> int:
    if ch == " " or ch == SPACE_SYMBOL:
        return 26
    return ord(ch.upper()) - ord("A")


def _index_to_char(idx: int) -> str:
    idx = idx % MOD
    if idx == 26:
        return SPACE_SYMBOL
    return chr(idx + ord("A"))


def _normalize(text: str) -> str:
    """Ubah ke uppercase dan pastikan hanya berisi A-Z dan spasi/@."""
    return text.upper()


def encrypt(plaintext: str, key: str) -> str:
    if not key:
        raise ValueError("Kunci Vigenere tidak boleh kosong.")

    plaintext = _normalize(plaintext)
    key = _normalize(key)

    result = []
    for i, ch in enumerate(plaintext):
        p_idx = _char_to_index(ch)
        k_idx = _char_to_index(key[i % len(key)])
        c_idx = (p_idx + k_idx) % MOD
        result.append(_index_to_char(c_idx))

    return "".join(result)


def decrypt(ciphertext: str, key: str) -> str:
    if not key:
        raise ValueError("Kunci Vigenere tidak boleh kosong.")

    ciphertext = _normalize(ciphertext)
    key = _normalize(key)

    result = []
    for i, ch in enumerate(ciphertext):
        c_idx = _char_to_index(ch)
        k_idx = _char_to_index(key[i % len(key)])
        p_idx = (c_idx - k_idx) % MOD
        result.append(_index_to_char(p_idx))

    return "".join(result)
