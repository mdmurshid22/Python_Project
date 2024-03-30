'''try:
	print(7/0)
except ZeroDivisionError:
	print('No Error')
finally:
	print('The flow of execution is correct!')
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
	a='idiot'
	print(b)
	a=(9,7,7)
	a[3]=99
	print(6+'0')
	print(7/0)
except ZeroDivisionError:
	print('hi')
except TypeError:
	print('bye')
except NameError:
	print('Guys')
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
	print(87+'k')
except:
	print('None.')
else:
	print('Else Block.')
finally:
	print('Completed.')
#else:
#	print('Else Block')
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
	print('Try Block.')
	print('idiot'+1)
except:
	print('Except Block.')
else:
	print('Else Block.')
finally:
	print('Finally Block.')
'''
#Only try, except, else, finally block not possible.
#The try block without except or finally not possible.
#Without try block -> except, else, finally we cannot use.
#Multiple except block is possible.
#One try block there Only one else, finally block is possible.
#Without except else block cannot use.
#The Flow is Try --> except.... --> else --> finnaly.