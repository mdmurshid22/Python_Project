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

number = int(input('enter some number:'))
prime = True
for x in range(2,number,1):
	if(number%x == 0):
		print(number,'not a prime number.')
		prime = False
		break
if(prime == True):
	print(number,'is prime number.')