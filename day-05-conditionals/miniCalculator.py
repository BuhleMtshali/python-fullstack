import threading

print("====== 🐝 Welcome To My Mini Calculator 🎮 =====")

def calculator_app():
    #STARTING WHILE LOOP
    while True:
        first_number = float(input("🎰 Enter your first number: "))
        operator = input("🧩 Choose an operator")




        #CLOSING THE LOOP
        runAgain = input("👾 Want to make another calculation? (yes/no): ")
        if runAgain != "yes":
            print("===== ⛳️ Thank you For Trying My Mini Calculator 🎲 =====")



