print("------- 🎲 MINI BUDGET SPLITTER 📝 -------")

while True:
    bill = float(input("🍛How much is the bill(R): "))
    people = int(input("👯‍♀️How many people are splitting the bill: "))
    tip = float(input("How much wold you like to tip(%): "))
    tip_converted = tip / 100
    total_bill_tip = (bill * tip_converted) + bill
    person_each = total_bill_tip / people
    print(f"""
          ====== 🧾 BILL TIP 🎲 ======
          
          Total Bill(excluding tip): R{bill:.2f}
          Number of people: {people}
          Tip: {tip}%
          Total Bill(with tip): R{total_bill_tip:.2f}
          Person Each: R{person_each:.2f}
          
          ======= THANK YOU ========
          """)
    
    calculateAgain = input("Wanna calculate again(yes/no): ").lower()
    if calculateAgain != "yes":
        print("==== THANK YOU FOR TRYING BUDGET SPLITTER ====")
        break