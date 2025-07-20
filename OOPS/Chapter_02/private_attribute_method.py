class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass      # using duble underscore __ for private anything

acc1 = Account(35556, "waffga")
print(acc1.acc_no)
print(acc1.__acc_pass)          # output: 'Account' object has no attribute '__acc_pass'; acc_pass not accessible.

# another example

class Person:
    __name = "abc"          # private class variable

    def __hello(self):              # # private method
        print("Hello person")
    def welcome(self):
        self.__hello()               # calling private method from inside the class

p1 = Person()
p1.welcome()