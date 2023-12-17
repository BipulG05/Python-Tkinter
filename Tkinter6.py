from tkinter import *

root = Tk()
root.geometry("444x444")
def hello():
    print("Hello tkinter button 1 ")

def name():
    print("name is bipul")

frame = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame,fg="red", text="print now 1",command=hello) # command take function name not function as hello()
b1.pack(side=LEFT,padx=20)


b2 = Button(frame,fg="red", text="print now 2",command=name)
b2.pack(side=LEFT,padx=20)

b3 = Button(frame,fg="red", text="print now 3")
b3.pack(side=LEFT,padx=20)


b3 = Button(frame,fg="red", text="print now 4")
b3.pack(side=LEFT,padx=20)




root.mainloop()

