# Program that takes a string input from the user and writes it to a text file
user_input = input("Enter text: ")
file_name = "user_input.txt"

with open(file_name, 'w', newline='') as file:
     file.write(user_input)
    
print(f"String input has been written to {file_name}")
