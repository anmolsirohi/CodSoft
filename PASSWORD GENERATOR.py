import random
import string

def generate_password(length):
    # Creating a string of possible characters: letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # Using random.choice to build a password of desired length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        # Ask the user to input the desired password length
        user_input = input("Enter the length of the password you want to generate: ")
        length = int(user_input)

        if length <= 0:
            print("Please enter a positive number greater than zero.")
            return

        # Call the password generator function
        new_password = generate_password(length)

        # Show the generated password to the user
        print(f"\nHere is your generated password:\n{new_password}")

    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()