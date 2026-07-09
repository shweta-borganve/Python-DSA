class Engine:
    def start(self):
        print("Engine started...")

class Car:
    def __init__(self):
        self.engine = Engine() 
    
    def drive(self):
        self.engine.start()
        print("Car started...")

c = Car()
c.drive() 

class Battery:
    def charge(self):
        print("Battery Charging") 

class Mobile:
    def __init__(self):
        self.poweron = Battery() 

    def power_on(self):
        self.poweron.charge()
        print("Mobile Started") 

d = Mobile() 
d.power_on() 