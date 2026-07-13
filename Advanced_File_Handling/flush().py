with open("student.txt" , "w") as f:
    f.write("Python")
    f.flush()
print("Data saved") 

with open("student.txt", "w") as f:
    f.write("hello")
    f.flush()
    f.write("shweta") 