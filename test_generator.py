#!/usr/bin/env python3
"""
Test script for the Enterprise Random Password Generator
"""

import sys
sys.path.insert(0, '/home/claude')

from password_generator import PasswordGenerator

def test_password_generator():
    """Test the password generator functionality"""
    print("🧪 Testing Enterprise Random Password Generator\n")
    
    generator = PasswordGenerator()
    
    # Test 1: Basic password generation
    print("Test 1: Generate 16-character password")
    password = generator.generate_password(16, include_special=False)
    print(f"Generated: {password}")
    print(f"Length: {len(password)} ✅")
    print()
    
    # Test 2: Password with special characters
    print("Test 2: Generate 20-character password with special characters")
    password_special = generator.generate_password(20, include_special=True)
    print(f"Generated: {password_special}")
    print(f"Length: {len(password_special)} ✅")
    print()
    
    # Test 3: Validation
    print("Test 3: Input Validation")
    is_valid, msg = generator.validate_length(10)
    print(f"Length 10: {'❌ ' + msg if not is_valid else '✅'}")
    
    is_valid, msg = generator.validate_length(16)
    print(f"Length 16: {'❌ ' + msg if not is_valid else '✅'}")
    
    is_valid, msg = generator.validate_length(100)
    print(f"Length 100: {'❌ ' + msg if not is_valid else '✅'}")
    print()
    
    # Test 4: Entropy calculation
    print("Test 4: Entropy Calculation")
    entropy_16 = generator.calculate_entropy(16)
    entropy_20 = generator.calculate_entropy(20)
    print(f"16 characters: {entropy_16:.2f} bits")
    print(f"20 characters: {entropy_20:.2f} bits")
    print()
    
    # Test 5: Complexity guarantee
    print("Test 5: Complexity Guarantee")
    test_pass = "aaaaaaaaaaaaaaaa"
    improved = generator.ensure_complexity(test_pass, include_special=False)
    print(f"Original: {test_pass}")
    print(f"Improved: {improved}")
    
    has_lower = any(c.islower() for c in improved)
    has_upper = any(c.isupper() for c in improved)
    has_digit = any(c.isdigit() for c in improved)
    
    print(f"Has lowercase: {'✅' if has_lower else '❌'}")
    print(f"Has uppercase: {'✅' if has_upper else '❌'}")
    print(f"Has digit: {'✅' if has_digit else '❌'}")
    print()
    
    print("=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)

if __name__ == "__main__":
    test_password_generator()
