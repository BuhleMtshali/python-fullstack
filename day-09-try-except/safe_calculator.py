print("======= 👾 Welcome to Mini Addition Calculator Using TRY/Except ========")

#OUTER LOOP keep trying until you get it right
while True:
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print(f"Result: {num1} + {num2} = {num1 + num2}")
        break
    except ValueError:
        print("Invalid input try again!")
