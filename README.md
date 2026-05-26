# 🔐 Enterprise-Grade Password Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![NIST 2024](https://img.shields.io/badge/NIST-2024%20Compliant-brightgreen)

**A professional-grade password generation tool with NIST 2024 compliance, enterprise security standards, and customizable character sets.**

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Security Standards](#security-standards)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Learning Outcomes](#learning-outcomes)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- ✅ **NIST 2024 Compliant**: Follows latest NIST password guidelines
- ✅ **Cryptographically Secure**: Uses secrets module for randomization
- ✅ **Custom Character Sets**: Choose from uppercase, lowercase, digits, symbols
- ✅ **Configurable Length**: Generate passwords of any desired length
- ✅ **Strength Meter**: Visual password strength indicator
- ✅ **Bulk Generation**: Create multiple passwords at once
- ✅ **Exclude Ambiguous**: Optional removal of easily confused characters
- ✅ **History Tracking**: Optional password generation history
- ✅ **Entropy Analysis**: Real-time entropy calculation

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/divyadhankhar2008-byte/password-generator-python.git
   cd password-generator-python
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Application

```bash
python main.py
```

### Command-Line Interface

```
╔════════════════════════════════════════════════════╗
║   🔐 PASSWORD GENERATOR                ║
╚════════════════════════════════════════════════════╝

1. ⚡ Quick Generate (Default Settings)
2. 🎨 Custom Generation
3. 📊 Generate with Strength Meter
4. 📋 Bulk Generate
5. 📝 View History
6. ⚙️  Settings
7. 🚪 Exit
```

### Example Usage

```python
from password_generator import PasswordGenerator

# Basic generation
gen = PasswordGenerator()
password = gen.generate(length=16)
print(f"Generated: {password}")

# Custom configuration
gen = PasswordGenerator(
    uppercase=True,
    lowercase=True,
    digits=True,
    symbols=True,
    length=20
)
password = gen.generate()
print(f"Strength: {gen.calculate_strength()}")
```

## 🔒 Security Standards

### NIST 2024 Compliance

- ✅ Minimum 12 characters recommended
- ✅ Cryptographically secure randomization
- ✅ No common password checks integrated
- ✅ Support for passphrases

### Security Features

- **Cryptographic Randomness**: Uses `secrets` module for true randomness
- **No Logging**: Passwords never logged without user consent
- **Secure Defaults**: Balanced character set by default
- **Input Validation**: Strict validation of user inputs

## 📁 Project Structure

```
password-generator-python/
├── main.py                      # Application entry point
├── password_generator/
│   ├── __init__.py
│   ├── generator.py             # Core generator logic
│   ├── strength_meter.py        # Password strength analysis
│   └── validators.py            # Input validation
├── tests/
│   ├── __init__.py
│   ├── test_generator.py
│   ├── test_strength_meter.py
│   └── test_validators.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## 🛠 Technologies Used

- **Python 3.8+**: Core language
- **secrets**: Cryptographically secure randomization
- **pytest**: Unit testing framework
- **flake8**: Code linting
- **mypy**: Static type checking

## 📚 Learning Outcomes

This project demonstrates:

1. **Security Best Practices**
   - Cryptographic randomization
   - Secure password generation
   - Defense against common attacks

2. **Algorithm Design**
   - Character selection algorithms
   - Strength calculation metrics
   - Randomization techniques

3. **Code Organization**
   - Module separation
   - Class design patterns

4. **Testing & Quality**
   - Unit test coverage
   - Code quality metrics

## 🧪 Testing

### Run All Tests

```bash
pytest
```

### Run with Coverage

```bash
pytest --cov=password_generator --cov-report=html
```

## 🔍 Code Quality

### Lint Code

```bash
flake8 .
pylint password_generator/
```

### Format Code

```bash
black .
```

### Type Check

```bash
mypy password_generator/
```

## 📈 Future Enhancements

- [ ] Passphrase generation (word-based)
- [ ] Breach database integration
- [ ] Desktop GUI (PyQt)
- [ ] Web interface (Flask)
- [ ] Password manager integration

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 👤 Author

**Divya Bharti**
- GitHub: [@divyadhankhar2008-byte](https://github.com/divyadhankhar2008-byte)
- DecodeLabs Industrial Training Kit - Project 3, Batch 2026

## ⚠️ Security Disclaimer

- Passwords are generated locally; none are transmitted
- For critical accounts, use a dedicated password manager
- This tool is for educational and personal use

---

**Made with ❤️ during DecodeLabs Internship 2026**
