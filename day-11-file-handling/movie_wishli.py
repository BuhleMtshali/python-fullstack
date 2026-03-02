import csv

print("======== 🐝 Welcome to My Mini Movie Wishlist Project ======")

# CREATING CSV FILE
with open('movie_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie Name", "Year"])
    
while True:
    ranking_number = int(input("What number is this movie ranking: "))
    movie_name = input("Enter the movie name: ").lower()
    movie_year = input("Enter the movie publication year: ")
    
    
    addAgain = input("Would you like to add another movie (yes/no): ").lower()
    if addAgain == "no":
        print("====== Thank you for Trying My Mini Movie Wishlist =====")
        break