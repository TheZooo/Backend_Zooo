shapes = ["Circle", "Triangle", "Rectangle", "Pentagon", "Hexagon"]
print(shapes)
print(shapes[1])
shapes[1] = "Square"
shapes.append("Octogon")
shapes.pop(0)
print(shapes)
print(str(len(shapes)) + " Shapes in Array")
y = 0
for x in shapes:
	y += 1
	print(str(y) + ". " + x)
