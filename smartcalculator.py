from tkinter import *
import math


def find_gcd(x,y):
    while(y):
        x, y = y , x % y
    return x

def calculate():
    oprends=[]
    operator=[]
    text = TextArea.get("1.0","end")
    intext=text.split()
    l=len(intext)
    for i in range(l):
        if intext[i].isdigit()==True or intext[i].replace('.','',1).isdigit():
            oprends.append(intext[i])
        else:
            operator.append(intext[i])
    for i in range(0,len(oprends)):
            oprends[i]=float(oprends[i])
    result=0
    for i in operator:
        if i == 'add' or i == 'addition' or i == '+' or i =='sum' or i == 'plus' :
            for i in range(0,len(oprends)):
                result=result+oprends[i]
        elif i == 'minas' or i == '-' :
            result=oprends[0]
            for i in range(1,len(oprends)):
                result=result-oprends[i]
        elif i == 'multiplie' or i=='*':
            result=1
            for i in range(0,len(oprends)):
                result=result*oprends[i]
        elif i == 'divition' or i=='/':
            result=oprends[0]
            for i in range(1,len(oprends)):
                result=result/oprends[i]
        elif i =='gcd' or i=='hcf' or i=='gcf' :
            l=oprends[:]
            num1=l[0]
            num2=l[1]
            result=find_gcd(num1,num2)
            for i in range(2,len(l)):
                result=find_gcd(result,l[i])
        elif i =='lcm':
            l=oprends[:]
            min1=max(l)
            for i in range(0,len(l)):
                pass
        elif i =='pow':
            result=pow(oprends[0],oprends[1])
            if len(oprends)>2:
                for i in range(2,len(oprends)):
                    result=pow(result,oprends[i])
        elif i == 'root':
            result=math.sqrt(oprends[0])
        else:
            result="wrong input"
            


    result=str(result)
    fullresult=text+" : "+result
    TextArea.delete(1.0,"end")
    TextArea.insert(1.0, fullresult)

def speakOutput():
    mytext1 = TextArea.get("1.0","end")
    pass
    


if __name__ == "__main__":
    root = Tk()
    root.title(" Smart Calculator - YourOwn")
    #root.wm_iconbitmap("D:\\python programs\\turtle\\christmas_santa.ico")
    root.geometry("500x500")
    root.configure(bg='tomato')
    headlabel = Label(root, text="Welcome Your Smart Calculator - For You", fg='black',bg='burlywood1')
    headlabel.grid(row=0, column=3)


    TextArea = Text(root, font='lucida 13',width=50,height=10)
    file = None
    TextArea.grid(row=1,column=3,padx=10,pady=10)

    button_sub3 = Button(root,text="Speak", bg='steelblue1',command=speakOutput)
    button_sub3.grid(row=2,column=3,ipadx=10,pady=10)


    TextArea1 = Text(root, font='lucida 13',width=50,height=4)
    file = None
    TextArea1.grid(row=3,column=3,padx=10,pady=10)

    button_sub3 = Button(root,text="calculate", bg='steelblue1',command=calculate)
    button_sub3.grid(row=4,column=3,ipadx=10,pady=10)



    root.mainloop()