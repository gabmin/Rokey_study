class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def status_stack(self):
        return self.stack


s1 = Stack()
print(s1.peak())
s1.pop()
s1.push(1)
s1.push(2)
s1.pop()
s1.push(3)
s1.push(4)
print(s1.peak())
print(s1.status_stack())
