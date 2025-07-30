"""
A file contains a word "Monkey" multiple times. You need to write a program which replace the
word with ##### by updating the same file.

"""

word = "monkey"

with open("monkey.txt", "r") as f:
    text = f.read()

new_text = text.replace(word, "#####")

with open("monkey.txt", "w") as f:
    f.write(new_text)