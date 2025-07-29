# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, value):
#         self.stack.append(value)
#
#     def pop(self):
#         if not self.is_empty:
#             return self.stack.pop()
#         else:
#             return -1
#
#     def top(self):
#         if not self.is_empty:
#             return self.stack[-1]
#         else:
#             return -1
#
#     def is_empty(self):
#         if len(self.stack) == 0:
#             return True
#         else:
#             return False
#
#
# s1 = Stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
# s1.pop()
# print(s1.top())
# print(s1.is_empty())

#
# import re
#
#
# def get_postfix_notation(pattern):
#     stack = []
#
#     for item in pattern:
#         if re.match(r"\d", item):  # 숫자 여부
#             stack.append(item)
#         else:
#             item1 = int(stack.pop())
#             item2 = int(stack.pop())
#
#             if item == "+":
#                 stack.append(item2 + item1)
#             elif item == "-":
#                 stack.append(item2 - item1)
#             elif item == "*":
#                 stack.append(item2 * item1)
#             elif item == "/":
#                 stack.append(item2 / item1)
#
#     return stack[0]
#
#
# print("결과:", get_postfix_notation("3546-*2/+"))
# print("결과:", get_postfix_notation("34+"))


# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     def dequeue(self):
#         return self.queue.pop(0)
#
#     def front(self):
#         if not self.is_empty():
#             return self.queue[0]
#         else:
#             return -1
#
#     def is_empty(self):
#         if len(self.queue) == 0:
#             return True
#         else:
#             return False
#
#
# q1 = Queue()
# q1.enqueue(1)
# q1.enqueue(2)
# q1.enqueue(3)
# q1.dequeue()
# print(q1.front())
# print(q1.is_empty())

#
# class RotateQueue:
#     def __init__(self, size):
#         self.queue = []
#         self.size = size
#
#     def enqueue(self, data):
#         if self.is_full():
#             return
#
#         self.queue.append(data)
#
#     def dequeue(self):
#         if self.is_empty():
#             return -1
#         else:
#             return self.queue.pop(0)
#
#     def front(self):
#         if self.is_empty():
#             return -1
#         else:
#             return self.queue[0]
#
#     def is_empty(self):
#         if len(self.queue) == 0:
#             return True
#         else:
#             return False
#
#     def is_full(self):
#         if len(self.queue) >= self.size:
#             return True
#         else:
#             return False


class Deque:
    def __init__(self):
        self.queue = []

    def push_front(self, item):
        self.queue.insert(0, item)

    def push_back(self, item):
        self.queue.append(item)

    def pop_front(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return -1

    def pop_back(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            return -1

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
