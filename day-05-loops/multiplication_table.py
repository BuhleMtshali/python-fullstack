print("========== 🐝 MINI MULTIPLICATION GENERATOR 🎮 ========")

# STARTING THE WHILE LOOP
while True:
    multiplier = int(input("🔢 Choose your multipler (1-30): "))
    for num in range(multiplier):
        print(f"{num} * {multiplier} = {num * multiplier}")


    #CLOSING THE LOOP
    runAgain = input("🐝 Wanna generate another table(yes/no): ").lower()
    if runAgain != "yes":
        print("===== ⛳️ Thank you For Trying My Mini Calculator 🎲 =====")
        break