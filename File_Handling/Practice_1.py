f = open("practice.txt", "w")
f.write("Hi everyone\nWe are learning Fili I/O\nusing Java\nI like programming in Java")
f.close() 

f = open("practice.txt", "r")
data = f.read()
f.close()

new_data = data.replace("Java", "Python")
print(new_data) 

f = open("practice.txt", "w")
f.write(new_data)
f.close() 

word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("found") 
    else:
        print("not found") 