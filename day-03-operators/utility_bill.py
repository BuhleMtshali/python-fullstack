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
        
        #first calculation is for domestic
        if(type == 1):
            category == "Domestic"
            
            #CALCULATING IF THE USER USES <= 100
            if units <= 100:
                total_bill = units * 3.0
            
            # if the user uses more than 100 but less than 200
            elif units <= 200:
                #first 100 calculated at R3 per unit then the leftover R4
                total_bill = (100 * 3.0) + ((units - 100) * 4.0)
                
            # if they use more than 200 then first 200 calculated and then the rest at R5 per unit
            else:
                total_bill = (100 * 3.0) + (100 * 4.0) + ((units - 200) * 5.0)
        
        #CLOSING THE LOOP
        runagain = input("\n----- 💡 Wanna calculate again? (yes/no): ").lower()
        if runagain != "yes":
            print("\n --------- 🧾 THANK YOU FOR TRYING MY UTILITY BILL CALCULATOR 🧾 -----------")
            break



# CREATING THE TIMER FUNCTION
timer = threading.Timer(3, utility_bill_calculator)
timer.start()