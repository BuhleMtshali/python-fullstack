import threading

print("======= 🐝 Mini Grocery Console Game 🎲 ======")

grocery_list = [{"name": "rice", "quantity": 30, "price each": 21, "total price": 630}, {"name": "chicken", "quantity": 30, "price each": 21, "total price": 630}]

def add_item():
    item_name = input("Enter the name of the item⏲️: ").strip().lower()
    item_quantity = int(input("🔌 Enter the quantity you want to add: "))
    item_price = float(input("💵 How much is the item each(R): "))
    total_price_item = item_quantity * item_price

    new_item = {
        "name": item_name,
        "quantity": item_quantity,
        "price each": item_price,
        "total price": total_price_item
    }

    # check if item already exists
    for item in grocery_list:
        if item["name"].lower() == item_name:
            print("‼️ Item already exists in your cart.")
            return

    grocery_list.append(new_item)
    print(f"✅ {item_name.capitalize()} added to your cart!")

    # show cart after adding
    print("\n===== Items in Cart 🛒 =====")
    for index, item in enumerate(grocery_list, start=1):
        print(f"\n=== 🧺 Item {index} ===")
        for key, value in item.items():
            print(f"{key.capitalize()}: {value}")
      


#FUCNTION TO REMOVE ITEMS
def remove_item():
    removed_item = input("Enter the name of the product you want to remove: ").strip().lower()
    found = False

    for item in grocery_list:
        if removed_item == item["name"].lower():
            grocery_list.remove(item)
            print(f"✅ {removed_item.capitalize()} has been removed from your cart!")
            found = True
            break

    if not found:
        print(f"‼️ {removed_item.capitalize()} does not exist. Try adding it!")


#FUNCTION TO VIEW THE LIST
def view_items():
   if len(grocery_list) > 0:
      for index, item in enumerate(grocery_list):
         print(f"====== 🎮 Item {index} =======")
         for key, value in item.items():
            print(f"🐝 {key.capitalize()}: {value}")
         print("-" * 30)
   else:
      print("🐝 Unfortunately your cart is currently emplty, try adding a few more stuff")

def main_function():

   while True:
      print("1. View Grocery List 🛍️")
      print("2. Add Item 📦")
      print("3. Remove Item 🚫")
      print("4. Exit ‼️")
      choice = input("🧩 Please choose an Option: ")

      match choice:
         case "1":
            view_items()
         case "2":
            add_item()
         case "3":
            remove_item()
         case "4":
            print("🎲 ==== Thank you For Trying My Mini Grocery List =====")
            break

      #CLOSING THE LOOP
      runAgain = input("👾 Would you like to run another process? (yes/no): ")
      if runAgain != "yes":
         print("======== ⏳ Thank you for trying my Mini Console Game 🎮 =========")
         break;

#TIMER FOR DELAYED FUNCTION
timer = threading.Timer(3, main_function)
timer.start()