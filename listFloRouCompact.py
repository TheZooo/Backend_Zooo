myStringList = []
myFloatTuple = (3.141592, 8.249561, 21.0219421)
myItemTupleArray = (('Apple', 'Orange', 'Banana', 'Kiwi', 'Watermelon', 'Cantaloupe'), ('Durian', 'Starfruit', 'Lychee', 'Cherry'))
myListArray = [[1,5,8,3], [3,1,1,4,6], [9,3,3,2,8,5,4]]
def sortStrLen(lengths):
	#Used as a key in sort to sort by string length
	return len(lengths)
def rounder(*flo):
	#Goes through inputted numbers and rounds to the hundrenths
	for x in flo:
		return round(x, 2)
def alphebatizer(*tupArr):
	#Goes through the inputted array
	for subTup in tupArr:
		#Through the Sub Tuples
		for strings in subTup:
			#Through the strings in the tuples
			for item in strings:
				myStringList.append(item)
			#String List is sorted by alphabet and length, then printed out
			print(sorted(myStringList))
			print(f'Longest Word: {sorted(myStringList, reverse=True, key=sortStrLen)[0]} \n Shortest Word: {sorted(myStringList, reverse=True, key=sortStrLen)[-1]} \n')
			myStringList.clear()
def arrInfo(*mainArr):
	#Goes through the inputted array
	for subArr in mainArr:
		print(f'Main Array: {subArr} \n')
		#Goes through sub arrays to find the index, mean, max, and min
		for value in subArr:
			numList = value.copy()
			numList.sort()
			print(f'Sub-List {subArr.index(value) + 1} \n Sub-Length: {len(value)} \n Mean: {round(sum(value) / len(subArr), 2)} \n Max Value: {numList[-1]} \n Min Value: {numList[0]} \n')
#Triggering Functions
for num in myFloatTuple:
	print(f'{rounder(num)} Rounded \n')
alphebatizer(myItemTupleArray)
arrInfo(myListArray)
