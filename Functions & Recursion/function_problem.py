######## WAP to print the length of a list (list is the parameter)
from locale import currency

cities = ["ctg", "dhk", "cuml", "rang"]
names = ["shuvo", "pranta", "joy"]

def print_length(list):
    print(len(list))
    return list

print_length(names)
print_length(cities)

###### WAP to print the elements of a single line (list is the parameter)

cities = ["ctg", "dhk", "cuml", "rang"]
names = ["shuvo", "pranta", "joy"]

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(names)
print("\n")

###### WAP to find the factorial of n (n is the parameter)

# num = int(input("Enter your number: "))       : ekbar input nibe
def factorial():
    num = int(input("Enter your number: "))         # work everytime new input
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print("The factorial is: ", fact)

factorial()
#factorial()

###### Convert USD to TAKA

def converter():
    usd_money = int(input("Enter the USD : "))
    taka = usd_money * 121
    print(usd_money, "USD = ", taka, "Taka")

converter()

####### Write a function,user input & check even or odd, return string odd / even

def check():
    num = int(input("Enter a number: "))
    if num%2 == 0:
        print("The number is EVEN.")
    else:
        print("The number is ODD.")

check()


