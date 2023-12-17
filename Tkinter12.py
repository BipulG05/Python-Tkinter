from tkinter import *
import tkinter.messagebox as tmsg

def myfunc():
    print("It is an Exmaple")

def help():
    #print("I will help you ")
    a = tmsg.showinfo("Help","bipul will help you")

def rate():
    print("our rate")
    value=tmsg.askquestion("was your experience good ?","your experience this gui ..was yourexperience Good?")
    if value=="yes":
        msg = "Great.Rate us on appstore please ..."
        
    else:
        msg = "Tell us what wrong.We will call you soon .."
    tmsg.showinfo("Experience: ",msg)

def Amit():
    ans = tmsg.askretrycancel("amit is your brother ","sorry you ask wrong question")
    if ans:
        print("Retry karne pa vi kuch nhi hoga ")
    else:
        print("bohot barya vii ")



root = Tk()
root.geometry("444x444")
root.title("Menu or Sub-Menu")

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

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="help",command=help)
m3.add_command(label="rate us",command=rate)
m3.add_command(label="Amit",command=Amit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="help",menu=m3)

root.mainloop()