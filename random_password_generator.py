import random
import string

# Define Character Sets
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation

# Combine Character Sets
all_characters = uppercase_letters + lowercase_letters + digits + special_characters

# Define Password Length
password_length = int(input("Enter the desired password length: "))

# Generate Password
password = ''.join(random.choice(all_characters) for _ in range(password_length))

# Output the Password
print("Generated Password: ", password)