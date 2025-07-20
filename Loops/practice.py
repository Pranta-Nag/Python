# WAP to find the sum of first n natural numbers (using while)
from math import factorial

n = int(input("Enter the number: "))
i = 1
sum = 0

while i<=n :
    sum += i
    i += 1
print("Total sum is : ", sum)

# WAP to find the sum of first n natural numbers (using range)

n = int(input("Enter the number: "))
sum = 0
for i in range(1,n+1):
    sum += i

print("Total sum is: ", sum)


# WAP to find the factorial of first n numbers (using for)

num = int(input("Enter the number: "))
fact = 1

for m in range(1, num+1):
    fact *=m

print("The factorial is :",fact)

# Print a Right-Angled Triangle (Using for loop)

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print("*" * i)

# Reverse a Number (Using while loop)

num = int(input("Enter a number: "))
original = num  # Store original value if needed
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)
