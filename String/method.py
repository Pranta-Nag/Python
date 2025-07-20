# String methods

# convert to uppercase
text = "hello bangladesh !"
print(text.upper())

# convert to lowercase
text = "How are You ?"
print(text.lower())

# capitalize the first word
print(text.capitalize())

# title case
text = "pranta nag"
print(text.title())

# swap case
print(text.swapcase())

# replace a substring
print(text.replace("pranta", "shuvo"))

# split the string into a list
text = "Hello-world-with-Python"
print(text.split("_"))

# join list into a string
text= ["My", "name", "is", "Pranta"]
print(" ".join(text))

# strip whitespace form both side
text = "     Love     "
print(text.strip())

# remove leading whitespace
print(text.lstrip())

# remove trailing whitespace
print(text.rstrip())

# check if starting starts with a substring
text= "Hello Dear"
print(text.startswith("Hello"))    # return = true
print(text.startswith("Dear"))      # return = false
# as well as text.endswith

# substring position
print(text.find("Dear"))

# check if all characters are alphanumeric
print(text.isalnum())

# check if all characters are alphabatic
print(text.isalpha())

# check if all characters are number
print(text.isdigit())

# check if all characters are titlecase
print(text.istitle())

# removing extra spaces & converting to uppercase
text= "  Hello Dear  "
print(text.strip().upper())


"""
use case:
    - Data checking, formatting
    - text analysis
    - user input processing
    - generating dynamic text
    
"""