class c_value:
    def __init__(self):
        self.lista = []

    def add(self, num):
        self.lista.append(num)

    def f_print(self):
        print(self.lista)


p1 = c_value()
p1.add(1)
p1.add(2)
p1.add(3)


def plus(a, b):
    c = a + b
    return c
