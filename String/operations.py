# String indexing => positive, negative
from time import process_time

# positive indexing
text = 'Hello Bangladesh'
print(text[3])      # counting to start 0,1,2,3,4...

# negative indexing
text = 'Hello Bangladesh'
print(text[-4])     # counting to end -1,-2,-3,-4 ....

# String slicing => start, stop, step

# start slicing
text = 'Hello Bangladesh'
print(text[0:8])        # Cut down 0 to 7 index

# stop slicing
text = 'Hello Bangladesh'
print(text[7:])     # cut down 7 to last index

# step slicing
text = 'Hello Bangladesh'
print(text[0::3])       # cut down 2 step 2 index

"""
Use Case- 
1) Extracting substrings
2) Reversing Strings
3) Manipulating
4) Parsing data
5) Validation & Formating
6) Analyzing data
7) Cleaning data

"""

# String repetition
name = "Pranta "
print(name * 10)

# String concatenation
str1 = 'Pranta '
str2 = 'Nag'

combine1 = str1 + str2      # using + operator
print(combine1)

combine2 = "{} {} ".format(str1,str2)       # using format() method
print(combine2)

combine3 = "%s %s " %(str1,str2)        # using % formating method
print(combine3)

combine4 = " ".join([str1,str2])        # using join() method
print(combine4)

"""
Use case:
1) Building dynamic method
2) URL construction
3) File paths
4) Tamplate strings
5) Data formatting
6) Generate patterns
7) Formating , Initializaton

"""