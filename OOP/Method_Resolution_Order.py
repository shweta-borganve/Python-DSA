class Father:
    def show(self):
        print("father") 
class Mother:
    def show(self):
        print("mother") 
class Child(Father, Mother):
    pass 
c = Child()
c.show() 
