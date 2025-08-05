"""
Create a class 'pets' from a class 'animals' and further create a class 'dog' from 'pets'.
Add a method 'bark' to class 'dog'

"""
class Animal:
    pass
class Pets(Animal):
    pass
class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow !")

    def bark2(self):
        print("The dog sound Bow Bow !")


d = Dog()
d.bark()
d.bark2()

