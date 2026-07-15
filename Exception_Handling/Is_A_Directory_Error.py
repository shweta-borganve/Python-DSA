try:
    file = open("Documents","r")
except IsADirectoryError:
    print("This is a directory, not a file.") 