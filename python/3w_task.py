# 1번
import tkinter

my_tkinter = tkinter.Tk()

my_tkinter.title("간단한 Tkinter 앱")

my_tkinter.geometry("300x300")

my_button = tkinter.Button(
    my_tkinter, text="버튼", command=lambda: print("버튼이 클릭되었습니다!")
)

my_button.place(x=125, y=125)

my_tkinter.mainloop()


# 2번

path = "./data.txt"
mode = "w"
f = open(path, mode, encoding="utf-8")

for i in range(1, 11):
    f.write(f"{i}번째 줄입니다.\n")

path = "./data.txt"
mode = "r"
f = open(path, mode, encoding="utf-8")
f_list = f.readlines()

for i in f_list:
    print(i, end="")


# 3번
path = "./data.txt"
mode = "a"

f = open(path, mode, encoding="utf-8")

f.write("11번째 줄입니다.")


# 4번

while True:
    try:
        data = int(input("숫자를 입력하세요."))
        print(data)
        break
    except ValueError:
        print("올바른 숫자를 입력하세요!")


# 5번

list_a = [10, 20, 30, 40, 50]
squared_list = map(lambda x: x**2, list_a)
print(list(squared_list))


# 6번

text = """python one
life is too short
python two
you need python
python three"""

import re

pattern = r"^python"

for line in text.splitlines():
    if re.match(pattern, line):
        print(line)


# 7번


class MyIter:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        result = self.data[self.index]
        self.index += 1
        return result


list_a = [1, 2, 3, 4, 5, 6]
for i in MyIter(list_a):
    print(i)


# 8번

name = input()
age = input()

print(f"-이름을 입력하세요: {name}\n-나이를 입력하세요: {age}")


# 9번

import re

text = input("이메일을 입력하세요.")
pattern = r"\w+@\w+\.\w+"

if re.match(pattern, text):
    print("올바른 이메일 형식입니다.")
else:
    print("이메일 형식이 잘못되었습니다.")


# 10번


def generate_squares(n):
    for i in range(1, n + 1):
        yield i**2


print(list(generate_squares(10)))
