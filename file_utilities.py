
import os


def create_file():
    filename = input("Enter file name: ")

    with open(filename, "w") as file:
        pass

    print("File created successfully.")


def write_file():
    filename = input("Enter file name: ")
    data = input("Enter data: ")

    with open(filename, "w") as file:
        file.write(data)

    print("Data written successfully.")


def read_file():
    filename = input("Enter file name: ")

    if os.path.exists(filename):
        with open(filename, "r") as file:
            print("\nFile Content:")
            print(file.read())
    else:
        print("File does not exist.")


def append_file():
    filename = input("Enter file name: ")
    data = input("Enter data: ")

    with open(filename, "a") as file:
        file.write("\n" + data)

    print("Data appended successfully.")