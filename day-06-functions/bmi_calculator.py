def calculate_bmi():
    println("====== 🐝 Welcome to My Mini BMI Calculator 🎲 =======")
    name = input("🧩Enter your name: ")
    weight = float(input("📋 Enter your weight(kg): "))
    height = float(input("📏 Enter your height(m): "))
    bmi = weight / (height ** 2)
    print(f"{name}, Your BMI🎲 : {bmi:.2f}");
    