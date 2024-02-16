'''1. Write a function that accepts three numbers as arguments and returns the sum.
2. Write a function to check if a number is palindrome or not.
3. Write a function to find the factorial of the number.
4. Write a function that filters non vowels from the list using filter function.
5. Write a Python program to triple all numbers in a given list of integers. Use Python map.
N=[2,3,4,5,6,7,8,9]
6. Write a Python program to filter even and odd number in a list using Lambda.
N=[1,2,3,4,5,6,7,8,9,10,11,12,13]
7. Write a Python program to find the intersection of two given arrays using Lambda.
A=[12,10,9,8,4,5,25] b=[13,45,10,4,25,45,56]
8. Define a function in python that accepts 3 values and returns the maximum of three
numbers.
9. Define a function that accepts roll number and returns whether the student is present or
absent.
10. Define a function which counts vowels and consonant in a word.
11. Define a function that accepts radius and returns the area of a circle. Define a function that
accepts radius and returns the area of a circle.
12. Write a program to check whether a given key exists in a dictionary or not. a = {‘0’:1, ‘1’:2,
‘2’:3}
13. Write a program to concatenate two dictionaries to create one. dict1 = {‘key 1’: 2, ‘key 2’: 3}
dict2 = {‘key 3’: 4, ‘key 4’: 5}
14. Write a program to sum all the values of a dictionary. a = {‘x’: 500, ‘y’: 300, ‘z’: 300}
------------------------------------------------------------------------------------------------------------
1. Write a function that accepts three numbers as arguments and returns the sum.
def sum(n1,n2,n3):
	return n1+n2+n3
n1=int(input('enter first number:'))
n2=int(input('enter second number:'))
n3=int(input('enter third number:'))
print(sum(n1,n2,n3))
------------------------------------------------------------------------------------------------------------
2. Write a function to check if a number is palindrome or not.
def pali(strg):
	if strg == strg[::-1]:
		print('It is Palindrome:{}'.format(strg))
	else:
		print('It is not a Palindrome:{}'.format(strg))
strg=input('enter some string:')
pali(strg)
-------------------------------------------------------------------------------------------------------------
3. Write a function to find the factorial of the number.
def fact(num):
	f=num
	while num > 1:
		num-=1
		f=f*num
	return f
num=int(input('enter any number:'))
print('The given number:{} and Factorial:{}'.format(num,fact(num)))
--------------------------------------------------------------------------------------------------------------
4. Write a function that filters non vowels from the list using filter function.
character=input('enter any charcter:')
vowels=['a','e','i','o','u']
print(list(filter(lambda character:character not in vowels,character)))
--------------------------------------------------------------------------------------------------------------
5. Write a Python program to triple all numbers in a given list of integers. Use Python map.
N=[2,3,4,5,6,7,8,9]
n=[2,3,4,5,6,7,8,9]
print(list(map(lambda x:x*3,n)))
--------------------------------------------------------------------------------------------------------------
6. Write a Python program to filter even and odd number in a list using Lambda.
N=[1,2,3,4,5,6,7,8,9,10,11,12,13]
n=[1,2,3,4,5,6,7,8,9,10,11,12,13]
even=list(filter(lambda n:n%2 == 0,n))
odd=list(filter(lambda n:n%2 != 0,n))
print('Original Number:{}'.format(n))
print('Even Number:{}'.format(even))
print('Odd Number:{}'.format(odd))
--------------------------------------------------------------------------------------------------------------
7. Write a Python program to find the intersection of two given arrays using Lambda.
A=[12,10,9,8,4,5,25] b=[13,45,10,4,25,45,56]
a=[12,10,9,8,4,5,25]
b=[13,45,10,4,25,45,56]
i=0
l=[]
while i < len(a):
	for x in b:
		if x == a[i]:
			l.append(a[i])
	i+=1
print(l)
---------------------------------------------------------------------------------------------------------------
8. Define a function in python that accepts 3 values and returns the maximum of three
numbers.
def max(n1,n2,n3):
	if n1 > n2 and n1 > n3:
		return n1
	elif n2 > n3:
		return n2
	else:
		return n3
n1=int(input('enter first number:'))
n2=int(input('enter second number:'))
n3=int(input('enter third number:'))
print(max(n1,n2,n3))
---------------------------------------------------------------------------------------------------------------
9. Define a function that accepts roll number and returns whether the student is present or
absent.'''