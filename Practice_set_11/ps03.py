"""
Create a class 'Employee' and add salary and increment properties to it.

write a method 'incrementAfterSalary' method with a @property decorator with a setter
which changes the value of increment based on the salary.
"""

class Employee:
    def __init__(self, salary=400, increment=20):
        self.salary = salary
        self.increment = increment

    @property
    def incrementAfterSalary(self):
        return (f"Salary after increment : {self.salary + self.salary * (self.increment / 100)}")

    @incrementAfterSalary.setter
    def incrementAfterSalary(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100


e = Employee()
print(e.incrementAfterSalary)
e.incrementAfterSalary = 28000
print(e.increment)
