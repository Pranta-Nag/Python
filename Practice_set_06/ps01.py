##### Write a program to find the gratest of four numbers entered by the user

numbers = []

for i in range(1,5):
    num = int(input(f"Enter the {i} number: "))
    numbers.append(num)

print("The greatest number is: ", max(numbers))

# OR

a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
c = int(input("Enter the first number: "))
d = int(input("Enter the first number: "))

greatest = a

if b > greatest:
    print("The Greatest number is", b)
if c > greatest:
    print("The Greatest number is", b)
if d > greatest:
    print("The Greatest number is", d)
else:
    print("The greatest number is: ",a)

