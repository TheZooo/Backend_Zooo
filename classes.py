class numHold:
	def __init__(self, valA, valB):
		self.valA = valA
		self.valB = valB
	def compareEqual(para):
		if (para.valA == para.valB):
			print("Numbers are the same")
		elif (para.valA != para.valB):
			print("Numbers are different")

x = numHold(10,26)
x.compareEqual()
print(x.valA)
print(x.valB)

x.valA = 26
x.compareEqual()
print(x.valA)
print(x.valB)

del x
print("CLASS IS DELETED HERE")
print(x.valA)
