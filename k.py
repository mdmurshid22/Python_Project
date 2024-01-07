num=int(input("Enter Any Number:"))
for x in range(num+1):
	if x == 0:
		print("{}:is neither real or composite Number".format(x))
		continue
	if x%2 == 0:
		print("{}:is Real Number".format(x))
		continue
	print("{}:is Composite Number".format(x))