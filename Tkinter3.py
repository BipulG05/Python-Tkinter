"""
# it is from google

import tkinter as tk
from PIL import ImageTk, Image


bipul_root = tk.Tk()
image = Image.open("school1.gif")
photo = ImageTk.PhotoImage(image)
label = tk.Label(bipul_root, image=photo)
label.img = photo
label.pack()
bipul_root.mainloop()
"""
# it is from herry

from tkinter import *
from PIL import ImageTk, Image


bipul_root = Tk()
bipul_root.geometry("444x444")


# for jpg and other  photo 
image = Image.open("Amit2.jpg")
photo = ImageTk.PhotoImage(image)


amit_label = Label(image=photo)
amit_label.pack()


bipul_root.mainloop()
