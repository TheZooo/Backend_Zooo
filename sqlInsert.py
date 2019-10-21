import MySQLdb
#Connecting to database with mysqldb
db = MySQLdb.connect(host="192.168.0.131", user="erizho21", passwd="zhou", db="erizho21")
db.autocommit(True)
#Creating cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)
#Variables
name = 'Philip'
age = 16
gradeLevel = 11
#Sql command
sql = f"INSERT INTO students (name, age, gradeLevel) VALUES ({name}, {age}, {gradeLevel})"
#Cursor executing sql code
cur.execute(sql)
#------SELECT BLOCK-------
sql2 = "SELECT * FROM students"
#Cursor executing sql code
cur.execute(sql2)
#Fetch all rows in table
rows = cur.fetchall()
for row in rows:
	print("Name: " + row["name"] + " Age: " + str(row["age"]) + " GradeLevel: " + str(row["gradeLevel"]))
#------SELECT BLOCK-------
#Disconnecting cursor and database
cur.close()
db.close()
