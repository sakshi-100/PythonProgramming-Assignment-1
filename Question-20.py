# Sum of all numbers in a list
num_list_items = int(input("Enter number of terms in list: "))
lst = []
sum = 0

for i in range(num_list_items):
    num = int(input("Enter number: "))
    lst.append(num)

for j in lst:
    sum += j

print("Sum of all numbers of list", lst, ":", sum)

