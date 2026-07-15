try:
    file = open("demo.txt", "r", encoding = "ascii")
    print(file.read()) 
except UnicodeDecodeError:
    print("Encoding error while reading.") 