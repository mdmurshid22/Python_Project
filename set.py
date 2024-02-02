set1={False,7+9J,True,2.3,88,76,3,90,6.7,12,2,1}
print(set1)
print(type(set1))
s=set()
print(s)
print(type(s))
print(dir(set))
print(s.add('k'))#None.
#add method(exactly one argument) is add one elements to the set.
print(s)
s.clear()
#clear Method is to clear all elements from the set.
print(s)
s1=set1.copy()
print(s1)
#copy Method is to copy the all elements from the set to create new object.
print(set1.copy())
r=set1.remove(False)
print(r)
#remove Method is to remove some specidied element if the specified element does not exit raise KeyError. 
print(set1.remove(7+9j))#None.
print(set1.discard(True))#None.
set1.discard(88)
#discard Method is to remove some specified element if the specified element does not exit will won't raise Error.
print(set1)
print(set1.pop())
#pop(No argument) Method is remove some random element to the set.
p=set1.pop()
print(p)
print(set1)
s1={1,2,3,4,5}
s2={3,4,5,6,7,'k'}
print(s1)
print(s2)
print(s2.update(s1))#None
#update Method(Iterable elements like-list,set,tuple,dict->keys only)is updated an Iterable elements to the set.
print(s1)
print(s2)
s2.update({200,300,'idiot',400})
print(s2)