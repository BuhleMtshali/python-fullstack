import threading

print("===== 👾 Mini Tip Calculator 🎰 =====")

def calculate_tip():
    print("helo....")



#TIMER FOR THE DELAYED FUNCTION
timer = threading.Timer(3, calculate_tip)
timer.start()