import max2


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


print(__name__)
print(max2.__name__)

if __name__ == "__main__":
    p1 = c_value()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.f_print()
