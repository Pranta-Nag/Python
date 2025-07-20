"""
    create a new file "practice.txt" using python.
"""

with open("practice.txt", "w") as  f:
    f.write("Hello everyone,\nLearn python,\nNext learn mern stack.")

"""
    WAF that replaces all occurrences of "python" with "java" in the above file
     
"""

def replace():
    with open("practice.txt", "r") as f:
        data = f.read()
        print(data)

    new_data = data.replace("python", "java")
    print(new_data)

    with open("practice.txt", "w") as f:
        f.write(new_data)

replace()

"""
    Search if the word "Learn" exists the file or not
    
"""
word = "Learn"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not found")

"""
    WAF to find in which line of the does the word ' ' occurs first,
    print -1 if word not found
    
"""

def find_line_num():
    word = "mern"
    line = 1
    with open("practice.txt", "r") as f:
        for data in f:
            if word in data:
                print("Line number: ", line)
                return
            line += 1

    return -1

result = find_line_num()
if result == -1:
    print("Not found")

"""
    from a file containing numbers separated by comma, print the count of even numbers
    
"""

with open("numbers.txt", "w") as f:
    f.write("1,3,4,6,8,2")

with open("numbers.txt", "r") as f:
    count = f.read()
    num = count.split(",")

    """ for data in count: → এটা ক্যারেক্টার ধরে (string char by char)
         count = "1,3,4,6,8,2" → তাহলে for data in count: হলে data হবে:
                '1', ',', '3', ',', '4', ',', '6', ',', '8', ',', '2'
    """

    for data in num:
        if int(data) %2 == 0:           # parsing string to int
           # print("The even numbers are: ", data)
            result = data
            print("The even numbers are: ", data)



