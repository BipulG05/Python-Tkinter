# create a gui window which takes as input width and heighi
# and upon clicking apply , it should be to change its size accordingly
'''
# Harry code:-
from tkinter import *

def update():
    print("Updating the Gui")
    root.geometry(f"{width.get()}x{height.get()}")

root = Tk()
root.geometry("444x444")
root.title("My task 1")
Label(root, text="windows resizer",font="lucida 19 bold",pady=14).grid(column=2)
width = StringVar()
height = StringVar()
Width=Entry(root, textvariable=width).grid(row=1,column=2)
Height=Entry(root, textvariable=height).grid(row=2,column=2)
Button(root, text="Apply",command=update,pady=20,font="comicsansms").grid(column=2)


root.mainloop()
'''
from tkinter import *
def update():
    print("Updating the Gui")
    root.geometry(f"{width.get()}x{height.get()}")

root = Tk()
root.geometry("444x444")
root.title("Window Resized")

Label(root, text="windows resizer",font="lucida 19 bold",pady=14).grid(column=2)
Label(text="width",font='lucida 19 bold').grid(row=1,column=1)
Label(text="height",font='lucida 19 bold').grid(row=2,column=1)

width = StringVar()
height = StringVar()
Width=Entry(root, textvariable=width).grid(row=1,column=2)
Height=Entry(root, textvariable=height).grid(row=2,column=2)
Button(root, text="Apply",command=update,pady=20,font="comicsansms").grid(column=2)


root.mainloop()