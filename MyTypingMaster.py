from tkinter import *
global temp
global Gtime


def Start():
    global Gtime
    global temp
    text='''  The quick brown fox jumps over a lazy dog. The quick brown fox jumps over a lazy dog. 
    The quick brown fox jumps over a lazy dog. The quick brown fox jumps over a lazy dog. 
    The quick brown fox jumps over a lazy dog. The quick brown fox jumps over a lazy dog. 
    The quick brown fox jumps over a lazy dog. The quick brown fox jumps over a lazy dog. 
    The quick brown fox jumps over a lazy dog. The quick brown fox jumps over a lazy dog. 
    The quick brown fox jumps over a lazy dog. The quick brown fox jumps over a lazy dog. 
    The quick brown fox jumps over a lazy dog. The quick brown fox jumps over a lazy dog. 
    The quick brown fox jumps over a lazy dog. The quick brown fox jumps over a lazy dog. 
    The quick brown fox jumps over a lazy dog. The quick brown fox jumps over a lazy dog. 
    '''
    scvalue.set(text)
    import time
    from tkinter import messagebox
    try:
		# the input provided by the user is
		# stored in here :temp
        temp = int(minute.get())*60 + int(second.get())
        Gtime=temp
    except:
        print("Please input the right value")
    while temp >-1:
		# divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60) 

		# Converting the input entered in mins or secs to hours,
		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
		# 50min: 0sec)
        hours=0
        if mins >60:
			# divmod(firstvalue = temp//60, secondvalue 
			# = temp%60)
            hours, mins = divmod(mins, 60)
		
		# using format () method to store the value up to 
		# two decimal places
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

		# updating the GUI window after decrementing the
		# temp value every time
        root.update()
        time.sleep(1)

		# when temp value = 0; then a messagebox pop's up
		# with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
		# after every one sec the value of temp will be decremented
		# by one
        temp -= 1

def Result():
    global Gtime
    global temp
    Btime = temp
    Mytime=Gtime-Btime
    #print(Btime, Gtime, Mytime)
    min,sec = divmod(Mytime,60)
    temp= -2
    minute.set("00")
    second.set("00")
    text1=scvalue.get()
    Mtext=text1.split()
    #print(Mtext)
    text3=TextArea1.get("1.0","end")
    Yrtext=text3.split()
    Ylen=len(Yrtext)
    Mtext1=Mtext[0:Ylen]
    #print(Mtext1,Yrtext)
    #print(Mlen)
    #print(Yrtext)
    RightWord=0
    WrongWord=0
    wlist=[]
    for i in range(0,Ylen):
        if Yrtext[i] in Mtext1:
            RightWord=RightWord+1
        else:
            wlist.append(Yrtext[i])
            WrongWord=WrongWord+1

            #print(Mtext[i])
    print(min)
    #result=(f " Wrong Word: {WrongWord} {\n}' Right Word : {RighrWord} ")
    scvalue6.set(f" word/min : {(RightWord+WrongWord)/min} \n Time Given : 10:00  Time Take : {min}:{sec}  \n  Wrong Word: {WrongWord}   Right Word : {RightWord} \n Wrong words: {wlist} ")
    #print(wlist)
    



if __name__ == "__main__":
    root = Tk()
    root.title(" Transpad - YourOwn")
    root.wm_iconbitmap("christmas_santa.ico")
    root.geometry("700x765")
    root.configure(bg='tomato')
    root.minsize(444,444)
    #root.maxsize(777,777)
    headlabel = Label(root, text="Welcome MyTranslator - For You",font='lucida 15 bold', fg='black',bg='burlywood1')
    headlabel.pack(side=TOP,anchor=CENTER,pady=5)

    headlabel = Label(root, text="Your Text : ",font='lucida 15 bold', fg='black',bg='burlywood1')
    headlabel.pack(anchor=CENTER,pady=1)

    minute=StringVar()
    second=StringVar()

# setting the default value as 0
    minute.set("10")
    second.set("00")

    minuteEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=minute)
    minuteEntry.pack(anchor=NE,pady=1,padx=10)

    secondEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=second)
    secondEntry.pack(anchor=NE,pady=1,padx=10)

    scvalue = StringVar()
    scvalue.set("")

    TextArea = Label(root,textvar=scvalue, font='lucida 13',width=100,height=10)
    TextArea.pack(anchor=CENTER,pady=1,ipadx=10)

    button_sub1 = Button(root,text="Start", bg='steelblue1',command=Start)
    button_sub1.pack(anchor=CENTER,pady=10,ipadx=5)
    
    headlabel = Label(root, text="Type Here : ",font='lucida 15 bold', fg='black',bg='burlywood1')
    headlabel.pack(anchor=CENTER,pady=10)
    
    TextArea1 = Text(root, font='lucida 13',width=100,height=10)
    file = None
    TextArea1.pack(anchor=CENTER,pady=10)

    button_sub3 = Button(root,text="Submit", bg='steelblue1',command=Result)
    button_sub3.pack(anchor=CENTER,pady=10)

    scvalue6 = StringVar()
    scvalue6.set("")

    TextArea3 = Label(root,textvar=scvalue6, font='lucida 13',width=90,height=10)
    TextArea3.pack(anchor=CENTER,pady=10)
    
    root.mainloop()