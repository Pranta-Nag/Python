class Student:

    def __init__(self, math, phy, che):
        self.math = math
        self.phy = phy
        self.che = che

    @property
    def percentage(self):
        return str( ( self.che + self.math + self.phy ) / 3)  + "%"


s1 = Student(75,86,74)
print(s1.percentage)

s1.math = 66
print(s1.percentage)            # change the percentage calculation

"""
# Before using property method

     def calPercentage(self):
        self.percentage = str( ( self.che + self.math + self.phy ) / 3)  + "%"

s1.calPercentage()
print(s1.percentage)

s1.math = 57            # change the math number
print(s1.math)
print(s1.percentage)    # but don't change percentage calculation

"""
