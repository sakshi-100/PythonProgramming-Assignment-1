# Program that reads data from a CSV file and prints it to the console
import csv

file_data = [
    ['Name', 'Age', 'Profession'],
    ['Sam', 25, 'Engineer'],
    ['Jack', 30, 'Doctor'],
    ['Jim', 28, 'Lawyer']
]
csv_filename = 'data.csv'

# Creating a CSV File

with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(file_data)

print(f"CSV file {csv_filename} has been created !")
print("File content: ")

# Reading from CSV File

with open(csv_filename, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
