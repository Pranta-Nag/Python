"""
Create a class "Programmer" for storing information of few programmers working at Microsoft

"""

class Programmer:
    company = "Microsoft"
    print(company)

    def __init__(self, name, age, salary, language):
        self.name = name
        self.age = age
        self.salary = salary
        self.language = language


Shuvo = Programmer("Shuvo", 25, 200000, "Python")
print(Shuvo.name, Shuvo.age, Shuvo.salary, Shuvo.language)

Pranta = Programmer("Pranta", 26, 180000, "JavaScript")
print(Pranta.name, Pranta.age, Pranta.salary, Pranta.language)