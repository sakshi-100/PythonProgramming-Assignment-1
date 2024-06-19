# Factorial of a number
num = int(input("Enter a number: "))
factorial_of_num = 1
i = 1
while i<= num:
    factorial_of_num = factorial_of_num*i
    i+=1
print(factorial_of_num)