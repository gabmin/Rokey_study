import os

print(os.getcwd())


path = r"C:\Users\rlark\Desktop\Rokey\python\ch12\file2.txt"
mode = "w"

with open(path, mode) as f:
    f.write("Hello World")
