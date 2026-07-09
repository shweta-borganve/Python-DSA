class Student:
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name
    
s = Student("shweta")
print(s) 

class Employee:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
e = Employee("Rahul")
print(e) 