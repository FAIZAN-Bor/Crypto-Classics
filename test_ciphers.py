"""
Pytest unit tests for cipher implementations.
Run with: pytest -q
"""

from CeaserCipher import caesar_encrypt, caesar_decrypt
from AffineCipher import affine_encrypt, affine_decrypt
from PlayfairCipher import generate_key_matrix, prepare_plaintext, playfair_crypt
from RailFenceCipher import rail_fence_encrypt, rail_fence_decrypt
from RowTranspositionCipher import row_transposition_encrypt, row_transposition_decrypt
from VigenereCipher import vigenere_encrypt, vigenere_decrypt


def test_caesar_basic_roundtrip() -> None:
    plaintext = "Hello World"
    shift = 3
    encrypted = caesar_encrypt(plaintext, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    assert decrypted == plaintext


def test_affine_basic_roundtrip() -> None:
    plaintext = "HELLO WORLD"
    a, b = 5, 8
    encrypted = affine_encrypt(plaintext, a, b)
    decrypted = affine_decrypt(encrypted, a, b)
    assert decrypted.replace(" ", "") == plaintext.replace(" ", "")


def test_playfair_roundtrip_prepared_plaintext() -> None:
    # Use a plaintext that will cause padding/inserted X
    plaintext = "HELLO WORLD"
    keyword = "KEYWORD"
    key_matrix = generate_key_matrix(keyword)
    pairs = prepare_plaintext(plaintext)
    prepared = "".join(pairs)
    encrypted = playfair_crypt(pairs, key_matrix, 1)
    dec_pairs = [encrypted[i:i + 2] for i in range(0, len(encrypted), 2)]
    decrypted = playfair_crypt(dec_pairs, key_matrix, -1)
    assert decrypted == prepared


def test_playfair_roundtrip_simple_no_x_needed() -> None:
    # Choose input without repeated letters in a pair and even length
    plaintext = "MONARCHY"  # 8 letters, no doubled pair, no J, no X
    keyword = "KEYWORD"
    key_matrix = generate_key_matrix(keyword)
    pairs = prepare_plaintext(plaintext)
    encrypted = playfair_crypt(pairs, key_matrix, 1)
    dec_pairs = [encrypted[i:i + 2] for i in range(0, len(encrypted), 2)]
    decrypted = playfair_crypt(dec_pairs, key_matrix, -1)
    # No X should be inserted, so decrypted equals original
    assert decrypted == plaintext


def test_rail_fence_roundtrip() -> None:
    plaintext = "HELLO WORLD"
    rails = 3
    encrypted = rail_fence_encrypt(plaintext, rails)
    decrypted = rail_fence_decrypt(encrypted, rails)
    assert decrypted == plaintext


def test_rail_fence_trivial_cases() -> None:
    assert rail_fence_encrypt("A", 1) == "A"
    assert rail_fence_decrypt("A", 1) == "A"
    assert rail_fence_encrypt("AB", 1) == "AB"


def test_row_transposition_roundtrip() -> None:
    plaintext = "HELLO WORLD"
    key = "3142"
    encrypted = row_transposition_encrypt(plaintext, key)
    decrypted = row_transposition_decrypt(encrypted, key)
    assert decrypted.rstrip('X') == plaintext.replace(" ", "").upper()


def test_vigenere_roundtrip() -> None:
    plaintext = "HELLO WORLD"
    keyword = "KEY"
    encrypted = vigenere_encrypt(plaintext, keyword)
    decrypted = vigenere_decrypt(encrypted, keyword)
    assert decrypted == plaintext
