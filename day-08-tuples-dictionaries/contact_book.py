import threading

print("===== 🔖 Phone Book Console Appp 🔢 =====")

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

add_number()