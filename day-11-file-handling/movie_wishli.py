import csv

print("======== 🐝 Welcome to My Mini Movie Wishlist Project ======")

# CREATING CSV FILE
with open('movie_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)

while True:
    
    
    
    addAgain = input("Would you like to add another movie (yes/no): ").lower()
    if addAgain == "no":
        print("====== Thank you for Trying My Mini Movie Wishlist =====")
        break