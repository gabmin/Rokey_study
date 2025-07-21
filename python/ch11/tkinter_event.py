import tkinter


def msg():
    print("start tkinter")


root = tkinter.Tk()
mlabel = tkinter.Label(root, text="시작 레이블")
mlabel.pack()

mbutton = tkinter.Button(root, text="시작버튼", command=msg)
mbutton.pack()
root.mainloop()
