try:
    
    print("1. Addition: ")
    print("2. Substraction: ")
    print("3. Multiplication: ")
    print("4. Division: ") 

    choice = int(input("Enter your choice: "))
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))

    if choice == 1:
        print("Answer: ", num1 + num2)
    elif choice == 2:
        print("Answer: ", num1 - num2)
    elif choice == 3:
        print("Answer: ", num1 * num2)
    elif choice == 4:
        print("Answer: ", num1 / num2)
    else:
        print("Invalid Choice")
except ZeroDivisionError:
    print("Cannot divide by 0")
except ValueError:
    print("Please enter a valid number")
finally:
    print("Program Ended") 