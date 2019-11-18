myStringList = []
myFloatTuple = (3.141592, 8.249561, 21.0219421)
myListArray = [[1,5,8,3], [3,1,1,4,6], [9,3,3,2,8,5,4]]

def sortStrLen(lengths):
	#Used as a key in sort to sort by string length
	return len(lengths)

def rounder(*flo):
	#Goes through inputted numbers and rounds to the hundrenths
	for x in flo:
		return round(x, 2)
	
def alphebatizer(*items):
	#Goes through the inputted strings and appends to a list
	for string in items:
		myStringList.append(string)
	#String List is sorted by alphabet and length, then printed out
	myStringList.sort()
	print(myStringList)
	myStringList.sort(reverse=True, key=sortStrLen)
	print(f'Longest Word: {myStringList[0]}')
	print(f'Shortest Word: {myStringList[-1]} \n')
	myStringList.clear()

def arrInfo(*mainArr):
	#Goes through the inputted array
	for subArr in mainArr:
		print(f'Main Array: {subArr} \n')
		#Goes through sub arrays to find the index, mean, max, and min
		for value in subArr:
			print(f'Sub-List {subArr.index(value) + 1}')
			print(f'Sub-Length: {len(value)}')
			print(f'Mean: {round(sum(value) / len(subArr), 2)}')
			numList = value.copy()
			numList.sort()
			print(f'Max Value: {numList[-1]}')
			print(f'Min Value: {numList[0]} \n')

#Triggering Functions
for num in myFloatTuple:
	print(f'{rounder(num)} Rounded \n')
alphebatizer('Apple', 'Orange', 'Banana', 'Kiwi', 'Watermelon', 'Cantaloupe')
alphebatizer('Durian', 'Starfruit', 'Lychee', 'Cherry')
arrInfo(myListArray)
