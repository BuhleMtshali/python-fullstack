# IMPORTING THE TIMER FUNCTION

import threading

#WELCOME MESSAGE

print("-------- 🧾 UTILITY BILL CALCULATOR 💡 ---------")

def utility_bill_calculator():
    
    #STARTING THE WHILE LOOP
    while True:
        
        #GETTING USER CONSUMPTION UNITS & USE CASE TYPE
        units = float(input("💡 Enter units consumed (kWh): "))
        type = int(input("🕹️ Enter connection type (1 for Domestic, 2 for commercial): "))
        
        #CREATING VARIABLES FOR THE BILL AND CATEGORY
        total_bill = 0.0
        category = ""
        
        
        #STARTING ELECTRICITY BILL CALCULATIONS
        
        
        #CLOSING THE LOOP
        runagain = input("\n----- 💡 Wanna calculate again? (yes/no): ").lower()
        if runagain != "yes":
            print("\n --------- 🧾 THANK YOU FOR TRYING MY UTILITY BILL CALCULATOR 🧾 -----------")
            break



# CREATING THE TIMER FUNCTION
timer = threading.Timer(3, utility_bill_calculator)
timer.start()