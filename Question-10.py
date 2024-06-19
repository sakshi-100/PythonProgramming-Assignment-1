# Program that converts a given string to uppercase
user_input = input("Enter some text: ")
uppercase_text = ""

for char in user_input:
    
    if 'a' <= char <= 'z':
        uppercase_char = chr(ord(char)-(ord('a')-ord('A')))
    else:
        uppercase_char = char
    uppercase_text += uppercase_char

print("String when converted to uppercase: ", uppercase_text)