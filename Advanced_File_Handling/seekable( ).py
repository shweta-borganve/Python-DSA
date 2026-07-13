with open("student.txt", "r") as f:
    print(f.seekable())

with open("student.txt", "w") as f:
    print(f.seekable())

with open("student.txt", "a") as f:
    print(f.seekable())

with open("student.txt", "r+") as f:
    print(f.seekable())

with open("student.txt", "a+") as f:
    print(f.seekable()) 