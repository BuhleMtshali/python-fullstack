# IMPORTING TIMER FUNCTION
import threading

print("------ 💡 SCHOLASHIP ELIGIBILITY CHECKER 🕯️ -----")


# STARTING THE FUNCTION
def scholarship_eligibility_checker():
    print("function is running....")


# CALLING THE FUNCTION
timer = threading.Timer(3, scholarship_eligibility_checker)
timer.start()