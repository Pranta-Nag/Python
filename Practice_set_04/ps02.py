##### Write a program to accept marks of 6 students and display them is a sorted manner.

marks = []

for i in range(1,7):
    mark = int(input(f"Enter the {i} students mark: "))
    marks.append(mark)

marks.sort()
print(marks)


##### Write a program to sum a list with 4 numbers

list = [33, 64, 63, 73]
print(sum(list))