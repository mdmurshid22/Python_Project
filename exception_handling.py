'''try:
	print(7/0)
except ZeroDivisionError:
	print('No Error')
finally:
	print('The flow of execution is correct!')
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
try:
	t=6/0
except Exception as e:
	print(e)