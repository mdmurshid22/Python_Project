with open('closure.py','r') as c:
	r=c.read()
#	for x in c.readlines():
#		print(x)
#	for x in range(5):
#		print(c.readline())
	for x in reversed(r):
		print(x)