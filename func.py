'''l=[]
def fun(name=''):
	return name
f=fun(name=input('enter some string:'))
for x in f:
	l.append(x)
print(l)
def func(i):
	l=[]
	while True:	
		if i >= 0:
			l.append(i)
			i=int(input('enter some number:'))
			continue
		elif i >= -1:
			pass
		break
	print(l)
i=int(input('Enter Any Number:'))
func(i)'''