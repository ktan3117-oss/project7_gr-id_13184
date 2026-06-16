from utilities import *


def datetime_menu():
    while True:
        print("\n===== Datetime Operations =====")
        print("1. Display Current Date and Time")
        print("2. Date Difference")
        print("3. Custom Date Format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            display_current_datetime()

        elif choice == "2":
            date_difference()

        elif choice == "3":
            custom_format()

        elif choice == "4":
            stopwatch()

        elif choice == "5":
            countdown_timer()

        elif choice == "6":
            break


def math_menu():
    while True:
        print("\n===== Mathematical Operations =====")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Shapes")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            factorial_calculation()

        elif choice == "2":
            compound_interest()

        elif choice == "3":
            trigonometry()

        elif choice == "4":
            area_shapes()

        elif choice == "5":
            break


def random_menu():
    while True:
        print("\n===== Random Operations =====")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            random_number()

        elif choice == "2":
            random_list()

        elif choice == "3":
            random_password()

        elif choice == "4":
            random_otp()

        elif choice == "5":
            break


def file_menu():
    while True:
        print("\n===== File Operations =====")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            write_file()

        elif choice == "3":
            read_file()

        elif choice == "4":
            append_file()

        elif choice == "5":
            break


def main():
    while True:
        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            generate_uuid()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("Thank you for using Multi-Utility Toolkit.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()