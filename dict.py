dict={5:8,'k':7+9J,True:False,8:'idiot',5:7,6:7,8:8}
print(dict)
print(type(dict))
print(len(dict))
print(dict[5])
print(dict[8])
print(dict[True])
d=dict[5]='KK'
print(d)
print(dict)
d=dict[5]={1:2,2:3}
print(dict)
print(dict[5][1])
#print(dir(dict))
a={'students':{'name':{'sname':'i','mark':10},'name':{'sname':'j','mark':20}}}
print(a)
b=a['students']['name']='idiot'
print(b)
print(a)
d=a.copy()#Copy all elements from the Dictionay return deep copy. 
print(d)
a.clear()#Remove all elements from the Dictionay return {empty dict}.
print(a)
f=dict.get(99,{8:9,7:9})#To Get value by using get() method any key is not alive default value also declared.
print(f)
