'''string=input("Enter Any String:")
i=-1
output=""
l=-len(string)-1
while i > l:
	output=output+string[i]
	i-=1
print(output)
-----------------------------------------------------------------------------------------------------------------
num=int(input('Enter Any Number:'))
for i in range(num+1):
	print('* '*i)
num=int(input('Enter Any Number'))
i=1
while i <= num:
	print("* "*i)
	i+=1
-----------------------------------------------------------------------------------------------------------------
string=input("Enter Any String:")
for i in string:
	if i.isdigit() or i.isspace():
		continue
	if i.isalpha():
		if i.isupper():
			str=ord(i)+32
		else:
			str=ord(i)-32
		print(chr(str),end="")
------------------------------------------------------------------------------------------------------------------
num=int(input("Enter Any Number:"))
i=1
while i <= num:
	if i%3 == 0 or i%5 == 0:
		print(i)
	i+=1
-----------------------------------------------------------------------------------------------------------------
i=1
a=0
while i <= 10:
	a=a+i
	i+=1
print(a)
----------------------------------------------------------------------------------------------------------------
a=0
while True:
	num=int(input("Enter Any Positive Number:"))
	if num < 0:
		print(num)
		break
	else:
		a=a+num
	print(a)
-----------------------------------------------------------------------------------------------------------------
while True:
	name=input("Enter Any Name:")
	if len(name) >= 5:
		print(name)
		break
	else:
		print(name)
-----------------------------------------------------------------------------------------------------------------
'''