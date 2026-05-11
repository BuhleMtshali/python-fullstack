print("------- 🎲 MINI BUDGET SPLITTER 📝 -------")

while True:
    bill = float(input("🍛How much is the bill(R): "))
    people = int(input("👯‍♀️How many people are splitting the bill: "))
    
    
    calculateAgain = input("Wanna calculate again(yes/no): ").lower()
    if calculateAgain != "yes":
        print("==== THANK YOU FOR TRYING BUDGET SPLITTER ====")
        break