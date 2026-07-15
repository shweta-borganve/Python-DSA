try:
    a = 10
    b = 2
    print(a/b) 
except:
    print("error occured")
else:
    print("program executes successfully") 
print("program ends withour error") 

try:
    num = int(input("Enter a number: "))
    print("Entered num is:", num)
except:
    print("Invalid number")
else:
    print("Input accepted")
print("Program ends") 