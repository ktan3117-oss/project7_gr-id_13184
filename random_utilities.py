import random
import string


def random_number():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    print("Random Number:", random.randint(start, end))


def random_list():
    numbers = random.sample(range(1, 101), 10)
    print("Random List:", numbers)


def random_password():
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + "!@#$%"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)


def random_otp():
    otp = random.randint(100000, 999999)
    print("Generated OTP:", otp)