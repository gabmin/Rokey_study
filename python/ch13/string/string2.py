name = "홍길동"
age = 200
height = 191.3

# 1. 기본
print("이름:", name, "나이:", age, "키:", height)

# 2. % 연산자
print("이름: %s, 나이: %d, 키: %d"%(name, age, height))

# 3. format 메서드
print("이름: {}, 나이: {}, 키: {}".format(name, age, height))

# 4. f string
print(f"이름: {name}, 나이: {age}, 키: {height}")