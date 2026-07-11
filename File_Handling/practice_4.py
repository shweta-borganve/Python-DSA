with open("student.txt" , "w") as f:
    f.write("Shweta \nPython developer")

with open("student.txt" , "r") as f:
    data = f.read() 
    print(data) 


