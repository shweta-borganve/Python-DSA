try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter only numbers.")
print("Program end") 
