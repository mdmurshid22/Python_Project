def f1(message):
	msg=message
	print('outer function')
	def f2():
		print('k')
		print('inner function')
		print(message)
	return f1
f=f1('idiot')
f()
print()
del f1
print(f())
def add():
	a='hii'
	b=a
	def sub():
		a='hello'
		#print(a)
	sub()
	print(b)
	print(a)
add()