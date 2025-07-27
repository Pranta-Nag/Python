##### Write a program to create a dictionary of Bangla words with values as there English translation.
#       Provide user with an option to look it up!

language = {
    "Vat" : "Rice",
    "Kola" : "Banana",
    "Manush" : "Man",
    "Golap" : "Rice",
    "Galib" : "Fat & thick"

}
word = input("Enter the word you want meaning of: ")
print(f"The {word} meaning is :",language[word])



##### Write a program to input eight numbers from the user and display all the unique numbers (once)

uni_num = set()
for i in range(1,9):
    numbers = int(input(f"Enter the {i} numbers :"))
    uni_num.add(numbers)

#print(uni_num)
# or

print("Unique numbers entered:")
for num in uni_num:
    print(num)

