try:
    num1 = float(input("Enter a first number: "))
    num2 = float(input("Enter a second number: ")) 
    op = input("Enter operator (+,-,*,/): ")
    if op == "+":
       print("Answer =", num1 + num2)
    elif op == "-":
       print("Answer =", num1 - num2)
    elif op == "*":
       print("Answer =", num1 * num2)
    elif op == "/":
       print("Answer =", num1 / num2) 
    else:
       print("Invalid Input") 
except ValueError:
   print("Please enter a Valid number")
except ZeroDivisionError:
   print("Cannot devide by 0")
finally:
   print("program end") 