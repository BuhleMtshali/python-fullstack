def calculate_bmi():
    print("====== 🐝 Welcome to My Mini BMI Calculator 🎲 =======")
    name = input("🧩Enter your name: ")
    weight = float(input("📋 Enter your weight(kg): "))
    height = float(input("📏 Enter your height(m): "))
    bmi = weight / (height ** 2)
    print(f"{name}, Your BMI🎲 : {bmi:.2f}");

    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 25:
        print("Category: Normal weight")
    elif 25 <= bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")


calculate_bmi()