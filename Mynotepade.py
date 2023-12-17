from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os



def newFile():
    global file
    root.title("Untitle - Notepad")
    file = None
    TextArea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            # Save file as a new file
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")
            print("File saved")
    else:
         # Save file the file
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()


def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Christmas_Santa_Notepad","Notepad by bipul. You can too")


if __name__ == "__main__":
    root = Tk()
    root.title("Christmas_Santa_Notepad - YourOwn")
    root.wm_iconbitmap("D:\python programs\PYTHON_GUI_TKINTER\christmas_santa.ico")
    root.geometry("675x765")
    root.minsize(444,444)
    root.maxsize(777,777)
    # Add text area
    TextArea = Text(root, font='lucida 13')
    file = None
    TextArea.pack(fill=BOTH,expand=True)

    # lets create a Menubar
    MenuBar = Menu(root)

    #File menu starts
    FileMenu = Menu(MenuBar,tearoff=0)

    # To open new file
    FileMenu.add_command(label="New",command=newFile)

    #To open already existing file
    FileMenu.add_command(label="Open",command=openFile)

    #To save the current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    # File menu Ends

    #Edit menu starts
    EditMenu = Menu(MenuBar,tearoff=0)
    # To give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    

    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    MenuBar.add_cascade(label="Search",menu=EditMenu)
    MenuBar.add_cascade(label="View",menu=EditMenu)
    MenuBar.add_cascade(label="Language",menu=EditMenu)
    MenuBar.add_cascade(label="Setting",menu=EditMenu)
    MenuBar.add_cascade(label="Tools",menu=EditMenu)
    MenuBar.add_cascade(label="Run",menu=EditMenu)
    MenuBar.add_cascade(label="Plugins",menu=EditMenu)

    #Edit Menu Ends

    #Help Menu start
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)


    root.config(menu=MenuBar)

    #Add ScrollBar using rules from Tkinterlecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    root.mainloop()