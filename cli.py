"""
Unified CLI for classic ciphers in this project.

Usage examples:
  python cli.py caesar encrypt --shift 3 --message "Hello World"
  python cli.py caesar decrypt --shift 3 --message "Khoor Zruog"
  python cli.py affine encrypt --a 5 --b 8 --message "HELLO WORLD"
  python cli.py vigenere encrypt --key KEY --message "HELLO WORLD"
  python cli.py playfair encrypt --key KEYWORD --message "HELLO WORLD"
  python cli.py railfence encrypt --rails 3 --message "HELLO WORLD"
  python cli.py rowtrans encrypt --key 3142 --message "HELLO WORLD"
"""

import argparse
from typing import Callable, Optional

from CeaserCipher import caesar_encrypt, caesar_decrypt
from AffineCipher import affine_encrypt, affine_decrypt
from PlayfairCipher import generate_key_matrix, prepare_plaintext, playfair_crypt
from RailFenceCipher import rail_fence_encrypt, rail_fence_decrypt
from RowTranspositionCipher import row_transposition_encrypt, row_transposition_decrypt
from VigenereCipher import vigenere_encrypt, vigenere_decrypt


def cmd_caesar(args: argparse.Namespace) -> None:
    if args.action == "encrypt":
        print(caesar_encrypt(args.message, args.shift))
    else:
        print(caesar_decrypt(args.message, args.shift))


def cmd_affine(args: argparse.Namespace) -> None:
    if args.action == "encrypt":
        print(affine_encrypt(args.message, args.a, args.b))
    else:
        print(affine_decrypt(args.message, args.a, args.b))


def cmd_vigenere(args: argparse.Namespace) -> None:
    if not args.key.isalpha():
        raise SystemExit("Keyword must only contain alphabetic characters.")
    if args.action == "encrypt":
        print(vigenere_encrypt(args.message, args.key))
    else:
        print(vigenere_decrypt(args.message, args.key))


def cmd_playfair(args: argparse.Namespace) -> None:
    key_matrix = generate_key_matrix(args.key)
    if args.action == "encrypt":
        pairs = prepare_plaintext(args.message)
        print(playfair_crypt(pairs, key_matrix, 1))
    else:
        # Normalize ciphertext like the interactive CLI
        norm = args.message.upper().replace(" ", "").replace("J", "I")
        if len(norm) % 2 == 1:
            norm += "X"
        pairs = [norm[i:i + 2] for i in range(0, len(norm), 2)]
        print(playfair_crypt(pairs, key_matrix, -1))


def cmd_railfence(args: argparse.Namespace) -> None:
    if args.rails < 1:
        raise SystemExit("Rails must be >= 1")
    if args.action == "encrypt":
        print(rail_fence_encrypt(args.message, args.rails))
    else:
        print(rail_fence_decrypt(args.message, args.rails))


def cmd_rowtrans(args: argparse.Namespace) -> None:
    if not args.key.isdigit() or len(set(args.key)) != len(args.key):
        raise SystemExit("Key must be a sequence of unique digits, e.g., 3142")
    if args.action == "encrypt":
        print(row_transposition_encrypt(args.message, args.key))
    else:
        print(row_transposition_decrypt(args.message, args.key))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Unified CLI for classic ciphers")
    subparsers = parser.add_subparsers(dest="cipher", required=True)

    # Caesar
    p = subparsers.add_parser("caesar", help="Caesar cipher")
    p_sub = p.add_subparsers(dest="action", required=True)
    for action in ("encrypt", "decrypt"):
        sp = p_sub.add_parser(action)
        sp.add_argument("--shift", type=int, required=True)
        sp.add_argument("--message", type=str, required=True)
        sp.set_defaults(func=cmd_caesar)

    # Affine
    p = subparsers.add_parser("affine", help="Affine cipher")
    p_sub = p.add_subparsers(dest="action", required=True)
    for action in ("encrypt", "decrypt"):
        sp = p_sub.add_parser(action)
        sp.add_argument("--a", type=int, required=True)
        sp.add_argument("--b", type=int, required=True)
        sp.add_argument("--message", type=str, required=True)
        sp.set_defaults(func=cmd_affine)

    # Vigenere
    p = subparsers.add_parser("vigenere", help="Vigenere cipher")
    p_sub = p.add_subparsers(dest="action", required=True)
    for action in ("encrypt", "decrypt"):
        sp = p_sub.add_parser(action)
        sp.add_argument("--key", type=str, required=True)
        sp.add_argument("--message", type=str, required=True)
        sp.set_defaults(func=cmd_vigenere)

    # Playfair
    p = subparsers.add_parser("playfair", help="Playfair cipher")
    p_sub = p.add_subparsers(dest="action", required=True)
    for action in ("encrypt", "decrypt"):
        sp = p_sub.add_parser(action)
        sp.add_argument("--key", type=str, required=True)
        sp.add_argument("--message", type=str, required=True)
        sp.set_defaults(func=cmd_playfair)

    # Rail Fence
    p = subparsers.add_parser("railfence", help="Rail Fence cipher")
    p_sub = p.add_subparsers(dest="action", required=True)
    for action in ("encrypt", "decrypt"):
        sp = p_sub.add_parser(action)
        sp.add_argument("--rails", type=int, required=True)
        sp.add_argument("--message", type=str, required=True)
        sp.set_defaults(func=cmd_railfence)

    # Row Transposition
    p = subparsers.add_parser("rowtrans", help="Row Transposition cipher")
    p_sub = p.add_subparsers(dest="action", required=True)
    for action in ("encrypt", "decrypt"):
        sp = p_sub.add_parser(action)
        sp.add_argument("--key", type=str, required=True)
        sp.add_argument("--message", type=str, required=True)
        sp.set_defaults(func=cmd_rowtrans)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    func: Optional[Callable[[argparse.Namespace], None]] = getattr(args, "func", None)
    if func is None:
        parser.print_help()
        raise SystemExit(2)
    func(args)


if __name__ == "__main__":
    main()
