num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))
operation = input("Enter a operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
if operation == '*':
    result = num1 * num2
if operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero"
else:
    print("Result:", result) 
