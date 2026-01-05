from datetime import date

print("=== Welcome to My Mini Age Calculator App👯‍♀️ ===")

today = date.today()

while True:
    
    name = input("Enter your name: ")

    year = int(input("Enter your birth year: "))

    month = int(input("Enter your birth month(1-12): "))

    day = int(input("Enter your birth date(1-31): "))

    runAgain = input("run again? (yes/no): ").lower()
    if runAgain != "yes":
        print("Thank you for trying my code!")
        break