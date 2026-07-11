#

with open("student.txt", "r") as f:
    print(f.tell())
    print(f.read(6))
    print(f.tell())
    f.seek(0) 
    print(f.tell())