#! Python3

#Import needed libraries
import sys, pyperclip, webbrowser

if len(sys.argv) > 1:
	# Get address from command line
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()
	
webbrowser.open('https://www.google.com/maps/place/' + address)
