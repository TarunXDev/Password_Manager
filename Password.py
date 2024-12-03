import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Build a pool of characters based on the selected complexity
    char_pool = lower_case
    if 'upper' in complexity:
        char_pool += upper_case
    if 'digit' in complexity:
        char_pool += digits
    if 'special' in complexity:
        char_pool += special_chars

    # Generate password by randomly selecting characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

# Prompt the user for input with validation
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        break
    except ValueError as e:
        print(e)

while True:
    complexity = input("Enter the desired complexity (options: 'upper', 'digit', 'special') separated by commas: ").lower().split(',')
    valid_complexities = ['upper', 'digit', 'special']
    if all(option in valid_complexities for option in complexity):
        break
    else:
        print("Invalid complexity options. Please use 'upper', 'digit', and/or 'special'.")

# Generate and display the password
password = generate_password(length, complexity)
print("Generated Password:", password)
