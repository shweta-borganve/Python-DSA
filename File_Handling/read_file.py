f = open("demo.txt", "r") 
data = f.read()
print(data) 
f.close() 

f = open("demo.txt", "r") 
#data = f.read()
data = f.readline(5) 
print(data) 
f.close() 

f = open("demo.txt", "r") 

line1 = f.readline()
print(line1) 
data = f.read()
print(data) 
f.close() 