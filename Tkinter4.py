from tkinter import *
"""

root = Tk()
root.geometry("666x444")
root.title(" My GUI with Harry ")

# importent Label option
# text - adds the text
# bg - background
# fg - foreground
# padx - X padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

# font=("comicsansms",19,"bold") or font=("comicsansms 19 bold")
title_label = Label(text='''I am bipul guchhait \n I am bikram guchhait \n I am akash guchhait  \n I am Amit guchhait
I am rounak guchhait ''',bg="red",fg="white",padx=13,pady=94,font="comicsansms 9 bold", borderwidth=3,relief=GROOVE)

# importent pack option :-
# anchor = nw, ne, se, sw,
# side = to, bottom, left, right
#  title_label.pack(side=BOTTOM,anchor ="sw")
# fill 
# padx
# pady
#title_label.pack(side=BOTTOM,anchor ="sw",fill=X)
title_label.pack(side=LEFT, fill=Y,padx=43,pady=34)

root.mainloop()
"""

# Question :- make a newspaper :- it have name , date , photos ans text
from PIL import Image,ImageTk 

def every_100(text):
    final_text=""
    for i in range(0,len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text +="\n"

    return final_text


root = Tk()
root.title("BipulFasterNews - Apka Apna Akhabaar")
root.geometry("1000x1000")

texts=[]
photos=[]
for i in range(0,3):
    with open (f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
    image = Image.open(f"{i+1}.png")
    #TODO : Resize these images
    image = image.resize((225,225),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))
f0 = Frame(root,width=800,height=70)
Label(f0,text="Bullat news",font="lucida 33 bold").pack()
Label(f0,text=" Septembar 11 , 2020",font="lucida 13 bold",bg="blue").pack()
f0.pack()
for i in range(0,3):
    f1 = Frame(root,width=900,height=500,padx=22,pady=14)
    if i%2!=0:
        Label(f1,text=texts[i],padx=22,pady=22).pack(side=RIGHT)
    else:
        Label(f1,text=texts[i],padx=22,pady=22).pack(side=LEFT)
    
    Label(f1,image=photos[i],anchor="e").pack()
    f1.pack(anchor="w")

root.mainloop()