def addition(x,y,z):
    return x+y+z
print(addition(10,20,30)) 

addition = lambda x,y,z: x+y+z
print(addition(10,20,30)) 

numbers = [1,2,3,4,5] 
def square(number):
    return number**2
square(2) 

square = lambda number: number**2
print(square(2)) 

print(list(map(lambda number: number**2, numbers))) 