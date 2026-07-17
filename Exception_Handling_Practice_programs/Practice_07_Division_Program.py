try:
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))
    print(num1 / num2)
    print("Division is successful.")

except ZeroDivisionError:
    print("Cannot devide by 0")
except ValueError:
    print("Please enter a valid number")
finally:
    print("Program Ended.") 