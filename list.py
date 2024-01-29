list=[7,8.8,True,False,5+9J,'k',"idiot"]
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
l1=[3,6,3,2,9,7,6]
print(l1)
l1.sort(reverse=True)
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=False)
print(l1)