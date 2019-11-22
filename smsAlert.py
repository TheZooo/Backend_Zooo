from twilio.rest import Client
import time

def sendText(userInput='This is empty'):
	
	#Set up Twilio account credentials
	accountSID = ''
	authToken = ''
	
	#Create Twilio connection object and set phone numbers
	twilioCli = Client(accountSID, authToken)
	myTwilioNumber = 
	myCellPhone = 
	
	# Create message we want send with Twilio
	message = twilioCli.messages.create(
		body = 'My Python app says: ' + str(userInput),
		from_ = myTwilioNumber,
		to = myCellPhone
		)
