"""
Enterprise Random Password Generator
Project 3 - DecodeLabs Industrial Training Kit
Batch: 2026

Architecture: Input -> Process -> Output
- Phase 1: Environmental requirements and validation
- Phase 2: Building the backend transformation engine
- Phase 3: Mathematical provision of security

ENHANCED FEATURES:
  • Batch generation (multiple passwords at once)
  • Custom character exclusions (avoid ambiguous chars)
  • Passphrase generator mode
  • Password strength checker for user-supplied passwords
  • History log saved to file
  • Visual strength meter
"""

import secrets
import string
import math
import json
import os
from datetime import datetime

HISTORY_FILE = "password_history.json"
AMBIGUOUS = "0O1lI"          # Characters that look alike — optionally excluded
WORDLIST   = [               # Lightweight built-in wordlist for passphrases
    "apple","river","cloud","stone","tiger","flame","ocean","eagle","storm",
    "lunar","prism","glass","frost","spark","blade","coral","cedar","swift",
    "noble","crisp","vivid","amber","blaze","crest","delta","ember","flora",
    "grove","haven","ivory","jewel","karma","lemon","maple","nexus","oasis",
    "pearl","quest","ridge","scout","thorn","ultra","vapor","wheat","xenon",
    "yacht","zebra","solar","brave","chill","pixel","quark","relay","shade",
]


# ── Persistence ───────────────────────────────────────────────────────────────

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return []

def save_to_history(entry: dict):
    history = load_history()
    history.append(entry)
    history = history[-50:]   # Keep last 50 entries only
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


# ── Password Generator ────────────────────────────────────────────────────────

class PasswordGenerator:
    """
    Enterprise-grade password generator with NIST 2024 compliance.
    Uses secrets.choice() for cryptographically secure randomness.
    """

    LOWERCASE  = string.ascii_lowercase
    UPPERCASE  = string.ascii_uppercase
    DIGITS     = string.digits
    SPECIAL    = string.punctuation
    MIN_LENGTH = 15
    MAX_LENGTH = 64

    def __init__(self, exclude_ambiguous: bool = False):
        self.exclude_ambiguous = exclude_ambiguous
        self._rebuild_pool(include_special=False)

    def _rebuild_pool(self, include_special: bool):
        pool = self.LOWERCASE + self.UPPERCASE + self.DIGITS
        if include_special:
            pool += self.SPECIAL
        if self.exclude_ambiguous:
            pool = ''.join(c for c in pool if c not in AMBIGUOUS)
        self.character_pool = pool
        self.pool_size = len(pool)

    def validate_length(self, length: int) -> tuple[bool, str]:
        if not isinstance(length, int):
            return False, "Length must be an integer."
        if length < self.MIN_LENGTH:
            return False, f"Minimum length is {self.MIN_LENGTH} characters (NIST 2024)."
        if length > self.MAX_LENGTH:
            return False, f"Maximum length is {self.MAX_LENGTH} characters."
        return True, ""

    def calculate_entropy(self, length: int, pool_size: int = None) -> float:
        ps = pool_size if pool_size is not None else self.pool_size
        return length * math.log2(ps)

    def generate_password(self, length: int, include_special: bool = False) -> str:
        self._rebuild_pool(include_special)
        password_chars = [secrets.choice(self.character_pool) for _ in range(length)]
        return self._ensure_complexity(''.join(password_chars), include_special)

    def _ensure_complexity(self, password: str, include_special: bool) -> str:
        pl = list(password)
        required = [self.LOWERCASE, self.UPPERCASE, self.DIGITS]
        if include_special:
            required.append(self.SPECIAL)
        for pool in required:
            filtered = [c for c in pool if c not in (AMBIGUOUS if self.exclude_ambiguous else "")]
            if filtered and not any(c in filtered for c in pl):
                pl[secrets.randbelow(len(pl))] = secrets.choice(filtered)
        return ''.join(pl)

    def generate_batch(self, count: int, length: int, include_special: bool = False) -> list[str]:
        return [self.generate_password(length, include_special) for _ in range(count)]

    def generate_passphrase(self, word_count: int = 4, separator: str = "-") -> tuple[str, float]:
        words = [secrets.choice(WORDLIST) for _ in range(word_count)]
        # Add a random number for extra entropy
        words.append(str(secrets.randbelow(9000) + 1000))
        passphrase = separator.join(words)
        entropy = word_count * math.log2(len(WORDLIST)) + math.log2(9000)
        return passphrase, entropy


