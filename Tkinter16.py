from tkinter import *

root = Tk()
root.geometry("444x444")
root.title("Scrollbar tutorial ")

# For connectiong Scrollbar to a widget
# 1. Widget(Yscrollbar = scrollbar.set)
# 2. Scrollbar.config(command=widget.Yview)

Scrollbar = Scrollbar(root)
Scrollbar.pack(side=RIGHT,fill=Y)

'''
listbox = Listbox(root,yscrollcommand=Scrollbar.set)
for i in range(344):
    listbox.insert(END,f"Item {i}")

listbox.pack(fill=BOTH,padx=22)
'''
text= Text(root,yscrollcommand=Scrollbar.set)
text.pack(fill=BOTH)
Scrollbar.config(command=text.yview)



root.mainloop()