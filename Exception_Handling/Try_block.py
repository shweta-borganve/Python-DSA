try:
    a = 10
    b = 0
    print(a/b) 
except:
    print("error occured")
print("program end") 

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("invalid input")
print("program end") 