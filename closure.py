def f1(message):
	msg=message
	def f2():
		print('k')
	return f2
f=f1('idiot')
f()
del f1
f()