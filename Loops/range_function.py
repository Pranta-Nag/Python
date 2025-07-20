# range function returns a sequence a number, starting form 0 by default,
# increments by 1, and stop before a specified number.
# renge(start?, stop, step?)
from sum_sub_mul_div.main import multiplication

value = range(5)
for i in value:
    print(i)
print("loop end")
# or

for i in range(5):              # stop
    print(i)
print("loop end")

for i in range(2,5):            # start, stop
    print(i)
print("loop end")

for i in range(1,5,2):          # start, stop, step
    print(i)
print("loop end")

# print even number using range function

num = int(input("Enter the range value: "))

for i in range(0, num, 2):
    print(i)
print("loop end")

# print odd number using range function

num = int(input("Enter the range value: "))

for i in range(1, num, 2):
    print(i)
print("loop end")

# print the multiplication table on number n

num = int(input("Enter a number: "))

for mul in range(1, 11):
    multiplication = mul * num
    print(num, "*",mul, ":", multiplication)
print("Multiplication end")


# pass statement => pass is a null statement that does nothing.
# it is used as a placeholder for future code

for i in range(4):
    pass

if i > 4:               # pass also work on if - else condition
    pass

print("done the work in future")

