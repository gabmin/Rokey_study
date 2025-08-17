fruit = ["apple", "banana", "orange"]

fruit.append("tomatoe")

print(fruit)


weights = {"layer 1": 0.1, "layer 2": 0.3}

keys = weights.keys()

print(keys)

a = [1, 2, 3, 4, 5, 6]

print(a[2:5])


flower_price = {
    "rose": 10000,
    "iris": 3000,
    "stargauge": 12000,
    "lily": 9000,
    "daffodil": 3000,
}

for value in flower_price.values():
    print(value)


def mysum(n):
    a = 0
    i = 0
    while i < n + 1:
        a = a + i
        i += 1

    return a


print(mysum(5))


class Coffee:
    def __init__(self, name, price, temperature):
        self.name = name
        self.price = price
        self.temperature = temperature
        print(f"{self.name}, {self.temperature} 커피를 준비합니다.")
        print(f"가격은 {self.price} 입니다.")


americano1 = Coffee("아메리카노", 25000, "cold")
americano2 = Coffee("아메리카노", 25000, "hot")


class Cappuccino(Coffee):
    def __init__(self, name, price, temperature, milk):
        super().__init__(name, price, temperature)
        self.milk = milk

    def milking(self):
        print(f"{self.milk}를 첨가합니다.")


cappuccino = Cappuccino("카프치노", 4000, "hot", "milk")
cappuccino.milking()
