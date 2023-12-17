from tkinter import *
"""

def getvals():
    print(f"The user name is :- {uservalue.get()}")
    print(f"The user password is is :- {passvalue.get()} ")

root = Tk()
root.geometry("444x444")

user = Label(root,text="Username")
password = Label(root,text="password")

user.grid()
password.grid(row=1)

# variable classes in tkinter
# BooleanVar , DoubleVar , IntVar , stringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue )
passentry = Entry(root, textvariable = passvalue )

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()
"""

# Question :- Make a entry and exit Details with time and it save in file

