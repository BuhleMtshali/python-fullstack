# IMPORTING THE TIMER FUNCTION

import threading

#WELCOME MESSAGE

print("-------- 🧾 UTILITY BILL CALCULATOR 💡 ---------")

def utility_bill_calculator():
    
    #STARTING THE WHILE LOOP
    while True:
        
        
        
        #CLOSING THE LOOP
        runagain = input("\n----- 💡 Wanna calculate again? (yes/no): ").lower()
        if runagain != "yes":
            print("\n --------- 🧾 THANK YOU FOR TRYING MY UTILITY BILL CALCULATOR 🧾 -----------")
            break



# CREATING THE TIMER FUNCTION
timer = threading.Timer(3, utility_bill_calculator)
timer.start()