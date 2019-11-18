myStringList = []
myFloatTuple = (3.141592, 8.249561, 21.0219421)
myItemTupleArray = (('Apple', 'Orange', 'Banana', 'Kiwi', 'Watermelon', 'Cantaloupe'), ('Durian', 'Starfruit', 'Lychee', 'Cherry'))
myListArray = [[1,5,8,3], [3,1,1,4,6], [9,3,3,2,8,5,4]]
def sortStrLen(lengths):
	return len(lengths)
def rounder(*flo):
	for x in flo:
		return round(x, 2)
def alphebatizer(*tupArr):
	for subTup in tupArr:
		for strings in subTup:
			for item in strings:
				myStringList.append(item)
			print(sorted(myStringList))
			print(f'Longest Word: {sorted(myStringList, reverse=True, key=sortStrLen)[0]} \n Shortest Word: {sorted(myStringList, reverse=True, key=sortStrLen)[-1]} \n')
			myStringList.clear()
def arrInfo(*mainArr):
	for subArr in mainArr:
		print(f'Main Array: {subArr} \n')
		for value in subArr:
			numList = value.copy()
			numList.sort()
			print(f'Sub-List {subArr.index(value) + 1} \n Sub-Length: {len(value)} \n Mean: {round(sum(value) / len(subArr), 2)} \n Max Value: {numList[-1]} \n Min Value: {numList[0]} \n')
for num in myFloatTuple:
	print(f'{rounder(num)} Rounded \n')
alphebatizer(myItemTupleArray)
arrInfo(myListArray)
