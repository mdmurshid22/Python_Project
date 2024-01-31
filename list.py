'''list=[7,8.8,True,False,5+9J,'k',"idiot"]
print(type(list))
print(list)
print(list.append(['kk','kkk']))#To add the element at last only and only one value.
print(list)
list.extend(('h',9,8,7))#To add the elements at last only and multiples values.
print(list)
list.extend(['idiot'])
print(list)
print(list.extend(range(1,10)))
print(list)
print(list.clear())#To clear all element from the list.
print(list)
list.append('k')
print(list.copy())#To copy all elements from the list.
print(len(list))#To check the length of the list and return length.
l=len(list)
print(l)
list.extend((2,3.3,'','86+8j',2,3.3,'k','kk',''))
print(list)
print(list.count(2))
print(list.count('kk'))#To check the elements is alive and return the value or not alive con't raise the error.
l1=list.count('')
print(l1)
print(list)
print(list.index(2))#To check the specified elememt of the index.
print(list.insert(7,'l'))#None.
list.insert(8,('j',8,7.7))#To insert a specified element to inserted at two arguments only first is index position another one is value or iterables.
print(list)
l1=['k','kk','idiot']
print(l1)
print(l1.sort(reverse=True))#To order of in our list is assending order and reverse=True is descending order.
print(l1)
print(l1.sort())
print(l1)
print(l1.sort(reverse=False))
print(l1)
print(list.reverse())#To reverse a all elements of the list.
print(list)
print(list.pop())#To remove at last element from the list.
print(list)
print(list.pop(3))#To remove a particular index position of a list.
print(list)
print(list.remove(''))#To remove first element of the given list.
print(list)
print(dir(list))
------------------------------------------------------------------------------------------------------------------------------
list=[10,20,[30,40,[111,[60,70,80],90,100],111],222,333]
print(list)
list[2].pop()
list[2][2][1][2]='idiot'
list[2][2][1][1]=222
list[2][2].insert(2,577)
print(list)
----------------------------------------------------------------------------------------------------------------------------------
list=[3,1,5,2,6,2,9,6,7,9]
i=0
l=0
while i <= len(list):
	l=i
	i+=1
print(list)
print(l)
---------------------------------------------------------------------------------------------------------------------------------
list=[1,3,5,8,2,14,7,6]
i=0
l=[]
while i < len(list):
	if list[i]%2 == 0:
		l.append(list[i])
	i+=1
print(list)
print(l)
--------------------------------------------------------------------------------------------------------------------------------
li=[3,10,2,5,8,22,15,4,16,20,25]
l2=[]
l5=[]
a=0
while a < len(li):
	if li[a]%2 == 0:
		l2.append(li[a])
	if li[a]%5 == 0:
		l5.append(li[a])
	a+=1
print('list is:{}'.format(li))
print('Divisible by 2 is:{}'.format(l2))
print('Divisible by 5 is:{}'.format(list(l5)))
-----------------------------------------------------------------------------------------------------------------------------------
l=eval(input("Enter Any Sequences:"))
print(type(l))
print('Original List is:{}'.format(l))
s=set(l)
print(list(s))
print(type(list(s)))
------------------------------------------------------------------------------------------------------------------------------------
l=eval(input("Enter Any Sequences:"))
l1=[]
for x in l:
	if x not in l1:
		l1.append(x)
print(l1)
-------------------------------------------------------------------------------------------------------------------------------------
l=eval(input("Enter Any Sequences:"))
i=0
j=[]
while i < len(l):
	if l[i] not in j:
		j.append(l[i])
	i+=1
print('The Original Sequences is:{}'.format(l))
print("Remove the duplicates are:{}".format(j))
-------------------------------------------------------------------------------------------------------------------------------------'''