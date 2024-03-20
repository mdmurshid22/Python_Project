'''try:
	print(7/0)
except ZeroDivisionError:
	print('No Error')
finally:
	print('The flow of execution is correct!')
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
try:
	a=(9,7,7)
	a[3]=99
	print(6+'0')
	print(7/0)
except ZeroDivisionError:
	print('hi')
except TypeError:
	print('bye')
except Exception as e:
	print(e)
