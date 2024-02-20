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
-----------------------------------------------------------------------------------------------------------------------------
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
#Iterator=>iter(),next() Methods.
iter_method=eval(input('enter any iterable elements:'))
inbuilt_method=iter(iter_method)
print(next(inbuilt_method))
print(next(inbuilt_method))
print(next(inbuilt_method))
print(next(inbuilt_method))
print(next(inbuilt_method))
-----------------------------------------------------------------------------------------------------------------------------
iterable_objects=eval(input('enter any iterable object:'))
list=[]
for iteration in iterable_objects:
	if iteration%2 == 0:
		list.append(iteration)
	l=iter(list)
print('even number:{}'.format(next(l)))
print('even number:{}'.format(next(l)))
print('even number:{}'.format(next(l)))
-----------------------------------------------------------------------------------------------------------------------------
#iterable_objects=eval(input('enter any iterable object:'))
iterable_objects=[6,2,3,4,5,7,8,9,6,4]
list=[]
for iteration in iterable_objects:
	if iteration%2 != 0:
		list.append(iteration)
	l=iter(list)
print('odd number:{}'.format(next(l)))
print('odd number:{}'.format(next(l)))
print('odd number:{}'.format(next(l)))
----------------------------------------------------------------------------------------------------------------------------
num=int(input('enter some number:'))
def fact(num):
	if num == 1:
		return 1
	else:
		return num*fact(num-1)

print(fact(num))
----------------------------------------------------------------------------------------------------------------------------
def fact(num):
	f=num
	while num > 1:
		num-=1
		f=f*num
	print(f)
	return f
num=int(input('enter any number:'))
print('The given number:{} and Factorial:{}'.format(num,fact(num)))
fact(num)
----------------------------------------------------------------------------------------------------------------------------
def gererator():
	a='hii'
	yield a
	b='bye'
	yield b
o=gererator()
print(next(o))
print(next(o))
#print(next(o))
#print(next(gererator()))
#print(next(gererator()))
#print(next(gererator()))
----------------------------------------------------------------------------------------------------------------------------
string=input('enter any string:')
def gen(string):
	l=[]
	index = 0
	while index < len(string):
		yield string[index]
		index+=1
o=gen(string)
print(next(o),end='')
print(next(o))
print(next(o))
print(next(o))
print(next(o))
#print(next(o))
----------------------------------------------------------------------------------------------------------------------------
iterable_object=eval(input('enter any string:'))
def gen(iterable_object):
	l=[]
	index = 0
	while index < len(iterable_object):
		yield iterable_object[index],len(iterable_object[index])
		index+=1
o=gen(iterable_object)
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
----------------------------------------------------------------------------------------------------------------------------'''
