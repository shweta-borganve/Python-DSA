class Father:
    def show_father(self):
        print("I am a father") 

class Mother:
    def show_mother(self):
        print("I am a mother") 

class Child(Father, Mother):
    pass 

e = Child() 
e.show_father()
e.show_mother() 