# block of statement that performs specific task
"""
    def function_name(parameters):      # def => define
            # some work
        return value
"""

def calc_sum(a,b):              # create function with parameters
    sum = a+b
    print("The sum is: ", sum)
    return sum

calc_sum(10,10)
calc_sum(200,200)

def word():                 # create function without parameters
    print("hello")

word()
word()

# average of 3 numbers

def average(number1,number2,number3):
    ave = (number1+number2+number3)/3
    print("The average of number is: ", ave)
    return ave

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first number: "))
num3 = int(input("Enter the first number: "))

average(num1,num2,num3)

""" another way """
def average(number1,number2,number3):
    ave = (number1+number2+number3)/3
    print("The average of number is: ", ave)
    return ave

numbers = []
i = 0
while i < 3:
    num = (int(input(f"Enter the value {i + 1} :")))
    # f"..." হলো f-string, যেটা Python 3.6+ এ ব্যবহার হয়।
    # এটি ভেরিয়েবলকে স্ট্রিংয়ের মধ্যে embed করতে দেয়।
    numbers.append(num)
    i += 1

average(numbers[0],numbers[1], numbers[2])

