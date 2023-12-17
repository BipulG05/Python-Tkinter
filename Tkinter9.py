from tkinter import *

root = Tk()
Canvas_width = 800
Canvas_height = 400

root.geometry(f"{Canvas_width}x{Canvas_height}")
root.title("Bipul GUI")

can_widget = Canvas(root, width=Canvas_width, height=Canvas_height)
can_widget.pack()

# The line goes from the point x1, y1, to x2, y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="red")

# To create a rectangle specify parameter in this order - coors of top left and coors of bottom right
can_widget.create_rectangle(10,10,700,300,fill="blue")

can_widget.create_text(200,200,text="python gui")

can_widget.create_oval(240,130,130,250,fill="green")


root.mainloop()