class Car:

    def __init__(self):
        self.acc = False
        self.brc = False
        self.clutch = False
    def start(self):
        self.acc = True             # hide unnecessary implementation => abstraction
        self.clutch =True
        print("Car started....")

car1 = Car()
car1.start()

# class + data + function => encapsulation

