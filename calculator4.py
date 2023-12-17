from tkinter import *
from tkinter.ttk import *

def clean(event):
    scvalue.set("")
    screen.update()
    
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
        
def click(event):
    global scvalue
    text = event.widget.cget("text")
    Value = scvalue.get()
    if text == "=":
        if scvalue.get().isdigit():
            pass
        elif '^' in Value and text =="=":
            n = Value.strip().split("^")
            n[0]=int(n[0])
            n[1]=int(n[1])
            Value = pow(n[0],n[1])
            Value=str(Value)
            scvalue.set(Value)
        else:
            Value = eval(scvalue.get())

        scvalue.set(Value)
    else:
        scvalue.set(scvalue.get() + text)
root = Tk()
#root.geometry("350x520")
root.title("Mini Calculator ")
#root.wm_iconbitmap("calculator.ico")
root.configure(background="azure")


scvalue = StringVar()
scvalue.set("")
screen =Label(root,textvar=scvalue,font="lucida 10 bold",wraplength=600)
screen.pack(fill=BOTH,expand=1,ipadx=8,padx=10,pady=10)

mainFrame=Frame(root)
mainFrame.pack(side=BOTTOM)
f = Frame(mainFrame)
b = Button(f,text="C")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",clean)
b = Button(f,text="%")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="^")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="/")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
f.pack()

f = Frame(mainFrame)
b = Button(f,text="7")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="8")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="9")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="*")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
f.pack()

f = Frame(mainFrame)
b = Button(f,text="4")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="5")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="6")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="-")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
f.pack()

f = Frame(mainFrame)
b = Button(f,text="1")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="2")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="3")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="+")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
f.pack()

f = Frame(mainFrame)
b = Button(f,text="back")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",back)
b = Button(f,text="0")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text=".")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
b = Button(f,text="=")
b.pack(side=LEFT,padx=10,pady=20)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()