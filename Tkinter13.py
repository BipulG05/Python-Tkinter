from tkinter import *
import tkinter.messagebox as tmsg


def rupees():
    print(f"We have credited {myslider1.get()} rupees to ypur bank account")
    tmsg.showinfo("Amount Credited: ",f"We have credited {myslider1.get()} rupees to ypur bank account")

root = Tk()
root.geometry("444x444")
root.title("Slide in Tkinter")

#myslider = Scale(root, from_ =0, to=455)
#myslider.pack()
Label(root, text="how meny rupees do you want?").pack()

myslider1 = Scale(root, from_ =0, to=200,orient=HORIZONTAL,tickinterval=70)
myslider1.set(34)
myslider1.pack()
Button(root,text="Get rupees",pady=10,command=rupees).pack()

root.mainloop()