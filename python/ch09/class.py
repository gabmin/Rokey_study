class Singer:
    def __init__(self):
        self.name = "아이유"

    def sing(self):
        print("이 밤 그날에")


iu = Singer()

print(iu.name)
iu.sing()


class Bag:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def remove(self, item):
        self.data.remove(item)


hand_bag = Bag()
hand_bag.add("손")

cross_bag = Bag()
cross_bag.add("크로스")

print(hand_bag.data)
print(cross_bag.data)


class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name


kim = Human(12, "갑민")


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("야옹")


cats = Animal("고양이")
print(cats.name)
cats.sound()
