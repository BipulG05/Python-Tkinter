from tkinter import *

def add():
    global i
    #i = input("What you want add write here: ")
    i+=1
    lbx.insert(ACTIVE,f"{i}")
    
i=0

root = Tk()
root.geometry("444x444")
root.title("Listbox tutorial")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our list box")

Button(root,text="Add item",command=add).pack()

root.mainloop()