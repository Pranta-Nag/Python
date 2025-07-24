##### Write a python program to display a user entered name followed by Good afternoon using input() function.

name = input("Enter your name: ")
print(f"Good afternoon {name}")             # using f string



"""
Write a program to fill in a letter template given below with name and date
    letter = '''
                Dear <name>,
                You are selected!
                <date>    
    '''
"""

letter = '''
 Dear <name>,
 You are selected!
 <date>    
    '''
name = input("Enter a name:")
date = input("Enter date:")

print(letter.replace("<name>", name).replace("<date>", date))



##### Write a program to detect double space in a string

text = "I am a good  boy."

print(text.find("  "))              # find double space



##### Replace the double space form problem 3 with single space

print(text.replace("  ", " "))



