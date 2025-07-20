# a build in data type that lets us create immutable sequences of values

tup = (1,3,4,5)
print(type(tup))            # print type class
print(tup[3])               # print index element
# tup= (4,)     # coma must be need after set a single value

print(tup[1:3])     # slicing

tup2 = (3,2,7,0)
print(tup2.index(2))        # print index number of value: 2

tup3 = (4,2,7,2 ,6,2)
print(tup3.count(2))



