from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("order Recived",f"We have Recivead your order for {var.get()} . thanks for ordering")


root = Tk()
root.geometry("444x444")
root.title("Radio button :-")

#var = IntVar()
# var.set(1)
var = StringVar()
var.set("Radio")
Label(root, text="whait would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio = Radiobutton(root, text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idly",padx=14,variable=var,value="Idly").pack(anchor="w")
radio = Radiobutton(root, text="Paratha",padx=14,variable=var,value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Samosa",padx=14,variable=var,value="Samosa").pack(anchor="w")

Button(text="order Now",command=order).pack()


root.mainloop()