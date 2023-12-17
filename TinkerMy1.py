from tkinter import *
from PIL import ImageTk, Image

def photo():
        image = Image.open("school1.gif")
        photo = ImageTk.PhotoImage(image)

        amit_label = Label(image=photo)
        amit_label.pack()
        root.mainloop()
        print("bipul")



root = Tk()
root.geometry("444x444")

frame = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame,fg="red", text="show photo",command=photo) # command take function name not function as photo()
b1.pack(side=LEFT,padx=20)

root.mainloop()