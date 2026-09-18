import re

common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "password123",
    "admin",
    "welcome",
    "abc123",
    "letmein",
    "iloveyou"
]

def check_password(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Check common password
    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common passwords.")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


print("===================================")
print("     PASSWORD STRENGTH ANALYZER")
print("===================================")

password = input("Enter your password: ")

strength, suggestions = check_password(password)

print("\nPassword Strength:", strength)
print("Password Length:", len(password))

if suggestions:
    print("\nSuggestions to improve your password:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nYour password meets all basic security requirements.")