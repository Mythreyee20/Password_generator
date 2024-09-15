import random
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation),
    ]

    all_characters = lowercase + uppercase + digits + punctuation
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    try:
        password_length = 12  
        print("Generated Password:", generate_password(password_length))
    except ValueError as e:
        print(e)
