import os

print(os.getcwd())

path = "C:/Users/rlark/Desktop/Rokey/python/ch12/file.txt"
mode = "a"

f = open(path, mode, encoding="utf-8")

for i in range(11, 21):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)

f.close()
