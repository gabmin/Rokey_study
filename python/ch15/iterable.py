a = [1, 2, 3]

iter_a = iter(a)
print(type(iter_a))
print(iter_a)
print(iter(iter_a))


for i in iter_a:
    print(i)

print("---------")

for i in iter_a:  # 실행되지 않음
    print(i)

print(next(iter_a))  # for문 실행 후 사용시 에러 발생
