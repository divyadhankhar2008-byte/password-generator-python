# 🔒 Enterprise Random Password Generator — Project 3

> **DecodeLabs Industrial Training Kit | Batch 2026**
> Author: Divya Dhankhar | Python Programming Intern

---

## 📌 Project Overview

An enterprise-grade, cryptographically secure password generator built as Project 3 of the DecodeLabs Python Programming Industrial Training Kit. This project demonstrates mastery of security fundamentals, object-oriented design, and professional Python engineering practices.

Unlike basic random-based generators, this tool uses Python's `secrets` module to tap into OS-level entropy sources — making it suitable for real-world password generation, API key creation, and token management.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔑 Single Password | Generate one cryptographically secure password |
| 📦 Batch Generation | Generate 2–20 passwords in one go |
| 🗝️ Passphrase Mode | Human-memorable word-based passphrases with entropy scoring |
| 🔍 Strength Checker | Analyse any existing password with score, entropy, and improvement tips |
| 🕐 History Log | Last 50 generated passwords saved to `password_history.json` |
| 🚫 Ambiguous Char Filter | Optionally exclude `0`, `O`, `1`, `l`, `I` to avoid confusion |
| 📊 Entropy Display | Real-time entropy calculation with visual strength bar |
| ⏱️ Crack Time Estimate | Human-readable time-to-crack based on modern GPU capabilities |
| ✅ NIST 2024 Compliant | Enforces 15–64 character range per NIST SP 800-63B guidelines |

---

## 🎯 Key Concepts Demonstrated

| Concept | Implementation |
|---|---|
| OOP / Class Design | `PasswordGenerator` class encapsulates all generation logic |
| `secrets` module | `secrets.choice()` — cryptographically secure, unpredictable |
| String Manipulation | `.join()` for O(N) construction vs O(N²) concatenation |
| Input Validation | Length range check, yes/no guard, integer guard |
| Entropy Calculation | `E = L × log₂(R)` — mathematical security analysis |
| Complexity Guarantee | `_ensure_complexity()` forces at least one char from each required pool |
| File I/O | JSON history log with rolling 50-entry limit |
| Module Architecture | Separation of generator, checker, display helpers, and menu actions |

---

## 🔐 Why `secrets` Over `random`?

| | `random` module | `secrets` module |
|---|---|---|
| Source | Mersenne Twister algorithm | OS-level entropy (`/dev/urandom`) |
| Predictable? | Yes — seeded, reproducible | No — cryptographically unpredictable |
| Suitable for passwords? | ❌ No | ✅ Yes |
| NIST compliant? | ❌ No | ✅ Yes |

---

## 📐 Security Analysis

Password strength is calculated using Shannon entropy:

```
E = L × log₂(R)
```

Where `L` = password length, `R` = character pool size.

| Length | Pool | Entropy | Security Level | Est. Crack Time |
|---|---|---|---|---|
| 8 chars | 62 | 47.6 bits | ⚠️ Moderate | 2 days |
| 10 chars | 62 | 59.5 bits | ⚠️ Moderate | 5 years |
| 15 chars | 62 | 89.2 bits | ✅ Highly Secure | Centuries |
| 20 chars | 94 | 131.1 bits | 🛡️ Quantum Resistant | Millions of years |

---

## 🏗️ Architecture

```
Phase 1 — Input (Environmental Requirements)
  └── Validate length (NIST 2024: 15–64 chars)
  └── Handle special character preference
  └── Handle ambiguous character exclusion

Phase 2 — Process (Backend Transformation Engine)
  └── Build character pool (string module)
  └── secrets.choice() for each character
  └── .join() for O(N) string construction
  └── _ensure_complexity() for guaranteed variety

Phase 3 — Output (Security Validation)
  └── Calculate entropy: E = L × log₂(R)
  └── Assess security level and crack time
  └── Display result with visual entropy bar
  └── Save to history log
```

---

## 🚀 How to Run

### Prerequisites
- Python **3.6+** (`secrets` module support)
- No external libraries — uses stdlib only (`secrets`, `string`, `math`, `json`, `os`)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/divyadhankhar2008-byte/password-generator-python.git

# 2. Navigate into the folder
cd password-generator-python

# 3. Run the script
python password_generator.py

# 4. (Optional) Run tests
python test_generator.py
```

---

## 🖥️ Sample Output

```
======================================================================
🔒  ENTERPRISE RANDOM PASSWORD GENERATOR  🔒
DecodeLabs Industrial Training Kit — Project 3
Batch: 2026  |  NIST 2024 Compliant  |  Cryptographically Secure
======================================================================

── Menu ──────────────────────────────────────────────────────────────
  1. 🔑 Generate single password
  2. 📦 Generate batch of passwords
  3. 🗝️  Generate passphrase
  4. 🔍 Check password strength
  5. 🕐 View generation history
  6. 🚪 Exit
──────────────────────────────────────────────────────────────────────
```

**Generated Password Example:**
```
═════════════════════════════════════════════════════════════════
  🔑 Password: Kx7#mP2@vQnL9rT!
─────────────────────────────────────────────────────────────────
  Length        : 16 chars
  Pool Size     : 94 chars
  Entropy       : 105.12 bits  [████████████████░░░░]
  Security      : ✅ HIGHLY SECURE
  Est. Crack    : Centuries
═════════════════════════════════════════════════════════════════
```

---

## 📁 File Structure

```
password-generator-python/
├── password_generator.py    # Main application + PasswordGenerator class
├── test_generator.py        # Unit tests
├── password_history.json    # Auto-generated on first run (gitignored)
└── README.md
```

---

## 💡 What I Learned

By building this project I practised:

- **OOP design** — encapsulating state and behaviour in a class
- **Cryptographic security** — why `secrets` beats `random` for sensitive data
- **Entropy mathematics** — quantifying password strength with information theory
- **Professional engineering** — separation of concerns, input validation, history logging
- **NIST compliance** — applying real-world security standards to code

---

## 👩‍💻 Author

**Divya Dhankhar**
Python Programming Intern | DecodeLabs Batch 2026
