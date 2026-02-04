# 🛒🎮 Mini Grocery Console Game — Day 7 🐝🔥

## 🌟 Overview

### This project is a Mini Grocery Console Game built in Python 🐍.

- It allows users to view, add, and remove grocery items from a shared cart using a menu-driven console interface.

- The app starts with a short delay ⏳ for dramatic effect and then runs continuously until the user decides to exit.

## 🎯 What This App Does 🧠✨

- 🛍️ View all items currently in the grocery cart

- 📦 Add new grocery items with:

    - Name

    - Quantity

    - Price per item

    - Total price (auto-calculated)

- 🚫 Remove items from the cart by name

- 🛡️ Prevent duplicate items from being added

- 🔁 Run multiple operations without restarting the program


## 🧩 Key Python Concepts Practiced 🐍

🧠 Functions for clean, reusable logic

🔁 while True loops for menu-driven programs

🎛️ match / case (Python switch statements)

📋 Lists of dictionaries for structured data

🔍 Searching and modifying lists safely

🛡️ Defensive programming (no duplicates, no crashes)

⏱️ Delayed execution using threading.Timer


## ⚙️ How the App Works 🛠️

1. ⏳ The program waits 3 seconds before starting

2. 📜 A menu is displayed:

```

1. View Grocery List 🛍️
2. Add Item 📦
3. Remove Item 🚫
4. Exit ‼️

```

3. 👤 The user selects an option

4. 🧠 The program performs the selected action

5. 🔁 The user can continue performing actions or exit cleanly


## 📦 Data Structure Used 🧺

- Each grocery item is stored as a dictionary:

```
{
  "name": "rice",
  "quantity": 30,
  "price each": 21,
  "total price": 630
}

```
- All items are stored inside a list:

```grocery_list = []```

## ▶️ Example Output 📤

```
=== 🧺 Item 1 ===
Name: rice
Quantity: 30
Price each: 21
Total price: 630
------------------------------

```

## 🧠 What I Learned 🏆

- How to safely modify lists without causing infinite loops 🔥

- Why you should never modify a list while looping over it

- How to track whether an item exists using flags (found)

- How to build real console apps with proper flow control

- This project was a BIG logic upgrade 💪🐍


## 🌱 Possible Improvements 🌈

- Future upgrades could include:

    - 🔢 Input validation (try/except)

    - 🔄 Update item quantity instead of blocking duplicates

    - 💰 Cart subtotal & grand total

    - 💾 Save cart data to a file

    - 🖼️ GUI or web version 👀

## 🏁 Final Thoughts 🐝✨

- This project ties together everything learned so far:

    - Loops 🔁

    - Functions 🧩

    - Data structures 📋

    - User interaction 🎮

```It’s messy behind the scenes sometimes — but that’s real programming 😌🔥```

### Day 7 = COMPLETE ✅

```On to Day 8… things are about to get spicy 🌶️🐍```