with open("student.txt", "w") as f:
    print(f.writable())

with open("student.txt", "r") as f:
    print(f.writable())

with open("student.txt", "r+") as f:
    print(f.writable()) 