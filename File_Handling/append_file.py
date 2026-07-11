f = open("demo.txt", "a")
data = f.write("\n Hello")
f.close() 

f = open("demo.txt", "r+")
f.write("abc") 
print(f.read())
f.close() 

f = open("demo.txt", "w+")
print(f.read())
f.write("Hello world")
f.close() 

f= open("demo.txt", "a+")
print(f.read())
f.write("abc")
f.close() 