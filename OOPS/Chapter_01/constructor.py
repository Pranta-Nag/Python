class Student:
    college_name = "ABCDEF"
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks

s1 = Student("Shuvo", 70)
print(s1.name, s1.marks)

s2 = Student("Pranta", 78)
print(s2.name, s2.marks,"",s2.college_name)


"""
In Python, self is a fundamental concept when working with object-oriented programming (OOP).
It represents the instance of the class being used.
Whenever we create an object from a class, self refers to the current object instance. 
It is essential for accessing attributes and methods within the class.
"""

# create class



