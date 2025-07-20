number1 = input("Enter your first number :")
number2 = input("Enter your second number :")
# this number actually coming string type

number1 = int(number1)   # int() function use for "string" data type to "int" type
number2 = int(number2)

# calculation process
sum = number1 + number2
sub = number1 - number2
mul = number1 * number2
div = number1 / number2

# printing process
print("The Summation is : ", sum)
print("The Subtraction is : ", sub)
print("The Multiplication is : ", mul)
print("The Division is : ", div)

