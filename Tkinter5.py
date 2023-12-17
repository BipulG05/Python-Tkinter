from tkinter import *

root = Tk()

root.geometry("444x444")
f1 = Frame(root,bg="grey",borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root,borderwidth=8,bg="red",relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l = Label(f1, text="Project Tkinter - notebook ")
l.pack(pady=142)

l = Label(f2, text="Project Tkinter - pycharm ", font="Helvetica 16 bold",fg="blue" )
l.pack()



root.mainloop()

