import threading

print("===== 👾 Mini Tip Calculator 🎰 =====")

def calculate_tip():
    total_amount = float(input("What is the total of the bill 💵: "))
    number_of_people = int(input("How many people are Dining 👯‍♀️: "))
    tip_percentage = float(input("What percentage would you like to give as tip: "))

    #NITTY GRITTY CALCULATIONS
    total_bill_with_tip = (total_amount * ti)



#TIMER FOR THE DELAYED FUNCTION
timer = threading.Timer(3, calculate_tip)
timer.start()