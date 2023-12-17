from tkinter import *

def myfunc():
    print("It is an Exmaple")

root = Tk()
root.geometry("444x444")
root.title("Menu or Sub-Menu")

# Use this to create a non dropdown menu
"""
mymenu = Menu(root)
mymenu.add_command(label="File",command=myfunc)
mymenu.add_command(label="Exit",command=quit)
root.config(menu=mymenu)
"""
mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="new file",command=myfunc)
m1.add_separator()
m1.add_command(label="save as",command=myfunc)
m1.add_command(label="save",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="copy",command=myfunc)
m2.add_separator()
m2.add_command(label="paste",command=myfunc)
m2.add_command(label="Find",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)



root.mainloop()