# when a function calls itself repeatedly

# random function process
"""
def show(n):
    for i in range(n, 0, -1):
        print(i)
show(5)

"""
from math import factorial


# recursive function
def show(n):
    if(n == 0):                 # base case
        return
    print(n)
    show(n-1)           # function call itself

show(5)

# find factorial

num = int(input("Enter a number: "))

def fact(num):
    if (num == 0 or num ==1 ):
        return 1
    else:
        return fact(num-1) * num

result = fact(num)

print("The factorial is: ", result)
print("The factorial is: ", result)
