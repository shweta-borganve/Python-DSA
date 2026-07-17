try:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are Eligible to vote")
    elif age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("You are not eligible to vote")
except ValueError as e:
    print(e)
finally:
    print("Program end") 