class Student:
    def __getitem__(self, index):
        names = ["shweta", "Tanvi", "Pooja"]
        return names[index] 
s = Student()
print(s[2]) 