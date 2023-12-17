from tkinter import *
def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("stop Busy..")

root = Tk()
root.geometry("444x444")
root.title(" Status bar ")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()

root.mainloop()