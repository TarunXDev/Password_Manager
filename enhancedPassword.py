import random
import string

def generate_password(length, complexity, exclude_chars=None):
    
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    
    char_pool = lower_case
    if 'upper' in complexity:
        char_pool += upper_case
    if 'digit' in complexity:
        char_pool += digits
    if 'special' in complexity:
        char_pool += special_chars

    
    if exclude_chars:
        char_pool = ''.join(c for c in char_pool if c not in exclude_chars)

    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length (positive integer): "))
            if length <= 0:
                print("Error: Length must be a positive integer.")
            else:
                return length
        except ValueError:
            print("Error: Please enter a valid number for length.")

def get_complexity_options():
    valid_complexities = ['upper', 'digit', 'special']
    while True:
        complexity_input = input("Enter the desired complexity (options: 'upper', 'digit', 'special') separated by commas: ").lower().split(',')
        if all(option in valid_complexities for option in complexity_input):
            return complexity_input
        else:
            print("Error: Invalid complexity options. Please choose from 'upper', 'digit', and 'special'.")

def get_excluded_characters():
    exclude_input = input("Enter any characters you want to exclude (optional): ").strip()
    return exclude_input if exclude_input else None

def password_strength_indicator(password):
    
    if len(password) < 8:
        return "Weak"
    elif len(password) >= 8 and len(password) < 12:
        return "Moderate"
    else:
        return "Strong"

def main():
    print("Welcome to the Password Generator!")
    print("This tool will help you generate a strong and secure password.")

    
    length = get_password_length()

    
    complexity = get_complexity_options()

    
    excluded_chars = get_excluded_characters()

    
    password = generate_password(length, complexity, excluded_chars)

    
    print("\nGenerated Password:", password)
    print("Password Strength:", password_strength_indicator(password))

    print("\nThank you for using the Password Generator!")


if __name__ == "__main__":
    main()
