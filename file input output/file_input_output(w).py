# 'w' => open for writing, truncating the file first

"""
    w = write mode : override the entire file
    a = append mode : adds to the file / add at the end

"""

"""
    Previous text = My name is Pranta Nag
                    I learn Python
"""

f = open("demo.txt", "w")
data = f.write("r+ => opens for reading and writing (cannot truncate a file),\nw+ => for writing and reading (can truncate a file),\nrb+ => reading or writing a binary file,\nwb+ => writing a binary file,\na+ => opens for appending ")
#print(data)
f.close()

f = open("demo.txt", "a")
data2 = f.write("\nNext I'll move mern stack.")
f.close()


