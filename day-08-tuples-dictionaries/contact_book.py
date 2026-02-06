import threading

print("\n===== 🔖 Phone Book Console Appp 🔢 =====")

print("\n===== The program will start 🔜 =====")

contact_book = []

def add_number():
    number_name = input("🙋🏻‍♀️ Enter the person's number: ").lower()
    relationship_number = input("👥 What is your relationship with the person: ").lower()
    person_number = int(input("📞 Enter the number: "))

    #ACTUAL NUMBER
    new_number = {
        "name": number_name,
        "relationship": relationship_number,
        "number": person_number
    }

    #CHECKIGN IF THE NUMBER EXISTS
    for number in contact_book:
        if number["name"].lower() == number_name:
            print("‼️ You already have this number in your contact book!")
            return

    #THIS IS NOW ADDING THE NUMBER
    contact_book.append(new_number)

    #SHOW THE PHONE BOOK AFTER ADDING THE NUMBER
    print("\n====== 👥 Numbers in Your Phone Book 🎲 =======")
    for index, item in enumerate(contact_book, start=1):
        print(f"\n==== 📋 Number {index} =====")
        for key, value in item.items():
            print(f"{key.capitalize()}: {value}")


# FUNCTION TO REMOVE NUMBER
def remove_number():
    removed_name = input("🐝 Enter the name of the person who's number you want to remove: ").lower()
    found = False

    #NOW LETS LOOP INSIDE OUR LIST OF DICTIOANRIES
    for item in contact_book:
        if removed_name == item["name"].lower():
            contact_book.remove(item)
            print(f"✅ {removed_name.capitalize()} has been removed from your contact book!")
            found = True
            break

    if not found:
        print(f"🚫 {removed_name.capitalize()} does not exist")


# FUCTION TO VIEW THE LIST
def view_number():
    if len(contact_book) > 0:
        for index, item in enumerate(contact_book):
            print(f"===== 🎮 Number. {index} =======")
            for key, value in item.items():
                print(f"👾 {key.capitalize()}: {value}")
            print("-" * 30)
    else:
        print("✨ Unfortunately your contact book is currently empty, try adding some numbers first!")


#MAIN FUCNTION
def main_function():
    while True:
        print("1. View contact book 🪪")
        print("2. Add Contact 👥")
        print("3. Remove contact 🐝")
        print("4. Exit 🚫")
        choice = input("🔖 Choose an option to continue: ")

        #SWITCH STATEMENTS
        match choice:
            case "1":
                view_number()
            case "2":
                add_number()
            case "3":
                remove_number()
            case "4":
                print("===== 👥 Thank you for trying my mini contact book 📋 ======")
                break
        
        #CLOSING THE LOOP
        runAgain = input("🧩 Would you like to run again (yes/no): ").lower()
        if runAgain != "yes":
            print("===== 👥 Thank you for trying my mini contact book 📋 ======")
            break

#TIMER
timer = threading.Timer(3, main_function)
timer.start()