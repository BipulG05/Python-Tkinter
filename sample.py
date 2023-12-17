#Import all necessary modules.

from tkinter import *
from tkinter import ttk
import random
#Imnporting shuffle allows us to shuffle a list.
from random import shuffle
import time

#Create canvas and assign it to variable root.
root = Tk()

#Making photo accessible
def stimage(file):
    return PhotoImage(width=100,height=100,file=file)

clicks=[]

clickCount=0
faceUp=[]
score=0

back = PhotoImage(width=100, height=100, file="start.gif")
images = [stimage("1.gif"), stimage("2.gif"), stimage("3.gif"), stimage("4.gif"), stimage("5.gif"), stimage("6.gif"), stimage("7.gif"), stimage("8.gif")]

#Function returns a button, equipped with a command that changes its background colour. It takes the argument image.
def button(n):
    #Create a button with parent root, and a red colour for image. This will be the back of each card.
    button = Button(root,height=100,width=100, image=back)

    #Command for button. Flips over when clicked.
    def flip():
        global clickCount
        global faceUp
        clickCount+=1
        #Make the card display an image.
        button.config(image=images[n])
        #If image of button is displayed, append to list faceUp
        if button.cget("image")!=back:
            #Append the button object and image index n to list faceUp
            faceUp.append([button,n])
        if clickCount==2:
            clickCount=0
            if faceUp[0][1]==faceUp[1][1]:
                print("Hello")
            else:
                button.config(image=back)
            faceUp=[]

    button.config(command=flip)
    return button

#Create a list of coordinates that the buttons will occupy.
coord = [[a,b] for a in range(1,5) for b in range(1,5)]
#Randomise coordinates so buttons appear in random places.
random.shuffle(coord)
buttons=[]

for i in range(8):
    buttons.append(button(i))
    buttons[2*i].grid(row=coord[i][0], column=coord[i][1])
    buttons.append(button(i))
    buttons[2*i+1].grid(row=coord[i+8][0], column=coord[i+8][1])