def add(num1, num2):
    return num1 + num2


print(add(2, 3))


def funca(pa, pb):
    nc = pa + pb

    return nc


na = 10
nb = 11

nd = funca(na, nb)
print(nd)


def myabs(arg):
    if arg < 0:
        result = arg * -1
    else:
        result = arg
    return result


print(myabs(-2))


def fun_ca():
    print("fun_ca 함수 호출")


def fun_cb():
    fun_ca()
    print("fun_cb 함수 호출")


def fun_cc():
    fun_cb()
    print("fun_cc 함수 호출")


fun_cc()


def fadd(a, b):
    return a + b


def fsub(a, b):
    return a + b


def fmul(a, b):
    return a * b


def fdiv(a, b):
    return a / b


print(fadd(100, 3))
print(fsub(100, 3))
print(fmul(100, 3))
print(fdiv(100, 3))
