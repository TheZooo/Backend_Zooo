class students:
	def __init__(self, pName, pAge, pGrade):
		self.name = pName
		self.age = pAge
		self.gradeLevel = pGrade
		
	def respond(self):
		print("Hello my name is "+ self.name +" and I am "+ str(self.age) +" years old")
	
	def showGrade(self):
		return "Grade Level: " + str(self.gradeLevel)

user = students('Eric', 16, 11)
students.respond(user)
print(students.showGrade(user))
