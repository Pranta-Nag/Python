print( 2 + 5)       #3
print("Pranta" + " Nag")        # concatenate
print([1,4,5] + [6,7,8])        # marge
# this is also called operator overloading (polymorphism)

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, " j")

    # addition
    def __add__(self, other):           # Dunder function
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal,newImg)      # return new complex class

    # subtraction
    def __sub__(self, other):           # Dunder function
        newReal = num1.real - num2.real
        newImg = num1.img - num2.img
        return Complex(newReal,newImg)      # return new complex class

    # multiplication
    def __mul__(self, other):  # Dunder function
        newReal = num1.real * num2.real
        newImg = num1.img * num2.img
        return Complex(newReal, newImg)  # return new complex class

    # divition
    def __truediv__(self, other):  # Dunder function
        newReal = num1.real / num2.real
        newImg = num1.img / num2.img
        return Complex(newReal, newImg)  # return new complex class

num1 = Complex(2,4)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

add = num1 + num2
add.showNumber()

sub = num1 - num2
sub.showNumber()

mul = num1 * num2
mul.showNumber()

div = num1 / num2
div.showNumber()
