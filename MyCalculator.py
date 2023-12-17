from tkinter import *
#from tkinter.messagebox import *

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
            try:
                Value = eval(scvalue.get())
            except:
                Value = " Cannot dividied "

        scvalue.set(Value)
    else:
        scvalue.set(scvalue.get() + text)
root = Tk()
root.geometry("350x520")
root.title("codbyBipul- Calculator ")
#root.wm_iconbitmap("calculator.ico")
root.configure(background="azure")


scvalue = StringVar()
scvalue.set("")
screen = Label(root,textvar=scvalue,font="lucida 20 bold",bg="light grey")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f = Frame(root,bg="azure")
b = Button(f,text="C",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",clean)
b = Button(f,text="%",bg="white",padx=11,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="^",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="/",bg="white",fg="green",padx=16,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="azure")
b = Button(f,text="7",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="8",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="9",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="*",fg="green",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="azure")
b = Button(f,text="4",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="5",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="6",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="-",fg="green",bg="white",padx=15,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="azure")
b = Button(f,text="1",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="2",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="3",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="+",fg="green",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="azure")
b = Button(f,text="<=",bg="white",padx=9,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",back)
b = Button(f,text="0",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text=".",bg="white",padx=17,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="=",fg="green",bg="white",padx=14,pady=14,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()