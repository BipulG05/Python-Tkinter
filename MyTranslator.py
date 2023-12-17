from tkinter import *
from tkinter.ttk import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    Value = scvalue.get()
    if text == "AC":
        scvalue.set("")
        screen.update()
    elif text == "TO":
        from googletrans import Translator
        text = scvalue.get()
        translator = Translator()
        dt = translator.detect(text)
        print(dt)
        translated = translator.translate(text,src='fi',dest='bn')
        text3 = translated.text
        scvalue.set(text3)
    elif text == "speak":
        from gtts import gTTS
        import os
        mytext = scvalue.get()
        myobj = gTTS(text=mytext, lang='bn',slow=False)
        myobj.save("tran.mp3")
        import pygame
        from pygame import mixer
        mixer.init()
        # Loading Selected Song
        pygame.mixer.music.load("tran.mp3")
        # Playing Selected Song
        pygame.mixer.music.play()

    elif text == "<=":
        st = scvalue.get()
        n=len(st)
        if n>1:
            str1=""
            for i in range(0,len(st)-1):
                str1 = str1+ st[i]
            scvalue.set(str1)
        else:
    	    scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)


root = Tk()
root.geometry("800x350")
root.title("codbyBipul- Calculator ")
#root.wm_iconbitmap("calculator.ico")
root.configure(background="azure")


scvalue = StringVar()
scvalue.set("")
screen = Label(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=BOTH,ipadx=8,padx=10,pady=10)

f = Frame(root)

a1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','(',')','"','.',',',' ','AC','<=','TO','@','#','$','!','*','|',':','~','speak']
a=0
for i1 in range(0,6):
    for i2 in range(0,9):
        b = Button(f,text=f"{a1[a]}")
        b.grid(column=f"{i2}",row=f"{i1}",padx=6,pady=6)
        b.bind("<Button-1>",click)
        a+=1

f.pack()
root.mainloop()