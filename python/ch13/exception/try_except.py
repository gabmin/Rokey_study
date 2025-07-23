print("start")

while True:
    try:
        x = int(input("Please enter a number: "))
        result = 4 + x * 3
        print(result)
        result2 = 10 * (1 / x)
        print(result2)
        break
    except ValueError as e:
        print(e)
    except NameError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

print("exit")
