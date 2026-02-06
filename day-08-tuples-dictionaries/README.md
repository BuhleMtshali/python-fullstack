# 📞🔖 Phone Book Console App — Mini Project 🐝✨

## 🌟 Overview

- This project is a Phone Book Console Application built with Python 🐍.

- It allows users to store, view, and remove contacts using a menu-driven interface — just like a tiny CLI version of a real phone book 📱📋.

- The app starts with a short delay ⏳ for dramatic effect and then runs continuously until the user chooses to exit.

## 🎯 What This App Can Do 🎮

- 👥 Add contacts with:

    - Name

    - Relationship

    - Phone number

- 📋 View all saved contacts in a clean, readable format

- 🚫 Remove contacts by name

- 🛡️ Prevent duplicate entries

- 🔁 Perform multiple actions without restarting the program


## 🧠 Python Concepts Practiced 🐍

- 🧩 Functions for modular logic

- 🔁 while True loops for menu systems

- 🎛️ match / case (Python switch statements)

- 📋 Lists of dictionaries for structured data

- 🔍 Searching and modifying lists safely

- 🛡️ Defensive programming (duplicate checks & safe removal)

- ⏱️ Delayed execution using threading.Timer


## 📦 Data Structure Used 📒

- Each contact is stored as a dictionary:

```

{
  "name": "alex",
  "relationship": "friend",
  "number": 0812345678
}

```

- All contacts live inside a list:

```

contact_book = []

```
- This structure makes the app easy to scale and maintain 🚀


## ⚙️ How the App Works 🛠️

1. ⏳ The app waits 3 seconds before starting

2. 📜 A menu is displayed:

```
1. View contact book 🪪
2. Add Contact 👥
3. Remove Contact 🐝
4. Exit 🚫

```

3. 👤 User selects an option

4. 🧠 The app performs the selected action

5. 🔁 User can continue or exit gracefully

## 📤 Example Output

```

===== 🎮 Number 1 =======
👾 Name: mom
👾 Relationship: family
👾 Number: 0812345678
------------------------------

```
- Clean. Readable. No confusion 😌✨

## 🏆 What I Learned

- How to manage collections of structured data

- Why dictionaries are better than tuples for real-world records

- How to safely remove items from a list

- How to design menu-driven console applications

- How small logic mistakes (like typos or indentation) can break programs

- This project was a big logic confidence boost 💪🐍

## 🌱 Future Improvements 🌈

- Possible upgrades:

    - 🔢 Input validation using try/except

    - ✏️ Update contact details

    - 💾 Save contacts to a file

    - 🔍 Search contacts by name or relationship

    - 🖼️ GUI or web version 👀


## 🏁 Final Thoughts 🐝✨

- This app brings together:

- Loops 🔁

- Functions 🧩

- Data structures 📋

- User interaction 🎮

- It’s not just practice — it’s real programming fundamentals in action.

### Mini Phone Book App = COMPLETE ✅🔥

Onwards to the next level 🚀🐍