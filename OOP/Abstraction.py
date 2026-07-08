class Car:

    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False

    def start(self):
        self.cluch = True
        self.acc = True
        self.brk = True
        print("car started...") 

car1 = Car() 
car1.start() 