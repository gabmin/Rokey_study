import tkinter

oroot = tkinter.Tk()

radio_var = tkinter.IntVar()
radio_var.set(1)
lunch = {0: "A런치", 1: "B런치", 2: "C런치"}

orb1 = tkinter.Radiobutton(oroot, text=lunch[0], variable=radio_var, value=0)
orb2 = tkinter.Radiobutton(oroot, text=lunch[1], variable=radio_var, value=1)
orb3 = tkinter.Radiobutton(oroot, text=lunch[2], variable=radio_var, value=2)

orb1.pack()
orb2.pack()
orb3.pack()


def buy():
    value = radio_var.get()
    print(lunch[value])


obutton = tkinter.Button(oroot, text="주문", command=buy)
obutton.pack()
oroot.mainloop()
