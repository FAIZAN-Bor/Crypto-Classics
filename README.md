# 🔐 CryptoClassics

[![CI](https://github.com/FAIZAN-Bor/crypto-classics/actions/workflows/ci.yml/badge.svg)](https://github.com/FAIZAN-Bor/crypto-classics/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern Python implementation of classic cryptographic ciphers with a unified command-line interface, comprehensive test suite, and strict type checking.

## ✨ Features

- 🎯 **Six Classic Ciphers**: Caesar, Affine, Vigenère, Playfair, Rail Fence, Row Transposition
- 🚀 **Unified CLI**: Single command-line interface for all ciphers
- ✅ **Type-Safe**: Full type hints with mypy validation
- 🧪 **Well-Tested**: Comprehensive pytest suite with edge case coverage
- 📦 **Easy Install**: Package with console script entry point
- 🔍 **Linted**: Enforced code quality with ruff and flake8
- 🤖 **CI/CD**: Automated testing and linting via GitHub Actions

## 📚 Implemented Ciphers

| Cipher | Module | Description |
|--------|--------|-------------|
| **Caesar** | `CeaserCipher.py` | Simple substitution cipher with shift |
| **Affine** | `AffineCipher.py` | Mathematical cipher using modular arithmetic |
| **Vigenère** | `VigenereCipher.py` | Polyalphabetic substitution using keyword |
| **Playfair** | `PlayfairCipher.py` | Digraph substitution with 5×5 key matrix |
| **Rail Fence** | `RailFenceCipher.py` | Transposition cipher with zigzag pattern |
| **Row Transposition** | `RowTranspositionCipher.py` | Columnar transposition with numeric key |

## 🚀 Installation

### From Source
```bash
git clone https://github.com/YOUR_USERNAME/crypto-classics.git
cd crypto-classics
pip install -e .
```

### For Development
```bash
git clone https://github.com/YOUR_USERNAME/crypto-classics.git
cd crypto-classics
pip install -e .
pip install pytest mypy ruff flake8
```

## 💻 Usage

### As a Command-Line Tool

After installation, use the `classic-ciphers` command:

```bash
# Caesar Cipher
classic-ciphers caesar encrypt --shift 3 --message "Hello World"
# Output: Khoor Zruog

classic-ciphers caesar decrypt --shift 3 --message "Khoor Zruog"
# Output: Hello World

# Affine Cipher (a must be coprime with 26)
classic-ciphers affine encrypt --a 5 --b 8 --message "HELLO WORLD"
# Output: RCLLA OAPLX

# Vigenère Cipher
classic-ciphers vigenere encrypt --key KEY --message "HELLO WORLD"
# Output: RIJVS GSPVH

# Playfair Cipher
classic-ciphers playfair encrypt --key KEYWORD --message "HELLO WORLD"
# Output: GYIZSCOKCFBU

# Rail Fence Cipher
classic-ciphers railfence encrypt --rails 3 --message "HELLO WORLD"
# Output: HOREL OLLWD

# Row Transposition Cipher (key must be unique digits)
classic-ciphers rowtrans encrypt --key 3142 --message "HELLO WORLD"
# Output: EWDLRXHOLLOX
```

### Without Installation

Run directly using Python:

```bash
python cli.py caesar encrypt --shift 3 --message "Hello World"
```

### As a Python Library

```python
from CeaserCipher import caesar_encrypt, caesar_decrypt
from VigenereCipher import vigenere_encrypt, vigenere_decrypt

# Encrypt
ciphertext = caesar_encrypt("Hello World", 3)
print(ciphertext)  # Khoor Zruog

# Decrypt
plaintext = caesar_decrypt(ciphertext, 3)
print(plaintext)  # Hello World
```

## 🧪 Running Tests

```bash
# Run all tests
pytest -q

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test
pytest test_ciphers.py::test_caesar_basic_roundtrip -v
```

## 🔍 Code Quality

```bash
# Type checking
mypy .

# Linting
ruff check .
flake8 .

# Auto-format (if using ruff)
ruff format .
```

## 📖 Cipher Details

### Caesar Cipher
- **Key**: Integer shift value (0-25)
- **Example**: Shift 3: A→D, B→E, C→F
- **Security**: Very weak, only 26 possible keys

### Affine Cipher
- **Key**: Two integers (a, b) where a is coprime with 26
- **Formula**: E(x) = (ax + b) mod 26
- **Valid a values**: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

### Vigenère Cipher
- **Key**: Alphabetic keyword
- **Method**: Repeating key determines shift for each letter
- **Note**: Case-insensitive, preserves non-alphabetic characters

### Playfair Cipher
- **Key**: Alphabetic keyword
- **Method**: 5×5 matrix, encrypts digraphs (pairs of letters)
- **Note**: I/J are treated as same letter, adds X for padding

### Rail Fence Cipher
- **Key**: Number of rails (rows)
- **Method**: Write message in zigzag pattern, read row by row
- **Note**: Transposition cipher, doesn't change letters

### Row Transposition Cipher
- **Key**: Sequence of unique digits (e.g., 3142)
- **Method**: Write in rows, read columns in key order
- **Note**: Pads with X to fill grid

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`pytest`, `mypy .`, `ruff check .`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Educational Purpose

This project is designed for educational purposes to demonstrate:
- Classic cryptographic algorithms
- Python best practices (type hints, testing, documentation)
- Modern development workflows (CI/CD, linting, packaging)
- Command-line interface design

**⚠️ Note**: These ciphers are **not secure** for modern cryptographic use. They are intended for learning and demonstration only.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Classic cryptography references and historical context
- Python packaging and testing communities
- Open-source contributors
