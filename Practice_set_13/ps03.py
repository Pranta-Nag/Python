"""
Write a program to find the maximum of the number in a list using the reduce function.

"""
from functools import reduce

l = [84,35,84,2445,945,2433,854,3535,784]

def greate(a,b):
    if a > b:
        return a
    return b

s = reduce(greate,l)
print(s)
