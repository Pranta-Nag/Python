"""
    while condition:
                do work
"""
from sum_sub_mul_div.main import multiplication

count = 1
while count <=5:
    print("Hello", count)           # iterator
    count +=1

# print number from 1 to 5
i = 1
while i <=5:
    print(i)
    i +=1

print("Loop ended")

# print number from 5 to 1
j = 5
while j >=1:
    print(j)
    j -=1

print("Loop ended")

# print the multiplication table of n

mul = int(input("Enter a number: "))
i = 1
while i <=10:
    multiplication = mul * i
    print(mul, "*", i, ":", multiplication)
    i +=1

print("loop ended")

# print the following list using a loop

list = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(list):
    print(list[idx])        # list[0], list[1] ...... list[9]
    idx +=1

print("loop ended")

# search for a number x this tuple using loop
tuple= (1,4,9,16,25,36,49,64,81,100)
search = int(input("Enter the searching value: "))
i = 0
while i < len(tuple):
    if tuple[i] == search:
        print("Found at index: ", i)
    i +=1
else:
    print("This value don't exist the list")


# continue keyword
i = 1
print("Odd numbers are: ")
while i <=10:
    if(i%2 == 0):               # find odd number
        i +=1
        continue
    print(i)
    i +=1
else:
    print("End of loop")


j = 1
print("Even numbers are: ")
while j <=10:
    if(j%2 != 0):           # find even number
        j +=1
        continue
    print(j)
    j +=1
else:
    print("end of loop")

