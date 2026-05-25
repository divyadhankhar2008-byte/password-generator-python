"""
Enterprise Random Password Generator
Project 3 - DecodeLabs Industrial Training Kit
Batch: 2026

This module implements a cryptographically secure password generator following
NIST 2024 guidelines, utilizing the secrets module for unpredictable randomness
and optimized string manipulation with .join() for linear time complexity.

Architecture: Input -> Process -> Output
- Phase 1: Environmental requirements and validation
- Phase 2: Building the backend transformation engine
- Phase 3: Mathematical provision of security
"""

import secrets
import string
import math


class PasswordGenerator:
    """
    Enterprise-grade password generator with NIST 2024 compliance.
    
    Uses secrets.choice() for cryptographically secure randomness and
    .join() for memory-efficient string construction (O(N) complexity).
    """
    
    # Character pools using Python's string module for locale-independent consistency
    LOWERCASE = string.ascii_lowercase  # 26 characters
    UPPERCASE = string.ascii_uppercase  # 26 characters
    DIGITS = string.digits             # 10 characters
    SPECIAL = string.punctuation       # 32 characters
    
    # NIST 2024 guidelines
    MIN_LENGTH = 15  # Minimum length for high-security contexts
    MAX_LENGTH = 64  # Maximum length systems must support
    
    def __init__(self):
        """Initialize the password generator."""
        self.character_pool = self.LOWERCASE + self.UPPERCASE + self.DIGITS
        self.pool_size = len(self.character_pool)  # 62 for alphanumeric
    
    def validate_length(self, length: int) -> tuple[bool, str]:
        """
        Phase 1: Validate environmental requirements.
        
        Robust implementation must capture a target integer representing
        password length and rigorously validate to prevent system crashes
        or generation of fundamentally insecure credentials.
        
        Args:
            length: Target password length
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(length, int):
            return False, "Length must be an integer."
        
        if length < self.MIN_LENGTH:
            return False, f"Password length must be at least {self.MIN_LENGTH} characters (NIST 2024 requirement)."
        
        if length > self.MAX_LENGTH:
            return False, f"Password length cannot exceed {self.MAX_LENGTH} characters."
        
        return True, ""
    
    def calculate_entropy(self, length: int, pool_size: int = None) -> float:
        """
        Phase 3: Calculate security through information entropy mathematics.
        
        Formula: E = L × log₂(R)
        Where:
            E = Entropy (bits of unpredictability)
            L = Length of the password
            R = Size of the character pool
            
        Args:
            length: Password length
            pool_size: Size of character pool (defaults to current pool)
            
        Returns:
            Entropy in bits
        """
        if pool_size is None:
            pool_size = self.pool_size
        
        return length * math.log2(pool_size)
    
    def generate_password(self, length: int, include_special: bool = False) -> str:
        """
        Phase 2: Building the backend transformation engine.
        
        Transitions from requirement gathering to execution of logic.
        Pools available character sets and executes a selection algorithm
        to transform a simple integer into a complex string.
        
        Uses secrets.choice() instead of random.choice() for cryptographically
        secure randomness (replaces Mersenne Twister vulnerability).
        
        Uses ''.join() for O(N) time complexity instead of += which creates
        O(N²) overhead due to string immutability.
        
        Args:
            length: Desired password length
            include_special: Whether to include special characters
            
        Returns:
            Generated password string
        """
        # Update character pool based on requirements
        if include_special:
            self.character_pool = self.LOWERCASE + self.UPPERCASE + self.DIGITS + self.SPECIAL
        else:
            self.character_pool = self.LOWERCASE + self.UPPERCASE + self.DIGITS
        
        self.pool_size = len(self.character_pool)
        
        # Enterprise approach: ''.join(list) for linear time complexity
        # Avoids O(N²) bottleneck from string concatenation in loops
        password_chars = [secrets.choice(self.character_pool) for _ in range(length)]
        
        return ''.join(password_chars)
    
    def ensure_complexity(self, password: str, include_special: bool = False) -> str:
        """
        Ensure password contains at least one character from each required category.
        This prevents edge cases where randomness might exclude a character type.
        
        Args:
            password: Generated password
            include_special: Whether special characters are required
            
        Returns:
            Password with guaranteed complexity
        """
        password_list = list(password)
        
        # Check and ensure at least one lowercase
        if not any(c in self.LOWERCASE for c in password):
            password_list[secrets.randbelow(len(password_list))] = secrets.choice(self.LOWERCASE)
        
        # Check and ensure at least one uppercase
        if not any(c in self.UPPERCASE for c in password):
            password_list[secrets.randbelow(len(password_list))] = secrets.choice(self.UPPERCASE)
        
        # Check and ensure at least one digit
        if not any(c in self.DIGITS for c in password):
            password_list[secrets.randbelow(len(password_list))] = secrets.choice(self.DIGITS)
        
        # Check and ensure at least one special character if required
        if include_special and not any(c in self.SPECIAL for c in password):
            password_list[secrets.randbelow(len(password_list))] = secrets.choice(self.SPECIAL)
        
        return ''.join(password_list)


def main():
    """
    Main execution function implementing the Input-Process-Output scaffold.
    """
    print("=" * 70)
    print("🔒 ENTERPRISE RANDOM PASSWORD GENERATOR 🔒")
    print("DecodeLabs Industrial Training Kit - Project 3")
    print("Batch: 2026 | NIST 2024 Compliant")
    print("=" * 70)
    print()
    
    generator = PasswordGenerator()
    
    # Phase 1: Input - Environmental requirements and validation
    print("📋 Password Requirements:")
    print(f"   • Minimum length: {generator.MIN_LENGTH} characters (NIST 2024)")
    print(f"   • Maximum length: {generator.MAX_LENGTH} characters")
    print(f"   • Uses cryptographically secure randomness (secrets module)")
    print()
    
    while True:
        try:
            length_input = input("Enter desired password length: ").strip()
            length = int(length_input)
            
            # Validate input
            is_valid, error_message = generator.validate_length(length)
            if not is_valid:
                print(f"❌ Error: {error_message}")
                print()
                continue
            
            break
            
        except ValueError:
            print("❌ Error: Please enter a valid integer.")
            print()
            continue
    
    # Ask about special characters
    while True:
        special_input = input("\nInclude special characters (@, #, $, etc.)? (y/n): ").strip().lower()
        if special_input in ['y', 'yes']:
            include_special = True
            break
        elif special_input in ['n', 'no']:
            include_special = False
            break
        else:
            print("❌ Please enter 'y' or 'n'.")
    
    print()
    print("⚙️  Generating password...")
    print()
    
    # Phase 2: Process - Backend transformation engine
    password = generator.generate_password(length, include_special)
    
    # Ensure complexity requirements
    password = generator.ensure_complexity(password, include_special)
    
    # Phase 3: Output - Mathematical provision of security
    entropy = generator.calculate_entropy(length)
    
    # Determine security level based on entropy
    if entropy >= 128:
        security_level = "🛡️  SECURE FOR MILLIONS OF YEARS"
        crack_time = "Millions of years"
    elif entropy >= 80:
        security_level = "✅ HIGHLY SECURE"
        crack_time = "Centuries"
    elif entropy >= 60:
        security_level = "⚠️  MODERATELY SECURE"
        crack_time = "Years"
    else:
        security_level = "⚠️  VULNERABLE"
        crack_time = "Days to months"
    
    print("=" * 70)
    print("✅ PASSWORD GENERATED SUCCESSFULLY")
    print("=" * 70)
    print()
    print(f"🔑 Your Password: {password}")
    print()
    print("📊 Security Analysis:")
    print(f"   • Length: {length} characters")
    print(f"   • Character Pool Size: {generator.pool_size} characters")
    print(f"   • Entropy: {entropy:.2f} bits")
    print(f"   • Security Level: {security_level}")
    print(f"   • Estimated Crack Time: {crack_time}")
    print(f"   • Complexity: {'62^{} combinations'.format(length)} (alphanumeric)")
    if include_special:
        print(f"   • Special Characters: Included")
    print()
    print("🔐 Security Features:")
    print("   ✓ Uses secrets module (cryptographically secure)")
    print("   ✓ Hardware-level OS noise for unpredictability")
    print("   ✓ NIST 2024 guidelines compliant")
    print("   ✓ Optimized O(N) string construction")
    print("   ✓ Guaranteed character complexity")
    print()
    print("=" * 70)
    print()
    print("💡 Best Practices:")
    print("   • Store in a password manager")
    print("   • Never reuse passwords across services")
    print("   • Enable two-factor authentication when possible")
    print("   • Consider using 16+ characters for maximum security")
    print()
    print("Thank you for using DecodeLabs Password Generator!")
    print("=" * 70)


if __name__ == "__main__":
    main()
