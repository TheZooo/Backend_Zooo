def passes(arg1, *argy):
	answer = arg1 + 3
	print(arg1, "+ 3 =", answer)
	print(f"Length of argy list: {len(argy)}")
	argySum = 0
	for x in argy:
		argySum = argySum + x

	print("argy list sum: " + str(argySum))

passes(1,7,8,1)
