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
		isLeapYear = False
		div4 = para % 4
		div100 = para % 100
		div400 = para % 400
		if (div4 == float(0)):
			isLeapYear = True
		if (div100 == float(0)):
			isLeapYear = False
			if (div400 == float(0)):
				isLeapYear = True
		if (isLeapYear):
			print("The inputted year is a leap year: " + str(para))
		else:
			print("The inputted year is not a leap year: " + str(para))

print("Leap Year Checker")
print("-----------------")
yearStrCheck(input("Year: "))
