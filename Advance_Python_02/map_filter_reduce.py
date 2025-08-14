"""
The map() function applies a given function to each item of an iterable (like a list, tuple, or set)
and returns an iterator (a map object) with the results.
This is a concise way to perform transformations on collections of data without explicit for loops.

"""
from functools import reduce
# Map Example
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))


"""
The filter() function returns an iterator 
where the items are filtered through a function to test if the item is accepted or not.

"""
# Filter Example
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven= filter(even, l)
print(list(onlyEven))


"""
The reduce() function in Python, found within the functools module, is a higher-order function that applies a 
given function cumulatively to the items of an iterable, reducing the iterable to a single cumulative value. 
"""

# Reduce Example
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))