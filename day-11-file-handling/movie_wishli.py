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
    
    writer.writerow(ranking_number, movie_name, movie_year)
    
    #READING THE FILE
    with open('movie_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    
    addAgain = input("Would you like to add another movie (yes/no): ").lower()
    if addAgain == "no":
        print("====== Thank you for Trying My Mini Movie Wishlist =====")
        break