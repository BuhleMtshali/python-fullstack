## 👾 Mini Tip Calculator 🎰 (Day 3)

### 📌 Project Overview

- This is a simple Python Tip Calculator that helps users split a bill fairly, including a tip.

- The program waits a few seconds before starting (for ✨dramatic effect✨) and then asks the user for bill details, calculates the tip, and shows how much each person should pay.

- Built as part of Day 3 of my Python roadmap to practice:

- Functions

    - User input

    - Basic math operations

    - Using timers with threading


## 🛠️ Technologies Used

- Python 3

- threading module

## ⚙️ How It Works

1. The program displays a welcome message.

2. A 3-second delay is triggered using threading.Timer.

3. The user is prompted to enter:

    - Total bill amount

    - Number of people dining

    - Tip percentage

4. The program calculates:

    - Tip amount

    - Total bill including tip

    - Amount each person must pay

5. A clean bill summary is printed to the console.


## 🧮 Example Calculations

- If the bill is R500, tip is 10%, and 5 people are dining:

    - Tip Amount → R50

    - Total Bill → R550

    - Amount Per Person → R110

- No fights at the table. Everyone wins 😌🍽️


## ▶️ How to Run the Project

1. Make sure Python is installed:

```
python --version

```

2. Run the file:

```
python tip_calculator.py

```

3. Follow the prompts and enjoy the magic ✨


## 🧠 Key Concepts Practiced

- Python functions

- User input validation (basic)

- Arithmetic operations

- Delayed execution using threading.Timer

- Clean console output formatting


## 🚀 Future Improvements

- Input validation (no negative numbers, no zero people 🚨)

- Option to run the calculator again

- Currency formatting

- GUI or web version (👀 coming soon)

## 🏁 Final Thoughts

- This mini project helped reinforce core Python fundamentals while introducing delayed execution.
Simple, practical, and actually useful in real life.

#### On to Day 4 🐍🔥

Momentum = maintained.