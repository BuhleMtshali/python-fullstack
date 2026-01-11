import threading

print("====== 🐝 Welcome To My Mini Calculator 🎮 =====")

def calculator_app():
    #STARTING WHILE LOOP
    while True:
        first_number = float(input("🎰 Enter your first number: "))
        operator = input("🧩 Choose an operator (+, /, *, -): ")
        second_number = float(input("🥦 Enter your second number: "))
        output = 0

        match operator:
            case "+":
                return output == first_number + second_number
                print(f"Output: {output}")
            case "-":
                return output == first_number - second_number
                print(f"Output: {output}")
            case "*":
                return output == first_number * second_number
                print(f"Output: {output}")
            case "/":
                if second_number == 0:
                    print("🚫 Cannot divide by 0")
                else:
                    return output == first_number / second_number
                    print(f"Output: {output}")
            case _:
                print("‼️ Invalid Operators")

       

        #CLOSING THE LOOP
        runAgain = input("👾 Want to make another calculation? (yes/no): ")
        if runAgain != "yes":
            print("===== ⛳️ Thank you For Trying My Mini Calculator 🎲 =====")


#TIMER FOR DELAYED FUNCTION
timer = threading.Timer(2, calculator_app)
timer.start()
