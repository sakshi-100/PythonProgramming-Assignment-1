# Program that counts the occurrences of a specific element in a list
num_list = [3,7,6,2,4,8,9,3,10,5,3,9]
element_count = int(input("Enter element to count occurence: "))

count = 0

for num in num_list:
    if num == element_count:
        count += 1

print(f"The element {element_count} occurs {count} times.")

