# def sum_function(a, b):
#     return a + b
#
#
# print(10, 20)
#
#
# def total_number(number):
#     total = 0
#
#     for i in range(1, number + 1):
#         total += i
#
#     return total
#
#
# print(total_number(5))

#
#
# x = 5
#
#
# def example1():
#     global x
#     x = 15
#     print(x)
#
#
# example1()
# print(x)
#
#
#
# list_a = [12, 4, 25, 8, 14]
#
#
# def get_min_number(list):
#     min = list[0]
#
#     for i in range(1, len(list)):
#         if list[i] < min:
#             min = list[i]
#
#     return min
#
#
# print(get_min_number(list_a))


# import math
#
# print(math.factorial(5))


# class Animal:
#     def speak(self):
#         return "Animal speaks"
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
#
# dog = Dog()
# print(dog.speak())


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


kim = Student("Hendrix", "5273891")
print(kim.introduce())
print(kim.name)
print(kim.student_id)
