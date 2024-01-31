'''tuple=(7,9.7,True,8+9J,True,False,True)
print(type(tuple))
print(len(tuple))
print(tuple)
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple[3])
print(tuple.count(7))#Syntax->t.count(Exactly one value)
t=tuple.count(8)#count method is count in the tuple of values. 
print(t)
print(tuple.index(True))#To search the value and return the specified index or The value is not found Error value not in tuple.
i=tuple.index(7)#Syntax->t.index(value)
print(i)
print(dir(tuple))
----------------------------------------------------------------------------------------------------------------------------
a=9
b=8
print(a)
print(b)
a,b=b,a
print(a)
print(b)
----------------------------------------------------------------------------------------------------------------------------
a='Python'
i=-1
l=[]
l1=-len(a)
while i >= l1:
	l.append(a[i])
	i-=1
for x in l:
	print(x,end="")
-----------------------------------------------------------------------------------------------------------------------------
a=12345
aa=str(a)
output=0
i=0
while i < len(aa):
	output=output+int(aa[i])
	i+=1
print(output)
------------------------------------------------------------------------------------------------------------------------------
i=int(input("Enter Any Number:"))
if (i%3 == 0) and (i%5 == 0):
	print('bye')
elif i%3 == 0:
	print('hello')
elif i%5 == 0:
	print('hii')
else:
	print('Not Divisible by 3 and 5')
-------------------------------------------------------------------------------------------------------------------------------
a=8
b=9
print(a)
print(b)
temp=a
a=b
b=temp
print(a)
print(b)
-------------------------------------------------------------------------------------------------------------------------------
a=(1,2,3,4,5)
print(a)
b=list(a)
b.insert(2,'one')
print(tuple(b))
-------------------------------------------------------------------------------------------------------------------------------
a=('one','two','three')
x,y,z=a
print(a)
print(y)
-------------------------------------------------------------------------------------------------------------------------------'''