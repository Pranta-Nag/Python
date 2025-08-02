class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The employee name is {self.name} and the salary is {self.salary}")

class Address(Employee):

    def __init__(self,name, salary, address):
        super().__init__(name,salary)
        self.address = address
    def show_address(self):
        print(f"The Employee of {self.name} address is : {self.address} ")


class Programmer(Employee):
    company = "Itec"  # Fixed assignment

    def __init__(self,name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_language(self):
        print(f"{self.name} is good at {self.language} programming language")


# Creating objects with required data
a = Employee("Rafi", 25000)
b = Programmer("Tanvir", 35000, "Python")
c = Address("Pushpa",45000,"Ctg")

print(a.company)  # ITC
print(b.company)  # Itec

a.show()          # The employee name is Rafi and the salary is 25000
b.show()          # The employee name is Tanvir and the salary is 35000
c.show_address()
b.show_language() # Tanvir is good at Python programming language



