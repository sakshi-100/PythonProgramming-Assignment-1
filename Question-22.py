# Program that returns the minimum and maximum values in a list of numbers.
num_list = [3,4,5,7,2,9,1,55,25,10]

min_value = num_list[0]
max_value = num_list[0]

for num in num_list:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
