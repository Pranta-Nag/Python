"""
Write a program to find out whether a student has passed or failed if it requires a total of 40%
and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input
from the user

"""

"""
marks = []

a= int(input("Enter the marks gets on Bangla: "))
marks.append(a)
b= int(input("Enter the marks gets on English: "))
marks.append(b)
c= int(input("Enter the marks gets on Math: "))
marks.append(c)

total_mark = sum(marks)/300 * 100

if total_mark > 40 and a >= 33 and b >= 33 and c >=33:
    print("You passed.", round(total_mark, 2), "%")
    print("Best of luck for the future")
else:
    print("You Failed.", round(total_mark, 2), "%")
    print("Try again next year!")

"""

## Another Best Way

subjects = ["Bangla","English","Math"]
marks = []

for subject in subjects:
    mark = int(input(f"Enter the marks obtained in {subject}: "))
    marks.append(mark)

total_mark_percentage = sum(marks)/300 * 100

if all(mark >= 33 for mark in marks) and total_mark_percentage:
    print("You passed with", round(total_mark_percentage, 2), "%")
    print("Best of luck for the future")
else:
    print("You Failed.", round(total_mark_percentage, 2),"%")
    print("Try again next year!")