# ── Password Strength Checker ─────────────────────────────────────────────────

def check_password_strength(password: str) -> dict:
    length = len(password)
    has_lower   = any(c in string.ascii_lowercase for c in password)
    has_upper   = any(c in string.ascii_uppercase for c in password)
    has_digit   = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)

    pool = 0
    if has_lower:   pool += 26
    if has_upper:   pool += 26
    if has_digit:   pool += 10
    if has_special: pool += 32

    entropy = length * math.log2(pool) if pool else 0

    score = 0
    tips  = []
    if length >= 15: score += 2
    elif length >= 10: score += 1
    else: tips.append("Use at least 15 characters.")
    if has_lower:   score += 1
    else:           tips.append("Add lowercase letters.")
    if has_upper:   score += 1
    else:           tips.append("Add uppercase letters.")
    if has_digit:   score += 1
    else:           tips.append("Add numbers.")
    if has_special: score += 2
    else:           tips.append("Add special characters (!@#$...).")
    if entropy >= 80: score += 1

    if score >= 7:   label, color = "🛡️  VERY STRONG",  "██████████"
    elif score >= 5: label, color = "✅ STRONG",        "████████░░"
    elif score >= 3: label, color = "⚠️  MODERATE",     "█████░░░░░"
    else:            label, color = "❌ WEAK",           "███░░░░░░░"

    return {
        "length": length, "entropy": entropy, "score": score,
        "label": label, "bar": color, "tips": tips,
        "has_lower": has_lower, "has_upper": has_upper,
        "has_digit": has_digit, "has_special": has_special,
    }


# ── Display Helpers ───────────────────────────────────────────────────────────

def security_label(entropy: float) -> tuple[str, str]:
    if entropy >= 128: return "🛡️  QUANTUM RESISTANT",   "Millions of years"
    if entropy >= 100: return "🛡️  EXTREMELY SECURE",    "Billions of years"
    if entropy >= 80:  return "✅ HIGHLY SECURE",        "Centuries"
    if entropy >= 60:  return "⚠️  MODERATELY SECURE",   "Years"
    return "❌ VULNERABLE", "Days to months"


