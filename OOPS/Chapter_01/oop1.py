# creating class

class Student:
    name = "Pranta"         # when create any object on that class, given same name

#creating object (instance)

s1 = Student()
print(s1.name)

# another way

class Student:
    pass                # after, multiple input store this class

s1 = Student()
s1.name = "Pranta"
print(s1.name)

s2 = Student()
s2.name = "Shuvo"
print(s2.name)



class Car:
    pass

audi = Car()
audi.model = "Audi A4"
audi.color = "Black"

ferrari = Car()
ferrari.model = "Ferrari 488"
ferrari.color = "Green"

def show(Car):
    print("The model is: ", Car.model)
    print("The color is: ", Car.color)

show(audi)
show(ferrari)



