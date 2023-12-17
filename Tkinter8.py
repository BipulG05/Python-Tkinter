from tkinter import *
from PIL import ImageTk, Image

def getvals():
    print("Submatting form ")
    print(f"  {namevalue.get()} ,{phonevalue.get()} ,{gendervalue.get()} ,{numbervalue.get()} ,{paymentvalue.get()} ,{foodservicevalue.get()} ")
    with open("Food.txt","a") as f:
        f.write(f" ( {namevalue.get()} ,{phonevalue.get()} ,{gendervalue.get()} ,{numbervalue.get()} ,{paymentvalue.get()} ,{foodservicevalue.get()} )\n")
root = Tk()
root.geometry("444x444")
# Heading
Label(root,text="Welcome to my Tkinter",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)
# Text for our form
name = Label(root, text="name: ")
phone = Label(root, text="phone: ")
gender = Label(root, text="gender: ")
number = Label(root, text="emergency no: ")
payment = Label(root, text="payment mode: ")

# Pack text for our from
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
number.grid(row=4,column=2)
payment.grid(row=5,column=2)

# Tkinter variable for entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
numbervalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

# Entry for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
numberentry = Entry(root, textvariable=numbervalue)
paymententry = Entry(root, textvariable=paymentvalue)

# Packing the entry
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
numberentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

# checkbox and packing it
foodservice = Checkbutton(text="Want to pre book your meals?",variable = foodservicevalue)
foodservice.grid(row=6,column=3)

# Button and packing it
Button(text="Submit Here",bg="blue",command=getvals).grid(row=7,column=2)


root.mainloop()


