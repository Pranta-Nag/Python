##### Write a program to calculate the grade of a student.
from pywin32_testutil import non_admin_error_codes

mark = int(input("Enter your mark: "))

if mark >= 80 and mark <= 100:
    grade = "A+"
elif mark >= 70 and mark <= 79:
    grade = "A"
elif mark >= 60 and mark <= 69:
    grade = "A-"
elif mark >= 50 and mark <= 59:
    grade = "B"
elif mark >= 33 and mark <= 49:
    grade = "C"
elif mark < 33 and mark >= 0:
    grade = "F"
else:
    print("Invalid mark")
    grade = None

if (grade is not None):
    print("Your grade is: ", grade)