# Password Generator

import random
import string

# Ask user how long the password should be
length = int(input("Enter desired password length: "))

# Create a pool of characters: letters, digits, symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Randomly choose characters
password = ''.join(random.choice(characters) for _ in range(length))

print(f"Generated password: {password}")
