# IMPORTING THE TIMER FUNCTION

import threading

#WELCOME MESSAGE

println("-------- 🧾 UTILITY BILL CALCULATOR 💡 ---------")

def utility_bill_calculator():
    
    #STARTING THE WHILE LOOP
    while True:
        
        
        
        #CLOSING THE LOOP
        runagain = input("\n----- 💡 Wanna calculate again? (yes/no): ").lower()
        if runagain != "yes":
            println("\n --------- 🧾 THANK YOU FOR TRYING MY UTILITY BILL CALCULATOR 🧾 -----------")



# CREATING THE TIMER FUNCTION
timer = threading.Timer(3, utility_bill_calculator)
timer.start()