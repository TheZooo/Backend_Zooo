name1 = 'bob'
name2 = 'sally'
name3 = 'kai'
name4 = 'donald'

# Creating a list called 'students' with jen and name1, which is bob, in list
students = ['jen', name1]

# Changes the value in index [1], which is bob in students
students[1] = 'bobby'

# Adds the value to the end of the list
students.append(name2)
students.append(name3)
students.append(name4)

print(students)

# Adds the value right after 3, making callie the 4 in index
students.insert(3, 'callie')

print(students[1] + "\n")

print(students[3])

# Finds "kai" index in students
print(students.index("kai"))

# Adds on to the list with another list on the end
newStudents = ['tom', 'gill', 'jen']
students.extend(newStudents)

print(students)

# Gets index more than 4 and less than or equal to 7
print(students[4:7])

# Removes value in index 3
del students[3]

# Removes value in index 4, if empty, remove the end value
students.pop(4)

# Removes the first instance of 'gill'
students.remove('gill')

print(students)

# Counts how many times 'jen' appears in the list
print(students.count('jen'))

# Counting up from 0, count the vars in list
print(len(students))

# Copies the list to a variable
studentsCopy = students.copy()

print(studentsCopy)

# Joins the lists
studentsDouble = students + studentsCopy

print(studentsDouble)

# Sorts Alphebetically
students.sort()
print(students)

# Loops through the index-value and prints the value as var studentName
for studentName in students:
	print(studentName)
	
# Prints out 2nd to last value
print(students[-2])

# Reverses the list order
students.reverse()

print(students)

# Clear List
students.clear()
