def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/`~' for char in password)

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                        number_criteria, special_char_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = {
        "strength": strength,
        "length_ok": length_criteria,
        "uppercase_ok": uppercase_criteria,
        "lowercase_ok": lowercase_criteria,
        "number_ok": number_criteria,
        "special_char_ok": special_char_criteria,
    }

    return feedback

# Example usage:
password = input("Enter a password to assess its strength: ")
result = assess_password_strength(password)

print(f"Password Strength: {result['strength']}")
print("Feedback:")
print(f" - Length (>= 8): {'✔️' if result['length_ok'] else '❌'}")
print(f" - Uppercase: {'✔️' if result['uppercase_ok'] else '❌'}")
print(f" - Lowercase: {'✔️' if result['lowercase_ok'] else '❌'}")
print(f" - Number: {'✔️' if result['number_ok'] else '❌'}")
print(f" - Special Character: {'✔️' if result['special_char_ok'] else '❌'}")

