class Student:
    
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database...")

s1 = Student("Karan")  
print(s1.name)

s2 = Student("arjun")
print(s2.name) 