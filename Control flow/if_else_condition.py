# 1st way
age = 10

if age >= 18:
    print("You are eligible. ")
else:
    print("You are not eligible.")

# 2nd way
if age >= 18:
    Message = "You are eligible."
else:
    Message = "You are not eligible."
print(Message)

# 3rd way
Message = "You are eligible." if age >= 18 else "You are not eligible."
print(Message)