class c_value:
    def __init__(self):
        self.lista = []

    def add(self, num):
        self.lista.append(num)

    def f_print(self):
        print(self.lista)


def plus(a, b):
    c = a + b
    return c
