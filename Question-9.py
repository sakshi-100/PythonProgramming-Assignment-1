# Program that checks if a substring is present in a given string
user_input = input("Enter some text: ")
check_string = input("Enter substring you want to check: ")

if check_string in user_input:
    print("Substring found in main string")
else:
    print("Substring not found in main string")    
