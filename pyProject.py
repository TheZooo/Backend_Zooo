import MySQLdb
#-----MySQLdb SETUP
ip = "192.168.0.131"
user = "erizho21"
passwd = "zhou"
dtbase = "erizho21"
db = MySQLdb.connect(ip, user, passwd, dtbase)
cur = db.cursor(MySQLdb.cursors.Cursor)

#-----SELECT BLOCK
def selectData ():
	global choiceA
	choiceA = input('Do you want to see the students list? [Y/N]')
	if choiceA == 'Y':
		sql = "SELECT name,age,gradeLevel FROM students"
		cur.execute(sql)
		rows = cur.fetchall()
		for row in rows:
			print(row)
		else:
			print("-Search Done-")
		askAdd()
	elif choiceA == 'N':
		askAdd()
	else:
		print('Input is case sensitive')
		selectData()

def askAdd ():
	global choiceB
	if choiceA == 'Y':
		choiceB = input('Do you want to add a student [Y/N]')
	elif choiceA == 'N':
		choiceB = input('Do you still want to add a student? [Y/N]')
	if choiceB == 'Y':
		insertData()
	elif choiceB == 'N':
		print()
	else:
		print('Input is case sensitive')
		askAdd()

def insertData ():
	def checker1():
		global name
		nameCheck = input('Name: ')
		if len(nameCheck) != 0:
			name = nameCheck
		else:
			print('Input can\'t be empty')
			checker1()
	def checker2():
		global age
		ageCheck = input('Age: ')
		if ageCheck.isnumeric():
			age = int(ageCheck)
		else:
			print('Input is not a number')
			checker2()
	def checker3():
		global gradeLevel
		gradeLevelCheck = input('Grade Level: ')
		if gradeLevelCheck.isnumeric():
			gradeLevel = int(gradeLevelCheck)
		else:
			print('Input is not a number')
			checker3()
	checker1()
	checker2()
	checker3()
	dataCheck(name,age,gradeLevel)

def dataCheck (p1,p2,p3):
	validCheck = 1
	print('Checking inputs...')
	
	print(type(p1))
	if type(p1) == str and len(p1) < 22 and len(p1) != 0:
		print('Input Valid')
	elif len(p1) > 22:
		print('Input is too long')
		validCheck = 0
	elif len(p1) == 0:
		print('Input is empty')
		validCheck = 0
	else:
		print('Input Invalid')
		validCheck = 0
	
	print(type(p2))
	if type(p2) == int and p2 < 100 and p2 > 1:
		print('Input Valid')
	elif p2 > 99:
		print('Input is past max limit')
		validCheck = 0
	elif p2 < 1:
		print('Input is past min limit')
		validCheck = 0
	else:
		print('Input Invalid')
		validCheck = 0
	
	print(type(p3))
	if type(p3) == int and p3 <= 12 and p3 > 0:
		print('Input Valid')
	elif p3 > 12:
		print('Input is past max grade level')
		validCheck = 0
	elif p3 <= 0:
		print('Input is not a grade level')
		validCheck = 0
	else:
		print('Input Invalid')
		validCheck = 0
	
	if validCheck == 0:
		choiceA = 'N'
		askAdd()
	elif validCheck == 1:
		dataAdd(p1,p2,p3)
	
def dataAdd (p1,p2,p3):
	val = (p1,p2,p3)
	print(val)
	userCheck = input('Is this who you want to add [Y/N] ')
	if userCheck == 'Y':
		sql = "INSERT INTO students (name,age,gradeLevel) VALUES (%s, %s, %s)"
		cur.execute(sql, val)
		db.commit()
		print('Information uploaded')
	elif userCheck == 'N':
		choiceA = 'N'
		askAdd()
	else:
		print('Input is case sensitive')
		dataAdd(p1,p2,p3)
	
selectData()

#-----MySQLdb CLOSE
cur.close()
db.close()
