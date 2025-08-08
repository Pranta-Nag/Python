"""
Write a program to display a/b, where a and b are integers. If b = 0, display infinite
by handling the 'ZeroDivisionError'

"""

try:
    a = int(input("Input a number: "))
    b = int(input("Input a number: "))

    print(a/b)

except ZeroDivisionError as e:
    print("Exception")