'''
from tkinter import *
import tkinter

def play():
    pass

root = Tk()

Lb1 = Listbox(root)
Lb1.insert(1,"bbb",)
Lb1.insert(2,"bbb")
Lb1.insert(3,"bbb")
Lb1.insert(4,"bbb")
Lb1.insert(5,"bbb")

Lb1.pack()

root.mainloop()
'''
'''
from tkinter import *

root = Tk()
root.geometry("1200x1200")

# GUI logic

root.mainloop()
'''
'''
import os

#filename=raw_input("hi.mp3")
    ## delete only if file exists ##
if os.path.exists("hi.mp3"):
    os.remove("hi.mp3")
else:
    print("Sorry, I can not remove hi.mp3")
'''
'''
from gtts import gTTS

mytext = "i am bipul"
myobj =gTTS(text=mytext)
myobj.save("bipul.mp3")

from pyaudio import playsound

playsound("bipul.mp3")
'''
'''

from tkinter import *
import time
root = Tk()
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)
def tick():
# get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
# if time string has changed, update it
    clock.config(text=time2)
# calls itself every 200 milliseconds
# to update the time display as needed
# could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
root.mainloop( )
'''
'''
# import the time module 
import time 

# define the countdown func. 
def countdown(t): 
	
	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print("mytime: ",timer, end="\r") 
		time.sleep(1) 
		t -= 1
	
	print('Fire in the hole!!') 


# input time in seconds 
t = input("Enter the time in seconds: ") 

# function call 
countdown(int(t)) 
'''
'''
import time
from tkinter import *
from tkinter import messagebox


# creating Tk window
root = Tk()

# setting geometry of tk window
root.geometry("300x250")

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Time Counter")

# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("10")

# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=hour)
hourEntry.place(x=80,y=20)

minuteEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=minute)
minuteEntry.place(x=130,y=20)

secondEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=second)
secondEntry.place(x=180,y=20)


def submit():
	try:
		# the input provided by the user is
		# stored in here :temp
		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		print("Please input the right value")
	while temp >-1:
		
		# divmod(firstvalue = temp//60, secondvalue = temp%60)
		mins,secs = divmod(temp,60) 

		# Converting the input entered in mins or secs to hours,
		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
		# 50min: 0sec)
		hours=0
		if mins >60:
			
			# divmod(firstvalue = temp//60, secondvalue 
			# = temp%60)
			hours, mins = divmod(mins, 60)
		
		# using format () method to store the value up to 
		# two decimal places
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		# updating the GUI window after decrementing the
		# temp value every time
		root.update()
		time.sleep(1)

		# when temp value = 0; then a messagebox pop's up
		# with a message:"Time's up"
		if (temp == 0):
			messagebox.showinfo("Time Countdown", "Time's up ")
		
		# after every one sec the value of temp will be decremented
		# by one
		temp -= 1

# button widget
btn = Button(root, text='Set Time Countdown', bd='5',
			command= submit)
btn.place(x = 70,y = 120)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
'''
'''
min,sec = divmod(50,60)
print(min,sec)
'''
'''
list1 =['a','b','c']

list2=['a','v','c']

n = int(input("enter: "))
list3=list1[0:n]
print(list3)

for i in range(0,3):
	if list2[i] in list1:
		print("yes",list2[i])
	else:
		print("no",list2[i])

'''
'''
b='2.5'
c='4'
b=b.replace('.','',1).isdigit()
c=c.replace('.','',1).isdigit()
print(b,c)
'''
'''
#l=[6,12,24,48]
l=[5,3,11,30]
maxn=max(l)
p=0
prim=[]
for i in range(0,len(l)):
	if maxn%l[i]==0:
		p+=1
	else:
		nd=l[i]
if p==len(l):
	print("ans",maxn)
else:
	if p==len(l)-1:
		nn=-1
		while(nn<len(l)-2):
			nn+=1
			if l[nn]>9:
				for i in range(2,l[nn]):
					if (l[nn] %i)==0:
						print("not prime:",l[nn])
					else:
						prim.append(l[nn])
						print("prime",l[nn])
	else:
		n=3
		k=2
		div=0
		while(n>2):
			div=maxn*k
			if div%nd==0:
				n=0
				print("ans1",div)
			else:
				k+=1

'''
'''
******************************************************************************************************

# importing libraries 
import cv2 
import numpy as np 

# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture('tree.mp4') 

# Check if camera opened successfully 
if (cap.isOpened()== False): 
print("Error opening video file") 

# Read until video is completed 
while(cap.isOpened()): 
	
# Capture frame-by-frame 
ret, frame = cap.read() 
if ret == True: 

	# Display the resulting frame 
	cv2.imshow('Frame', frame) 

	# Press Q on keyboard to exit 
	if cv2.waitKey(25) & 0xFF == ord('q'): 
	break

# Break the loop 
else: 
	break

# When everything done, release 
# the video capture object 
cap.release() 

# Closes all the frames 
cv2.destroyAllWindows()

******************************************************************************************************
'''

