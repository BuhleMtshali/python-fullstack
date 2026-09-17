# IMPORTING TIMER FUNCTION
import threading

print("------ 💡 SCHOLASHIP ELIGIBILITY CHECKER 🕯️ -----")


# STARTING THE FUNCTION
def scholarship_eligibility_checker():
    
    #STARTING THE WHILE LOOP
    while True:
        name = input("Enter your full name: ")
        age = int(input("What is your age: "))
        gpa = float(input("Enter your GPA (out of 4.0): "))
        income = float(input("Enter your annual family income (R): "))
        
        # ELIGIGIBILITY LOGIC
        if age < 16 or age > 30:
            print(f"Sorry {name}, you are not eligible based on age requirements (16-30).")
        elif gpa >= 3.8 and income < 500000:
            print(f"Congratulations {name}! You qualify for the Full Scholarship.")
        elif gpa >= 3.4 and income < 600000:
            print(f"Congratulations {name}! You qualify for the Partial Scholarship.")
        else:
            print(f"Sorry {name}, you do not meet the academic or income criteria for a scholarship at this time.")
        
        #CLOSING THE LOOP
        runAgain = input("\n----- 🕹️ Wanna check again? (yes/no): ").lower()
        if runAgain != "yes":
            print("\n --------- 🧾 THANK YOU FOR TRYING MY SCHOLARSHIP ELIGIBILITY CHECKER 🧾 -----------")
            break


# CALLING THE FUNCTION
timer = threading.Timer(3, scholarship_eligibility_checker)
timer.start()