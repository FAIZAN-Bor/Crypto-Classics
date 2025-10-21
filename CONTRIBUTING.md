# Contributing to CryptoClassics

Thank you for your interest in contributing to CryptoClassics! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- Basic understanding of cryptographic ciphers (helpful but not required)

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/crypto-classics.git
   cd crypto-classics
   ```

2. **Create a Virtual Environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install in Development Mode**
   ```bash
   pip install -e .
   ```

4. **Install Development Dependencies**
   ```bash
   pip install pytest mypy ruff flake8
   ```

## 🔧 Development Workflow

### Making Changes

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make Your Changes**
   - Write clear, concise code
   - Follow the existing code style
   - Add type hints to all functions
   - Update docstrings

3. **Write Tests**
   - Add tests for new features in `test_ciphers.py`
   - Ensure all tests pass:
     ```bash
     pytest -q
     ```

4. **Type Check**
   - Ensure type hints are correct:
     ```bash
     mypy .
     ```

5. **Lint Your Code**
   ```bash
   ruff check .
   flake8 .
   ```

### Code Style Guidelines

- **Type Hints**: All functions must have complete type annotations
- **Docstrings**: Use clear docstrings for all public functions
- **Line Length**: Maximum 100 characters
- **Imports**: Organize imports (standard library, third-party, local)
- **Naming**: 
  - Functions: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`

### Example Function

```python
from typing import List

def example_cipher_function(plaintext: str, key: int) -> str:
    """
    Brief description of what the function does.
    
    Args:
        plaintext: The text to encrypt.
        key: The encryption key.
    
    Returns:
        The encrypted ciphertext.
    """
    # Implementation here
    return ciphertext
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest -q

# Run with verbose output
pytest -v

# Run specific test file
pytest test_ciphers.py -v

# Run specific test
pytest test_ciphers.py::test_caesar_basic_roundtrip -v

# Run with coverage
pytest --cov=. --cov-report=html
```

### Writing Tests

- Use pytest fixtures when appropriate
- Test both encryption and decryption
- Include edge cases
- Test invalid inputs
- Add type hints to test functions

Example:
```python
def test_new_cipher_roundtrip() -> None:
    plaintext = "TEST MESSAGE"
    key = "KEY"
    encrypted = new_cipher_encrypt(plaintext, key)
    decrypted = new_cipher_decrypt(encrypted, key)
    assert decrypted == plaintext
```

## 📝 Commit Guidelines

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>: <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
git commit -m "feat: add Columnar Transposition cipher"
git commit -m "fix: handle edge case in Playfair decryption"
git commit -m "docs: update README with new examples"
git commit -m "test: add edge cases for Rail Fence cipher"
```

## 🔍 Pull Request Process

1. **Update Documentation**
   - Update README.md if adding new features
   - Add docstrings to new functions
   - Update CONTRIBUTING.md if changing development process

2. **Ensure Quality Checks Pass**
   - All tests pass (`pytest -q`)
   - Type checks pass (`mypy .`)
   - Linting passes (`ruff check .`, `flake8 .`)

3. **Create Pull Request**
   - Use a clear, descriptive title
   - Reference any related issues
   - Describe what changed and why
   - Include screenshots/examples if relevant

4. **PR Template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Code refactoring
   
   ## Testing
   - [ ] All tests pass
   - [ ] Type checks pass
   - [ ] Linting passes
   
   ## Related Issues
   Fixes #123
   ```

## 🐛 Reporting Bugs

When reporting bugs, please include:
- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages/stack traces
- Minimal code example

## 💡 Suggesting Features

Feature suggestions are welcome! Please:
- Check if the feature already exists
- Describe the use case
- Explain why it would be valuable
- Provide examples if possible

## 📚 Adding New Ciphers

To add a new cipher:

1. **Create Module** (`NewCipher.py`)
   ```python
   from typing import ...
   
   def new_cipher_encrypt(plaintext: str, key: ...) -> str:
       """Encrypt plaintext using NewCipher."""
       # Implementation
       pass
   
   def new_cipher_decrypt(ciphertext: str, key: ...) -> str:
       """Decrypt ciphertext using NewCipher."""
       # Implementation
       pass
   ```

2. **Add CLI Support** (in `cli.py`)
   - Add subparser
   - Add command function
   - Wire up to main parser

3. **Write Tests** (in `test_ciphers.py`)
   - Basic roundtrip test
   - Edge cases
   - Invalid inputs

4. **Update Documentation**
   - Add to README.md cipher table
   - Add usage examples
   - Document key requirements

## ❓ Questions?

Feel free to:
- Open an issue for discussion
- Ask in pull request comments
- Contact maintainers

## 🙏 Thank You!

Your contributions make this project better for everyone!
