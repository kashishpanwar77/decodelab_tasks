import random
import string


def generate_password(length, use_symbols=True):
    if length < 4:
        print("Password length should be at least 4.")
        return None

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits)
    ]

    characters = uppercase + lowercase + digits

    if use_symbols:
        password.append(random.choice(symbols))
        characters += symbols

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)


def main():
    print("=" * 40)
    print("     RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    choice = input("Include special characters? (yes/no): ").lower()

    if choice == "yes":
        password = generate_password(length, True)
    else:
        password = generate_password(length, False)

    if password:
        print("\nGenerated Password:")
        print(password)


if __name__ == "__main__":
    main()
