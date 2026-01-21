import threading

print("======= 🐝 Mini Grocery Console Game 🎲 ======")

def grocery_list():
    list = []

    #STARTING THE WHILE LOOP
    while True:
        items = input("🧩 Enter your first item: ").lower()
        if len(items) > 2:
            list.append(items)
            if len(list) > 0:
                print("🛍️ Items In Your List: ")
                for index, item in enumerate(list):
                    print(f"{index}: {item}")
            else:
                print("‼️ List is currently empty!")
        else:
            print("‼️INVALID, please add an item first!")

        #CLOSING THE LOOP
        add_again = input("✨ Wanna Add Another item(yes/no): ").lower()
        if add_again != "yes":
            print("====== 🛁 THANK YOU FOR TRYING MY MINI CONSOLE CART 🛍️ =====")
            break


#TIMER FOR DELAYED FUNCTION
timer = threading.Timer(3, grocery_list)
timer.start()