def print_result(password: str, entropy: float, generator: PasswordGenerator, label: str = "Password"):
    sec_label, crack_time = security_label(entropy)
    bar = "█" * int(min(entropy, 128) // 6.4) + "░" * (20 - int(min(entropy, 128) // 6.4))
    print(f"\n{'═'*65}")
    print(f"  🔑 {label}: {password}")
    print(f"{'─'*65}")
    print(f"  Length        : {len(password)} chars")
    print(f"  Pool Size     : {generator.pool_size} chars")
    print(f"  Entropy       : {entropy:.2f} bits  [{bar}]")
    print(f"  Security      : {sec_label}")
    print(f"  Est. Crack    : {crack_time}")
    print(f"{'═'*65}")


# ── Menu Actions ──────────────────────────────────────────────────────────────

def get_length_and_special(generator: PasswordGenerator) -> tuple[int, bool] | None:
    while True:
        try:
            raw = input(f"Password length ({generator.MIN_LENGTH}–{generator.MAX_LENGTH}): ").strip()
            length = int(raw)
            ok, msg = generator.validate_length(length)
            if not ok:
                print(f"❌ {msg}")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid integer.")

    while True:
        sp = input("Include special characters? (y/n): ").strip().lower()
        if sp in ("y", "yes"):   return length, True
        if sp in ("n", "no"):    return length, False
        print("❌ Please enter 'y' or 'n'.")


def action_single(generator: PasswordGenerator):
    result = get_length_and_special(generator)
    if result is None: return
    length, include_special = result
    pwd = generator.generate_password(length, include_special)
    entropy = generator.calculate_entropy(length)
    print_result(pwd, entropy, generator)
    save_to_history({"type": "single", "password": pwd, "entropy": round(entropy, 2),
                     "generated": datetime.now().isoformat()})


def action_batch(generator: PasswordGenerator):
    try:
        count = int(input("How many passwords to generate? (2–20): ").strip())
        if not 2 <= count <= 20:
            print("❌ Please enter a number between 2 and 20.")
            return
    except ValueError:
        print("❌ Invalid number.")
        return

    result = get_length_and_special(generator)
    if result is None: return
    length, include_special = result
    passwords = generator.generate_batch(count, length, include_special)
    entropy = generator.calculate_entropy(length)
    sec_label, crack_time = security_label(entropy)

    print(f"\n{'═'*65}")
    print(f"  🔑 Generated {count} Passwords  |  Entropy: {entropy:.2f} bits  |  {sec_label}")
    print(f"{'─'*65}")
    for i, pwd in enumerate(passwords, 1):
        print(f"  {i:>2}. {pwd}")
    print(f"{'═'*65}")
    for pwd in passwords:
        save_to_history({"type": "batch", "password": pwd, "entropy": round(entropy, 2),
                         "generated": datetime.now().isoformat()})


def action_passphrase(generator: PasswordGenerator):
    try:
        words = int(input("Number of words (3–6) [default 4]: ").strip() or "4")
        if not 3 <= words <= 6:
            print("❌ Please enter between 3 and 6.")
            return
    except ValueError:
        print("❌ Invalid number.")
        return
    sep = input("Separator (default '-'): ").strip() or "-"
    phrase, entropy = generator.generate_passphrase(words, sep)
    print(f"\n{'═'*65}")
    print(f"  🔑 Passphrase : {phrase}")
    print(f"  Entropy       : {entropy:.2f} bits")
    sec_label, crack_time = security_label(entropy)
    print(f"  Security      : {sec_label}  |  Est. Crack: {crack_time}")
    print(f"{'═'*65}")
    save_to_history({"type": "passphrase", "password": phrase, "entropy": round(entropy, 2),
                     "generated": datetime.now().isoformat()})


def action_check():
    pwd = input("Enter password to analyse: ").strip()
    if not pwd:
        print("⚠️  Nothing entered.")
        return
    r = check_password_strength(pwd)
    print(f"\n{'═'*55}")
    print(f"  Password Strength Analyser")
    print(f"{'─'*55}")
    print(f"  Strength  : {r['label']}")
    print(f"  Meter     : [{r['bar']}]  ({r['score']}/8 pts)")
    print(f"  Length    : {r['length']} chars")
    print(f"  Entropy   : {r['entropy']:.2f} bits")
    print(f"  Lowercase : {'✅' if r['has_lower'] else '❌'}")
    print(f"  Uppercase : {'✅' if r['has_upper'] else '❌'}")
    print(f"  Digits    : {'✅' if r['has_digit'] else '❌'}")
    print(f"  Specials  : {'✅' if r['has_special'] else '❌'}")
    if r["tips"]:
        print(f"\n  💡 Suggestions:")
        for tip in r["tips"]:
            print(f"     • {tip}")
    print(f"{'═'*55}")


def action_history():
    history = load_history()
    if not history:
        print("\n📝 No password history yet.")
        return
    print(f"\n{'═'*70}")
    print(f"  🕐 Last {min(10, len(history))} Generated Passwords")
    print(f"{'─'*70}")
    for entry in history[-10:][::-1]:
        ts = entry.get("generated", "—")[:16].replace("T", " ")
        print(f"  [{ts}]  {entry['type'].upper():<12} {entry['password'][:40]:<42} {entry['entropy']:.0f}b")
    print(f"{'═'*70}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("🔒  ENTERPRISE RANDOM PASSWORD GENERATOR  🔒")
    print("DecodeLabs Industrial Training Kit — Project 3")
    print("Batch: 2026  |  NIST 2024 Compliant  |  Cryptographically Secure")
    print("=" * 70)

    excl = input("\nExclude ambiguous characters (0,O,1,l,I)? (y/n) [default n]: ").strip().lower()
    generator = PasswordGenerator(exclude_ambiguous=(excl in ("y", "yes")))

    menu = {
        "1": ("🔑 Generate single password",           lambda: action_single(generator)),
        "2": ("📦 Generate batch of passwords",        lambda: action_batch(generator)),
        "3": ("🗝️  Generate passphrase",                lambda: action_passphrase(generator)),
        "4": ("🔍 Check password strength",            lambda: action_check()),
        "5": ("🕐 View generation history",            lambda: action_history()),
        "6": ("🚪 Exit",                               None),
    }

    while True:
        print("\n── Menu ──────────────────────────────────────────────────────────")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        print("──────────────────────────────────────────────────────────────────")
        choice = input("Enter choice: ").strip()

        if choice == "6":
            print("\n🔐 Stay secure! Goodbye from DecodeLabs!")
            break
        elif choice in menu:
            _, action = menu[choice]
            action()
        else:
            print("⚠️  Invalid choice. Please enter 1–6.")

if __name__ == "__main__":
    main()
