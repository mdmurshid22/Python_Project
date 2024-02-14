'''print(eval("'idiot'+'idiot'"))
a=['one','two','three','one']
print(dict(enumerate(a[::-1],10)))
a=['a','b','c','d']
#print(dict(enumerate(a)))
l=[]
for x in enumerate(a):
	l.append(x)
print(dict(l))
a=['a','b','c','d','f']
b=[6,7,8,9,10]
print(dict(zip(a[::-1],b[::-1])))'''
a=['a','b','c','d']
b=[1,2,3,4]
l=tuple(enumerate(a))
l1=[]
for x,y in l:
	l1.append(x)
	l1.append(y)
	l1.append(b[x])
print(tuple(l1))