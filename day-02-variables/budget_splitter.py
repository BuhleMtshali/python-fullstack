print("------- 🎲 MINI BUDGET SPLITTER 📝 -------")

while True:
    bill = float(input("🍛How much is the bill(R): "))
    people = int(input("👯‍♀️How many people are splitting the bill: "))
    tip = float(input("How much wold you like to tip(%): "))
    tip_converted = tip / 100
    total_bill_tip = (bill * tip_converted) + bill
    print(total_bill_tip)
    
    calculateAgain = input("Wanna calculate again(yes/no): ").lower()
    if calculateAgain != "yes":
        print("==== THANK YOU FOR TRYING BUDGET SPLITTER ====")
        break