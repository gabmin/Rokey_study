my_gen = (i * i for i in range(20))

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

my_list = [i * 2 for i in range(20) if i % 2 == 0]
print(my_list)

my_dict = {x: x * 2 for x in range(20) if x % 2 == 0}

print(my_dict)

a = [[] for i in range(5)]

b = [[]] * 5

print(a)
print(b)
