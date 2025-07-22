with open("./계좌1.txt", "r", encoding="utf-8") as account:
    data = account.readlines()
    account_data = {}

    for item in data:
        name, number = item.split(" ")
        account_data[name] = number.strip()

    print(account_data)
