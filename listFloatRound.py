myStringList = []
myArray = [[1,5,8,3] , [3,1,1,4,6] , [9,3,3,2,8,5,4]]

def rounder(*num):
	#Goes through inputted numbers and rounds to the hundrenths
	for x in num:
		return round(x, 2)

def sortStrLen(lengths):
	#Used as a key in sort to sort by string length
	return len(lengths)
	
def alphebatizer(*item):
	#Goes through the inputed strings and appends to a list
	for string in item:
		myStringList.append(string)
	#String List is sorted by alphabet and length, then printed out
	myStringList.sort()
	print(myStringList)
	myStringList.sort(reverse=True, key=sortStrLen)
	print('Longest Word: ' + myStringList[0])
	print('Shortest Word: ' + myStringList[-1] + '\n')
	myStringList.clear()


def arrInfo(*mainArr):
	#Goes through the inputed array
	for subArr in mainArr:
		print(subArr)
		print()
		#Goes through sub arrays to find the index, mean, max, and min
		for value in subArr:
			print('Sub-List ' + str(subArr.index(value) + 1))
			print('Sub-Length: ' + str(len(value)))
			print('Mean: ' + str(round(sum(value) / len(subArr), 2)))
			numList = value.copy()
			numList.sort()
			print('Max Value: ' + str(numList[-1]))
			print('Min Value: ' + str(numList[0]) + '\n')

#Triggering Functions
print(str(rounder(3.141592)) + '\n')
alphebatizer('Apple', 'Orange', 'Banana', 'Kiwi', 'Watermelon', 'Cantaloupe')
arrInfo(myArray)
