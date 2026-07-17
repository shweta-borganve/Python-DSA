try:
    file = open("student.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File does not exist") 
finally:
    print("Program End") 