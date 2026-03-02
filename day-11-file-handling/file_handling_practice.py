import os
import csv


#THIS PRINTS THE CURRENT WORKING DIRECORY

print(f"Directory: {os.getcwd()}")

os.listdir()

#WRITING TO A CSV FILE
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "LOTR", "Frodo"])
    
    
#TRYING TO READ THE FILE
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)