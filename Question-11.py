#  First n numbers of Fibonacci sequence
number_of_terms = int(input("Enter number of terms: "))
a = 0
b = 1

if number_of_terms == 1:
    print(a)

else:
    print(a, b, end=" ")

    for i in range(number_of_terms - 2):
        sum = a + b
        print(sum, end=" ")
        a = b
        b = sum

