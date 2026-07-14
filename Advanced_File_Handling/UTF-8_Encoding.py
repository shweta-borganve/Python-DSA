with open("demo.txt", "w", encoding = "utf-8") as f:
    data = f.write("Hello World!!") 
print(data) 

with open("demo.txt", "r", encoding = "utf-8") as f:
    data = f.read() 
print(data) 