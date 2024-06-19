# Program that removes all punctuation from a given string
import string
user_input = "Hello, world! How are you today?"
punctuation_chars = string.punctuation

string_without_punctutation = ""
for char in user_input:
   if char not in punctuation_chars:
        string_without_punctutation += char

print("String without punctuation:")
print(string_without_punctutation)
