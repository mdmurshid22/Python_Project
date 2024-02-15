'''def add(a,b):
	return a+b
a=int(input('enter a value:'))
b=int(input('enter b value:'))
print(add(a,b))'''
s='PyThonLanguage'
print(s)
l=len(s)-1
i=0
l1=[]
while i < l:
	if s[i].isupper():
		l1.append(ord(s[i])+32)
	else:
		l1.append(ord(s[i])-32)
	i+=1
for x in l1:
	print(chr(x),end="")