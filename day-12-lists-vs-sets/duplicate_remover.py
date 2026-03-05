import threading

print("===== 👾 Welcome To My Mini Duplicate Remover 🎮 ====")

#MAIN LIST
main_list = []

def add_movie():
    movie_name = input("🎥 Enter the name of the movie you wanna add to the list: ")
    movie_publication = input("🎲 When was the movie published?: ")
    movie_duration = float(input("⌛️ How long is the movie? (in minutes): "))
    
    new_movie = {
        "name": movie_name,
        "publification": movie_publication,
        "duration": movie_duration
    }

#MAIN FUNCTION
def check_item():
    print("printing the main function...")
    
    
    
#TIMER FOR DELAYED FUNCTION
timer = threading.Timer(3, check_item)
timer.start()