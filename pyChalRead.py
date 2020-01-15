scanTarget = ('!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '[', ']', '^', '_', '{', '}', '\n', ' ')

def read():
	filledFile = open("pyChalText.txt", "r")
	lotsOfText = filledFile.readlines()
	for line in lotsOfText:
		for symbol in line:
			isScanned = False
			for scan in scanTarget:
				if symbol is scan:
					isScanned = True
			if isScanned == True:
				pass
			elif isScanned == False:
				print(symbol)
read()

