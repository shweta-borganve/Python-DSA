try:
    file = open("student.txt", "r")
    print(file.read()) 
except FileNotFoundError:
    print("file not found")
finally:
    print("program finished") 

try:
    file = open("demo.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found")
else:
    print("file read successfully.")
finally:
    if 'file' in locals():
        file.close()
    print("file closed") 