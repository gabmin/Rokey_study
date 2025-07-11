num = 0

while num < 5:
    print('안녕', num)
    num += 1

stra = "파이썬"
strb = "프로그래밍"
stra += strb

print(stra)


count = 0

while count < 3:
    count += 1
    if count == 2:
        continue
    print(count)

fruits = ['사과', '배', '포도', '파인애플', '바나나']

for fruit in enumerate(fruits):
    print(fruit)

print(list(range(3, 100, 3)))