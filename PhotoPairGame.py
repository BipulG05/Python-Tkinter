
#  *** NO FINISHED CODING ****
from tkinter import *
from tkinter import ttk
import random
from  PIL import  (Image,ImageTk)

count =0
btn=[]

def distribute():
    l=[]
    for i in range(12):
        l.append(i)
    print(i)

    i=1
    for i1 in range(1,5):
        for i2 in range(0,3):
            photo=ImageTk.PhotoImage(Image.open(f"D:\\python programs\\memorygame\\{i}.png"))
            b.grid(column=f"{i2}",row=f"{i1}",padx=2,pady=2)
            b.bind("<Button-1>",click)
            i+=1
            

def click(event):
    global count
    count = count + 1
    text = event.widget.cget("image")
    gallery1['1.jpg']=ImageTk.PhotoImage(Image.open('D:\\python programs\\memorygame\\1.jpg'). resize(( 90,110)))
    btn[0].configure(image=gallery1['1.jpg'],text=text)
    btn[0].update()


root = Tk()
root.geometry("340x520")
root.resizable(False,False)
root.title("codbyBipul- Photo Pair Game ")
root.wm_iconbitmap("D:\python programs\PYTHON_GUI_TKINTER\calculator.ico")
root.configure(background="azure")

shadschosen =ttk.Combobox(root, width = 13)
shadschosen ['values'] =(4,6,8,10,12,15)
shadschosen.grid(column = 0, row=0,padx=2,pady=2)
shadschosen.current()
gallery= {}
gallery1={}
gallery1['base.jpg']=ImageTk.PhotoImage(Image.open('D:\\python programs\\memorygame\\base.jpg'). resize(( 90,110)))
gallery['bg.jpg']=ImageTk.PhotoImage(Image.open('D:\\python programs\\memorygame\\bg.jpg'). resize(( 90,110)))
def start():
    global btn
    for i in range(1,13):
        btn.append(Button(root,text=f'{i-1}',image=gallery1['base.jpg']))
        btn[i-1].bind("<Button-1>",click)

    i=0
    for i1 in range(1,5):
        for i2 in range(0,3):
            btn[i].grid(column=f"{i2}",row=f"{i1}",padx=2,pady=2)
            i+=1
    #distribute()

    #Handling the event when the user want to close window 
def close_window():
    feedback=askyesno("Memory Booster","If you close this window, \ngame will be automatically stopped ")
    if feedback:
        root.destroy()


start()
root.mainloop()