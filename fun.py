'''def my_fun(a,b,c):
	print(a,b,c)
a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=int(input('enter third number:'))
r=my_fun(a,b,c)
print(type(r))
print(r)
print(type(my_fun(a,b,c)))
my_fun(a,b,c)
print(my_fun(a,b,c))
print(type(my_fun(a,b,c)))
def my_fun(r='rollno',n='name',a='age',m='mark',ad='address'):
	print('Roll no:{} Name:{} Age:{} Mark:{} and Address:{}'.format(r,n,a,m,ad))
r=int(input('enter your roll no:'))
n=input('enter your name:')
a=int(input('enter your age:'))
m=int(input('enter your mark:'))
ad=input('enter your address:')
my_fun(r,n,a,m,ad)
def fact(num):
	if num == 1:
		return 1
	else:
		return num*fact(num-1)
num=int(input('enter any number:'))
print(fact(num))
-----------------------------------------------------------------------------------------------------------------------------
number=int(input('enter any number and factorial is:'))
def factorial(number):
	if number == 1:
		return 1
	else:
		return number*factorial(number-1)
print(factorial(number))
-----------------------------------------------------------------------------------------------------------------------------
'''
#Iterator=>iter(),next() Methods.
#l=eval(input('enter any iterable object:'))
#print([x for x in range(1,11)])
