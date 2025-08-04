import tkinter


def hello():
    print("Hello world!")


otk = tkinter.Tk()

otk.geometry("300x300+800+400")

ostring = tkinter.StringVar()
oent = tkinter.Entry(otk, textvariable=ostring)

olabel = tkinter.Entry(otk, textvariable=ostring)

obtn = tkinter.Button(otk, text="Click me", bg="red", command=hello)

oent.pack()
olabel.pack()
obtn.pack()
otk.mainloop()
