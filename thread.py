from threading import *
def M():
	print('Good Morning.')

def A():
	print('Good Afternoon.')

def E():
	print('Good Evening.')

def N():
	print('Good Night.')

a1 = Thread(target = M)

a2 = Thread(target = E)

a3 = Thread(target = N)

a4 = Thread(target = A)

a1.start()

a2.start()

a3.start()

a4.start()