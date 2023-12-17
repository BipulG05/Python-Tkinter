from tkinter import *

root = Tk()
root.geometry("444x444")
root.title("codbyBipul- title ")
root.wm_iconbitmap("dino_dinosaur.ico")
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")
Button(text="close",command=root.destroy).pack()


root.mainloop()

