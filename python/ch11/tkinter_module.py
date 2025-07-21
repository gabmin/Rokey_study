import tkinter


def hello():
    print("Hello world!")


otk = tkinter.Tk()

ostring = tkinter.StringVar()
oent = tkinter.Entry(otk, textvariable=ostring)

olabel = tkinter.Entry(otk, textvariable=ostring)

oent.pack()
olabel.pack()
otk.mainloop()
