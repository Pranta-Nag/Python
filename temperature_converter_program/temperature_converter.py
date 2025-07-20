from random import choice

print("Please choose an option:")
print("1. Celsius To Fahrenheit ")
print("2. Fahrenheit To Celsius")

choice = input("Enter an Option (1/2): ")  # choice => user choice

if choice == "1":
    celsius = input("Enter Celsius Value: ")
    celsius = float(celsius)        # Convert string data type to float data type
    fahrenheit = (9 / 5 * celsius) + 32     # cel to far convertion formula
    print("The Fahrenheit Value is: ", fahrenheit)

elif choice == "2":
    fahrenheit = input("Enter fahrenheit Value: ")
    fahrenheit = float(fahrenheit)       # Convert string data type to float data type
    celsius = (fahrenheit - 32) * 5/9       # far to cel convertion formula
    print("The Celsius Value is: ", celsius)

else:
    print("Invalid choice. Please try again.")

