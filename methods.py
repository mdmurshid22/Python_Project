'''print(eval("'idiot'+'idiot'"))
a=['one','two','three','one']
print(dict(enumerate(a[::-1],10)))'''
a=['a','b','c','d']
#print(dict(enumerate(a)))
l=[]
for x in enumerate(a):
	l.append(x)
print(dict(l))