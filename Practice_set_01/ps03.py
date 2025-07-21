###### P-3: Write a python program to print the contents of a directory using the OS model.
    # Search online for the function which does that

import os

# Specify the directory path (you can change this to any directory)
directory_path = "/"

# Get the list of files and directories
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permissions to access this directory.")