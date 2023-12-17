from tkinter import *
from tkinter.ttk import *
#from tkinter.messagebox import *

def clean(event):
    scvalue.set("")
    screen.update()
def back(event):
    #print("it's now working now :-")
    global scvalue
    st = scvalue.get()
    #clean(event)
    n=len(st)
    if n>1:
        str1=""
        for i in range(0,len(st)-1):
            str1 = str1+ st[i]
        scvalue.set(str1)
        #screen.update()
    else:
        scvalue.set("")
        #screen.update()
        
def click(event):
    global scvalue
    text = event.widget.cget("text")
    Value = scvalue.get()
    #showinfo("title", Value)
    #print(Value)
    #print(text)
    if text == "=":
        if scvalue.get().isdigit():
            pass
        elif '^' in Value and text =="=":
            n = Value.strip().split("^")
            #showinfo("title",f"{n[0]} ,{n[1]}")
            #print(n[0],n[1])
            n[0]=int(n[0])
            n[1]=int(n[1])
            #showinfo("title",f"{n[0]} ,{n[1]}")
            Value = pow(n[0],n[1])
            Value=str(Value)

            scvalue.set(Value)
            #screen.update()
        else:
            try:
                Value = eval(scvalue.get())
            except:
                Value = " Cannot be divided "

        scvalue.set(Value)
        ##screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        ##screen.update()
root = Tk()
root.geometry("350x520")
root.title("codbyBipul- Calculator ")
#root.wm_iconbitmap("calculator.ico")
root.configure()


scvalue = StringVar()
scvalue.set("")
screen = Label(root,textvar=scvalue)
screen.pack()

f = Frame(root)
b = Button(f,text="C")
b.pack(side=LEFT)
b.bind("<Button-1>",clean)
b = Button(f,text="%")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="^")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="/")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root)
b = Button(f,text="7")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="8")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="9")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="*")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root)
b = Button(f,text="4")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="5")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="6")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="-")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root)
b = Button(f,text="1")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="2")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="3")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="+")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root)
b = Button(f,text="back")
b.pack(side=LEFT)
b.bind("<Button-1>",back)
b = Button(f,text="0")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text=".")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b = Button(f,text="=")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()