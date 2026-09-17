# IMPORTING TIMER FUNCTION
import threading

print("------ 💡 SCHOLASHIP ELIGIBILITY CHECKER 🕯️ -----")


# STARTING THE FUNCTION
def scholarship_eligibility_checker():
    
    #STARTING THE WHILE LOOP
    while True:
        print("loop is running...")
        
        
        #CLOSING THE LOOP
        runAgain = input("\n----- 🕹️ Wanna check again? (yes/no): ").lower()
        if runAgain != "yes":
            print("\n --------- 🧾 THANK YOU FOR TRYING MY SCHOLARSHIP ELIGIBILITY CHECKER 🧾 -----------")
            break


# CALLING THE FUNCTION
timer = threading.Timer(3, scholarship_eligibility_checker)
timer.start()