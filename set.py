set1={False,7+9J,True,2.3,88,76,3,90,6.7,12,2,1}
print(set1)
print(type(set1))
s=set()
print(s)
print(type(s))
print(dir(set))
print(s.add('k'))#None.
#set method(exactly one argument) is add one elements to the set.
print(s)
s.clear()
#clear Method is to clear all elements from the set.
print(s)
s1=set1.copy()
print(s1)
#copy Method is to copy the all elements from the set to create new object.
print(set1.copy())