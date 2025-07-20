"""
    create student class that takes name & marks of 3 subjects as arguments in constructor.
    Then create a method to print the average

"""

class Student:
    def __init__(self, name, bangla, english, math):
        self.name = name
        self.bangla = bangla
        self.english = english
        self.math = math

    def student_name(self):
            print("Your name is: ", self.name)
    def marks(self):
            print("Bangle: ",self.bangla, "\nEnglish: ", self.english, "\nMath: ", self.math)
    def average(self):
        avg = (self.bangla + self.english + self.math)/3
        print("The average marks is: ", avg)


s1 = Student("Pranta", 96, 77, 85)
s1.student_name()
s1.marks()
s1.average()

# another way (best approach)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def student_name(self):
            print("Your name is: ", self.name)
    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("The average marks is: ", sum/3)

s1 = Student("Pranta", [66, 75, 84])
s1.student_name()
s1.average()


"""
    create account class with 2 attributes- balance & account no
    create methods for debit, credit & printing the balance
    
"""

class Account:
    def __init__(self,balance,account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance -= amount              # formula: Debit = balance - amount
        print("Tk.", amount, "was debited." )
        print("Your total balance = ",self.balance)

    def credit(self, amount):
        self.balance += amount                  # formula: Credit = balance + amount
        print("Tk.", amount, "was credited.")
        print("Your total balance = ",self.balance)

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 35265)
acc1.debit(1000)
acc1.credit(3000)
acc1.debit(1000)
acc1.credit(20000)

