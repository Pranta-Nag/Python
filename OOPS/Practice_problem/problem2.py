"""
Define an Employee class with attributes role, department & salary .
This class also showDetails() method.
Create an Engineer class that inherits properties from employee and has additional attributes : name & age

"""

class Employee:

    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role =", self.role)
        print("Department = ", self.department)
        print("Salary =", self.salary)

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Name = ", self.name)
        super().__init__("Engineer", "IT", "70000")


engr1 = Engineer("Pranta Nag", "25")
engr1.showDetails()