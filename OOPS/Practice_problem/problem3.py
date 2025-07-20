"""
Create a class call order which store item & its price
Use dunder function __gr__()to convey that
order1 > order2 if price of order1 > price of order2

__gt__ means: greater than

"""

class Order:

    def __init__(self, item, price):
        self.item =item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 = Order("Chips", 20)
odr2 = Order("Tea", 15)

print(odr1 > odr2)