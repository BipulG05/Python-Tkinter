from tkinter import *

def bipul(event):
    print(f"button click at {event.x} , {event.y}")

root = Tk()
root.geometry("444x444")
root.title("Event in Tkinter")

Widget = Button(root,text="click here",bg="blue")
Widget.pack()

Widget.bind('<Button-1>',bipul)
Widget.bind('<Double-1>',quit)



root.mainloop()