path = "C:/Users/rlark/Desktop/Rokey/python/ch12/pizza_file1.txt"
mode = "r"

file = open(path, mode, encoding="utf-8")

pizza_list = file.readlines()
pizza_name_list = []

for pizza in pizza_list:
    pizza_name_list.append(pizza.split(" ")[0])

print(pizza_name_list)

file.close()
