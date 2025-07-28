"""
A spam comment is defined as a text containing following keywords :
"Make a lot of money","buy now","Subscribe this","click this". Write a program to detect these spams.

"""
keyword = ["Make a lot of money","buy now","Subscribe this","click this"]

comment = input("Enter your comment: ")

if comment in keyword:
    print("This comment is a spam.")
else:
    print("There has no spam comment.")



#### Write a program to find whether a given username contains less than 10 characters or not

char = input("Give a username: ")

if len(char) < 10:
    print("Username less than 10 characters.")
else:
    print("Username not less than 10 characters")
