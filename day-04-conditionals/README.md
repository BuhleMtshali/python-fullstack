# **🎓🕯️ Scholarship Eligibility Checker — Day 4 🐍🚀**

## **🌟 Overview**

Welcome to my **🎓 Scholarship Eligibility Checker!**

For Day 4 of my **100 Days of Python 🐍🔥**, I built a program that checks whether a student qualifies for a scholarship based on their:

* 👤 Age
* 🎓 GPA
* 💰 Annual family income

The program uses **conditional statements** to make decisions based on the information entered by the user.

It also runs inside a loop 🔁, allowing users to check multiple applicants without restarting the program.

---

## **🎯 What I Learned 🧠✨**

This project helped me understand how Python can make decisions using:

* 🧠 `if` statements
* 🔀 `elif` statements
* 🚪 `else` statements
* 🔗 Logical operators such as `and` and `or`
* 🔢 Comparing numbers with operators like `<`, `>`, and `>=`
* 🔄 `while True` loops for repeated interaction
* 🎭 `.lower()` for handling different forms of user input
* 🧱 Functions for organizing code
* ⌨️ `input()` for collecting information from users
* 🔄 Type conversion using `int()` and `float()`
* ⏱️ `threading.Timer` for delayed program execution

---

## **⚙️ How the Program Works 🛠️**

### **1. ⏳ Program Startup**

The program displays a welcome message and uses `threading.Timer` to wait **3 seconds** before starting the eligibility checker.

```python
timer = threading.Timer(3, scholarship_eligibility_checker)
timer.start()
```

A little dramatic entrance never hurt anybody. 😭🎬

---

### **2. 👤 User Enters Applicant Information**

The program asks the user for:

* 👤 Full name
* 🎂 Age
* 🎓 GPA out of 4.0
* 💰 Annual family income

The inputs are converted into the appropriate data types:

```python
age = int(input("What is your age: "))

gpa = float(input("Enter your GPA (out of 4.0): "))

income = float(input("Enter your annual family income (R): "))
```

This allows Python to perform numerical comparisons with the information.

---

### **3. 🧠 Python Checks Eligibility**

The program uses conditional logic to determine which scholarship category the applicant qualifies for.

### 🚫 Age Requirement

If the applicant is younger than 16 or older than 30:

```python
if age < 16 or age > 30:
```

The applicant is considered ineligible based on the age requirement.

---

### 🏆 Full Scholarship

If the applicant meets the following requirements:

* Age is within the allowed range
* GPA is at least `3.8`
* Family income is below `R500,000`

Python checks:

```python
elif gpa >= 3.8 and income < 500000:
```

The applicant qualifies for the **Full Scholarship**.

---

### 🥈 Partial Scholarship

If the applicant does not qualify for the full scholarship but has:

* GPA of at least `3.4`
* Family income below `R600,000`

Python checks:

```python
elif gpa >= 3.4 and income < 600000:
```

The applicant qualifies for the **Partial Scholarship**.

---

### ❌ No Scholarship

If none of the previous conditions are satisfied:

```python
else:
```

The program informs the applicant that they do not currently meet the scholarship criteria.

---

## **🔁 Repeating the Program**

After checking an applicant, the program asks:

```text
🕹️ Wanna check again? (yes/no):
```

The `.lower()` method converts the answer to lowercase:

```python
runAgain = input(...).lower()
```

This means inputs such as:

```text
YES
Yes
yes
```

can all be treated as:

```text
yes
```

If the user enters anything other than `"yes"`, the loop stops.

```python
if runAgain != "yes":
    break
```

---

## **🧩 Key Python Concepts Used 🐍**

| Concept           | What I Used It For                                  |
| ----------------- | --------------------------------------------------- |
| `if`              | Checking the first eligibility condition            |
| `elif`            | Checking alternative scholarship conditions         |
| `else`            | Handling applicants who don't meet the requirements |
| `and`             | Requiring multiple conditions to be true            |
| `or`              | Allowing either age condition to trigger            |
| `>=`              | Checking minimum GPA requirements                   |
| `<`               | Checking income and age limits                      |
| `!=`              | Checking whether the user wants to continue         |
| `while True`      | Repeating the eligibility checker                   |
| `break`           | Exiting the loop                                    |
| `input()`         | Collecting applicant information                    |
| `int()`           | Converting age into an integer                      |
| `float()`         | Converting GPA and income into decimals             |
| `.lower()`        | Normalizing user input                              |
| Functions         | Keeping the eligibility logic organized             |
| `threading.Timer` | Delaying program execution                          |

---

## **🛡️ Eligibility Logic**

The decision-making structure of the program is:

```text
                    👤 Applicant
                         │
                         ▼
                  Is age 16–30?
                    /       \
                  ❌         ✅
                  │          │
              Not eligible   ▼
                       Is GPA ≥ 3.8
                       AND income < R500k?
                         /       \
                       ✅         ❌
                       │           │
                🏆 Full           ▼
                             Is GPA ≥ 3.4
                             AND income < R600k?
                               /       \
                             ✅         ❌
                             │           │
                       🥈 Partial       ❌ No Scholarship
```

This was my first real project where I used **multiple conditions together to make decisions**. 🧠🔥

---

## **▶️ How to Run 💻**

Make sure Python is installed.

Run the program from the terminal:

```bash
python scholarship_eligibility_checker.py
```

The program will display the welcome message, wait 3 seconds, and then start the scholarship eligibility checker. ⏳🎓

---

## **🌱 Future Upgrades**

There are a few things I could improve as my Python skills grow:

* 🛡️ Add error handling for invalid age, GPA, and income inputs
* 📊 Add more scholarship categories
* 📋 Display a formatted eligibility summary
* 💾 Save applicant results to a file
* 📈 Track how many applicants qualify for each scholarship
* 🧪 Add tests for different eligibility scenarios
* 🗃️ Store applicant information using data structures
* 🖥️ Eventually build a GUI version

---

## **🏁 Final Thoughts 🏆**

This project helped me understand one of the most important ideas in programming:

> **Programs can make decisions based on conditions. 🧠**

Instead of simply running every instruction from top to bottom, Python can evaluate information and choose what should happen next.

I practiced using:

* `if` ✅
* `elif` ✅
* `else` ✅
* `and` ✅
* `or` ✅
* Comparison operators ✅
* Loops 🔁
* Functions 🧱
* User input ⌨️

The project started as a simple eligibility checker, but it gave me a proper introduction to **decision-making in Python**.

### **Day 4 = COMPLETED ✅🔥**

🐍 **4 Days Down. 96 To Go.**

**Onwards, Python warrior 🚀**
