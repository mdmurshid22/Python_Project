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
list.extend({2,3.3,'','86+8j'})
print(list)