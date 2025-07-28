"""
write a program that * patterns, n = 3

    *
   ***
  *****

"""

n = int(input("Enter a number: "))

for i in range(1,n+1):
    print(" "* (n-i) + "*" * (2*i - 1))


"""
write a program that * patterns, n = 3

*
**
***

"""
n = int(input("Enter a number: "))

for i in range(1,n+1):
    print("*"*i)


"""
write a program that * patterns

***
* *
***

"""
n = int(input("Enter a number: "))

for i in range(n):
   if i == 0 or i == n-1:
       print("*"*n)
   else:
       print("*" + " "*(n-2) + "*")