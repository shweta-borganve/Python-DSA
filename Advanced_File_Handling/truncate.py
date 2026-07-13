with open("student.txt", "w") as f:
    data = f.write("Python Developer")

with open("student.txt", "r+") as f:
    data = f.truncate(6) 
    print(data) 
