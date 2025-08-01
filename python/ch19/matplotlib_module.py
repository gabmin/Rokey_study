import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]

# plt.plot(x, y)
# plt.title("Line plot")
# plt.xlabel("time")
# plt.ylabel("value")
# plt.show()

# categories = ["A", "B", "C", "D"]
# values = [3, 7, 8, 5]
# plt.bar(categories, values)
# plt.show()

plt.rcParams["font.family"] = "Malgun Gothic"

categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]

plt.bar(categories, values, color="red")
plt.title("막대 그래프")
plt.show()
