# Single Inheritance; Base -> derived

class School:
    name ="ABC high school"
    @staticmethod
    def welcome():
        print("Welcome dear students.")

    @staticmethod
    def location():
        print("London")

class Students(School):             # inherit parent(School) class

    def class_six(self, name, roll):
        self.name = name
        self.roll = roll

        print("Hi,", self.name)
        print("Your roll number is: ", self.roll)

s1 = Students()
s1.class_six("Shuvo", 9)
s1.welcome()
s1.location()
print("\n")


# Multi - level inheritance; Base -> derived -> derived

class School:
    name ="ABC high school"
    @staticmethod
    def welcome():
        print("Welcome dear students.")

    @staticmethod
    def location():
        print("London")

class Students(School):             # inherit parent(School) class

    def class_six(self, name, roll):
        self.name = name
        print("Hi,", self.name)

class Roll(Students):               # inherit parent(Students) class

    def roll_no(self, roll):
        self.roll = roll
        print("Your roll is: ", self.roll)


s1 = Roll()
s1.class_six("Shuvo", 9)
s1.welcome()
s1.location()
s1.roll_no(3)
print("\n")


# Multiple inheritance; Base1 -> derived <- Base2

class A:
    var1 = "Welcome to class A."

class B:
    var2 = "Welcome to class B."

class C(A,B):               # inherit Class A & B both
    var3 = "Welcome to class C."

c1 = C()
print(c1.var1)
print(c1.var2)
print(c1.var3)

