print("------- 🎲 MINI BUDGET SPLITTER 📝 -------")

bill = float(input("🍛How much is the bill(R): "))
people = int(input("👯‍♀️How many people are splitting the bill: "))

while True:
    print("loop running")
    
    
    
    calculateAgain = input("Wanna calculate again(yes/no): ").lower()
    if calculateAgain != "yes":
        print("==== THANK YOU FOR TRYING BUDGET SPLITTER ====")