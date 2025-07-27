# 1st way
age = int(input("Enter Your Age: "))

# If statement no: 1
if age%2 == 0:
    print("Age is even.")
else:
    print("Age in Odd.")
# End if statement no: 1

# If statement no: 2
if age >= 18:
    print("You are eligible. ")

elif age < 0:
    print("Please entering a valid age.")

elif age == 0:
    print("Please entering 0 which is not valid age.")

else:
    print("You are not eligible.")
# End if statement no: 2

# 2nd way
"""if age >= 18:
    Message = "You are eligible."

elif age < 0:
    print("Please entering a valid age.")

else:
    Message = "You are not eligible."

print(Message)
"""

# 3rd way
""" Message = "You are eligible." if age >= 18 else "You are not eligible."
print(Message)
"""

