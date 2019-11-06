class cars:
	#init a list of the attributes and the set attributes
	def __init__(self, year, make, model, color = "white"):
		self.attributes = ('year', 'make', 'model', 'color')
		self.carAttr = [year, make, model, color]
		
	#Asks for which attribute to change and what to change it to
	def changeAttr(self):
		sel = input("Which attribute (year, make, model, color) do you want to change? : ")
		for x in self.attributes:
			if (x == sel):
				self.carAttr[self.attributes.index(x)] = input("Input Change: ")

	#Loops through carAttr lists and prints it out
	def display(self):
		for x in self.carAttr:
			print(x)

car = cars(2016, 'Toyota', 'Camry')
print('Current Car')
print('-----------')
car.display()
print()
car.changeAttr()
car.display()
