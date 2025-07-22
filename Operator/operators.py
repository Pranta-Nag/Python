# Arithmetic operator

a = 10
b = 20
c = a + b
print(c)

# Assignment operator

a = 4 - 2           # Assign 4-2 in a
print(a)            # output : 2

b = 6

b += 3              # increment the value of b by 3 and then assign it to b
print(b)            # 6 + 3 = 9

b -= 2              # decrement the value of b by 3 and then assign it to b
print(b)            # 9 - 2 = 7

b *= 4              # multiply the value of b by 3 and then assign it to b
print(b)            # 7 * 4 = 28

b /=2               # divided the value of b by 3 and then assign it to b
print(b )           # 28 / 2 = 14

# Comparison operator; return always boolean - True or False

g = 5 < 8
print(g)                # return true

f = 5 <=5
print(f)                # return true

i = 5 != 5
print(i)                # return false


# Logical operator

a = True or False       # if any value is true; return always true (or operator)
print("True or True is =>", True or True)
print("True or False is =>", True or False)
print("False or True is =>", False or True)
print("False or False is =>", False or False)

print("\n")
b = True and False      #  if both values are true; return true, otherwise return false.(and operator)
print("True and True is =>", True and True)
print("True and False is =>", True and False)
print("False and True is =>", False and True)
print("False and False is =>", False and False)

print("\n")
print(not(True))          # return False  (not operator => True -> False, False -> True)
print(not(False))          # return True

