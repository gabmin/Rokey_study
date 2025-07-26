# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
#
# gen = countdown(3)
# for x in gen:
#     print(x, end=" ")


# numbers = [1, 2, 3, 4, 5]
#
# num_iter = iter(numbers)
#
# for i in num_iter:
#     print(i)


# fruits = ["apple", "banana", "cherry"]
#
# fruits_iter = iter(fruits)
#
# try:
#     while True:
#         print(next(fruits_iter))
# except StopIteration:
#     pass


# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#
#         result = self.data[self.index] ** 2
#         self.index += 1
#         return result
#
#
# list_a = list(range(0, 10))
# my_iterator = MyIterator(list_a)
# for _ in range(len(list_a)):
#     print(next(my_iterator))


# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while True:
#             if self.index >= len(self.data):
#                 raise StopIteration
#
#             if self.data[self.index] % 2 == 0:
#                 result = self.data[self.index]
#                 self.index += 1
#                 return result
#
#             self.index += 1
#
#
# list_a = list(range(0, 10))
# my_iterator = MyIterator(list_a)
# for i in my_iterator:
#     print(i)


class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (
            self.step < 0 and self.current <= self.stop
        ):
            raise StopIteration

        result = self.current
        self.current += self.step
        return result


for i in MyRange(5, 10, 2):
    print(i)
