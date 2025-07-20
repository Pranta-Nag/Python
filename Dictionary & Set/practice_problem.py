"""
    Q 1: store following word meanings in the python Dictionary
            table: 'a piece of furniture', 'list of facts & figures'
            cat: 'a small animal'
"""

dictionary = {
        "cat" : "a small animal",
        "table" : {                 # store list form
            "a piece of furniture",
            "list of facts & figures"
        },
    "table2" : (                    # store tuple form
        "a piece of furniture",
        "list of facts & figures"
    )
}

print(dictionary)
print(type(dictionary))

"""
    Q 2: you are given a list of subjects for students. Assume one classroom 
            is required for 1 subjects. How many classrooms are needed by all students.
        
        "python", "java", "c++", "python", "javascript"
        "java", "python", "java", "c++", "c"
"""

subjetcs = {
         "python", "java", "c++", "python", "javascript",
        "java", "python", "java", "c++", "c"
}

#print(subjetcs)
print(len(subjetcs))
print(type(subjetcs))


"""
    Q 3 : WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
            start with an empty dictionary & add one by one. use subjects name as key, marks as values.
"""

subjetcs_dic = {}

x = int(input("Enter physics mark: "))
subjetcs_dic.update({"Phy" : x})

x = int(input("Enter math mark: "))
subjetcs_dic.update({"Math" : x})

x = int(input("Enter bangla mark: "))
subjetcs_dic.update({"Bangla" : x})

print(subjetcs_dic)

"""
    Q 4: Figure out of way to store 9 & 9.0 as separate value in the set
            (use built in data type)
"""

value = { 9, "9.0"}             # one way ; string form
print(value)

value2 = {
    ("int", 9),                 # another way ; tuple form
    ("float", 9.0)
}
print(value2)