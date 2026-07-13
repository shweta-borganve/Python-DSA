with open("student.txt", "r") as f:
    print(f.read()) 

with open("photo.jpg", "rb") as f:
    data = f.read()
    print(data) 