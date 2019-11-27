#! python3

#Import needed libraries
from tkinter import *
import time
import random

count = 0

def clicked():
	# Starts the random countdown and get rid of the button
	global count
	lbl.configure(text="Get Ready...")
	btn.destroy()
	time.sleep(random.randint(2, 4))
	
	#Starts timer and creates a new button
	count = time.time()
	global btn2
	btn2 = Button(window, text="NOW!!!", bg="gray", command=clickedStop)
	btn2.grid(column=2, row=2)
	
def clickedStop():
	global count
	
	# Subtracts the current time by counted time and displays it
	finalTime = time.time() - count
	finalTime = round(finalTime, 3)
	results = str(finalTime), "seconds"
	lbl.configure(text=results)
	btn2.destroy()
	
	# Recreates a new button that triggers "clicked" function
	btn = Button(window, text="Restart", bg="gray", command=clicked)
	btn.grid(column=2, row=2)
	
# Create a window
window = Tk()
window.title("Reaction Game")
window.geometry("500x140")

# Add a Label
lbl = Label(window, text="Click to Begin", font=("ArialBold", 12))
lbl.grid(column=0, row=0, columnspan=2)

# Add a Button
btn = Button(window, text="Start", bg="gray", command=clicked)
btn.grid(column=2, row=2)

# Create Window Loop
window.mainloop()
