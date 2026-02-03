import threading

print("======= 🐝 Mini Grocery Console Game 🎲 ======")

def grocery_list():
   while True:
      print("loop is running...")
      
      #CLOSING THE LOOP
      runAgain = input("👾 Would you like to run another process? (yes/no): ")
      if runAgain != "yes":
         print("======== ⏳ Thank you for trying my Mini Console Game 🎮 =========")
         break;

#TIMER FOR DELAYED FUNCTION
timer = threading.Timer(3, grocery_list)
timer.start()