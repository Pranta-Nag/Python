class Student:
    name = "ABC"

    @classmethod
    def changeName(cls, name):      # change the class Student name
        cls.name = name

c1 = Student()
c1.changeName("Rahul")
print(Student.name)
