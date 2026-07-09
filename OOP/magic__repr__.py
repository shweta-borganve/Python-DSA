class Student:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return f"Student('{self.name}')" 
    
s = Student("shweta")
print(s) 

class Book:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return f"Book('{self.name}')" 
b = Book("Python")
print(b) 
