#! python3

from tkinter import *
import smsAlert

def clicked():
	
	response = "Message: " + txt.get()
	lbl.configure(text=response)
	smsAlert.sendText(response)
	
# Construct a window
window = Tk()
window.title('Text Myself')
window.geometry('500x140')

# Add a Label
lbl = Label(window, text = "Enter your message", font = ("ArialBold", 13))
lbl.grid(column = 0, row = 0)

# Add a text entry box
txt = Entry(window, width = 23)

# Allows focus so you can start typing
txt.focus()
txt.grid(column = 0, row = 2)

# Add Button
btn = Button(window, text="Send Text Msg", bg="grey", command=clicked)
btn.grid(column = 2, row = 2)

# Create Window
window.mainloop()
