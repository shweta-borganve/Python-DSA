class AgeError(Exception):
    pass
age = int(input("Enter your age: "))
if age < 18:
    raise AgeError("Age must be 18 or above.")
print("Eligible to vote") 