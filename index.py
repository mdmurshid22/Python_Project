#1) Write a python program to given number is prime or not by using while loop?

'''number = int(input('enter some number:'))
i = 2
prime = True
while(i<number):
	if(number%i == 0):
		print(number, 'not a prime number.')
		prime = False
		break
	i=i+1
if(prime == True):
	print(number, 'is a prime number.')'''

#1) for loop?

'''number = int(input('enter some number:'))
prime = True
for x in range(2,number,1):
	if(number%x == 0):
		print(number,'not a prime number.')
		prime = False
		break
if(prime == True):
	print(number,'is prime number.')'''

#2) write a python program to find the N number of prime number by using while loop?

number = int(input('enter N number of prime number:'))
i = 2
prime = True
num = 3
print('prime number are:')
print(2)
count = 1
while(count<=number):
	while(i<num):
		if(num%i == 0):
			prime = False
			break
		i=i+1
	if(prime == True):
		print(num)
		count+=1
	num+=2









