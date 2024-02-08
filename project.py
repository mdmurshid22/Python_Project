num=int(input('Enter Some Number:'))
'''for i in range(1,num+1):
	for j in range(1,i+1):
		print(j,end=" ")
	print()'''
for i in range(1,num+1):
	for j in range(1,num+2-i):
		print(j,end=" ")
	print()
for i in range(1,num):
	for j in range(1,i+2):
		print(j,end=" ")
	print()