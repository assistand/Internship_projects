import random
import string

def generate_password(length=12):
    
    
    characters = string.ascii_letters  
    
    digits = string.digits  
    
    symbols = "!@#$%^&*()_-+=<>?/[]{}|"

    all_characters = characters + digits + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


password = generate_password(16)
print("Your password :")
print(password)
