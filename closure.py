def f1(message):
	msg=message
	print('outer function')
	def f2():
		print('k')
		print('inner function')
		print(message)
	return f2
f=f1('idiot')
f()
print()
del f1
print(f())