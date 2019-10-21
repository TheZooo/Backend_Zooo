import MySQLdb
#Connecting to database with mysqldb
db = MySQLdb.connect(host="192.168.0.131", user="erizho21", passwd="zhou", db="erizho21")
#Creating cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)
sql = "SELECT * FROM students"
#Cursor executing sql code
cur.execute(sql)
#Fetch all rows in table
rows = cur.fetchall()
for row in rows:
	print("Name: " + row["name"] + " Age: " + str(row["age"]) + " GradeLevel: " + str(row["gradeLevel"]))
#Disconnecting cursor and database
cur.close()
db.close()
