from tkinter import *
import random
from tkinter.messagebox import *

count=1

def back(event):
    global scvalue
    st = scvalue.get()
    n=len(st)
    if n>1:
        str1=""
        for i in range(0,len(st)-1):
            str1 = str1+ st[i]
        scvalue.set(str1)
    else:
        scvalue.set("")

def cheek(text):
    r1=random.randint(0,9)
    r2=random.randint(0,9)
    r3=random.randint(0,9)
    f=str(r1)+str(r2)+str(r3)
    ystr=scvalue.get()
    if len(ystr)==3:
        if f==ystr:
            showinfo(" *** HURRYA *** ",' < YOU WIN THE PRICES > ')
        else:
            showinfo("!!! OPPS !!! ",f"opps ,bad luck try again \n number is {f} ")
    else:
        showinfo("PLESE"," ENTER MINIMUM 3 NUMBER  ")
    
    

def click(event):
    global scvalue
    text = event.widget.cget("text")
    text1=scvalue.get()
    strlen=len(text1)
    if strlen>=3:
        showinfo('ohh','You can type only 3 number !!! \n if you can change number click => button')
    else:
        scvalue.set(scvalue.get() + text)


root = Tk()
root.geometry("250x400")
#root.resizable(False,False)
root.title("codbyBipul- Welcome Your xoxo game ")
root.wm_iconbitmap("calculator.ico")
root.configure(background="tomato")

scvalue = StringVar()
scvalue.set("")
screen =Label(root,textvar=scvalue,width=32,height=2)
screen.grid(row=0,column=3,padx=10,pady=10,ipady=5)


mainFrame=Frame(root,bg='blue')

i=0
for i1 in range(1,4):
    for i2 in range(0,3):
        b = Button(mainFrame,text=f"{i}")
        b.grid(column=f"{i2}",row=f"{i1}",padx=5,pady=5,ipadx=20,ipady=20)
        b.bind("<Button-1>",click)
        i+=1

mainFrame.grid(row=3,column=3,padx=10,pady=10)


b = Button(mainFrame,text='OK')
b.grid(column=0,row=4,padx=5,pady=5,ipadx=20,ipady=20)
b.bind("<Button-1>",cheek)

b = Button(mainFrame,text="=>")
b.grid(column=2,row=4,padx=5,pady=5,ipadx=20,ipady=20)
b.bind("<Button-1>",back)

showinfo('Hurra','if you write right number you can win One cror')

root.mainloop()