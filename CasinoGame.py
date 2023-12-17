from tkinter import *
import random
from tkinter.messagebox import *
import time



def cheek(text):
    r1=random.randint(0,9)
    r2=random.randint(0,9)
    r3=random.randint(0,9)
    f=str(r1)+str(r2)+str(r3)
    scvalue.set(f)
    # for i in range(0,10):
    #     r1=random.randint(0,9)
    #     r2=random.randint(0,9)
    #     r3=random.randint(0,9)
    #     f=str(r1)+str(r2)+str(r3)
    #     time.sleep(1)
    #     scvalue.set(f)
    if r1==r2==r3:
        scvalue1.set(f"Hurrryyy!!!!! \n You win jackpot \n Your lucky number is \n {f}")
    else:
        scvalue1.set(f"sorry.. \n  better luck next time ")
    


root = Tk()
root.geometry("250x400")
#root.resizable(False,False)
root.title("codbyBipul- Welcome Your game ")
root.wm_iconbitmap("calculator.ico")
root.configure(background="tomato")

scvalue = StringVar()
scvalue.set("???")
screen =Label(root,textvar=scvalue,width=32,height=5)
screen.grid(row=0,column=1,padx=10,pady=10,ipady=5)

scvalue1 = StringVar()
scvalue1.set("If 3 digit are same you can win Jackpot")
screen1 =Label(root,textvar=scvalue1,width=32,height=5)
screen1.grid(row=1,column=1,padx=10,pady=10,ipady=5)

b = Button(root,text='OK')
b.grid(column=1,row=2,padx=5,pady=5,ipadx=20,ipady=20)
b.bind("<Button-1>",cheek)


root.mainloop()