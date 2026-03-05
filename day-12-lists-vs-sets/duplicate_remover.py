import threading

print("===== 👾 Welcome To My Mini Duplicate Remover 🎮 ====")


#MAIN FUNCTION
def check_item():
    print("printing the main function...")
    
    
#TIMER FOR DELAYED FUNCTION
timer = threading.Timer(3, check_item)
timer.start()