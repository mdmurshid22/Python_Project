'''def add(a,b):
	return a+b
a=int(input('enter a value:'))
b=int(input('enter b value:'))
print(add(a,b))
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
#scope
a=5
def fun():
	global b
	b=30
	print(b)
	#print(b)
fun()
print(b+1)
#print(b)'''
def fun1():
	a=10
	print(a)
	def fun2():
		b=20
		print(b)
	fun2()
fun1()