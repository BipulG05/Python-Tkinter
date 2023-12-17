from tkinter import *
import os

def delete():
    if os.path.exists( f'{i}'+'.mp3' ):
        os.remove( f'{i}' +'.mp3' )
    else:
        print("Sorry, I can not remove hi.mp3")

def Trans():
    from googletrans import Translator
    text = TextArea.get("1.0","end")
    #print(text,"------------------------------------------")
    translator = Translator()
    from langdetect import detect
    #dt = translator.detect(text)
    dt = detect(text)
    print(text,"------------------------------------------")
    print(dt)
    leng = variable2.get()
    print(leng)
    #translated = translator.translate(text,src='fi',dest=f'{leng}')
    #translated = translator.translate(text,src=f'{dt}',dest=f'{leng}')
    translated=translator.translate(text,src= dt,dest= leng)

    #translator= Translator(to_lang=leng)
    #translator= Translator(from_lang=dt,to_lang=leng)
    #translated = translator.translate(text)

    print(text,"------------------------------------------")
    text3 = translated.text
    print(text3,"*****************************************")
    TextArea1.delete(1.0,"end")
    TextArea1.insert(1.0, text3)

def speakInput():
   # from gtts import gTTS
    import gtts
    mytext = TextArea.get("1.0","end")
    leng1 = variable1.get()
    myobj = gtts.gTTS(text=mytext)
    print('line 4')
    myobj.save( "input.mp3" )
    print('line 5')
    audio_file="input.mp3"
    import playsound
    import os
    playsound.playsound(audio_file)
    os.remove(audio_file)
    '''from pygame import mixer
    mixer.init()
    mixer.music.load( "input.mp3" )
    mixer.music.play()'''
    
def speakOutput():
    from gtts import gTTS
    mytext1 = TextArea1.get("1.0","end")
    leng2 = variable2.get()
    myobj1 = gTTS(text=mytext1)
    myobj1.save("output.mp3")
    audio_file="output.mp3"
    import playsound
    import os
    playsound.playsound(audio_file)
    os.remove(audio_file)
    '''
    from pygame import mixer
    mixer.init()
    mixer.music.load("output.mp3")
    mixer.music.play()
    '''


if __name__ == "__main__":
    root = Tk()
    root.title(" Transpad - YourOwn")
    #root.wm_iconbitmap("christmas_santa.ico")
    #root.geometry("765x765")
    root.geometry("765x290")
    root.configure(bg='tomato')
    #root.minsize(550,400)
    #root.maxsize(680,400)
    headlabel = Label(root, text="Welcome YourTranslator - For You", fg='black',bg='burlywood1')
    headlabel.grid(row=0, column=3)

    cur_list = ['en','bn','da','hi','fi','de','id','zh-cn','ja']
    variable1 = StringVar()
    variable1.set(cur_list[0])
    variable2 = StringVar()
    variable2.set(cur_list[1])

    from_cur_option = OptionMenu(root,variable1,*cur_list)
    to_cur_option = OptionMenu(root,variable2,*cur_list)

    from_cur_option.grid(row=1, column=2, ipadx=15,padx=15)
    to_cur_option.grid(row=1, column=4, ipadx=15,padx=15)

    #TextArea = Text(root, font='lucida 13',width=70,height=30)
    TextArea = Text(root, font='lucida 13',width=30,height=10)
    file = None
    TextArea.grid(row=3,column=2,padx=10)

    button_sub1 = Button(root,text="Speak", bg='steelblue1',command=speakInput)
    button_sub1.grid(row=4,column=2,ipadx=10,pady=10)

    button_sub2 = Button(root,text="Translate", bg='spring green',command=Trans)
    button_sub2.grid(row=3,column=3,ipadx=10)

    #TextArea1 = Text(root, font='lucida 13',width=70,height=30)
    TextArea1 = Text(root, font='lucida 13',width=30,height=10)
    file = None
    TextArea1.grid(row=3,column=4)

    button_sub3 = Button(root,text="Speak", bg='steelblue1',command=speakOutput)
    button_sub3.grid(row=4,column=4,ipadx=10,pady=10)



    root.mainloop()