"""
Write a python function to remove the given word from a list
and strip it at the same time.
"""

"""
def remove_word(list, word_to_remove):
    clean_list = []
    for w in list:
        w = w.strip()
        if w != word_to_remove:
            clean_list.append(w)
    return clean_list

list = []
n = int(input("How many words? Ans: "))

for i in range(n):
    w = input(f"Enter word {i + 1}: ")
    list.append(w)
print(list)

p = input("Which Word you want to remove? Ans: ")
result = remove_word(list,p)
print(result)

"""

def remove_word(word,word_to_remove):
    clean_list = []
    for a in word:
        a = a.strip()
        if a != word_to_remove:
            clean_list.append(a)
    return clean_list


word = []
word_input = input("How many you want to input? Ans: ")

for i in range(word_input):
    inp = input(f"Enter the {i} word: ")
    word.append(inp)
print(word)

p = input("Which word you want to remove? Ans: ")
result = remove_word(word,p)
print(result)

