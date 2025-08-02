"""
Create a class 'calculator' capable of finding squares, cube and square root of a number
"""

class Calculator:

    def __init__(self, a):
        self.a = a

    def square(self):
        print(f"The square of number {self.a} is {self.a * self.a}")

    def cube(self):
        print(f"The square of number {self.a} is {self.a * self.a * self.a}")

    def square_root(self):
        print(f"The square of number {self.a} is {self.a ** 0.5}")

a = int(input("Enter a number: "))
cal = Calculator(a)
cal.square()
cal.cube()
cal.square_root()
