import re
import string

def password_strength_checker(password):
    score = 0
    feedback = []

    # Length Check
    length = len(password)
    if length < 8:
        feedback.append("Password is too short. Consider using at least 8 characters.")
    elif 8 <= length < 12:
        score += 1
        feedback.append("Good length, but longer passwords are more secure.")
    else:
        score += 2
        feedback.append("Excellent length.")

    # Complexity Checks
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters to increase complexity.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters to increase complexity.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers to increase complexity.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters to increase complexity.")

    # Uniqueness Check
    unique_chars = len(set(password))
    if unique_chars < length / 2:
        feedback.append("Avoid using repeated characters to increase uniqueness.")
    else:
        score += 1

    # Strength Assessment
    if score <= 2:
        strength = "Weak"
    elif 3 <= score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    result = password_strength_checker(password)
    print(f"\nPassword Strength: {result['strength']}")
    print("Feedback:")
    for item in result['feedback']:
        print(f"- {item}")

if __name__ == "__main__":
    main()
