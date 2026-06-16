import math


def factorial_calculation():
    n = int(input("Enter number: "))
    print("Factorial:", math.factorial(n))


def compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate (%): "))
    t = float(input("Enter time (years): "))

    amount = p * ((1 + r / 100) ** t)
    print("Compound Interest Amount:", round(amount, 2))


def trigonometry():
    degree = float(input("Enter angle in degrees: "))
    rad = math.radians(degree)

    print("Sin:", round(math.sin(rad), 2))
    print("Cos:", round(math.cos(rad), 2))
    print("Tan:", round(math.tan(rad), 2))


def area_shapes():
    print("1. Circle")
    print("2. Rectangle")
    choice = input("Enter choice: ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        area = math.pi * radius ** 2
        print("Area:", round(area, 2))

    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area:", length * width)