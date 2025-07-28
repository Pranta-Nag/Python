#### Write a program to find whether a given number is prime or not.

num = int(input("Enter a number: "))

if num <= 1:
    print("The number is not prime.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")
