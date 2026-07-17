try:
    marks = int(input("Enter the Student marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Invalid marks")
    elif marks >= 35 and marks <= 100:
        print("Pass")
    else:
        print("Fail")

except ValueError as f:
    print(f)
finally:
    print("Program ended") 