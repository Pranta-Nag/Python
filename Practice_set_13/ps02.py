"""
Generate and print the multiplication table using join of 7 from 1 to 10, each on a new line.

"""

table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)
print(s)