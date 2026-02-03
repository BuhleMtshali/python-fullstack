import threading

print("======= 🐝 Mini Grocery Console Game 🎲 ======")

grocery_list = []

#DEF FOR ADDING TO THE LIST
def add_item():
   item_name = input("Enter the name of the item⏲️: ").lower()
   item_quantity = int(input("🔌 Enter the quantity you want to add: "))
   item_price = float(input("💵 How much is the item each(R): "))
   total_price_item = item_quantity * item_price
   
   item = {
       "name": item_name,
       "quntity": item_quantity,
       "price_each": item_price,
       "total_price": total_price_item
    }
   
   grocery_list.append(item)
   print(grocery_list)



def grocery_list():

   while True:
      print("our options will mgo in here")



      #CLOSING THE LOOP
      runAgain = input("👾 Would you like to run another process? (yes/no): ")
      if runAgain != "yes":
         print("======== ⏳ Thank you for trying my Mini Console Game 🎮 =========")
         break;

#TIMER FOR DELAYED FUNCTION
timer = threading.Timer(3, grocery_list)
timer.start()