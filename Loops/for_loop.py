str = "bangladesh"
for char in str:
    if(char == "l"):
        print("l found")
        break
else:
    print("End")


"""
    print the elements of the following list using for loop

"""
list = [1,4,9,16,25,36,49,64,81,100]

for ele in list:
    print(ele)

"""
    search for a number of the following tuple using for loop
    
"""
my_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
search = int(input("Enter the value: "))

idx = 0
for src in my_tuple:
    if src == search:
        print("Found the value at index:", idx)
        break
    idx += 1
else:
    print("This value does not exist in the tuple")



