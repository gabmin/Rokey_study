# class Stack:
#     def __init__(self):
#         self.stack = ["두산", "로키", "부트"]
#
#     def push(self, value):
#         self.stack.append(value)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return None
#
#     def is_empty(self):
#         if len(self.stack) == 0:
#             return True
#         else:
#             return False
#
#
# s1 = Stack()
# s1.push("캠프")
# s1.pop()
#
# print(s1.stack)


# import turtle
#
# turtle.title("쿠루쿠루의 마법진")
# turtle.setup(500, 500)
# t = turtle.Turtle()
# t.shape("turtle")
# t.pensize(3)
# t.circle(100)
# t.penup()
# t.goto(0, 200)
# t.pendown()
# t.right(60)
#
# for i in range(3):
#     t.forward(170)
#     t.right(120)
#
# turtle.mainloop()


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./task_data.csv", encoding="cp949")

df_data = pd.DataFrame(data)

x = df_data["년도"]
y = df_data["영치대수"]

plt.rcParams["font.family"] = "Malgun Gothic"
plt.plot(x, y)
plt.xlabel("년도")
plt.ylabel("영치대수")

plt.show()
