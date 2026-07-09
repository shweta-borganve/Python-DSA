class Student:

    college = "HSIT"

    @classmethod
    def show_college(cls):
        print(cls.college) 

Student.show_college() 