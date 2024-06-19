# Program for Simple Calculator
# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Choose operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 - num2

elif operator == '*':
    result = num1 * num2

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")
