class Teacher:
    def show_teach(self):
        print("Teaching") 

class Singer:
    def show_sing(self):
        print("Singing") 

class Person(Teacher, Singer):
    pass

e = Person()
e.show_teach()
e.show_sing() 