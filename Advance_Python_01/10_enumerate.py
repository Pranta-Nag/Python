l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

# The enumerate() function in Python is a built-in function that adds
# a counter to an iterable and returns it as an enumerate object.

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")