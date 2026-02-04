import threading

print("======= 🐝 Mini Grocery Console Game 🎲 ======")

grocery_list = [{"name": "rice", "quantity": 30, "price each": 21, "total price": 630}, {"name": "chicken", "quantity": 30, "price each": 21, "total price": 630}]

#DEF FOR ADDING TO THE LIST
def add_item():
   item_name = input("Enter the name of the item⏲️: ").lower()
   item_quantity = int(input("🔌 Enter the quantity you want to add: "))
   item_price = float(input("💵 How much is the item each(R): "))
   total_price_item = item_quantity * item_price
   
   item = {
       "name": item_name,
       "quntity": item_quantity,
       "price each": item_price,
       "total price": total_price_item
    }

   grocery_list.append(item)
   print("===== Items in Cart 🛒 =====")
   for index, item in enumerate(grocery_list):
      print(f"=== 🧺 Item {index} =====")
      for key, value in item.items():
         print(f"{key.capitalize()}: {value}")
         
#FUCNTION TO REMOVE ITEMS
def remove_item():
   remove_item = input("Enter the name of the product you want to remove: ").lower()
   for item in grocery_list:
      if remove_item == item["name"]:
         grocery_list.remove(item)
         print(f"✅ {remove_item.capitalize()} has been removed from your cart!")
         print(grocery_list)
      else:
         print(f"‼️ {remove_item.capitalize()} does not exist try adding it!")

#FUNCTION TO VIEW THE LIST
def view_items():
   if len(grocery_list) > 0:
      for index, item in enumerate(grocery_list):
         print(f"====== 🎮 Item {index} =======")
         for key, value in item.items():
            print(f"{key.capitalize()}: {value}")
         print("-" * 30)



view_items()

def grocery_list():

   while True:
      print("our options will mgo in here")



      #CLOSING THE LOOP
      runAgain = input("👾 Would you like to run another process? (yes/no): ")
      if runAgain != "yes":
         print("======== ⏳ Thank you for trying my Mini Console Game 🎮 =========")
         break;

#TIMER FOR DELAYED FUNCTION
#timer = threading.Timer(3, grocery_list)
#timer.start()