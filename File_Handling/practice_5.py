with open("student.txt", "r") as f:
    data = f.read(5) 
    print(data) 

with open("student.txt", "r") as f:
    data = f.seek(7)
    print(f.tell()) 