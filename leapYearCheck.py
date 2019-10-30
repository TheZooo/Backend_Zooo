def yearStrCheck(para):
	#Function will check if the string only has digits
	#passes its parameter to other function
	if (para.isdigit()):
		leapYearChecker(int(para))
	else:
		print("Input needs to be digits only")
		yearStrCheck(input("Year: "))
		
def leapYearChecker(para):
	if (para < 0):
		print("Year can't be less than 0")
		yearStrCheck(input("Year: "))
	else:
		isLeapYear = 0
		div4 = para / 4
		div100 = para / 100
		div400 = para / 400
		div4Deci = div4 - int(div4)
		div100Deci = div100 - int(div100)
		div400Deci = div400 - int(div400)
		if (div4Deci == float(0)):
			isLeapYear = 1
		if (div100Deci == float(0)):
			isLeapYear = 0
			if (div400Deci == float(0)):
				isLeapYear = 1
		if (bool(isLeapYear)):
			print("The inputted year is a leap year: " + str(para))
		else:
			print("The inputted year is not a leap year: " + str(para))
		#print(str(div4Deci) + " " + str(div100Deci) + " " + str(div400Deci))
		#print(str(div4) + " " + str(div100) + " " + str(div400))

print("Leap Year Checker")
print("-----------------")
yearStrCheck(input("Year: "))
