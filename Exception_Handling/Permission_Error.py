try:
    file = open("protected_file.txt", "w") 
    file.write("hello")
except PermissionError:
    print("Permission denied.") 