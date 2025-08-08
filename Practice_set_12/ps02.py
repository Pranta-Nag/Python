"""
Write a program to print third, fifth and seventh element from a list using enumerate function

"""

list = [3,6,2,7,8,10,67,34,75]

for i, item in enumerate(list):
    if i == 3 or i == 5 or i == 7:
        print(item)

