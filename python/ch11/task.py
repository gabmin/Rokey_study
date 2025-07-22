import tkinter

otk = tkinter.Tk()

otk.title("조각 피자 주문 프로그램")

otk.geometry("400x300")

tkinter.Label(otk, text="피자").pack()

pizza_name = {
    0: "치즈 피자",
    1: "콤비네이션 피자",
    2: "불고기 피자",
}

pizza_price = {0: 3200, 1: 3500, 2: 3600}

check_value = {}

for i in range(len(pizza_name)):
    check_value[i] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        otk, text=f"{pizza_name[i]} ({pizza_price[i]}원)", variable=check_value[i]
    ).pack(anchor="w")


label_value = tkinter.StringVar()


def order():
    order_list = "주문내역:"
    total_price = 0

    for j in check_value:
        if check_value[j].get():
            order_list += f"\n - {pizza_name[j]}({pizza_price[j]}원)"
            total_price += pizza_price[j]

    order_list += f"\n \n 총 가격 : {total_price}원"
    label_value.set(order_list)


tkinter.Button(otk, text="주문", command=order).pack()

tkinter.Label(otk, textvariable=label_value).pack()

otk.mainloop()
