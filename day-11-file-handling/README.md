# 🎬 Mini Movie Wishlist (Day 7)

## 📌 Project Overview

### Welcome to my Mini Movie Wishlist project! 🍿

- This Python program allows users to continuously add movies to a wishlist and saves them into a CSV file for persistent storage.

- The user can:

    - Add a movie ranking number

    - Enter the movie name

    - Provide the release year

    - View the full wishlist after each entry

- All movie entries are stored in a movie_list.csv file, meaning the data is saved even after the program ends 💾

## 🚀 Features

✨ Create a CSV file with headers

✨ Continuously add movies using a loop

✨ Store data permanently using append mode

✨ Display the updated movie wishlist after each addition

✨ Simple and interactive CLI experience

## 🚀 Features

✨ Create a CSV file with headers

✨ Continuously add movies using a loop

✨ Store data permanently using append mode

✨ Display the updated movie wishlist after each addition

✨ Simple and interactive CLI experience

## 💻 Code Implementation

```

import csv

print("======== 🐝 Welcome to My Mini Movie Wishlist Project ======")

# CREATING CSV FILE AND THE HEADER ONCE
with open('movie_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie Name", "Year"])

# STARTING THE WHILE LOOP SO THE PERSON CAN KEEP ADDING A MOVIE
while True:
    ranking_number = int(input("What number is this movie ranking: "))
    movie_name = input("Enter the movie name: ").lower()
    movie_year = input("Enter the movie publication year: ")
    
    # OPEN FILE IN APPEND MODE
    with open('movie_list.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ranking_number, movie_name, movie_year])
        
    # READING THE FILE
    with open('movie_list.csv', 'r') as file:
        reader = csv.reader(file)
        print("\n🎥 Your Movie Wishlist: ")
        for row in reader:
            print(row)
    
    addAgain = input("Would you like to add another movie (yes/no): ").lower()
    if addAgain == "no":
        print("====== Thank you for Trying My Mini Movie Wishlist =====")
        break

```

## 🧠 Key Concepts Learned

- This project helped me understand:

    - File handling in Python 📁

    - Writing data using CSV writer

    - Appending vs overwriting files ('a' vs 'w')

    - Using loops for continuous user interaction 🔁

    - Reading and displaying stored data

## 🧩 Challenges Faced

- One major issue I encountered was trying to write to a CSV file after it had already been closed.

- I fixed this by reopening the file in append mode ('a') inside the loop, ensuring new entries were added correctly without overwriting existing data.

## 🌱 Future Improvements

- Add input validation using try-except

- Allow deleting movies from the list

- Prevent duplicate rankings

- Format output nicely in table form

- Convert into a GUI app later 🎨

## 🎯 Project Goal

- The goal of this project was to practice:

    - Persistent data storage

    - User input handling

    - Loops and file operations

- This is part of my Full-Stack Software Engineering Roadmap (Day 7) 🚀

## 🪄 Final Thoughts

- This project marks my first step into building programs that remember data instead of forgetting everything once they stop running.

### Small project… big developer evolution 💻✨