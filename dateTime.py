#Uses the datetime object to create and manipulate date and time

#import modules needed from datetime
#Main Module: datetime - Sub Modules (Manipulates...): time, date, datetime
from datetime import time
from datetime import date 
from datetime import datetime

#Creates a main loop so this module can be imported 
def main():
	
	#Create a new date time object that holds the current datetime BASED ON COMPUTER'S TIMEZONE
	currentTime = datetime.now()
	print(type(currentTime))
	print(currentTime)
	
	#Prints only the time from the datetime onject
	print(datetime.time(currentTime))
	
	#Uses strftime to print only the year from datetime object
	print("Current Year:", currentTime.strftime("%Y"))
	
	#Uses strftime to print a very human readable date
	print("Current Date:", currentTime.strftime("%a, %B %d, %Y"))

#Before and after underscore (Dunder) is a magic method
if __name__ == "__main__":
	main()
