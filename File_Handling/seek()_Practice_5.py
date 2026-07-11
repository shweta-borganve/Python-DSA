with open("student.txt", "r") as f:
    f.seek(2)
    data = f.read()
    print(data) 