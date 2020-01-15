garbledString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. map"
decode = ""
strSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '\'', '"', ')', '(', ':', '/']
strShift = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', ' ', '.', ',', '\'', '"', ')', '(', ':', '/']

def exponent():
	print(2 ** 38)

def decodeShift():
	global decode
	for char in garbledString:
		shiftIndex = strSet.index(char)
		decode += strShift[shiftIndex]
	return decode

decodeString = decodeShift()
exponent()
print()
print(decodeString)
