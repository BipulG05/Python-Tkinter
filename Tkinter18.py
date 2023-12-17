from tkinter import *


class GUI(Tk):
    def __init__(self):   # HERE ROOT IS SELF
        super().__init__()
        self.geometry("444x444")
        self.title("Object oriented prog - Class")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self,textvar=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("Button click")


    def creatbutton(self):
        Button(text="inptext",command=self.click).pack()



if __name__ == "__main__":
    window = GUI()
    window.status()
    window.creatbutton()
    window.mainloop()
