#### Write a program using function to find the greatest number


def grest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = 10
b = 20
c = 6

print(grest(a, b, c))  # Output: 20

"""
write a program using function the given pattern

***
**
*

"""

def pattern():
    for i in range(n,0,-1):
        print("*"* i)

n = int(input("Enter a number: "))
pattern()