import threading

print("===== 👾 Mini Tip Calculator 🎰 =====")

def calculate_tip():
    total_amount = float(input("What is the total of the bill 💵(R): "))
    number_of_people = int(input("How many people are Dining 👯‍♀️: "))
    tip_percentage = float(input("What percentage would you like to give as tip: "))

    #NITTY GRITTY CALCULATIONS
    tip = tip_percentage / 100
    tip_money = total_amount * total_amount
    total_bill_with_tip = (total_amount * tip) + total_amount
    amount_each = total_bill_with_tip / number_of_people

    print(f"===== 🎰 Bill Summary 🎮 ========")
    print(f"💵 Total Amount: R{total_amount} ")
    print(f"Number of people Dining 👯‍♀️: {number_of_people}")
    print(f"Tip Percentage 🧩: {tip_percentage}%")
    print(f"Tip Amount 🧩: R{total_amount}")
    print(f"Total with Tip 🎲 R:{total_bill_with_tip} ")
    print(f"Amount Per Person 👾: R{amount_each}")
    print("======= Thank You ⛳️ ========== ")

#TIMER FOR THE DELAYED FUNCTION
timer = threading.Timer(3, calculate_tip)
timer.start()