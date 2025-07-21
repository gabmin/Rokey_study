import tkinter

otk = tkinter.Tk()
otk.geometry("200x100")
obutton1 = tkinter.Button(otk, text="push1")
obutton2 = tkinter.Button(otk, text="push2")
obutton3 = tkinter.Button(otk, text="push3")

obutton1.grid(row=2, column=0)
obutton2.grid(row=2, column=1)
obutton3.grid(row=0, column=4)

otk.mainloop()
