from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from  PIL import  (Image,ImageTk)

score=0
p=['pyimage1','pyimage1','pyimage1','pyimage1','pyimage1','pyimage1','pyimage1','pyimage1','pyimage1']
count=0
player1=0
player2=0

def cheek():
    global score
    global p
    global player1
    global player2
    global count
    
    if p[0]!='pyimage1':
        if p[0]==p[1]==p[2]:
            if p[0]=='pyimage2':
                player2=player2+1
                showinfo("ohh",f"player 2 win \n player2 score:- {player2}")
            else:
                player1=player1+1
                showinfo("ohh",f"player 1 win \n player1 score:- {player1}")
            score=1
    if p[3]!='pyimage1':
        if p[3]==p[4]==p[5]:
            if p[3]=='pyimage2':
                player2=player2+1
                showinfo("ohh",f"player 2 win \n player2 score:- {player2}")
            else:
                player1=player1+1
                showinfo("ohh",f"player 1 win \n player1 score:- {player1}")
            score=1
    if p[6]!='pyimage1':
        if p[6]==p[7]==p[8]:
            if p[6]=='pyimage2':
                player2=player2+1
                showinfo("ohh",f"player 2 win \n player2 score:- {player2}")
            else:
                player1=player1+1
                showinfo("ohh",f"player 1 win \n player1 score:- {player1}")
            score=1
    if p[0]!='pyimage1':
        if p[0]==p[3]==p[6]:
            if p[0]=='pyimage2':
                player2=player2+1
                showinfo("ohh",f"player 2 win \n player2 score:- {player2}")
            else:
                player1=player1+1
                showinfo("ohh",f"player 1 win \n player1 score:- {player1}")
            score=1
    if p[1]!='pyimage1':
        if p[1]==p[4]==p[7]:
            if p[1]=='pyimage2':
                player2=player2+1
                showinfo("ohh",f"player 2 win \n player2 score:- {player2}")
            else:
                player1=player1+1
                showinfo("ohh",f"player 1 win \n player1 score:- {player1}")
            score=1
    if p[2]!='pyimage1':
        if p[2]==p[5]==p[8]:
            if p[2]=='pyimage2':
                player2=player2+1
                showinfo("ohh",f"player 2 win \n player2 score:- {player2}")
            else:
                player1=player1+1
                showinfo("ohh",f"player 1 win \n player1 score:- {player1}")
            score=1
    if p[0]!='pyimage1':
        if p[0]==p[4]==p[8]:
            if p[0]=='pyimage2':
                player2=player2+1
                showinfo("ohh",f"player 2 win \n player2 score:- {player2}")
            else:
                player1=player1+1
                showinfo("ohh",f"player 1 win \n player1 score:- {player1}")
            score=1
    if p[6]!='pyimage1':
        if p[2]==p[4]==p[6]:
            if p[6]=='pyimage2':
                player2=player2+1
                showinfo("ohh",f"player 2 win \n player2 score:- {player2}")
            else:
                player1=player1+1
                showinfo("ohh",f"player 1 win \n player1 score:- {player1}")
            score=1
    if count==9:
        showinfo("ohh",f"You two lost !!! \n player 1 score:- {player1} \n player2 score:- {player2}")
        score=1

    if score!=0:
        ans=askyesno("Author","Do you want to continue ?")
        if ans==True:
            score=0
            count=0
            p=['pyimage1','pyimage1','pyimage1','pyimage1','pyimage1','pyimage1','pyimage1','pyimage1','pyimage1']
            i=0
            for i1 in range(1,4):
                for i2 in range(0,3):
                    btn[i].config(image=gallery1['base.jpg'],padx=2,pady=2)
                    btn[i].bind("<Button-1>",click)
                    i+=1
        else:
            if player1>player2:
                showinfo("ohh",f"player 1 win whole turnament !!! \n player 1 score:- {player1} \n player2 score:- {player2}")
            elif player2>player1:
                showinfo("ohh",f"player 2 win whole turnament !!! \n player 1 score:- {player1} \n player2 score:- {player2}")
            else:
                showinfo("ohh",f" OPPS Drow !!! \n player 1 score:- {player1} \n player2 score:- {player2}")
            root.destroy()


def click(event):
    global count
    text=event.widget.cget("text")
    n=int(text)

    if count%2!=0:
        if btn[n].cget('image')=='pyimage1':
            btn[n].configure(image=gallery['player1.jpg'],padx=2,pady=2)
            btn[n].update()
            p[n]='pyimage2'
            count=count+1
    else:
        if btn[n].cget('image')=='pyimage1':
            btn[n].configure(image=gallery['player2.jpg'],padx=2,pady=2)
            btn[n].update()
            p[n]='pyimage3'
            count=count+1
    if count>=5:
        cheek()
    
    



root = Tk()
root.geometry("340x520")
#root.resizable(False,False)
root.title("codbyBipul- Welcome Your xoxo game ")
root.wm_iconbitmap("D:\python programs\PYTHON_GUI_TKINTER\calculator.ico")
root.configure(background="tomato")

#headlabel = Label(root, text="Welcome Your xoxo game - For You", fg='black',bg='burlywood1')
#headlabel.grid(row=0, column=3)

gallery1={}
gallery={}
gallery1['base.jpg']=ImageTk.PhotoImage(Image.open('D:\\python programs\\memorygame\\base.jpg'). resize(( 100,120)))
gallery['player1.jpg']=ImageTk.PhotoImage(Image.open('D:\\python programs\\memorygame\\player1.jpg'). resize(( 90,110)))
gallery['player2.jpg']=ImageTk.PhotoImage(Image.open('D:\\python programs\\memorygame\\player2.jpg'). resize(( 90,110)))

btn=[]


for i in range(1,10):
    btn.append(Button(root,text=f'{i-1}',image=gallery1['base.jpg']))
    btn[i-1].bind("<Button-1>",click)

i=0
for i1 in range(1,4):
    for i2 in range(0,3):
        btn[i].grid(column=f"{i2}",row=f"{i1}",padx=2,pady=2)
        i+=1

root.mainloop()
