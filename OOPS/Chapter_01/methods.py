class Car:

    def __init__(self,model,color):
        self.model_name = model
        self.color_name = color

    def show(self):
        print("The car model is: ", self.model_name)
        print("The car color is: ", self.color_name)

# object create

audi = Car(model= "Audi A4", color= "Black")
ferrari = Car(model= "Ferrari 488", color= "Blue")

# print

audi.show()
ferrari.show()


# another

class Students:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def show_name(self):
        print("Welcome,", self.name)

    def show_mark(self):
        print("Your mark is: ",self.mark)

s1 = Students("Pranta Nag", 70)
s1.show_name()
s1.show_mark()

