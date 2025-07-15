def persona(width, height):
    print("함수 디폴트값 없음", "width=", width, "height=", height)


def personb(width, height=3):
    print("함수 디폴트값 설정", "width=", width, "height=", height)


persona(10, 20)
personb(3)
personb(3, 5)


def typed_function(a: int, b: int) -> int:
    return a + b


print(typed_function(10, 20))
