from datetime import datetime
import time


def display_current_datetime():
    now = datetime.now()
    print("\nCurrent Date and Time:")
    print(now.strftime("%d-%m-%Y %I:%M:%S %p"))


def date_difference():
    date1 = input("Enter first date (YYYY-MM-DD): ")
    date2 = input("Enter second date (YYYY-MM-DD): ")

    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    diff = abs((d2 - d1).days)
    print("Difference:", diff, "days")


def custom_format():
    now = datetime.now()
    print("Format 1:", now.strftime("%d/%m/%Y"))
    print("Format 2:", now.strftime("%A, %d %B %Y"))
    print("Format 3:", now.strftime("%I:%M:%S %p"))


def stopwatch():
    input("Press Enter to start...")
    start = time.time()

    input("Press Enter to stop...")
    end = time.time()

    print("Elapsed Time:", round(end - start, 2), "seconds")


def countdown_timer():
    sec = int(input("Enter seconds: "))

    while sec > 0:
        print(sec)
        time.sleep(1)
        sec -= 1

    print("Time's Up!")