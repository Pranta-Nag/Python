"""
Write a program to print multiplication table of using for loop
in reverse order

"""

n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} * {11- i} = {n * (11-i)}")

# or

n = int(input("Enter a number: "))

for i in range(10,0,-1):
    print(f"{n} * {i} = {n*i}")