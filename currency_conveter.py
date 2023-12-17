from tkinter import *
import requests , json

def convert_cur():
    import requests , json
    Fst_cur =  variable1.get()
    sec_cur = variable2.get()
    amount = float(amount1_fil.get())
    prin=requests.get(url).json()
    cur_list=prin['rates']
    # print(cur_list)
    Fst_cur1 = cur_list[f'{Fst_cur}']
    sec_cur1 = cur_list[f'{sec_cur}']

    if sec_cur1>=Fst_cur1:                      # usd to inr -> 1.16225 usd = 85.65722 inr
        main_cur = sec_cur1/Fst_cur1
        from_cur = 1 * amount                    
        To_cur = main_cur * amount
    else:                                      # inr to usd -> 85.65722 inr = 1.16225 usd  0.005427446744622369
        main_cur = sec_cur1/Fst_cur1     
        from_cur = amount
        To_cur = amount*main_cur

        #print(sec_cur1,Fst_cur1,main_cur)
    
    
    #print(f"{from_cur} {Fst_cur} is to {To_cur} {sec_cur}")
    amount1_fi2.insert(0, str(To_cur))
    if To_cur<1:
        To_cur = To_cur
    else:
        To_cur = round(To_cur)
    name = f"{from_cur} {Fst_cur} equals {To_cur} {(sec_cur)}"
    #amount1_fi2.insert(0, str(To_cur))
    scvalue.set(name)
    screen.update()


if __name__ == "__main__":
    root = Tk()
    root.geometry("699x666")
    root.title("Currency conveter - By Bipul")
    root.configure(bg='green')
    headlabel = Label(root, text="Welcome to real time conveter - For You", fg='white',bg='black')
    headlabel.grid(row=0, column=2)

    cur_list = ['INR','USD','CAD','CNY','DKK','EUR']
    variable1 = StringVar()
    variable1.set(cur_list[0])
    variable2 = StringVar()
    variable2.set(cur_list[1])

    from_cur_option = OptionMenu(root,variable1,*cur_list)
    to_cur_option = OptionMenu(root,variable2,*cur_list)

    from_cur_option.grid(row=3, column=1, ipadx=15,padx=15)
    to_cur_option.grid(row=3, column=3, ipadx=15,padx=15)

    amount1_fil = Entry()
    amount1_fi2 = Entry()

    amount1_fil.grid(row=5,column=1,padx=15,ipadx='25')
    amount1_fi2.grid(row=5,column=3,padx=15,ipadx='25')

    button_sub = Button(root,text="Convert", bg='red',command=convert_cur)
    button_sub.grid(row=7,column=2)

    scvalue = StringVar()
    scvalue.set("")
    screen = Label(root,text="Result",textvar=scvalue,font="lucida 20 bold",bg="white")
    screen.grid(row=9,column=2,ipadx='140',padx=0)

    YOUR_ACCESS_KEY ='9214683b0dc4d556bddb0886ce316872'
    #YOUR_ACCESS_KEY ='QCGH8VEFM8L547VP'   # 'YIRJKH2IS9CZNO2C'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)




    root.mainloop()