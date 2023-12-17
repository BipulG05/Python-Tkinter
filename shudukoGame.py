from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import random


root = Tk()
root.geometry("475x750")
#root.resizable(False,False)
root.title("codbyBipul- Welcome Your xoxo game ")
root.wm_iconbitmap("calculator.ico")
root.configure(background="tomato")


mainFrame=Frame(root,bg='blue')
scvalue = StringVar()
scvalue.set("")

d=[]

for i in range(10):
    rand=random.randint(1,9)
    d.append(rand)
print(d)

i=0
for i1 in range(0,10):
    for i2 in range(0,10):
        if (i2 in d):
            T=Text(mainFrame,width=5,height=4)
            T.grid(column=f"{i2}",row=f"{i1}",padx=1,pady=1)
        else:
            screen =Label(mainFrame,text=f'{i}',width=5,height=4)
            screen.grid(column=f"{i2}",row=f"{i1}",padx=1,pady=1)
        print(i2)
    i+=1

mainFrame.grid(row=3,column=3,padx=20,pady=20)


root.mainloop()
