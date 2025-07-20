"""
Define a Circle class to create a circle with redis r with a constructor.
Define an area() method of the class which calculates the area of the circle.
Define a perimeter() method of the class which allows you to calculate the perimeter of the circle

"""

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius **2         # area = pie * r ^2

    def perimeter(self):
        return 2 * (22/7) * self.radius         # perimeter = 2 * pie * r


c1 = Circle(12)
print("The circle area is : ", c1.area())
print("The circle perimeter is : ", c1.perimeter())
