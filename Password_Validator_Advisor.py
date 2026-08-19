import string 

def checker(pas):
    if len(pas)<8:
        return f'Password should have at least eight characters'
    if not any(ch in string.ascii_uppercase for ch in pas):
         return f'Password must include at least one uppercase letter'
    if not any(ch in string.ascii_lowercase for ch in pas):
        return f'Password must include at least one lowercase letter'
    if not any(ch in string.digits for ch in pas):
        return 'Password must include at least one digit'
    if not any(ch in string.punctuation for ch in pas):
        return f'Password must include at least one special character'
    return 'Valid Password'

def strength(pas):
    score = 0

    conditions = [
        len(pas) >= 8,
        len(pas) >= 12,
        len(pas) >= 16,
        any(ch.isupper() for ch in pas),
        any(ch.islower() for ch in pas),
        any(ch.isdigit() for ch in pas),
        any(ch in string.punctuation for ch in pas),
        len(set(pas)) > len(pas) / 2
    ]

    score = sum(conditions)

    if score == 5:
        return "Weak"
    elif score <= 6:
        return "Moderate"
    elif score <= 7:
        return "Strong"
    else:
        return "Excellent"

def has_repeated_characters(pas):
    for ch in set(pas):
        if pas.count(ch) >=4:
            return True
    return False


def show_recommendations():
    print("\n----- PASSWORD SECURITY TIPS -----")
    print("1. Avoid commonly used passwords.")
    print("2. Avoid using the same character repeatedly.")
    print("3. Avoid predictable sequences, such as 123456 or abcdef.")
    print("4. Avoid common keyboard patterns, such as qwerty or asdfgh.")
    print("5. Avoid using easily guessable personal information.")




show_recommendations()
password=input("Enter your password")
result=checker(password)
if result != 'Valid Password':
    print(result)
else:
    print("Valid Password")
    print("Strength:",strength(password))

    if has_repeated_characters(password):
        print("Warning: Password contains too many repeated characters.")
    else:
        print("No excessive character repetition detected.")
