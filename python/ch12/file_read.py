import os

print(os.getcwd())


path = "C:/Users/rlark/Desktop/Rokey/python/ch12/file.txt"
mode = "r"

f = open(path, mode, encoding="utf-8")

# lines = f.readlines()
#
# for i in lines:
#     print(i, end=" ")

data = f.read()
print(data)

f.close()
