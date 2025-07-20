# with open("file name", "mode") as f:
# data = f.write()

with open("sample.txt", "r") as f:

    data = f.read()
    print(data)

# with => file closed automatically

# previous text = "I learn python"

with open("sample.txt", "w") as f:

    data = f.write("I learn mern stack")