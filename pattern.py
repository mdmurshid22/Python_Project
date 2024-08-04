#1)Square star pattern in python.

'''num = int(input('Enter Any Number of Rows:'))
for i in range(1,num+1):
	print('* '*num)'''
#----------------------------------------------------------------------------------

#2)Hollow square pattern program in python.

'''num = int(input('Enter Any Number of Rows:'))
for i in range(1,num+1):
	if(i==1) or (i==num):
		print('* '*num)
	else:
		print('*'+'  '*(num-2),'*')'''
#----------------------------------------------------------------------------------

#3)Right triangle pattern program in python.

'''num = int(input('Enter any Number of Rows:'))
for i in range(1,num+1):
	print(' '*(num-i),'*'*(i))'''
#----------------------------------------------------------------------------------

#4)Left triangle pattern program in python.

'''num = int(input('Enter Any Number of Rows:'))
for i in range(1,num+1):
	print('*'*i)'''
#----------------------------------------------------------------------------------

#5)Downward triangle star pattern program in python.

'''num = int(input('Enter Any Number Of Rows:'))
for i in range(1,num+1):
	print('*'*(num-i+1))'''
#----------------------------------------------------------------------------------

#Eg ->1 :-

'''num = int(input('Enter Any Number Of Rows:'))
for i in range(1,num+1):
	print('*'*i)
for j in range(1,num):
	print('*'*(num-j))'''
#----------------------------------------------------------------------------------

#Eg ->2:-

'''num = int(input('Enter Any Number Of Rows:'))
for i in range(1,num+1):
	print(' '*(num-i)+'*'*i)
for j in range(1,num):
	print(' '*j+'*'*(num-j))'''
#----------------------------------------------------------------------------------

#Eg ->3:-

'''num = int(input('Enter Any Number Of Rows:'))
for i in range(1,num+1):
	print(' '*(i-1)+'*'*(num-i+1))'''
#----------------------------------------------------------------------------------

#Eg ->4:-

'''num = int(input('Enter Any Number of rows:'))
for i in range(1,num+1):
	print('*'*(num-i+1))
for j in range(1,num):
	print('*'*(j+1))'''
#----------------------------------------------------------------------------------

#Eg ->5:-

'''num = int(input('Enter Any Number of rows:'))
for i in range(1,num+1):
	print(' '*(i-1)+'*'*(num-i+1))
for j in range(1,num):
	print(' '*(num-j-1)+'*'*(j+1))'''
#----------------------------------------------------------------------------------

#6)Pyramid pattern program in python.

'''num = int(input('Enter Any Number Of Rows:'))
for i in range(1,num+1):
	print(' '*(num-i)+'* '*i)'''
#----------------------------------------------------------------------------------

#7)Reversed Pyramid pattern program in python.

'''num = int(input('Enter Any Number Of Rows:'))
for i in range(1,num+1):
	print(' '*(i-1)+'* '*(num-i+1))'''
#----------------------------------------------------------------------------------

#8)Diamond pattern program in python.

num = int(input('Enter Any Number Of Rows:'))
for i in range(1,num+1):
	print(' '*(num-i)+'* '*i)
for j in range(1,num):
	print(' '*j+'* '*(num-j))




























