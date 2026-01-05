## 🐍 Day 2 – Mini Age Calculator App

### 📌 Overview

Day 2 was all about user input, the date object, and basic calculations in Python.

- The goal for today:

- Ask the user for their name and birthdate

- Calculate their current age

- Display the result in a friendly message

- Practice loops to allow re-running the program

## 🧠 What I Learned

- How to use input() to get strings and numbers from users

- How to use the datetime.date object to work with calendar dates

- How to calculate age by subtracting years and checking if the birthday has passed this year

- How to loop programs for multiple runs

- How to format strings with f-strings for readable output


## 🧪 Code Example

```
from datetime import date

print("=== Welcome to My Mini Age Calculator App👯‍♀️ ===")

today = date.today()

while True:
    name = input("Enter your name: ").strip()
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month (1-12): "))
    day = int(input("Enter your birth date (1-31): "))

    birth_date = date(year, month, day)
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    print(f"Hey {name}, you are currently {age} years old!")

    run_again = input("Run again? (yes/no): ").lower()
    if run_again != "yes":
        print("Thank you for trying my code!")
        break


```

## 🔍 How It Works

1. The program gets the current date with date.today().

2. It asks the user for their birth year, month, and day.

3. It calculates age:

    - age = today.year - birth_date.year

    - If birthday hasn’t happened yet this year, subtract 1.

4. It prints a friendly message with the user’s name and age.

5. It loops until the user decides to quit.


## 🎯 Why This Matters

- Shows the power of variables + user input

- Introduces Python’s date/time manipulation

- Demonstrates control flow with loops

- Lays groundwork for more advanced apps (like diaries, trackers, and games)

## 🔥 Next Steps (Day 3)

- Validate user input properly (try/except)

- Calculate age in years, months, and days accurately

- Explore functions to organize your code

## ✨ Status

### Day 2 Complete ✅

Mindset: Learning how Python interacts with real-world input — next stop, mastering control flow and functions!