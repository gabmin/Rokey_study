path = "./계좌1.txt"
mode = "w"

with open(path, mode, encoding="utf-8") as account:
    account.write("김삿갓 597-89-000089\n")
    account.write("이수근 343-64-000064\n")
    account.write("박혁거세 136-97-000097\n")
