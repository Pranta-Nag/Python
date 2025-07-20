"""
    Text file: .txt, .docx, .log etc
    Binary file: .mp4, .mov, .png, .jpeg

    f = open("file name", "mode")  => sample.txt, r : read mode / w : write mode
        data = f.read() / f.write()

    f.read() => reads entire file
    f.readline() => reads one line at a time

"""

f = open(r"C:\Users\L.Point\Desktop\Python\Number\type_conversion.py", "r")     # connect type_conversion file
# complete path of this file. r use for identity raw string. OR we used \\. Because python ignores single \.
data = f.read()     # if I pass a parameter f.read(5) , output = first 5 letter
#data = f.read(10)
print(data)

#line1 = f.readline()                # print first line
#print(line1)

#print(type(data))
f.close()

"""
    'r' => open for reading (default)
    'w' => open for writing, truncating the file first
    'x' => create a new file & open it for waiting
    'a' => open for waiting, appending to the end of the file if it exists
    'b' => binary mode
    't' => text mode (default)
    '+' => open a disk file for updating (reading & writing)

"""



