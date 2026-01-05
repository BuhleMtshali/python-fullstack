from datetime import date

print("=== Welcome to My Mini Age Calculator App👯‍♀️ ===")

today = date.today()

while True:
    
    name = input("Enter your name: ")

    year = int(input("Enter your birth year: "))

    month = int(input("Enter your birth month(1-12): "))

    day = int(input("Enter your birth date(1-31): "))

    birth_date = date(year, month, day)

    age = today.year - birth_date.year

    months_diff = birth_date.month - today.month 

    days_diff = today.day - birth_date.day

    if(today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    print(f"Hey {name}, you are currently {age}, {months_diff} months and {days_diff} days old!")

    runAgain = input("run again? (yes/no): ").lower()
    if runAgain != "yes":
        print("Thank you for trying my code!")
        break