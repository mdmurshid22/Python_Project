#1)Square star pattern in python.

'''num = int(input('Enter Any Number of Rows:'))
for i in range(1,num+1):
	print('* '*num)'''
#----------------------------------------------------------------------------------

#2)Hollow square pattern program in python.

num = int(input('Enter Any Number of Rows:'))
for i in range(1,num+1):
	if(i==1) or (i==num):
		print('* '*num)
	else:
		print('*'+'  '*(num-2),'*')