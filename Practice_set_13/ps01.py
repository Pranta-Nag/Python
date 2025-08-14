"""
Write a program to filter a list of numbers which are divisible by 5

"""

def divisible(n):
    if(n%5 == 0):
        return True
    return False

l = [4,65,35,82,68,33,86,3455]

m = list(filter(divisible, l))

print(m)
