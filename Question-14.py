# Program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
line_list = []

while True:
    line = input("Enter a line (or press Enter to finish):\n")
    if line == "":
        break
    line_list.append(line)

print("Lines entered:")
for line in line_list:
    print(line)
