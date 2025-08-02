"""
Repeat program 4 for a list of such words to be censored

"""

words = ["Monkey", "Donkey", "Little"]

with open("text.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "&"*len(word))

with open("text.txt", "w") as f:
    f.write(content)