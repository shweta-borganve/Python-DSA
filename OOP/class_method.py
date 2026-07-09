class Student:

    college = "HSIT"

    @classmethod
    def show_college(cls):
        print(cls.college) 

Student.show_college() 

class Employee:

    company = "IBM"
    @classmethod
    def show_company(cls):
        print(cls.company)

Employee.show_company() 