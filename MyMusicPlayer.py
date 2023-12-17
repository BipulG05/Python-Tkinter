import os
from PIL import ImageTk,Image
from tkinter import *
import pygame
import mutagen
from tkinter.messagebox import *

def Selectsong(event):
    global scvalue
    name = str((Lb1.get(ACTIVE)))
    if name =="":
        scvalue.set("1(Wapvidz.net)Despacito-Hindi-Version--Lovely-Song--Whatsapp-Status-Video--Dideo-Ki-Video_high_quality.mp3")
        screen.update()
    else:
        scvalue.set(name)
        screen.update()
        playsong()

def playsong():
    name = str((Lb1.get(ACTIVE)))
    if name =="":
        showinfo("please select a song first")
        scvalue.set("1(Wapvidz.net)Despacito-Hindi-Version--Lovely-Song--Whatsapp-Status-Video--Dideo-Ki-Video_high_quality.mp3")
        screen.update()
    else:
        scvalue.set(name)
        screen.update()
    from pygame import mixer
    mixer.init()
    # Loading Selected Song
    print(scvalue.get(),"--------------------------------------------")
    mixer.music.load(scvalue.get())
    # Playing Selected Song
    mixer.music.play()
    #os.startfile(os.path.join(music_dir,songs[3]))

    
def pausesong():
    from pygame import mixer
    mixer.init()
    mixer.music.pause()
def stopsong():
    print("hhhhh")
    from pygame import mixer
    #from mutagen.mp3 import MP3
    import os
    mixer.init()
    mixer.music.stop()

    # Changing Directory for fetching Songs
    #os.chdir("D:\\music\\my folder\\UCMusic")
    # Fetching Songs
    #songtracks = os.listdir()
    #siz=(len(songtracks))
    #name=songtracks[1]



if __name__ == "__main__":
    root = Tk()
    root.geometry("444x444")
    root.title(" MY - Music Player")
    root.configure(bg='black')
    frame = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
    
    scvalue = StringVar()
    scvalue.set("")
    screen = Label(root,text="playing music",textvar=scvalue,font="lucida 20 bold",bg="light grey")
    screen.pack(fill=X,ipadx=8,padx=10,pady=10)

    label = Label(root, text=" Your Musics ",bg="blue")
    
    Scroll = Scrollbar(root)
    Scroll.pack(side=RIGHT,fill=Y)

    Lb1 = Listbox(root,bg="grey",font="Helveti",fg="black",width=90)
    Lb1.bind ('<<ListboxSelect>>',Selectsong)
    
    # Changing Directory for fetching Songs
    os.chdir("D:\\music\\my folder\\UCMusic")
    # Fetching Songs
    songtracks = os.listdir()
    #print(songtracks)
    for track in songtracks:
        if '.mp3' in track:
            Lb1.insert(END,track)
        
    
    Lb1.pack(side=RIGHT,anchor=NE,fill=BOTH)
    Scroll.config(command=Lb1.yview)

    # Inserting Play Button
    photo=PhotoImage(file="D:\\python programs\\PYTHON_GUI_TKINTER\\start.gif")
    play = Button(root,image=photo,command=playsong,font=("times new roman",15,"bold")).pack(side=BOTTOM,anchor=CENTER,pady=5)
    # Inserting Pause Button
    # photo1=PhotoImage(file="D:\\python programs\\PYTHON_GUI_TKINTER\\pause.gif")
    # pause = Button(root,image=photo1,command=pausesong,font=("times new roman",15,"bold")).pack(side=BOTTOM,anchor=CENTER)
    # Inserting Stop Button
    photo2=PhotoImage(file="D:\\python programs\\PYTHON_GUI_TKINTER\\stop .gif")
    stop = Button(root,image=photo2,command=stopsong,font=("times new roman",15,"bold")).pack(side=BOTTOM,anchor=CENTER)


    frame.pack(side=LEFT, anchor="nw")

    
    background_image = PhotoImage(file="D:\\python programs\\PYTHON_GUI_TKINTER\\unnamed.gif")
    background = Label(root, image=background_image, bd=0)
    background.pack()

    #showinfo('welcome','For play selected Music plese double click on your selected music')
    
    
    root.mainloop()