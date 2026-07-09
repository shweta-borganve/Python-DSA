class Animal:
    def __init__(self):
        print("Animal constructor") 

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog constructor") 

e = Dog() 

class Person:
    def __init__(self):
        print("Person Constructor") 

class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student Constructor") 

g = Student() 