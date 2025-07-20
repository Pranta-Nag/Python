# nested dictionary = one dic under another dic

students = {
    "Name" : "Pranta",
    "Subjects" : {
        "COA" : 77,
        "OOP" : 67,
    }
}

print(students)
print(students["Subjects"])             # print subjects
print(students["Subjects"]["COA"])      # print Coa number

print(students.keys())              # .key()method used for print keys strings, returns all keys
print(list(students.keys()))        # list() used for type casting
print(len(students))                # len() used for print keys length
print(len(list(students.keys())))       # all methods in a single line

print(students.values())            # .value() method return all values

print(students.items())         # .item() method return all (key, value) pair value
print(list(students.items()))       # type casting
#or
pairs = list(students.items())
print(pairs[0])             # print any index pair

print(students["Name"])             # natural way; if change index like students["Name2"] => show error.
                                    # and it interfare to execute after code
print(students.get("Name"))         #.get() method ; students.get("Name") => return none

new_dic = {
    "City" : "Chittagong",
    "Age" : 25
}
students.update(new_dic)            # add / update new dictionary
print(students)




