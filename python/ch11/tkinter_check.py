import tkinter

oroot = tkinter.Tk()

coffee = {0: "아메리카노", 1: "라떼", 2: "카프치노", 3: "에스프레소"}

check_value = {}

for i in range(len(coffee)):
    check_value[i] = tkinter.BooleanVar()
    ocheckbutton = tkinter.Checkbutton(oroot, text=coffee[i], variable=check_value[i])
    ocheckbutton.pack(anchor="w")


def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(coffee[i])


tkinter.Button(oroot, text="주문", command=buy).pack()
oroot.mainloop()
