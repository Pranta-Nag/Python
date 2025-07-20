# Problem 1: WAP to task the user to enter names of their three favourite movies & store them in a list

movies = list(input("Enter your three favourite movies name: ").split(","))
print(movies)

# another way

movies = []
mov1 = input("Enter your 1st favourite movie :")
mov2 = input("Enter your 2nd favourite movie :")
mov3 = input("Enter your 3rd favourite movie :")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# another way

movies = []
movies.append(input("Enter your 1st favourite movie :"))
movies.append(input("Enter your 2nd favourite movie :"))
movies.append(input("Enter your 3rd favourite movie :"))

print(movies)


# Problem 2: WAP to check if a list contains a palindrome of elements (hint: using copy() method)

list1 =[1,2,3,2,1]
list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("This is palindrome")
else:
    print("This is not palindrome")

# or,
list1 = list(input("Enter few numbers: "))
list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("This is palindrome")
else:
    print("This is not palindrome")

