##### Write a program to store seven fruits in a list entered by the user

fruits = []

f1= input("Enter the first fruit name: ")
fruits.append(f1)
f2= input("Enter the second fruit name: ")
fruits.append(f2)
f3= input("Enter the third fruit name: ")
fruits.append(f3)
f4= input("Enter the forth fruit name: ")
fruits.append(f4)
f5= input("Enter the fifth fruit name: ")
fruits.append(f5)
f6= input("Enter the sixth fruit name: ")
fruits.append(f6)
f7= input("Enter the seventh fruit name: ")
fruits.append(f7)

print(fruits)

# or -> easy way using the loop
"""
for i in range(1,8):
    fruit = input(f"Enter the {i} fruit name: ")
    fruits.append(fruit)

print(fruits)

"""

