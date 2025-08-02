"""
Write a class 'Train' which was method to book a ticket, get status(no of seats) and get fare information
of train running under Bangladesh Railways.

"""
from random import randint


class Train:

    def __init__(self, trainNo):
        self.traintNo = trainNo

    def book(self, starting, to):
        print(f"The Ticket is booked in Train No:{self.traintNo} {starting} to {to}")

    def status(self):
        print(f"The Train no: {self.traintNo} is running.....")

    def getfare(self, starting, to):
        print(f"Ticket fare in train no: {self.traintNo} from {starting} to {to} is {randint(122,450)} ")

t = Train(3566)
t.book("Dhaka", "Chittagong")
t.status()
t.getfare("Dhaka", "Chittagong")