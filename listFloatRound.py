myStringList = []
myArray = [[1,5,8,3] , [3,1,1,4,6] , [9,3,3,2,8,5,4]]

def rounder(*num):
	for x in num:
		return round(x, 2)

def sortStrLen(lengths):
	return len(lengths)
	
def alphebatizer(*n):
	for x in n:
		myStringList.append(x)
	myStringList.sort()
	print(myStringList)
	myStringList.sort(reverse=True,key=sortStrLen)
	print('Longest: ' + myStringList[0])
	print('Shortest: ' + myStringList[-1])
	myStringList.clear()
	
def arrInfo(*arr):
	for x in arr:
		print(x[1])
		print(len(x))
		for y in x:	
			mean = sum(y) / len(x)
			
print(rounder(3.141592))
alphebatizer('Apple', 'Orange', 'Banana', 'Kiwi', 'Watermelon', 'Cantaloupe')
arrInfo(myArray)
