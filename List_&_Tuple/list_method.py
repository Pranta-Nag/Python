num = [3,2,5,7]
num.append(9)       # add value in the last index
print(num)

num2 = list(input("Enter the numbers: ").split())   # user input into list
num2.sort()          # sorting ascending order
print(num2)
# sort() method do not return anything

num2.sort(reverse= True)        # sorting descending order
print(num2)

fruits = ["banana", "apple", "mango"]
fruits.sort()       # sort also work on strings
print(fruits)
fruits.reverse()    # reverse string items
print(fruits)

# list.insert(idx,el)
fruits.insert(1,"watermelon")       # add new string on index 1
print(fruits)

# list.pop(index) remove occurrence on first
fruits.pop(3)
print(fruits)

fruits.remove("mango")
print(fruits)

