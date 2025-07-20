class School:
    def __init__(self,school):
        self.school =school

    @staticmethod
    def welcome():
        print("Welcome dear students.")

    @staticmethod
    def location():
        print("London")

class Students(School):             # inherit parent(School) class

    def class_six(self, school):
        super().__init__(school)          # inherit method to parent class

s1 = Students("ABC high school")
print(s1.school)
print(s1.welcome())

