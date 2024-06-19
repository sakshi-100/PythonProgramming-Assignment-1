# Program in python that counts the frequency of each character in a string
user_input = input("Please enter a string: ")
check_frequency_dict = {}

for char in user_input:
    if char in check_frequency_dict:
        check_frequency_dict[char] += 1
    else:
        check_frequency_dict[char] = 1

print("Character frequencies:")
for char, count in check_frequency_dict.items():
    print(f"{char}: {count}")
